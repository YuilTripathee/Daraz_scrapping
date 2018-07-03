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

# class for search and sort algorithm to manage data in json (now in array of dictionaries)
class SearchSort:
    # sorts the data making SKU as index
    def sort_by_sku(self, json_list, reference):
        if len(json_list) < 2: return json_list
        ipivot = len(json_list)//2        # dividing the array
        pivot = json_list[ipivot]         # partitioning the array
        if type(json_list[0]) is int:
            before = [x for i,x in enumerate(json_list) if x <= pivot and i != ipivot] 
            after = [x for i,x in enumerate(json_list) if x > pivot and i != ipivot]   
            return self.sort_by_sku(before, reference) + [pivot] + self.sort_by_sku(after, reference)    
        elif type(json_list[0]) is dict:
            before = [x for i,x in enumerate(json_list) if x[reference] <= pivot[reference] and i != ipivot] 
            after = [x for i,x in enumerate(json_list) if x[reference] > pivot[reference] and i != ipivot]   
            return self.sort_by_sku(before, reference) + [pivot] + self.sort_by_sku(after, reference)    
    
    # performs binary search on the data by sku
    def search_sku(self, encoded_list, sku):
        lo, hi = 0, len(encoded_list)
        while lo < hi:
            mid = (hi + lo)//2
            if encoded_list[mid]['sku'] == sku:
                return mid
            elif encoded_list[mid]['sku'] > sku:
                hi = mid
            else:
                lo = mid + 1
        return None
    
# function to find if product from scrap is already present and returns its index in array
def get_index(encoded_list, sku_data):
    search = SearchSort()
    index_num = search.search_sku(encoded_list, sku_data)
    return index_num

# main() function
if __name__ == '__main__':
    # extracting data from internal source
    with open('dataset.json', 'r', encoding='utf-8') as fp:
        data_from_file = json.load(fp)    
        encoded_list = encodeFromJSON(data_from_file)
        fp.close()
    
    # extracting database server configuration
    with open('../config/DBconf.json', 'r', encoding="utf-8") as fp:
        dbConf = json.load(fp)
        fp.close()
    
    # Open database connection
    db = pymysql.connect(dbConf['server'], dbConf['username'], dbConf['password'], dbConf['database'])
    # connect(server, username, password, database)
    print('Established connection with database server.')
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute a SQL query using execute() method
    cursor.execute("SELECT VERSION()")
    # fetch a single row using fetchone() method
    db_info = cursor.fetchone()
    
    # send product data to MariaDB server
    for product in encoded_list:
        # for finding category
        if product.category == 'Cables':
            cat_id = 1
        elif product.category == 'Wireless Speakers':
            cat_id = 2
        elif product.category == 'Computing & Gaming':
            cat_id = 3
        elif product.category == 'Smartwatches':
            cat_id = 4
        elif product.category == 'VR Headsets':
            cat_id = 5
        else:
            cat_id = None
        insert_query = "INSERT INTO products(sku, product_name, category, link, image_link, date_issued, date_updated)VALUES('%s', '%s', '%d', '%s', '%s', '%s', '%s')" % (product.sku, product.name.strip().replace('\u2013',''), cat_id, product.link, product.image_link, product.date_issued, product.prices[-1].date)
        try:
            cursor.execute(insert_query)
            db.commit()
        except:
            db.rollback()
            continue
        print('Added new product : ', product)
    
    # push up the price
    # fetch all the products with their skus and product.id in array of dictionary
    get_id_sku = "SELECT id, sku FROM products;"
    try:
        # Execute SQL command
        cursor.execute(get_id_sku)
        # Fetch all the rows in a list of list
        results = cursor.fetchall()
        link_data = []
        for data in results:
            data = {
                'id' : data[0],
                'sku' : data[1]
            }
            link_data.append(data)
    except:
        print('Unable to fetch data from database: ID and SKU') 
    # Sort data in order of SKU (to get foreign key reference)
    ss = SearchSort()
    ss.sort_by_sku(link_data, 'sku')
        
    # fetching all foreign key
    for product in encoded_list:
        # find foreign key of prices i.e. product_id
        foreign_key = link_data[ss.search_sku(link_data, product.sku)]['id']     
        # fetch the array of objects of prices of same product
        get_prices = "SELECT * FROM prices WHERE prod_id = '%d'" % foreign_key
        try:
            cursor.execute(get_prices)
            results = cursor.fetchall()
            prices_DB = []
            for price in results:
                price_tuple = {
                    'id' : price[0],
                    'price' : price[2],
                    'date' : price[4]
                }
                prices_DB.append(price_tuple)
        except:
            print("Couldn't fetch price from the table : PRICES")
            pass
        # check the date of last price update (if matches, go out of loop)/(if not push as new price)
        if prices_DB != []:
            if prices_DB[-1]['date'] != product.prices[-1].date:
                price = product.prices[-1]
                insert_query = "INSERT INTO prices(prod_id, price, discount, date, currency_iso)VALUES('%d','%d','%s','%s','%s')" % (foreign_key, price.price, price.discount, price.date, price.currency)
                update_product_date = "UPDATE products SET date_updated = '%s' WHERE id = '%d'" % (price.date, foreign_key)
                try:
                    cursor.execute(insert_query)
                    cursor.execute(update_product_date)
                    db.commit()
                    print('New price updated on : ', product.sku)
                    continue
                except:
                    db.rollback()
                    print('Unable to push price to database')
                    continue
            else:
                print('Price already present!!!')
                continue
        # put the price entry for new product
        else:
            for price in product.prices:
                insert_query = "INSERT INTO prices(prod_id, price, discount, date, currency_iso)VALUES('%d','%d','%s','%s','%s')" % (foreign_key, price.price, price.discount, price.date, price.currency)
                try:
                    cursor.execute(insert_query)
                    db.commit()
                    print('New price added on : ', product.sku)
                    continue
                except:
                    db.rollback()
                    print('Unable to push price to database')
                    continue

    # end of operation
    print('Database operation performed sucessfully on : ', db_info[0])
    