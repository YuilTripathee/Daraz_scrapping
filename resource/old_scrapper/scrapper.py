# old scrapper system (now depreciated)
import requests # to make HTTP requests
import urllib   # standard python URL library
import urllib.parse # parse object from standard python URL library
import json       # standard python JSON libary
import time       # standard python library for time
from bs4 import BeautifulSoup as soup   # import beautiful soup module to scrap data
import pickle   # pickle module to support python serializable format (aka Pickle)

# class to determine a unit price format
class Price:
    def __init__(self, price_object):
        self.id = price_object['id']
        self.discount = price_object['discount']
        self.price = price_object['price']
        self.date = price_object['date']
        self.currency = price_object['currency']
        pass
    
    def __repr__(self):
        return '%s' % self.id

# class to determine a unit product format
class Product:
    def __init__(self, data_object):
        self.sku = data_object['sku']
        self.id = data_object['id']
        self.name = data_object['name']
        self.category = data_object['category']
        self.link = data_object['link']
        self.image_link = data_object['image_link']
        self.date_issued = data_object['date_issued']
        self.prices = []
        for item in data_object['prices']:
            unit = Price(item)
            self.prices.append(unit)
            pass
        self.recent_price_id = self.prices[-1].id
    
    def __repr__(self):
        return '%s' % (self.sku)

# scraper class
class Scraper:
    # initializes variable objects
    def __init__(self, url):
        self.r = requests.get(url)
        self.my_soup = soup(self.r.text, 'html.parser')
        self.cat = self.my_soup.h1
        for tag in self.cat.find_all('span'):
            tag.replace_with('')
        self.category = self.cat.text
        self.containers = self.my_soup.find_all('div', {'class' : ['sku', '-gallery']})
        
    def run(self, encoded_list, index_count):
        # iterate the scrapping process over each item
        for item in self.containers:
            # check for discount
            if item.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
                # scraping items to mine
                prod_cont = item.a.find_all("div")
                product_discount = prod_cont[1].find_all("span")[0].text
                price_mini = prod_cont[1].find_all("span")[1]
                product_price = int(price_mini.span.find_all("span")[1]['data-price'])
                sku = item['data-sku']
                name = item.a.h2.text.strip().replace('\u00a0','')
                link = item.a['href']
                image_link = prod_cont[0].noscript.img['src']
                # binary search if it is previous product, check by SKU, and update price only
                index = get_index(encoded_list, sku)
                if index != None: 
                    # get old object
                    old_object = encoded_list[index]
                    # make price dictionary to push to price object
                    last_price = old_object.prices[-1].id
                    price = {
                        'id' : last_price + 1,
                        'discount' : product_discount,
                        'price' : int(product_price),
                        'date' : time.asctime(),
                        'currency' : 'NPR'
                    }
                    # push to price object
                    old_object.prices.append(Price(price))
                # if new item, push to JSON
                else:
                    # increment the index
                    index_count += 1
                    # initialise data to push
                    product = {
                        'sku' : sku,
                        'id' : index_count,
                        'name' : name,
                        'category' : self.category,
                        'link' : link,
                        'image_link' : image_link,
                        'date_issued' : time.asctime(),
                        "prices" : [
                            {
                                "id": 1,
                                "discount": product_discount,
                                "price": product_price,
                                "date": time.asctime(),
                                "currency": "NPR"
                            }
                        ]
                    }
                    # push to Product list as object
                    encoded_list.append(Product(product))
                    pass
            # flush out items without discount
            else:
                pass  

# class for search and sort algorithm to manage data in json (now in array of dictionaries)
class SearchSort:
    # sorts the data making SKU as index
    def sort_by_sku(self, json_list, reference):
        if len(json_list) < 2: return json_list # if the array has single element, it is already sorted
        ipivot = len(json_list)//2        # dividing the array
        pivot = json_list[ipivot]         # partitioning the array
        if type(json_list[0]) is int:
            before = [x for i,x in enumerate(json_list) if x <= pivot and i != ipivot] 
            after = [x for i,x in enumerate(json_list) if x > pivot and i != ipivot]   
            return self.sort_by_sku(before, reference) + [pivot] + self.sort_by_sku(after, reference)    
        elif type(json_list[0]) is dict:
            before = [x for i,x in enumerate(json_list) if x[reference] <= pivot[reference] and i != ipivot] 
            after = [x for i,x in enumerate(json_list) if x[reference] > pivot[reference] and i != ipivot]   
            return self.sort_by_sku(before, reference) + [pivot] + self.sort_by_sku(after, reference)    
    
    # performs binary search on the data by sku
    def search_sku(self, encoded_list, sku):
        lo, hi = 0, len(encoded_list)
        while lo < hi:
            mid = (hi + lo)//2
            if encoded_list[mid].sku == sku:
                return mid
            elif encoded_list[mid].sku > sku:
                hi = mid
            else:
                lo = mid + 1
        return None
    
# function to find if product from scrap is already present and returns its index in array
def get_index(encoded_list, sku_data):
    search = SearchSort()
    index_num = search.search_sku(encoded_list, sku_data)
    return index_num

# encoder to encode JSON object (dict now) to Python objects
def encodeFromJSON(list):
    new_list = []
    for item in list:
        new_list.append(Product(item))
    return new_list

# decoder to decode Python objects to array of dict (for JSON)
def decodetoJSON(list):
    new_list = []
    for item in list:
        prices = []
        for price in item.prices:
            price = {
                'id' : price.id,
                'discount' : price.discount,
                'price' : price.price,
                'date' : price.date,
                'currency' : price.currency
            }
            prices.append(price)
        product = {
            'sku' : item.sku,
            'id' : item.id,
            'name' : item.name,
            'category' : item.category,
            'link' : item.link,
            'image_link' : item.image_link,
            'date_issued' : item.date_issued,
            'prices' : prices
        }
        new_list.append(product)
    return new_list

# main function
if __name__ == '__main__': 
    
    ## start of initiation ##
    
    # scraping variable
    with open('config/scrapsite.json', 'r+', encoding='utf-8') as fp:
        file_content = json.load(fp)
        urls_to_scrape = file_content["sites"]
        fp.close()

    # check it file is empty and initializes the structure of database
    with open('database/dataset.json', 'r+', encoding='utf-8') as fp:
        # check if data.json is empty and write empty array into it, also initialize config.json
        if fp.read() == '':
            fp.write('[]')
            fp.close()
            with open('database/config.json','w', encoding='utf-8') as ip:
                # initialization for config.json
                init = {
                    'id_count' : 0
                }
                json.dump(init, ip, indent=4)
                ip.close()
    
    # extracting data from internal source
    with open('database/dataset.json', 'r', encoding='utf-8') as fp:
        data_from_file = json.load(fp)
        fp.close()      
    
    # to initialise index for file having data
    count = len(data_from_file)
    with open('database/config.json','w', encoding='utf-8') as fp:
        init_full = {
            'id_count' : count
        }
        json.dump(init_full, fp, indent=4)
        fp.close()
    
    # encoding list from JSON to standard python objects
    ss = SearchSort()
    encoded_list = encodeFromJSON(ss.sort_by_sku(data_from_file, 'sku'))

    ## end of initiation ##
    ## start scraping robot ##
    for url in urls_to_scrape:
        scrap = Scraper(url)
        scrap.run(encoded_list, count)
    ## end of scraping robot operation ##

    # decoding list from list of python objects to JSON convertible
    json_list = decodetoJSON(encoded_list)

    # writing into JSON file
    with open('database/dataset.json', 'w', encoding="utf-8") as fp:
        ss = SearchSort()
        json.dump(ss.sort_by_sku(json_list, 'sku'), fp, indent=4, sort_keys=False)
        fp.close()

    # updating configuration file
        key_config = {
            "id_count" : len(encoded_list)
        }
        # writing into config file
        with open('database/config.json', 'w', encoding="utf-8") as fp:
            json.dump(key_config, fp, indent=4, sort_keys=True) 
            fp.close()    

    # encoded list of python objects in serializable
    with open('database/serializable.p', 'wb') as fp:
        fp.write(pickle.dumps(encoded_list))
        fp.close
    
    print('Operation performed over %s products.' % len(encoded_list))