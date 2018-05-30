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
            '''
                Now, you have to just update the pricing
                    Put up the foreign key, and set INSERT query in SQL
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
            print('New product : %s' % product_sku)
    print('Thread Ending')       
#             # check for discount
#             if item.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
#                 # scraping items
#                 prod_cont = item.a.find_all("div")
#                 # marking category
#                 # product_cat = main_soup.h1
#                 # for tag in product_cat.find_all('span'):
#                 #     tag.replace_with('')
#                 # product_category = product_cat.text
#                 product_discount = prod_cont[1].find_all("span")[0].text
#                 price_mini = prod_cont[1].find_all("span")[1]
#                 product_price = int(price_mini.span.find_all("span")[1]['data-price'])
#                 sku = item['data-sku']
#                 name = item.a.h2.text.strip().replace('\u00a0','')
#                 link = item.a['href']
#                 image_link = prod_cont[0].noscript.img['src']
#                 # binary search if it is previous product, check by SKU, and update price only
#                 index = get_index(encoded_list, sku)
#                 if index != None: 
#                     # get old object
#                     old_object = encoded_list[index]
#                     # make price dictionary to push to price object
#                     last_price = old_object.prices[-1].id
#                     price = {
#                         'id' : last_price + 1,
#                         'discount' : product_discount,
#                         'price' : int(product_price),
#                         'date' : time.asctime(),
#                         'currency' : 'NPR'
#                     }
#                     # push to price object
#                     old_object.prices.append(Price(price))
#                 # if new item, push to JSON
#                 else:
#                     # increment the index
#                     index_count += 1
#                     # initialise data to push
#                     product = {
#                         'sku' : sku,
#                         'id' : index_count,
#                         'name' : name,
#                         'category' : self.category,
#                         'link' : link,
#                         'image_link' : image_link,
#                         'date_issued' : time.asctime(),
#                         "prices" : [
#                             {
#                                 "id": 1,
#                                 "discount": product_discount,
#                                 "price": product_price,
#                                 "date": time.asctime(),
#                                 "currency": "NPR"
#                             }
#                         ]
#                     }
#                     # push to Product list as object
#                     encoded_list.append(Product(product))
#                     pass
#             # flush out items without discount
#             else:
#                 pass  
'''
    Acheiving multithreading in object oriented style
'''
# import threading
# import time

# exitFlag = 0

# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       print_time(self.name, self.counter, 5)
#       print ("Exiting " + self.name)

# def print_time(threadName, delay, counter):
#    while counter:
#       if exitFlag:
#          threadName.exit()
#       time.sleep(delay)
#       print ("%s: %s" % (threadName, time.ctime(time.time())))
#       counter -= 1

# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# # Start new Threads
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print ("Exiting Main Thread")

if __name__ == '__main__':
    # getting database connection
    with open('./config/DBconf.json', 'r+', encoding='utf-8') as fp:
        DB_conf_data = json.load(fp)
        fp.close()

    # connect to database and set cursor to execute query

    db = pymysql.connect(DB_conf_data['server'], DB_conf_data['username'], DB_conf_data['password'], DB_conf_data['database'])
    cursor = db.cursor()

    # get urls to scrape
    target_page_url = get_target_page_urls(cursor)
    
    '''
        create threads to scrap each page
        and peform concurrently
        (Check architecture if necessary)
    '''
 
    cursors = []
    for i in range(0, len(target_page_url)):
        cursors.append(pymysql.connect(DB_conf_data['server'], DB_conf_data['username'], DB_conf_data['password'], DB_conf_data['database']).cursor())
        threading.Thread(target=scraper, args=(cursors[i], target_page_url[i])).start()
    