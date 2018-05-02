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
        self.product = self.containers[13]
          
    def run(self, json_data):
        for item in self.containers:
            if item.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
                if index_finder(json_data, self.scrap_sku(item)):
                    print('Item already on index')
                    pass
                else:
                    dict_to_add = {
                        'sku' : self.scrap_sku(item)
                    }
                    json_data.append(dict_to_add)
                    print('Item not in index')
                    pass
                
            else:
                print('No discount here')
            
        
    def scrap_sku(self, item):
        self.prod_sku = item['data-sku']
        return self.prod_sku
    

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

    # data collection
    with open('database/dataset.json', 'r') as fp:
        data_file = json.load(fp)
    # configuration text file for id
    with open('database/id_config.txt', 'r') as fp:
        last_id = int(fp.read())
    
    scrap.run(data_file)
    
    # index_rank = index_finder(data_file)
    # if index_rank:   
    #     print('Product already present and price is constant, no need to change')
    # else:
    #     print('This product is not in our database. It should be added.')
    #     dict_to_add = {
    #         'sku' : sku_web
    #     }
    #     data_file.append(dict_to_add)
    
    # write to the file finally
    with open('database/dataset.json', 'w') as fp:
        json.dump(data_file, fp)
    