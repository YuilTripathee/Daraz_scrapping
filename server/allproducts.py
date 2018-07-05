import sys
import json
import pymysql
import time

<<<<<<< HEAD
# Flask microservice modules
from flask import Flask, jsonify, request
from werkzeug.contrib.cache import SimpleCache

# Flask app and cache declaration
app = Flask(__name__)
cache = SimpleCache()
# Note : apply this in development environment only
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

=======
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
# Acquire database config info
with open('../config/DBconf.json', 'r', encoding='utf-8') as fp:
    DB_data = json.load(fp)
    fp.close()

# Acquire status codes for response message status
with open('status.json', 'r', encoding='utf-8') as fp:
    status_codes = json.load(fp)
    fp.close()

database_cursor = database_cursor = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database']).cursor()
def validatePriceRange(list_of_products, minPrice = None, maxPrice = None, fullPrice = False):
    new_product_list = []
    # for the list of products that comes with the list of prices
<<<<<<< HEAD
    if fullPrice == True:
=======
    if fullPrice:
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
        if minPrice:
            new_product_list = list(filter(lambda x : x['prices'][-1]['price'] >= minPrice, list_of_products))
        if maxPrice:
            new_product_list = list(filter(lambda x : x['prices'][-1]['price'] <= maxPrice, new_product_list))          
<<<<<<< HEAD
=======
        if minPrice is None and maxPrice is None:
            return list_of_products
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
    # for the list of products that comes with single price
    else:
        if minPrice:
            new_product_list = list(filter(lambda x : x['prices']['price'] >= minPrice, list_of_products))
        if maxPrice:
            new_product_list = list(filter(lambda x : x['prices']['price'] <= maxPrice, new_product_list))                  
<<<<<<< HEAD
=======
        if minPrice is None and maxPrice is None:
            return list_of_products
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
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

<<<<<<< HEAD
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

def fetchProductRandom(database_cursor, number, fullPrice=False):
    getRandomQ = "SELECT * FROM products ORDER by RAND() LIMIT %d" % number
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

def fetchAllProducts(database_cursor, minPrice = None, maxPrice = None, order = None, fullPrice = False):
    if order == None:
        getAllProductsQ = "SELECT * FROM products ORDER BY 'id' ASC;"

    else:
        getAllProductsQ = "SELECT * FROM products ORDER BY '%s' DESC;" % order 
    try:
        database_cursor.execute(getAllProductsQ)
        product_results_tuple = database_cursor.fetchall()
        data = {
            "category" : getCategory(database_cursor, all_category=True),
            "products" : validatePriceRange(buildProduct(database_cursor, product_results_tuple=product_results_tuple), minPrice=minPrice, maxPrice=maxPrice)
=======
def fetchAllProducts(database_cursor, minPrice = None, maxPrice = None, order = None, fullPrice = False):
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
            "products" : validatePriceRange(products_list ,minPrice=minPrice, maxPrice=maxPrice)
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
        }
        # return 'Query executed for the least'
        message = status_codes[1]
        message['data'] = data
        return json.dumps(message, indent=4)
    except:
<<<<<<< HEAD
        return status_codes[2]
    
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
=======
        # return status_codes[2]
        raise
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
