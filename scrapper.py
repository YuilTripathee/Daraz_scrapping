import pymysql
import requests 
import urllib
from bs4 import BeautifulSoup as soup   
import time 
import json       
import threading

# returns a database cursor to perform SQL operations
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
            target_url.append(unit[2])
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

'''
    start of new modules
'''
# checks the discount in the product card given as argument
def check_discount(product):
    try:
        for container in product.find_all("span"):
            if container['class'][0] == 'sale-flag-percent':
                return True
    except:
        return False

# return brand name from the product card given as argument
def get_product_brand(product):
    for container in product.h2.find_all("span"):
        if container['class'][0] == 'brand':
            brand = container.text
    return brand

# return brand name from the product card given as argument
def get_product_name(product):
    for container in product.h2.find_all("span"):
        if container['class'][0] == 'name':
            name = container.text
    return name

# return the image link of the product card given as argument
def get_product_image_link(product_container):
    try:
        for container in product_container:
            if container['class'][0] == 'image-wrapper':
                return container.img["data-src"]
    except:
        pass

# returns the price details for the products provided
def get_price_details(product_container):
    try:
        for container in product_container:
            if container['class'][0] == 'price-container':
                disc_raw = container.find_all("span")[0].text.strip().replace('-','')
                product_discount = int(disc_raw.strip().replace('%',''))
                price_mini = container.find_all("span")[1]
                product_price = int(price_mini.span.find_all("span")[1]['data-price'])
                break
        return product_discount, product_price
    except:
        pass

# return the reviews of the product card given as argument
def get_product_review(product_container):
    try:
        for container in product_container:
            if container['class'][0] == 'total-ratings':
                rev1 = container.text.strip().replace('(','')
                return int(rev1.strip().replace(')',''))
    except:
        return int(0)
    # For the ideal data value, (i.e. 0 if no review) following tweak sould be provided:
    # product_review = get_product_review(products)
    # if product_review is None:
    #     product_review = int(0)

# return the category from the page given as argument
def get_category(page):
    cat_section = page.h1
    for tag in cat_section.find_all('span'):
        tag.replace_with('')
    return cat_section.text

# return the foreign key value for the product
def select_category_id(product_category):
    if product_category.lower() == 'cables':
        cat_id = 1
    elif product_category.lower() == 'smart':
        cat_id = 2
    elif product_category.lower() == 'wireless speakers':
        cat_id = 3
    elif product_category.lower() == 'vr headsets':
        cat_id = 4
    else:
        cat_id = None
    return cat_id
'''
    end of new modules
'''
# scraper function that takes single url and scrap the contents
def scraper(database_connection, url_to_scrape):
    db = database_connection
    database_cursor = db.cursor()
    r = requests.get(url_to_scrape)
    main_soup = soup(r.text, 'html.parser')
    # marking category
    product_category = get_category(main_soup)
    product_group = main_soup.find_all('div', {'class' : ['sku', '-gallery']})
    # iteration over each product
    for product in product_group:
        # getting product sku 
        product_sku = product['data-sku']
        # Now search for the product in database relation
        primary_key_inDB = search_product_in_DB(database_cursor, product_sku) # acts as foreign key of price -> product
        # If the product is already present in our database
        if primary_key_inDB:
            try:
                product_container = product.find_all("div") # all divs inside card listed
                product_discount, product_price = get_price_details(product_container)
                product_review = get_product_review(product_container)
                if product_review is None:
                    product_review = int(0)
                # SQL query to update price to an existing product
                insert_price_Q = "INSERT INTO prices(prod_id, price, discount, date, currency_iso)VALUES('%d','%d','%d', CURRENT_TIMESTAMP,'%s')" % (primary_key_inDB, product_price, product_discount, 'NPR')
                update_product_date_Q = "UPDATE products SET reviews = '%d', date_updated = CURRENT_TIMESTAMP WHERE id = '%d'" % (product_review,primary_key_inDB) # aka foreign key
                try:
                    database_cursor.execute(insert_price_Q)
                    database_cursor.execute(update_product_date_Q)
                    db.commit()
                    print("[%s] Updated existing product" % primary_key_inDB)
                except:
                    db.rollback()
            except:
                continue
        # as the product is new (not in database), the script make a new entry for product and prices
        else:
            if check_discount(product):
                product_container = product.a.find_all("div") # contents within the product card
                product_discount, product_price = get_price_details(product_container)
                product_brand = get_product_brand(product)
                product_name = get_product_name(product)
                product_link = product.a['href'] # link
                product_image_link = get_product_image_link(product_container) # image link
                product_reviews = get_product_review(product_container)
                if product_reviews is None:
                    product_reviews = int(0)
                product_category_id = select_category_id(product_category)
                insert_product_Q = "INSERT INTO products(sku, brand, name, category, link, image_link, reviews) VALUES ('%s', '%s', '%s', '%d', '%s', '%s', '%d');" % (product_sku, product_brand, product_name, product_category_id, product_link, product_image_link, product_reviews)
                try:
                    database_cursor.execute(insert_product_Q)
                    foreign_key = search_product_in_DB(database_cursor, product_sku) # foreign key to link price with product
                    database_cursor.execute("INSERT INTO prices(prod_id, price, discount, date, currency_iso)VALUES('%d','%d','%d', CURRENT_TIMESTAMP, '%s')" % (foreign_key, product_price, product_discount, 'NPR'))
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
