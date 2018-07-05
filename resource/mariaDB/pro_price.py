<<<<<<< HEAD
import pymysql
import json
import datetime
def pretty_date(datetimeobject):
    t = datetimeobject
    return t.strftime('%c')
    
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
                'date' : pretty_date(price[4]),
                'currency' : price[5]
            }
            price_list.append(price_unit)
    except:
        raise
    return price_list

def get_products(cursor, category, sku):
    if category != None:
        get_product_by_cat_Q = "SELECT * FROM products WHERE category = '%d';" % category
        try:
            cursor.execute(get_product_by_cat_Q)
            product_results = cursor.fetchall()
            array_of_products = []
            for data in product_results:
                product_unit = {
                    'id' : data[0],
                    'sku' : data[1],
                    'name' : data[2],
                    'category' : data[3],
                    'link' : data[4],
                    'image_link' : data[5],
                    'date_issued' : pretty_date(data[6]),
                    'date_updated' : pretty_date(data[7]),
                    'prices' : get_prices(cursor, data[0])
                }
                array_of_products.append(product_unit)
            return array_of_products
        except:
            print('[err] Unable to fetch data from the database.')
            raise
    elif sku != None:
        get_product_by_sku_Q = "SELECT * FROM products WHERE sku = '%s';" % sku
        try:
            cursor.execute(get_product_by_sku_Q)
            product_results = cursor.fetchall()
            array_of_products = []
            for data in product_results:
                product_unit = {
                    'id' : data[0],
                    'sku' : data[1],
                    'name' : data[2],
                    'category' : data[3],
                    'link' : data[4],
                    'image_link' : data[5],
                    'date_issued' : pretty_date(data[6]),
                    'date_updated' : pretty_date(data[7]),
                    'prices' : get_prices(cursor, data[0])
                }
                array_of_products.append(product_unit)
            return array_of_products
        except:
            print('[err] Unable to fetch data from the database.')
            raise
    else:
        get_product_Q = "SELECT * FROM products;"
        try:
            cursor.execute(get_product_Q)
            product_results = cursor.fetchall()
            array_of_products = []
            for data in product_results:
                product_unit = {
                    'id' : data[0],
                    'sku' : data[1],
                    'name' : data[2],
                    'category' : data[3],
                    'link' : data[4],
                    'image_link' : data[5],
                    'date_issued' : pretty_date(data[6]),
                    'date_updated' : pretty_date(data[7]),
                    'prices' : get_prices(cursor, data[0])
                }
                array_of_products.append(product_unit)
            return array_of_products
        except:
            print('[err] Unable to fetch data from the database.')
            raise

if __name__ == '__main__':
    message_log = 0
    # getting database configuration
    with open('../../config/DBconf.json', 'r+', encoding='utf-8') as fp:
        DB_data = json.load(fp)
        fp.close()
    
    # getting array of products
    db = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database'])
    message_log = message_log + 1
    print('[%d] Sucessfully connected to the database.' % message_log)
    cursor = db.cursor()

    array_of_products, message_log = get_products(cursor, category = 1, sku = None), message_log + 1
    print('[%d] Products with prices sucessfully loaded from database' % message_log)
    
    with open('latestdata.json', 'w', encoding='utf-8') as fp:
        json.dump(array_of_products, fp, indent=4, sort_keys=True)
        fp.close()
        message_log = message_log + 1
        print('[%d] JSON file written sucessfully' % message_log)

    message_log = message_log + 1
    print("[%d] Program executed sucessfully" % message_log)
=======
import pymysql
import json
import datetime
def pretty_date(datetimeobject):
    t = datetimeobject
    return t.strftime('%c')
    
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
                'date' : pretty_date(price[4]),
                'currency' : price[5]
            }
            price_list.append(price_unit)
    except:
        raise
    return price_list

def get_products(cursor, category, sku):
    if category != None:
        get_product_by_cat_Q = "SELECT * FROM products WHERE category = '%d';" % category
        try:
            cursor.execute(get_product_by_cat_Q)
            product_results = cursor.fetchall()
            array_of_products = []
            for data in product_results:
                product_unit = {
                    'id' : data[0],
                    'sku' : data[1],
                    'name' : data[2],
                    'category' : data[3],
                    'link' : data[4],
                    'image_link' : data[5],
                    'date_issued' : pretty_date(data[6]),
                    'date_updated' : pretty_date(data[7]),
                    'prices' : get_prices(cursor, data[0])
                }
                array_of_products.append(product_unit)
            return array_of_products
        except:
            print('[err] Unable to fetch data from the database.')
            raise
    elif sku != None:
        get_product_by_sku_Q = "SELECT * FROM products WHERE sku = '%s';" % sku
        try:
            cursor.execute(get_product_by_sku_Q)
            product_results = cursor.fetchall()
            array_of_products = []
            for data in product_results:
                product_unit = {
                    'id' : data[0],
                    'sku' : data[1],
                    'name' : data[2],
                    'category' : data[3],
                    'link' : data[4],
                    'image_link' : data[5],
                    'date_issued' : pretty_date(data[6]),
                    'date_updated' : pretty_date(data[7]),
                    'prices' : get_prices(cursor, data[0])
                }
                array_of_products.append(product_unit)
            return array_of_products
        except:
            print('[err] Unable to fetch data from the database.')
            raise
    else:
        get_product_Q = "SELECT * FROM products;"
        try:
            cursor.execute(get_product_Q)
            product_results = cursor.fetchall()
            array_of_products = []
            for data in product_results:
                product_unit = {
                    'id' : data[0],
                    'sku' : data[1],
                    'name' : data[2],
                    'category' : data[3],
                    'link' : data[4],
                    'image_link' : data[5],
                    'date_issued' : pretty_date(data[6]),
                    'date_updated' : pretty_date(data[7]),
                    'prices' : get_prices(cursor, data[0])
                }
                array_of_products.append(product_unit)
            return array_of_products
        except:
            print('[err] Unable to fetch data from the database.')
            raise

if __name__ == '__main__':
    message_log = 0
    # getting database configuration
    with open('../../config/DBconf.json', 'r+', encoding='utf-8') as fp:
        DB_data = json.load(fp)
        fp.close()
    
    # getting array of products
    db = pymysql.connect(DB_data['server'], DB_data['username'], DB_data['password'], DB_data['database'])
    message_log = message_log + 1
    print('[%d] Sucessfully connected to the database.' % message_log)
    cursor = db.cursor()

    array_of_products, message_log = get_products(cursor, category = 1, sku = None), message_log + 1
    print('[%d] Products with prices sucessfully loaded from database' % message_log)
    
    with open('latestdata.json', 'w', encoding='utf-8') as fp:
        json.dump(array_of_products, fp, indent=4, sort_keys=True)
        fp.close()
        message_log = message_log + 1
        print('[%d] JSON file written sucessfully' % message_log)

    message_log = message_log + 1
    print("[%d] Program executed sucessfully" % message_log)
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
