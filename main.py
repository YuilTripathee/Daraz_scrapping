import requests
from bs4 import BeautifulSoup as soup
import urllib
import urllib.parse
import json

class Scraper:
    def __init__(self, url):
        self.r = requests.get(url)
        self.my_soup = soup(self.r.text, 'html.parser')
        self.containers = self.my_soup.find_all('div', {'class' : ['sku', '-gallery']})
        # self.product = self.containers[2] # testing

    def make_soup(self):
        return self.containers
            
    def scrap_sku(self, item):
        self.prod_sku = item['data-sku']
        print(self.prod_sku)
        return self.prod_sku

    # def discount_classifier(self):
    #     for item in self.containers:
    #         if item.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
    #             print('Discount here')
    #             pass
            
    # def scrap_full(self):
    #     if self.product.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
    #         self.prod_cont = self.product.a.find_all("div")
    #         self.product_name = self.product.a.h2.text.strip().replace(',',' ')
    #         self.product_hash = self.product['data-sku']
    #         self.product_link = self.product.a['href']
    #         self.product_image_link = self.prod_cont[0].noscript.img['src']
    #         self.product_discount = self.prod_cont[1].find_all("span")[0].text
    #         self.price_mini = self.prod_cont[1].find_all("span")[1]
    #         self.product_price = self.price_mini.span.find_all("span")[1]['data-price']
    #         print(self.product_price)
    #     else:
    #         print('No discount on: ', self.product_name)

class SearchSort:
    # sorts the data making SKU as index
    def sort_by_sku(self, json_list):
        if len(json_list) < 2: return json_list
        ipivot = len(json_list)//2        # dividing the array
        pivot = json_list[ipivot]         # partitioning the array
        if type(json_list[0]) is int:
            before = [x for i,x in enumerate(json_list) if x <= pivot and i != ipivot] 
            after = [x for i,x in enumerate(json_list) if x > pivot and i != ipivot]   
            return self.sort_by_sku(before) + [pivot] + self.sort_by_sku(after)    
        elif type(json_list[0]) is dict:
            before = [x for i,x in enumerate(json_list) if x['sku'] <= pivot['sku'] and i != ipivot] 
            after = [x for i,x in enumerate(json_list) if x['sku'] > pivot['sku'] and i != ipivot]   
            return self.sort_by_sku(before) + [pivot] + self.sort_by_sku(after)    
    
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

if __name__ == '__main__': 
    scrap = Scraper('https://www.daraz.com.np/earphones-headsets/')
    sku_web = scrap.scrap_sku()
    # scraped_items = scrap.scrap_full()
    for item in scrap.make_soup():

        pass
    with open('database/dataset.json', 'r') as fp:
        data_file = json.load(fp)
    with open('database/id_config.txt', 'r') as fp:
        last_id = int(fp.read())
    index_rank = index_finder(data_file, sku_web)
    if index_rank:
        print('Product already present and price is constant, no need to change')
    else:
        print('This product is not in our database. It should be added.')
        dict_to_add = {
            'sku' : sku_web
        }
        data_file.append(dict_to_add)
    
    # write to the file finally
    with open('database/dataset.json', 'w') as fp:
        json.dump(data_file, fp)
    