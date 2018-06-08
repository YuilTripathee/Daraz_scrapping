import sys
import json
import pymysql
import datetime
from flask import Flask, jsonify, request   # import objects from the Flask model
# importing cache object
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

app = Flask(__name__) # define app using flask

# acquiring database configuration for connection to the database and query execution
with open('../config/DBconf.json', 'r+', encoding='utf-8') as fp:
    DB_data = json.load(fp)
    fp.close()

# returns prices of the product iterable provided
def get_prices(database_cursor, foreign_key_in_price):
    get_prices_Q = "SELECT * FROM prices WHERE prod_id = '%d' ORDER BY id ASC" % foreign_key_in_price
    try:
        database_cursor.execute(get_prices_Q)
        price_result = database_cursor.fetchall()
        price_list = []
        for price in price_result:
            price_unit = {
                'id' : price[0],
                'price' : price[2],
                'discount' : price[3],
                'date' : price[4].strftime('%c'),
                'currency' : price[5]
            }
            price_list.append(price_unit)
        return price_list   
    except:
        raise

# build a JSON like list of products dictionaries according to parameters provided
def build_product_list(cursor, product_results):
    array_of_products = []
    for data in product_results:
        product_unit = {
            'id' : data[0],
            'sku' : data[1],
            'name' : data[2],
            'category' : data[3],
            'link' : data[4],
            'image_link' : data[5],
            'date_issued' : data[6].strftime('%c'),
            'date_updated' : data[7].strftime('%c'),
            'prices' : get_prices(cursor, data[0])
        }
        array_of_products.append(product_unit)
    return array_of_products

# returns the products with prices based on the arguments provided
# fetches data from database through SQL query and acquire JSON like data from build_products()
def get_products(cursor, category=None, sku=None):
    if category != None:
        get_product_by_cat_Q = "SELECT * FROM products WHERE category = '%d';" % int(category)
        try:
            cursor.execute(get_product_by_cat_Q)
            product_results = cursor.fetchall()
            array_of_products = build_product_list(cursor, product_results)
            return array_of_products
        except:
            print('[err] Unable to fetch data from the database.')
            raise
    elif sku != None:
        get_product_by_sku_Q = "SELECT * FROM products WHERE sku = '%s';" % sku
        try:
            cursor.execute(get_product_by_sku_Q)
            product_results = cursor.fetchall()
            array_of_products = build_product_list(cursor, product_results)
            return array_of_products[0]
        except:
            print('[err] Unable to fetch data from the database.')
            raise
    else:
        get_product_Q = "SELECT * FROM products;"
        try:
            cursor.execute(get_product_Q)
            product_results = cursor.fetchall()
            array_of_products = build_product_list(cursor, product_results)
            return array_of_products
        except:
            print('[err] Unable to fetch data from the database.')
            raise

# simple API response test   
@app.route('/api/', methods=['GET'])
def test():
    data = {
        'data' : {
            'provider' : 'Yuil Tripathee',
            'host' : '127.0.0.1'
        }
    }
    return jsonify(data)

# cache section
def get_all_products():
    rv = cache.get('my-cache')
    if rv is None:
        rv = get_products(pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor())
        cache.set('my-cache', rv, timeout=300)
    return rv

def get_products_by_category(category_id):
    rc = cache.get('cat-cache : %d' % int(category_id))
    if rc is None:
        rc = get_products(pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor(), category=category_id)
        cache.set('cat-cache : %d' % int(category_id), rc, timeout=300)
    return rc

def sku(sku_data):
    rc = cache.get('cat-cache : %s' % sku_data)
    if rc is None:
        rc = get_products(pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor(), category=category_id)
        cache.set('cat-cache : %s' % sku_data, rc, timeout=300)
    return rc

# products
@app.route('/api/products/', methods=['GET'])
def product_print():
    return jsonify({ "products" : get_all_products() })

# category of products
@app.route('/api/products/category/', methods=['GET'])
def send_category():
    args = request.args
    category = args['category']
    return jsonify({ "category" : get_products_by_category(category)})

# individual product
@app.route('/api/product/', methods=['GET'])
def send_product():
    args = request.args
    sku_data = args['sku']
    connection = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database'])
    cursor = connection.cursor()
    return jsonify({"product" : get_products(cursor, sku=sku_data)})

# returns the number of categories in our database
def get_category_IDs():
    get_category_data_Q = "SELECT * FROM category;"
    cursor = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor()
    cursor.execute(get_category_data_Q)
    cat_data_raw = cursor.fetchall()
    list_category_id = []
    for unit in cat_data_raw:
        list_category_id.append(unit[0])
    return list_category_id

# running flask app
if __name__ == '__main__':
    #initiating cache
    get_all_products()
    for category_id in get_category_IDs():
        get_products_by_category(category_id)
    # setting up port
    try:
        port = int(sys.argv[1])
    except:
        port = 5000

    # starting server
    app.run(port=port, threaded=True)
