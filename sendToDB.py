# import library necessary for Python to work with MySQL server
import pymysql
import json       # standard python JSON libary

# class to determine a unit price format
class Price:
    def __init__(self, price_object):
        self.id = price_object['id']
        self.discount = price_object['discount']
        self.price = price_object['price']
        self.date = price_object['date']
        self.currency = price_object['currency']
        pass
    
    def __repr__(self):
        return '%s' % self.id

# class to determine a unit product format
class Product:
    def __init__(self, data_object):
        self.sku = data_object['sku']
        self.id = data_object['id']
        self.name = data_object['name']
        self.category = data_object['category']
        self.link = data_object['link']
        self.image_link = data_object['image_link']
        self.date_issued = data_object['date_issued']
        self.prices = []
        for item in data_object['prices']:
            unit = Price(item)
            self.prices.append(unit)
            pass
        self.recent_price_id = self.prices[-1].id
    
    def __repr__(self):
        return '%s' % (self.sku)

# encoder to encode JSON object (dict now) to Python objects
def encodeFromJSON(list):
    new_list = []
    for item in list:
        new_list.append(Product(item))
    return new_list

# decoder to decode Python objects to array of dict (for JSON)
def decodetoJSON(list):
    new_list = []
    for item in list:
        prices = []
        for price in item.prices:
            price = {
                'id' : price.id,
                'discount' : price.discount,
                'price' : price.price,
                'date' : price.date,
                'currency' : price.currency
            }
            prices.append(price)
        product = {
            'sku' : item.sku,
            'id' : item.id,
            'name' : item.name,
            'category' : item.category,
            'link' : item.link,
            'image_link' : item.image_link,
            'date_issued' : item.date_issued,
            'prices' : prices
        }
        new_list.append(product)
    return new_list

# main() function
if __name__ == '__main__':
    # extracting data from internal source
    with open('database/dataset.json', 'r', encoding='utf-8') as fp:
        data_from_file = json.load(fp)    
        encoded_list = encodeFromJSON(data_from_file)
        fp.close()
    

    # Open database connection
    db = pymysql.connect("localhost", "root", "123456", "TESTDB")
    # connect(server, username, password, database)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute a SQL query using execute() method
    cursor.execute("SELECT VERSION()")
    # fetch a single row using fetchone() method
    data = cursor.fetchone()
    
    # sending data to MariaDB server
    for product in encoded_list:
        insert_query = "INSERT INTO products(sku, product_name, link, image_link, date_issued, price, discount, currency_iso)VALUES('%s', '%s', '%s', '%s', '%s', '%d', '%s', '%s')" % (product.sku, product.name.strip().replace('\u2013',''), product.link, product.image_link, product.date_issued, product.prices[-1].price, product.prices[-1].discount, product.prices[-1].currency)
        try:
            cursor.execute(insert_query)
            db.commit()
        except:
            db.rollback()
            continue
        print(product)
    
    # end of operation
    print('Database operation performed sucessfully on : ', data)