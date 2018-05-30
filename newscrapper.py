import pymysql
import requests 
import urllib   
import urllib.parse 
from bs4 import BeautifulSoup as soup   
import time 
import json       
import threading 

# scraping function (class system depreciated)
'''
    cursor and url should be passed inside the function that 
    can later work itself to scrap up the contents from the
    web, search on database if product has been previously
    scraped. If yes, make a new tuple in prices relation of 
    the product; and if not, make a new tuple in products 
    relation.
'''
def scraper(database_cursor, url_to_scrape):
    sql_cursor = database_cursor
    target_page = url_to_scrape
    pass

# this function loads up the urls of the page to be scraped
def get_target_page_url(database_cursor):
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

if __name__ == '__main__':
    # getting database connection
    with open('./config/DBconf.json', 'r+', encoding='utf-8') as fp:
        DB_conf_data = json.load(fp)
        fp.close()

    # connect to database and set cursor to execute query
    db = pymysql.connect(DB_conf_data['server'], DB_conf_data['username'], DB_conf_data['password'], DB_conf_data['database'])
    cursor = db.cursor()

    # get urls to scrape
    target_page_url = get_target_page_url(cursor)
    
    '''
        create threads to scrap each page
        and peform concurrently
    '''
    
### Defines scrapping methodology
# # scraper class
# class Scraper:
#     # initializes variable objects
#     def __init__(self, url):
#         self.r = requests.get(url)
#         self.my_soup = soup(self.r.text, 'html.parser')
#         self.cat = self.my_soup.h1
#         for tag in self.cat.find_all('span'):
#             tag.replace_with('')
#         self.category = self.cat.text
#         self.containers = self.my_soup.find_all('div', {'class' : ['sku', '-gallery']})
        
#     def run(self, encoded_list, index_count):
#         # iterate the scrapping process over each item
#         for item in self.containers:
#             # check for discount
#             if item.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
#                 # scraping items
#                 prod_cont = item.a.find_all("div")
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

# get primary key if present in data just to update the price
def get_index(encoded_list, sku_data):
    # need re-build
    primary_key = None # search from database
    return primary_key

# # encoder to encode JSON object (dict now) to Python objects
# def encodeFromJSON(list):
#     new_list = []
#     for item in list:
#         new_list.append(Product(item))
#     return new_list

# # decoder to decode Python objects to array of dict (for JSON)
# def decodetoJSON(list):
#     new_list = []
#     for item in list:
#         prices = []
#         for price in item.prices:
#             price = {
#                 'id' : price.id,
#                 'discount' : price.discount,
#                 'price' : price.price,
#                 'date' : price.date,
#                 'currency' : price.currency
#             }
#             prices.append(price)
#         product = {
#             'sku' : item.sku,
#             'id' : item.id,
#             'name' : item.name,
#             'category' : item.category,
#             'link' : item.link,
#             'image_link' : item.image_link,
#             'date_issued' : item.date_issued,
#             'prices' : prices
#         }
#         new_list.append(product)
#     return new_list

# # main function
# if __name__ == '__main__': 
    
#     ## start of initiation ##
    
#     # declare pages to scrap
#     with open('config/scrapsite.json', 'r+', encoding='utf-8') as fp:
#         file_content = json.load(fp)
#         urls_to_scrape = file_content["sites"]
#         fp.close()

#     # check it file is empty and initializes the structure of database
#     with open('database/dataset.json', 'r+', encoding='utf-8') as fp:
#         # check if data.json is empty and write empty array into it, also initialize config.json
#         if fp.read() == '':
#             fp.write('[]')
#             fp.close()
#             with open('database/config.json','w', encoding='utf-8') as ip:
#                 # initialization for config.json
#                 init = {
#                     'id_count' : 0
#                 }
#                 json.dump(init, ip, indent=4)
#                 ip.close()
    
#     # extracting data from internal source
#     with open('database/dataset.json', 'r', encoding='utf-8') as fp:
#         data_from_file = json.load(fp)
#         fp.close()      
    
#     # to initialise index for file having data
#     count = len(data_from_file)
#     with open('database/config.json','w', encoding='utf-8') as fp:
#         init_full = {
#             'id_count' : count
#         }
#         json.dump(init_full, fp, indent=4)
#         fp.close()
    
#     # encoding list from JSON to standard python objects
#     ss = SearchSort()
#     sku = lambda encoded_list : encoded_list['sku'] 
#     encoded_list = encodeFromJSON(ss.sort_by_sku(data_from_file, 'sku'))

#     ## end of initiation ##

#     ## start scraping robot ##
#     for url in urls_to_scrape:
#         scrap = Scraper(url)
#         scrap.run(encoded_list, count)
#     ## end of scraping robot operation ##

#     # decoding list from list of python objects to JSON convertible
#     json_list = decodetoJSON(encoded_list)

#     # writing into JSON file
#     with open('database/dataset.json', 'w', encoding="utf-8") as fp:
#         ss = SearchSort()
#         json.dump(ss.sort_by_sku(json_list, 'sku'), fp, indent=4, sort_keys=False)
#         fp.close()

#     # updating configuration file
#     with open('database/config.json', 'w', encoding="utf-8") as fp:
#         key_config = {
#             "id_count" : len(encoded_list)
#         }
#         json.dump(key_config, fp, indent=4, sort_keys=True) 
#         fp.close()    
    
#     print('Operation performed over %s products.' % (len(encoded_list)))


# exitFlag = 0

# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       print_time(self.name, self.counter, 10)
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
# thread3 = myThread(3, "Thread-3", 3)

# # Start new Threads
# thread1.start()
# thread2.start()
# thread3.start()
# print("Active threads : ", threading.active_count())
# thread1.join()
# print("Active threads : ", threading.active_count())
# thread2.join()
# print("Active threads : ", threading.active_count())
# thread3.join()
# print("Active threads : ", threading.active_count())

# def calc_square(numbers):
#     for n in numbers:
#         time.sleep(0.3)
#         print('Square : ', n*n)

# def calc_cube(numbers):
#     for n in numbers:
#         print('Cube : ', n*n*n)

# arr = [2, 3, 4, 5, 6, 7]

# t1 = threading.Thread(target=calc_square, args=(arr,))
# t2 = threading.Thread(target=calc_cube, args=(arr,))

# t1.start()
# t2.start()

# t1.join() 
# print ("Exiting Main Thread")