import pymysql
import requests 
import urllib   
import urllib.parse 
from bs4 import BeautifulSoup as soup   
import time 
import json       
import threading 

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
        return product_DB[1]
    else:
        return None

# scraper function that takes single url and scrap the contents
def scraper(database_cursor, url_to_scrape):
    sql_cursor = database_cursor
    target_page = url_to_scrape
    r = requests.get(target_page)
    main_soup = soup(r.text, 'html.parser')
    product_group = main_soup.find_all('div', {'class' : ['sku', '-gallery']})
    print('Thread Starting')
    for item in product_group:
        '''
            Check if product if available in the database
            if yes just update the price
        '''
        product_sku = item['data-sku']
        # Now search for the product in database relation
        primary_key_inDB = search_product_in_DB(sql_cursor, product_sku)
        if primary_key_inDB:
            product_content = item.a.find_all("div") # contents with the product card
            product_discount = product_content[1].find_all("span")[0].text # discount
            product_price = int(product_content[1].find_all("span")[1].span.find_all("span")[1]['data-price']) # price
            
            '''
                Now, you have to just update the pricing
                    1. Put up the foreign key, and set INSERT query in SQL
                    2. Update new date to the products table for the product
            '''
            print("Existing product : %s " % primary_key_inDB)
            pass
        else:
            '''
                Now, you have got new product (not in database)
                Here's the algorithm:
                    1. Check if product has a discount
                    2. If yes, (3)
                        Else (4)
                    3. Put a new product entry to the database.
                        3.1. Update its price
                    4. Discard working on the product and check on the next iteration
            '''
            if item.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
                print('New product : %s' % product_sku)
                product_content = item.a.find_all("div") # contents within the product card
                # marking category
                product_cat = main_soup.h1
                for tag in product_cat.find_all('span'):
                    tag.replace_with('')
                product_category = product_cat.text # category
                product_discount = product_content[1].find_all("span")[0].text # discount
                price_content = product_content[1].find_all("span")[1]
                product_price = int(price_content.span.find_all("span")[1]['data-price']) # price
                product_name = item.a.h2.text.strip().replace('\u00a0','') # name
                product_link = item.a['href'] # link
                product_image_link = product_content[0].noscript.img['src'] # image link
                '''
                    Now, 
                        1. put a new entry to the database.
                        2. insert a new price
                '''      
'''
    Acheiving multithreading in object oriented style
'''

class Thread4Scrap (threading.Thread):
   def __init__(self, threadID, name, database_cursor, url_to_scrape):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.cursor = database_cursor
      self.page = url_to_scrape
      
   def run(self):
      print ("Starting " + self.name)
      scraper(self.cursor, self.page)
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
    
    '''
        create threads to scrap each page
        and peform concurrently
        (Check architecture if necessary)
    '''
 
    cursors = []
    # creating array of cursors
    for i in range(0, len(target_page_urls)):
        cursors.append(pymysql.connect(DB_conf_data['server'], DB_conf_data['username'], DB_conf_data['password'], DB_conf_data['database']).cursor())
        
    # creating objects
    thread_objects = []
    for i in range(0, len(cursors)):
        thread_objects.append(Thread4Scrap(i+1, "Thread - %d" % (i+1), cursors[i], target_page_urls[i]))
    
    # running threads
    for thread in thread_objects:
        thread.start()
        