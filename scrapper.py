import pymysql
import requests 
import urllib
from bs4 import BeautifulSoup as soup   
import time 
import json       
import threading

# gives a cursor
def get_cursor():
    DB_conf_data = json.load(open('./config/DBconf.json', 'r+', encoding='utf-8'))
    db = pymysql.connect(DB_conf_data['server'], DB_conf_data['username'], DB_conf_data['password'], DB_conf_data['database'])
    return db.cursor()

# this function loads up the urls of the page to be scraped
def get_target_page_urls(database_cursor):
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

# get primary key if present in data just to update the price
def search_product_in_DB(database_cursor, sku_data):
    search_product_DB_Q = "SELECT * FROM products WHERE sku = '%s'" % sku_data
    database_cursor.execute(search_product_DB_Q)
    product_DB = database_cursor.fetchone()
    if product_DB:
        return product_DB[0]
    else:
        return None

# scraper function that takes single url and scrap the contents
def scraper(database_connection, url_to_scrape):
    db = database_connection
    database_cursor = db.cursor()
    r = requests.get(url_to_scrape)
    main_soup = soup(r.text, 'html.parser')
    # marking category
    product_cat = main_soup.h1
    for tag in product_cat.find_all('span'):
        tag.replace_with('')
    product_category = product_cat.text # category
    product_group = main_soup.find_all('div', {'class' : ['sku', '-gallery']})
    # iteration over each product
    for item in product_group:
        product_sku = item['data-sku']
        # Now search for the product in database relation
        primary_key_inDB = search_product_in_DB(database_cursor, product_sku) # acts as foreign key of price -> product
        if primary_key_inDB:
            product_content = item.a.find_all("div") # contents with the product card
            product_discount = product_content[1].find_all("span")[0].text # discount
            price_content = product_content[1].find_all("span")[1]
            product_price = int(price_content.span.find_all("span")[1]['data-price']) # price
            insert_price_Q = "INSERT INTO prices(prod_id, price, discount, date, currency_iso)VALUES('%d','%d','%s', CURRENT_TIMESTAMP,'%s')" % (primary_key_inDB, product_price, product_discount, 'NPR')
            update_product_date_Q = "UPDATE products SET date_updated = CURRENT_TIMESTAMP WHERE id = '%d'" % (primary_key_inDB) # aka foreign key
            try:
                database_cursor.execute(insert_price_Q)
                database_cursor.execute(update_product_date_Q)
                db.commit()
                print("[%s] Updated existing product" % primary_key_inDB)
            except:
                db.rollback()
        # as the product is new (not in database), let's make a new entry for product and prices
        else:
            if item.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
                product_content = item.a.find_all("div") # contents within the product card
                product_discount = product_content[1].find_all("span")[0].text # discount
                price_content = product_content[1].find_all("span")[1]
                product_price = int(price_content.span.find_all("span")[1]['data-price']) # price
                product_name = item.a.h2.text.strip().replace('\u00a0','') # name
                product_link = item.a['href'] # link
                product_image_link = product_content[0].noscript.img['src'] # image link
                if product_category == 'Cables':
                    cat_id = 1
                elif product_category == 'Wireless Speakers':
                    cat_id = 2
                elif product_category == 'Computing & Gaming':
                    cat_id = 3
                elif product_category == 'Smartwatches':
                    cat_id = 4
                elif product_category == 'VR Headsets':
                    cat_id = 5
                else:
                    cat_id = 0
                insert_product_Q = "INSERT INTO products(sku, product_name, category, link, image_link)VALUES('%s', '%s', '%d', '%s', '%s')" % (product_sku, product_name.strip().replace('\u2013',''), cat_id, product_link, product_image_link)
                try:
                    database_cursor.execute(insert_product_Q)
                    foreign_key = search_product_in_DB(database_cursor, product_sku) # foreign key to link price with product
                    database_cursor.execute("INSERT INTO prices(prod_id, price, discount, date, currency_iso)VALUES('%d','%d','%s', CURRENT_TIMESTAMP, '%s')" % (foreign_key, product_price, product_discount, 'NPR'))
                    db.commit()
                    print("[%s] Added new product and price" % product_sku)
                except:
                    db.rollback()
                    print("[%s] Could not add this product" % product_sku)
    database_cursor.close()
            
# single object that acts as single thread to acheive multithreading            
class Thread4Scrap (threading.Thread):
   def __init__(self, threadID, name, db_connection, url_to_scrape):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.connection =  db_connection
        self.page = url_to_scrape
      
   def run(self):
      print ("Starting " + self.name)
      scraper(self.connection, self.page)
      print ("Exiting " + self.name)

if __name__ == '__main__':
    # getting database connection
    with open('./config/DBconf.json', 'r+', encoding='utf-8') as fp:
        DB_conf_data = json.load(fp)
        fp.close()

    # connect to database and set cursor to execute query
    db = pymysql.connect(DB_conf_data['server'], DB_conf_data['username'], DB_conf_data['password'], DB_conf_data['database'])
    cursor = db.cursor()

    # get urls to scrape
    target_page_urls = get_target_page_urls(cursor)
 
    connections = []
    # creating list of connections
    for i in range(0, len(target_page_urls)):
        connections.append(pymysql.connect(DB_conf_data['server'], DB_conf_data['username'], DB_conf_data['password'], DB_conf_data['database']))
        
    # creating objects (aka thread)
    thread_objects = []
    for i in range(0, len(target_page_urls)):
        thread_objects.append(Thread4Scrap(i+1, "Thread - %d" % (i+1), connections[i], target_page_urls[i]))
    
    # running threads
    for thread in thread_objects:
        thread.start()
    
