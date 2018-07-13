import sys
import json
import pymysql
import time

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
        }
        # return 'Query executed for the least'
        message = status_codes[1]
        message['data'] = data
        return json.dumps(message, indent=4)
    except:
        # return status_codes[2]
        raise
