import pymysql
import json

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

# Function to load data from database as in our regular format
def loadData(cursor):
    sql = "SELECT VERSION()"
    cursor.execute(sql)
    data = cursor.fetchone()
    print ("Established connection with the database : %s " % data)

def get_target_page(database_cursor):
    access_url_Q = "SELECT * FROM target_pages;"
    try:
        cursor.execute(access_url_Q)
        page_urls = cursor.fetchall()
        target_url = []
        for unit in page_urls:
            target_url.append(unit[1])
        return target_url
    except:
        print("Unable to fetch data from database : URLS to scrape")
        return None  

# Define main module
if __name__ == '__main__':
    # getting database configuration
    with open('../../config/DBconf.json', 'r+', encoding='utf-8') as fp:
        DB_data = json.load(fp)
        fp.close()
    
    # Open database connection
    db = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database'])
    cursor = db.cursor()
    loadData(cursor)
    urls = get_target_page(cursor)
    
    # # load products
    # get_product_Q = "SELECT * FROM products;"
    # try:
    #     cursor.execute(get_product_Q)
    #     product_results = cursor.fetchall()
    #     product_data = []
    #     for data in product_results:
    #         product_unit = {
    #             'id' : data[0],
    #             'sku' : data[1],
    #             'name' : data[2],
    #             'category' : data[3],
    #             'link' : data[4],
    #             'image_link' : data[5],
    #             'date_issued' : data[6],
    #             'date_updated' : data[7],
    #             'prices' : []
    #         }
    #         product_data.append(product_unit)
    # except:
    #     print('Unable to fetch data from database: ID and SKU') 
    
    # # fits in the price
    # get_price_Q = "SELECT * FROM prices;"
    # try:
    #     cursor.execute(get_price_Q)
    #     price_result = cursor.fetchall()
    #     price_data = []
    #     for price in price_result:
    #         price_unit = {
    #             'prod_id' : price[0],
    #             'price' : price[1],
    #             'discount' : price[2],
    #             'currency_iso' : price[3]
    #         }
    #         price_data.append(price_unit)
    # except:
    #     raise

    # with open('newdata.json', 'w', encoding='utf-8') as fp:
    #     json.dump(product_data, fp, indent=4)
    #     fp.close()

    # with open('price.json', 'w', encoding='utf-8') as fp:
    #     json.dump(price_data, fp, indent=4)
    #     fp.close()
