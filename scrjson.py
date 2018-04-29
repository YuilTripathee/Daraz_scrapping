# importing request module to fetch down the page
import requests
# importing html parser to parse HTML
import urllib
import urllib.parse
# importing beautiful soup module to scrap things out of HTML
from bs4 import BeautifulSoup as soup
# importing time library for timestamp
import time
import json

# fetching down the page in web
r = requests.get('https://www.daraz.com.np/earphones-headsets/')

# making a soup
my_soup = soup(r.text, 'html.parser') # soup of the whole page
containers = my_soup.find_all("div",{"class":['sku', '-gallery']}) # soup of product containers only

# use only one product (for testing)
product = containers[1]
prod_cont = product.a.find_all("div")
product_name = product.a.h2.text.strip().replace('\u00a0', '')
product_hash = product['data-sku']
product_link = product.a['href']
product_image_link = prod_cont[0].noscript.img['src']
product_discount = prod_cont[1].find_all("span")[0].text
price_mini = prod_cont[1].find_all("span")[1]
product_price = price_mini.find_all("span")[2]['data-price']

# writing into dictionary
products_dataset = [
    {
        'product_id' : 1,
        'product_hash' : product_hash,
        'product_name' : product_name,
        'site_name' : 'Daraz.com.np',
        'product_link' : product_link,
        'product_image_link' : product_image_link,
        'date_created' : time.asctime(),
        'date_modified' : time.asctime(),
        'price' : [
            {
                'price_id' : 1,
                'discount' : product_discount,
                'price' : int(product_price),
                'date' : time.asctime(),
                'currency' : 'NPR'
            }
        ]
    }
]
with open('data.json', 'w') as fp:
    fp.write(json.dumps(products_dataset, sort_keys=False, indent=4))
    fp.close()