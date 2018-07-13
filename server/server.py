import sys
import json
import pymysql
import time

# add SSL encryption module for standard library
import ssl

# Flask microservice modules
from quart import Quart, jsonify, request
from werkzeug.contrib.cache import SimpleCache

# Flask app and cache declaration

app = Quart(__name__)
cache = SimpleCache()
# Note : apply this in development environment only
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# app.config['JSON_SORT_KEYS'] = False

# Acquire database config info for connection
with open('../config/DBconf.json', 'r', encoding='utf-8') as fp:
    DB_data = json.load(fp)
    fp.close()

# Acquire status codes for response message status
with open('status.json', 'r', encoding='utf-8') as fp:
    status_codes = json.load(fp)
    fp.close()

# Takes products list, minPrice and maxPrice and return filtered list
def validatePriceRange(list_of_products, minPrice = None, maxPrice = None, fullPrice = False):
    new_product_list = []
    # for the list of products that comes with the list of prices
    if fullPrice:
        if minPrice:
            new_product_list = list(filter(lambda x : x['prices'][-1]['price'] >= minPrice, list_of_products))
        if maxPrice:
            new_product_list = list(filter(lambda x : x['prices'][-1]['price'] <= maxPrice, new_product_list))          
        if minPrice is None and maxPrice is None:
            return list_of_products
    # for the list of products that comes with single price
    else:
        if minPrice:
            new_product_list = list(filter(lambda x : x['prices']['price'] >= minPrice, list_of_products))
        if maxPrice:
            new_product_list = list(filter(lambda x : x['prices']['price'] <= maxPrice, new_product_list))                  
        if minPrice is None and maxPrice is None:
            return list_of_products
    return new_product_list

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
            'date_updated' : one_product_tuple[9].strftime('%c'),
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
        # returns a list of dictionaries if all prices invoked
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
        # returns a last entry of a single distionary if single price invoked
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
def getCategory(database_cursor, all_category = False, category_list = None, category_id = None):
    # returns the whole set of categories present in the database
    if all_category == True:
        getCategoryQ = "SELECT * FROM category"
        try:
            database_cursor.execute(getCategoryQ)
            catResult = database_cursor.fetchall()
            return_list = []
            for data in catResult:
                categoryData = {
                    'id' : data[0],
                    'category' : data[1],
                    'sub_category' : data[2]
                } 
                return_list.append(categoryData)
            return return_list
        except:
            pass
    # returns the list of category objects when array of category supplied
    elif category_list is not None:
        return_list = []
        for category_id in category_list:
            getCategoryQ = "SELECT * FROM category WHERE id = '%d'" % (category_id)
            try:
                database_cursor.execute(getCategoryQ)
                catResult = database_cursor.fetchone()
                categoryData = {
                    'id' : catResult[0],
                    'category' : catResult[1],
                    'sub_category' : catResult[2]
                } 
                return_list.append(categoryData)
            except:
                break       
        return return_list
    # returns an object of category when a single category <int> supplied
    else:
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

# find category for a single product when SKU supplied
def findCategoryID(database_cursor, sku):
    findCategoryQ = "SELECT category FROM products WHERE sku = '%s'" % (sku)
    try:
        database_cursor.execute(findCategoryQ)
        DBResult = database_cursor.fetchone()
        category_id = DBResult[0]
        return category_id
    except:
        raise

# returns the list of category for the product as mentioned in skustr
def getCategoryGroup(database_cursor, skustr):
    SKU = skustr.split(',')
    raw_list = []
    for sku in SKU:
        database_cursor.execute("SELECT category FROM products WHERE sku = '%s';"%sku)
        raw_list.append(database_cursor.fetchone())
    cooked_list = []
    for data in raw_list:
        cooked_list.append(data[0])
    fine_list = list(set(cooked_list))
    if len(fine_list) == 1:
        category_list = getCategory(database_cursor, category_id=fine_list[0])
    else:
        category_list = getCategory(database_cursor, category_list=fine_list)        
    return category_list

# returns the list of products as referred in skustr
def getProductGroup(database_cursor, skustr, fullPrice=False):
    SKUs = skustr.split(',')
    products_list = []
    for sku in SKUs:
        product_unit = getProduct(database_cursor, sku, fullPrice = fullPrice)
        products_list.append(product_unit)
    return products_list

# returns an inidividual product when sku of the product provided
def getProduct(database_cursor, sku, fullPrice = False):
    get1ProductSKU = "SELECT * FROM products WHERE sku = '%s'" % (sku)
    try:
        database_cursor.execute(get1ProductSKU)
        product_result = database_cursor.fetchone()
        product = buildProduct(database_cursor, one_product_tuple=product_result, fullPrice = fullPrice)
        return product
    except:
        return int('1+2+3')

# route to provide info about the backend
@app.route('/api/', methods=['GET'])
async def send_info_msg():
    data = {
        'data' : {
            'provider' : 'Product monitoring system',
            'content-type' : 'application/json',
            'host' : 'localhost',
            'server' : 'Gunicorn',
            'python_version' : '3.6.5',
            'developer' : 'Yuil Tripathee',
            'date' : time.asctime()
        }
    }
    return jsonify(data)

# route to return the number of random products as specified
@app.route('/api/products/', methods=['GET'])
async def sendSomeProducts():
    args = request.args
    # getting the number of products
    try:
        number = int(args.get('number', None))
        if number == 0:
            return jsonify(status_codes[5]), 500
    except TypeError:
        return jsonify(status_codes[5]), 500
    except ValueError:
        return jsonify(status_codes[4]), 500
    
    # choosing if all the prices tracked to be displayed or not    
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
        # making database cursor
    database_cursor = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor()
    # dumping out data
    return fetchProductRandom(database_cursor, number, fullPrice=fullPrice)
def fetchProductRandom(database_cursor, number, fullPrice=False):
    getRandomQ = "SELECT * FROM products ORDER by RAND() LIMIT %d;" % number
    try:
        database_cursor.execute(getRandomQ)
        product_results_tuple = database_cursor.fetchall()
        data = {
            "category" : getCategory(database_cursor, all_category=True),
            "products" : buildProduct(database_cursor, product_results_tuple=product_results_tuple, fullPrice=fullPrice)
        }
        message = status_codes[1]
        message['data'] = data
        return jsonify(message), 200
    except:
        return jsonify(status_codes[2]), 404

# route to provide all the products in the database
@app.route('/api/products/all/', methods=['GET'])
async def sendAllProducts():
    args = request.args
    # fetching minimum price range from URL
    try:
        minPrice = int(args.get('minPrice', None))
        if minPrice == 0:
            minPrice = None
    except TypeError:
        minPrice = None
    except ValueError:
        return jsonify(status_codes[4]), 500
    
    # fetching maximum price range from URL
    try:
        maxPrice = int(args.get('maxPrice', None))
        if maxPrice == 0:
            maxPrice = None
        if maxPrice < minPrice:
            return jsonify(status_codes[3]), 500
    except TypeError:
        maxPrice = None
    except ValueError:
        return jsonify(status_codes[4]), 500

    # taking order field
    order = args.get('order', None)
    if order is None:
        order = None
    elif order == 'reviews':
        order = 'reviews'
    elif order == 'time':
        order = 'date_updated'
    else:
        return jsonify(status_codes[4]), 500
    
    # choosing if all the prices tracked to be displayed or not    
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
    database_cursor = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor()
    return fetchAllProducts(database_cursor, minPrice = minPrice, maxPrice=maxPrice, order=order, fullPrice = fullPrice)
def fetchAllProducts(database_cursor, minPrice = None, maxPrice = None, order = None, fullPrice = False):
    message = cache.get('AllProducts%s%s%s%s' % (minPrice, maxPrice, order, fullPrice))
    if message is None:
        if order == None:
            getAllProductsQ = "SELECT * FROM products ORDER BY 'id' ASC;"
        else:
            getAllProductsQ = "SELECT * FROM products ORDER BY products.%s DESC;" % order 
        try:
            database_cursor.execute(getAllProductsQ)
            product_results_tuple = database_cursor.fetchall()
            products_list = buildProduct(database_cursor, product_results_tuple=product_results_tuple, fullPrice=fullPrice)
            data = {
                "category" : getCategory(database_cursor, all_category=True),
                "products" : validatePriceRange(products_list ,minPrice=minPrice, maxPrice=maxPrice, fullPrice=fullPrice)
            }
            message = status_codes[1]
            message['data'] = data
            cache.set('AllProducts%s%s%s%s' % (minPrice, maxPrice, order, fullPrice), message, timeout=500)
            return jsonify(message), 200
        except:
            return jsonify(status_codes[2]), 404
    return jsonify(message), 200
    
# route to return a search query
@app.route('/api/products/search/', methods=['GET'])
async def sendSearchResults():
    args = request.args
    # get the query to search on database
    try:
        query = args.get('query', None)
        if query is None:
            return jsonify(status_codes[7]), 500
        if query == '':
            return jsonify(status_codes[7]), 500
    except TypeError:
        return jsonify(status_codes[7]), 500
     
    # choosing if all the prices tracked to be displayed or not    
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

    database_cursor = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor()
    return fetchSearchedProduct(database_cursor, query, fullPrice)
def fetchSearchedProduct(database_cursor, search_query, fullPrice = False):
    searchProductQ = "SELECT * FROM `products` WHERE MATCH(brand,name) AGAINST ('%s' IN NATURAL LANGUAGE MODE)" % search_query
    try:
        database_cursor.execute(searchProductQ)
        product_results_tuple = database_cursor.fetchall()
        data = {
            "category" : getCategory(database_cursor, all_category=True),
            "products" : buildProduct(database_cursor, product_results_tuple=product_results_tuple, fullPrice=fullPrice)
        }
        if len(data['products']) is 0:
            return jsonify(status_codes[2]), 404
        message = status_codes[1]
        message['data'] = data
        return jsonify(message), 200
    except:
        return jsonify(status_codes[2]), 404

# route to return the product from the category specified
@app.route('/api/products/category/', methods=['GET'])
async def sendProductInCategory():
    args = request.args
    # getting category number
    try:
        category = int(args.get('category', None))
    except TypeError:
        return jsonify(status_codes[6]), 500
    except ValueError:
        return jsonify(status_codes[4]), 500
     
    # fetching the number of required products
    try:
        number = int(args.get('number', None))
    except TypeError:
        number = None
    except ValueError:
        return jsonify(status_codes[4]), 500
    
    # fetching minimum price range from URL
    try:
        minPrice = int(args.get('minPrice', None))
        if minPrice == 0:
            minPrice = None
    except TypeError:
        minPrice = None
    except ValueError:
        return jsonify(status_codes[4]), 500
    
    # fetching maximum price range from URL
    try:
        maxPrice = int(args.get('maxPrice', None))
        if maxPrice == 0:
            maxPrice = None
        if maxPrice < minPrice:
            return jsonify(status_codes[3]), 500
    except TypeError:
        maxPrice = None
    except ValueError:
        return jsonify(status_codes[4]), 500
        

    # taking order field
    order = args.get('order', None)
    if order is None:
        order = None
    elif order == 'time':
        order = 'date_updated'
    elif order == 'reviews':
        order = 'reviews'
    else:
        return jsonify(status_codes[4]), 500

    # choosing if all the prices tracked to be displayed or not    
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
    database_cursor = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor()
    return fetchCategoryProd(database_cursor, category, number = number, minPrice = minPrice, maxPrice = maxPrice, order = order, fullPrice = fullPrice)
def fetchCategoryProd(database_cursor, category, number = None, minPrice = None, maxPrice = None, order = None, fullPrice = False):
    message = cache.get('CategoryProd%s%s%s%s%s%s' % (category, number, minPrice, maxPrice, order, fullPrice))
    if message is None:
        if number == None:
            if order:
                getCategoryProdQ = "SELECT * FROM products WHERE category = %d ORDER BY products.%s DESC;" % (category, order)
            else:
                getCategoryProdQ = "SELECT * FROM products WHERE category = %d ORDER BY products.id ASC;" % category
            try:
                database_cursor.execute(getCategoryProdQ)
                products_results_tuple = database_cursor.fetchall()
                products_list = buildProduct(database_cursor, product_results_tuple=products_results_tuple, fullPrice=fullPrice)
                data = {
                    "category" : getCategory(database_cursor, category_id=category),
                    "products" : validatePriceRange(products_list, minPrice=minPrice, maxPrice=maxPrice, fullPrice=fullPrice)
                }
                message = status_codes[1]
                message['data'] = data
                cache.set('CategoryProd%s%s%s%s%s%s' % (category, number, minPrice, maxPrice, order, fullPrice), message, timeout=500)
                return jsonify(message), 200
            except:
                return jsonify(status_codes[2]), 404
        else:
            getCategoryProdQ = "SELECT * FROM products WHERE category = %d ORDER BY RAND() LIMIT %d;" % (category, number)
            try:
                database_cursor.execute(getCategoryProdQ)
                products_results_tuple = database_cursor.fetchall()
                data = {
                    "category" : getCategory(database_cursor, category_id=category),
                    "products" : buildProduct(database_cursor, product_results_tuple=products_results_tuple, fullPrice=fullPrice)
            }
                message = status_codes[1]
                message['data'] = data
                return jsonify(message), 200
            except:
                return jsonify(status_codes[2]), 404
    return jsonify(message), 200

# route that return status codes to the browser
@app.route('/api/statusCodes/', methods=['GET'])
async def sendStatusCodes():
    with open('status.json', 'r', encoding='utf-8') as fp:
        return jsonify(json.load(fp)), 200

# route where you set 
@app.route('/api/products/skugroup/', methods=['GET'])
async def sendGroup():
    args = request.args
    # getting the list of SKUs as string with comma separated formats
    try:
        skustr = str(args.get('sku', ''))
    except TypeError:
        return jsonify(status_codes[6]), 500
    except ValueError:
        return jsonify(status_codes[4]), 500

    fullPrice = args.get('fullPrice', False)
    # making fullPrice
    if fullPrice is False:
        fullPrice = False
    elif fullPrice.lower() == 'false':
        fullPrice = False
    elif fullPrice.lower() == 'true':
        fullPrice = True
    else:
        return jsonify(status_codes[3]), 500
    # now get list of SKUs
    if skustr == '':
        return jsonify(status_codes[3]), 500
    # making database cursor
    database_cursor = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor()
    return fetchProductGroup(database_cursor, skustr, fullPrice)
# prepare a whole response data when database_cursor and skustr provided
def fetchProductGroup(database_cursor, skustr, fullPrice):
    message = cache.get('groupProduct%s%s' % (skustr, str(fullPrice).lower()) )
    if message is None:
        try:
            data = {
                "category" : getCategoryGroup(database_cursor, skustr),
                "products" : getProductGroup(database_cursor, skustr, fullPrice) 
            }
            message = status_codes[1]
            message['data'] = data
            cache.set('groupProduct%s%s' %(skustr, str(fullPrice).lower()), message, timeout=600)
            return jsonify(message), 200
        except:
            return jsonify(status_codes[2]), 404
    return jsonify(message), 200

@app.route('/api/product/', methods=['GET'])
async def sendOneProduct():
    args = request.args
    try:
        sku = str(args.get('sku', ''))
        if sku == '':
            return jsonify(status_codes[3]), 500
    except TypeError:
        return jsonify(status_codes[6]), 500
    except ValueError:
        return jsonify(status_codes[4]), 500
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
    database_cursor = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor()
    return fetchoneProduct(database_cursor, sku, fullPrice)
# prepare a whole response message when database_cursor and sku provided
def fetchoneProduct(database_cursor, sku, fullPrice):
    message = cache.get('oneProduct%s%s' %(sku, str(fullPrice).lower()))
    if message is None:
        try:
            data = {
                "category" : getCategory(database_cursor, category_id=findCategoryID(database_cursor, sku)),
                "product" : getProduct(database_cursor, sku, fullPrice = fullPrice)
            }
            message = status_codes[1]
            message['data'] = data
            cache.set('oneProduct%s%s' %(sku, str(fullPrice).lower()), message, timeout=600)
            return jsonify(message), 200
        except:
            return jsonify(status_codes[2]), 404
    return jsonify(message), 200
   
# Running flask application (IP configuration and startup)
if __name__ == '__main__':
    # setting up port with default port settings
    try:
        port = int(sys.argv[1]) # takes the port provided as argument during function call
    except:
        port = 8000 # default port when argument not provided during script call

    # setup SSL encryption route
    ssl_context = ssl.create_default_context(
        ssl.Purpose.CLIENT_AUTH,
    )
    ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 
    ssl_context.set_ciphers('ECDHE+AESGCM')
    ssl_context.load_cert_chain(
        certfile='cert.pem', keyfile='key.pem',
    )
    ssl_context.set_alpn_protocols(['h2', 'http/1.1'])
    # starting server
    app.run(host = '0.0.0.0', port=port, ssl=ssl_context)    
