import sys
import json
import pymysql
import time

# Flask microservice modules
from flask import Flask, jsonify, request
from werkzeug.contrib.cache import SimpleCache

# Flask app and cache declaration
app = Flask(__name__)
cache = SimpleCache()
# Note : apply this in development environment only
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

# Acquire database config info
with open('../config/DBconf.json', 'r', encoding='utf-8') as fp:
    DB_data = json.load(fp)
    fp.close()

# Acquire status codes for response message status
with open('status.json', 'r', encoding='utf-8') as fp:
    status_codes = json.load(fp)
    fp.close()

# common function to build JSON data from tuple incoming from database
def buildProduct(database_cursor, product_results_tuple = None, one_product_tuple=None, fullPrice = False):
    array_of_products = []
    if one_product_tuple is not None:
        product = {
            'id' : one_product_tuple[0],
            'sku' : one_product_tuple[1],
            'brand' : one_product_tuple[2],
            'name' : one_product_tuple[3],
            'category' : one_product_tuple[4],
            'link' : one_product_tuple[5],
            'image_link' : one_product_tuple[6],
            'reviews' : one_product_tuple[7],
            'date_issued' : one_product_tuple[8].strftime('%c'),
            'date_issued' : one_product_tuple[9].strftime('%c'),
            'prices' : getPrice(database_cursor, one_product_tuple[0], fullPrice)
        }
        return product
    else:
        for data in product_results_tuple:
            product_unit = {
                'id' : data[0],
                'sku' : data[1],
                'brand' : data[2],
                'name' : data[3],
                'category' : data[4],
                'link' : data[5],
                'image_link' : data[6],
                'reviews' : data[7],
                'date_issued' : data[8].strftime('%c'),
                'date_updated' : data[9].strftime('%c'),
                'prices' : getPrice(database_cursor, data[0], fullPrice)
            }
            array_of_products.append(product_unit)
        return array_of_products     
    
# common function to return the price for the product specified
def getPrice(database_cursor, foreign_key_in_price, fullPrice = False):
    getPriceQ = "SELECT * FROM prices WHERE prod_id = '%d' ORDER BY id ASC" % foreign_key_in_price
    try:
        database_cursor.execute(getPriceQ)
        if fullPrice:
            price_list = []
            price_result = database_cursor.fetchall()
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
        else:
            price_result = database_cursor.fetchall()[-1]
            price_unit = {
                'price' : price_result[2],
                'discount' : price_result[3],
                'date' : price_result[4].strftime('%c'),
                'currency' : price_result[5]
            }
        return price_unit  
    except:
        raise 
 
# common function to return list of categories for reference
def getCategory(database_cursor, category_id):
    getCategoryQ = "SELECT * FROM category WHERE id = '%d'" % (category_id)
    try:
        database_cursor.execute(getCategoryQ)
        catResult = database_cursor.fetchone()
        categoryData = {
            'id' : catResult[0],
            'category' : catResult[1],
            'sub_category' : catResult[2]
        } 
        return categoryData
    except:
        raise

# find category for a single product
def findCategoryID(database_cursor, sku):
    findCategoryQ = "SELECT category FROM products WHERE sku = '%s'" % (sku)
    try:
        database_cursor.execute(findCategoryQ)
        DBResult = database_cursor.fetchone()
        category_id = DBResult[0]
        return category_id
    except:
        raise

# route to provide info about the backend
@app.route('/api/', methods=['GET'])
def send_info_msg():
    data = {
        'data' : {
            'provider' : 'Product monitoring system',
            'content-type' : 'application/json',
            'host' : 'localhost',
            'server' : 'Werkeug/0.14.1',
            'python_version' : '3.6.5',
            'developer' : 'Yuil Tripathee',
            'date' : time.asctime()
        }
    }
    return jsonify(data)

@app.route('/api/products/', methods=['GET'])
def sendProducts():
    return "All the products!!!"

@app.route('/api/products/category/', methods=['GET'])
def sendCategory():
    return "All the products in this category"

@app.route('/api/products/skugroup/', methods=['GET'])
def sendGroup():
    args = request.args
    skustr = args.get('sku', '')
    fullPrice = args.get('fullPrice', False)
    # making fullPrice
    if fullPrice is False:
        fullPrice = False
    elif fullPrice.lower() == 'false':
        fullPrice = False
    elif fullPrice.lower() == 'true':
        fullPrice = True
    else:
        return jsonify(status_codes[3]), 400
    # now get list of SKUs
    if skustr == '':
        return jsonify(status_codes[3]), 400
    # making database cursor
    database_cursor = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor()
    return fetchProductGroup(database_cursor, skustr, fullPrice)
def fetchProductGroup(database_cursor, skustr, fullPrice):
    message = cache.get('groupProduct%s%s' % (skustr, str(fullPrice).lower()) )
    if message is None:
        try:
            data = {
                # "category" : getCategory(database_cursor, findCategoryID(database_cursor, sku)),
                "products" : getProductGroup(database_cursor, skustr, fullPrice) 
            }
            message = status_codes[1]
            message['data'] = data
            cache.set('groupProduct%s%s' %(skustr, str(fullPrice).lower()), message, timeout=600)
            return jsonify(message), 200
        except:
            return jsonify(status_codes[2]), 404
    return jsonify(message), 200
def getProductGroup(database_cursor, skustr, fullPrice=False):
    SKUs = skustr.split(',')
    products_list = []
    for sku in SKUs:
        product_unit = getProduct(database_cursor, sku, fullPrice = fullPrice)
        products_list.append(product_unit)
    return products_list

def getProduct(database_cursor, sku, fullPrice = False):
    get1ProductSKU = "SELECT * FROM products WHERE sku = '%s'" % (sku)
    try:
        database_cursor.execute(get1ProductSKU)
        product_result = database_cursor.fetchone()
        product = buildProduct(database_cursor, one_product_tuple=product_result, fullPrice = fullPrice)
        return product
    except:
        return int('1+2+3')

@app.route('/api/product/', methods=['GET'])
def sendOneProduct():
    args = request.args
    fullPrice = args.get('fullPrice', False)
    sku = args.get('sku')
    # making fullPrice
    if fullPrice is False:
        fullPrice = False
    elif fullPrice.lower() == 'false':
        fullPrice = False
    elif fullPrice.lower() == 'true':
        fullPrice = True
    else:
        return jsonify(status_codes[3]), 400
    database_cursor = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor()
    return fetchoneProduct(database_cursor, sku, fullPrice)
def fetchoneProduct(database_cursor, sku, fullPrice):
    message = cache.get('oneProduct%s%s' %(sku, str(fullPrice).lower()))
    if message is None:
        try:
            data = {
                "category" : getCategory(database_cursor, findCategoryID(database_cursor, sku)),
                "product" : getProduct(database_cursor, sku, fullPrice = fullPrice)
            }
            message = status_codes[1]
            message['data'] = data
            cache.set('oneProduct%s%s' %(sku, str(fullPrice).lower()), message, timeout=600)
            return jsonify(message), 200
        except:
            return jsonify(status_codes[2]), 404
    return jsonify(message), 200

    
@app.route('/api/stats/', methods=['GET'])
def sendStats():
    return "Data for statistical analysis"
   
# Running flask application
if __name__ == '__main__':
    # setting up port with default port settings
    try:
        port = int(sys.argv[1]) # takes the port provided as argument during function call
    except:
        port = 5000 # default port when argument not provided during script call

    # starting server
    app.run(host = '0.0.0.0', port=port, threaded=True)    