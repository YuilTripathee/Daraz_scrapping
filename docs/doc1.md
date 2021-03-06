---
id: doc1
title: Latin-ish
sidebar_label: Example Page
---

Check the [documentation](https://docusaurus.io) for how to use Docusaurus.

## Lorem

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque elementum dignissim ultricies. Fusce rhoncus ipsum tempor eros aliquam consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus elementum massa eget nulla aliquet sagittis. Proin odio tortor, vulputate ut odio in, ultrices ultricies augue. Cras ornare ultrices lorem malesuada iaculis. Etiam sit amet libero tempor, pulvinar mauris sed, sollicitudin sapien.

## Mauris In Code

```python
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

# scraper function that takes single url and scrap the contents
def scraper_typeA(database_connection, url_to_scrape):
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
            primary_key_inDB = put_price_inDB(database_cursor, product_sku, product_price, product_discount)
            update_product_inDB(database_cursor, primary_key_inDB)
        # as the product is new (not in database), let's make a new entry for product and prices
        else:
            if item.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
                product_content = item.a.find_all("div") # contents within the product card
                product_disc = product_content[1].find_all("span")[0].text.strip.replace('-','') # discount
                product_discount = int(product_disc.strip.replace('&','')) # discount
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
                    put_price_inDB(database_cursor, product_sku, product_price, product_discount)
                except:
                    db.rollback()
                print("[%s] Added new product and price" % product_sku)
    database_cursor.close()

# get primary key if present in data just to update the price
def search_product_in_DB(database_cursor, sku_data):
    search_product_DB_Q = "SELECT * FROM products WHERE sku = '%s'" % sku_data
    database_cursor.execute(search_product_DB_Q)
    product_DB = database_cursor.fetchone()
    if product_DB:
        return product_DB[0]
    else:
        return None
# update the timestamp of product in the database
def update_product_inDB(database_cursor, primary_key_inDB, index = None):
    update_product_date_Q = "UPDATE products SET date_updated = CURRENT_TIMESTAMP WHERE id = '%d'" % (primary_key_inDB) # aka foreign key
    try:
        database_cursor.execute(update_product_date_Q)
        db.commit()
        print("[%s] Updated existing product" % primary_key_inDB)
    except:
        db.rollback()

# inserts an entry of products into the database
def put_product_inDB(database_cursor, product_sku, product_name, category, product_link, product_image_link):
    insert_product_Q = "INSERT INTO products(sku, product_name, category, link, image_link)VALUES('%s', '%s', '%d', '%s', '%s')" % (product_sku, product_name.strip().replace('\u2013',''), category, product_link, product_image_link)
    try:
        database_cursor.execute(insert_product_Q)
    except:
        db.rollback()

# inserts an entry of price into the database
def put_price_inDB(database_cursor, product_sku, product_price, product_discount):
    try:
        foreign_key = search_product_in_DB(database_cursor, product_sku) # foreign key to link price with product
        database_cursor.execute("INSERT INTO prices(prod_id, price, discount, date, currency_iso)VALUES('%d','%d','%s', CURRENT_TIMESTAMP, '%s')" % (foreign_key, product_price, product_discount, 'NPR'))
        db.commit()
        return foreign_key
    except:
        db.rollback()
           
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
      scraper_typeA(self.connection, self.page)
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
    
```

## Nulla

Nulla facilisi. Maecenas sodales nec purus eget posuere. Sed sapien quam, pretium a risus in, porttitor dapibus erat. Sed sit amet fringilla ipsum, eget iaculis augue. Integer sollicitudin tortor quis ultricies aliquam. Suspendisse fringilla nunc in tellus cursus, at placerat tellus scelerisque. Sed tempus elit a sollicitudin rhoncus. Nulla facilisi. Morbi nec dolor dolor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras et aliquet lectus. Pellentesque sit amet eros nisi. Quisque ac sapien in sapien congue accumsan. Nullam in posuere ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin lacinia leo a nibh fringilla pharetra.

## Orci

Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin venenatis lectus dui, vel ultrices ante bibendum hendrerit. Aenean egestas feugiat dui id hendrerit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur in tellus laoreet, eleifend nunc id, viverra leo. Proin vulputate non dolor vel vulputate. Curabitur pretium lobortis felis, sit amet finibus lorem suscipit ut. Sed non mollis risus. Duis sagittis, mi in euismod tincidunt, nunc mauris vestibulum urna, at euismod est elit quis erat. Phasellus accumsan vitae neque eu placerat. In elementum arcu nec tellus imperdiet, eget maximus nulla sodales. Curabitur eu sapien eget nisl sodales fermentum.

## Phasellus

Phasellus pulvinar ex id commodo imperdiet. Praesent odio nibh, sollicitudin sit amet faucibus id, placerat at metus. Donec vitae eros vitae tortor hendrerit finibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque vitae purus dolor. Duis suscipit ac nulla et finibus. Phasellus ac sem sed dui dictum gravida. Phasellus eleifend vestibulum facilisis. Integer pharetra nec enim vitae mattis. Duis auctor, lectus quis condimentum bibendum, nunc dolor aliquam massa, id bibendum orci velit quis magna. Ut volutpat nulla nunc, sed interdum magna condimentum non. Sed urna metus, scelerisque vitae consectetur a, feugiat quis magna. Donec dignissim ornare nisl, eget tempor risus malesuada quis.
