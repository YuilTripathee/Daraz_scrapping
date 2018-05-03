# importing necessary libraries
import requests
import urllib
import urllib.parse
import json
import time
from bs4 import BeautifulSoup as soup
import bs4

# price class to check and push price
class Price:
    def __init__(self, product_discount, product_price):
        self.id = 1
        self.product_discount = product_discount
        self.product_price = int(product_price)
    
    def insertprice(self):
        self.price_data = {
            'id' : self.id,
            'disount' : self.product_discount,
            'price' : self.product_price,
            'date' : time.asctime(),
            'currency' : 'NPR'
        }
        self.price = []
        self.price.append(self.price_data)
        return self.price

    def updateprice(self, json_data_unit):
        self.data_store = json_data_unit
        previous_id = self.data_store['price'][-1]['id']
        self.id = previous_id + 1
        self.price_data = {
            'id' : self.id,
            'discount' : self.product_discount,
            'price' : self.product_price,
            'date' : time.asctime(),
            'currency' : 'NPR'
        }
        self.data_store['price'].append(self.price_data)
        pass

# product class for pushing data into json
class Product:
    def __init__(self, sku_data, name, link, image_link, primary_key, category, discount, price):
        self.sku = sku_data
        self.id = primary_key
        self.name = name
        self.link = link
        self.image_link = image_link
        self.date_issued = time.asctime()
        self.category = category
        self.product_discount = discount
        self.product_price = price
        self.price = []
        pass

    def pushdata(self, json_data):
        price = Price(self.product_discount, self.product_price)
        self.price = price.insertprice()
        product = {
            'sku' : self.sku,
            'id' : self.id,
            'name' : self.name,
            'category' : self.category,
            'link' : self.link,
            'image_link' : self.image_link,
            'date-issued' : self.date_issued,
            'price' : self.price
        }
        json_data.append(product)
    
# scraping class
class Scraper:
    def __init__(self, url):
        self.r = requests.get(url)
        self.my_soup = soup(self.r.text, 'html.parser')
        self.cat = self.my_soup.h1
        for tag in self.cat.find_all('span'):
            tag.replace_with('')
        self.category = self.cat.text
        self.containers = self.my_soup.find_all('div', {'class' : ['sku', '-gallery']})
        self.product = self.containers[1]
          
    def run(self, json_data, key_count):
        # iterate over each item
        for item in self.containers:
            # check for discount
            if item.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
                # binary search if it is previous product, check by SKU
                if index_finder(json_data, self.scrap_sku(item)):
                    # scrap the price and compare
                    index = index_finder(json_data, self.scrap_sku(item))
                    data = json_data[index]
                    prod_cont = item.a.find_all("div")
                    product_discount = prod_cont[1].find_all("span")[0].text
                    price_mini = prod_cont[1].find_all("span")[1]
                    product_price = price_mini.span.find_all("span")[1]['data-price']
                    p = Price(product_discount, product_price)
                    p.updateprice(data)
                # if new item, push to JSON
                else:
                    # increment the index
                    key_count += 1
                    # scrap
                    prod_cont = item.a.find_all("div")
                    sku = self.scrap_sku(item)
                    name = item.a.h2.text.strip().replace('\u00a0','')
                    link =  item.a['href']
                    image_link = prod_cont[0].noscript.img['src']
                    product_discount = prod_cont[1].find_all("span")[0].text
                    price_mini = prod_cont[1].find_all("span")[1]
                    product_price = price_mini.span.find_all("span")[1]['data-price']
                    # push to Product object
                    p = Product(sku, name, link, image_link, key_count, self.category, product_discount, product_price)
                    # push to JSON
                    p.pushdata(json_data)
            else:
                print('No discount here')  
        # update index in our primary key (id)
        key_config = {
            "id_count" : key_count
        }
        # writing into config file
        with open('database/config.json', 'w', encoding="utf-8") as fp:
            json.dump(key_config, fp, indent=4, sort_keys=True) 
            fp.close()    
        
    # returns stock collection unit
    def scrap_sku(self, item):
        self.prod_sku = item['data-sku']
        return self.prod_sku
    
# class for search and sort algorithm to manage data in json (now in array of dictionaries)
class SearchSort:
    # sorts the data making SKU as index
    def sort_by_sku(self, json_list, reference):
        if len(json_list) < 2: return json_list
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
    def search_sku(self, json_list, sku):
        lo, hi = 0, len(json_list)
        while lo < hi:
            mid = (hi + lo)//2
            if json_list[mid]['sku'] == sku:
                return mid
            elif json_list[mid]['sku'] > sku:
                hi = mid
            else:
                lo = mid + 1
        return False
    
# function to find if product from scrap is already present and returns its index in array
def index_finder(json_list, sku_data):
    search = SearchSort()
    index_num = search.search_sku(json_list, sku_data)
    return index_num

# main function
if __name__ == '__main__': 
    # scraping variable
    scrap = Scraper('https://www.daraz.com.np/led-tvs/')

    # extracting data from internal source
    with open('database/dataset.json', 'r', encoding="utf-8") as fp:
        data_file = json.load(fp)
    # configuration text file for id
    with open('database/config.json', 'r') as fp:
        key_number = json.load(fp)

    # sort data in order of sku
    ss = SearchSort()
    ss.sort_by_sku(data_file, 'sku')
    
    scrap.run(data_file, key_number['id_count'])
    
    # write to the file finally
    with open('database/dataset.json', 'w', encoding="utf-8") as fp:
        json.dump(ss.sort_by_sku(data_file, 'sku'), fp, indent=4, sort_keys=False)
        fp.close()
    print('Total data : ', len(data_file))
