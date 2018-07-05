<<<<<<< HEAD
# importing request module and beautiful soup module
import requests
# importing beautiful soup to scrape
from bs4 import BeautifulSoup as soup
# importing urllib to parse HTML page and to encode URL(check output rendering section)
import urllib
import urllib.parse
# import data library for timestamp
import time
# pages to collect data
pages = ['https://www.daraz.com.np/earphones-headsets/', 
    'https://www.daraz.com.np/earphones-headsets/?page=2',
    'https://www.daraz.com.np/earphones-headsets/?page=3',
    'https://www.daraz.com.np/earphones-headsets/?page=4',
    'https://www.daraz.com.np/earphones-headsets/?page=5',
    'https://www.daraz.com.np/earphones-headsets/?page=6',
    'https://www.daraz.com.np/earphones-headsets/?page=7',
    'https://www.daraz.com.np/earphones-headsets/?page=8',
    'https://www.daraz.com.np/earphones-headsets/?page=9',
    'https://www.daraz.com.np/earphones-headsets/?page=10',
    'https://www.daraz.com.np/earphones-headsets/?page=11',
]
# creating CSV file and writing header data
filename = "products.csv"
f = open(filename, 'w', encoding="utf-8")
fileheaders = 'product_name, product_hash, product_link, product_image_link, date_scraped, product_discount, product_price\n'
f.write(fileheaders)
# scraping engine (using iteration to go through each page)
count = 0
for page in pages:
    # requesting page
    r = requests.get(page)
    # making soup of whole page
    my_soup = soup(r.text, 'html.parser')
    # selecting product containers only
    containers = my_soup.find_all("div",{"class":['sku', '-gallery']})
    try:
        # iterating over each product containers
        for product in containers:
            # choosing if product possess discount or not
            if product.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
                # getting product content
                prod_cont = product.a.find_all("div")
                # getting product name
                product_name = product.a.h2.text.strip().replace(',',' ')
                product_name.replace('\xa0', ' ')
                # getting product's hash value
                product_hash = product['data-sku']
                # getting product link and image link
                product_link = product.a['href']
                product_image_link = prod_cont[0].noscript.img['src']
                # getting discount and price
                product_discount = prod_cont[1].find_all("span")[0].text
                price_mini = prod_cont[1].find_all("span")[1]
                product_price = price_mini.span.find_all("span")[1]['data-price']
                # writing into a CSV file on each iteration of iterations
                f.write(product_name + "," + product_hash + "," + urllib.parse.quote_plus(product_link) + "," + urllib.parse.quote_plus(product_image_link) + "," + time.asctime() + "," + product_discount + "," + product_price + "\n")
        # returns sucess message
        count += 1
        print('Data scraped and written sucessfully from page: ' + str(count))
    except Exception:
        print('Script failed')
        raise
print('Scraping data on earphone/headphones section')

=======
# importing request module and beautiful soup module
import requests
# importing beautiful soup to scrape
from bs4 import BeautifulSoup as soup
# importing urllib to parse HTML page and to encode URL(check output rendering section)
import urllib
import urllib.parse
# import data library for timestamp
import time
# pages to collect data
pages = ['https://www.daraz.com.np/earphones-headsets/', 
    'https://www.daraz.com.np/earphones-headsets/?page=2',
    'https://www.daraz.com.np/earphones-headsets/?page=3',
    'https://www.daraz.com.np/earphones-headsets/?page=4',
    'https://www.daraz.com.np/earphones-headsets/?page=5',
    'https://www.daraz.com.np/earphones-headsets/?page=6',
    'https://www.daraz.com.np/earphones-headsets/?page=7',
    'https://www.daraz.com.np/earphones-headsets/?page=8',
    'https://www.daraz.com.np/earphones-headsets/?page=9',
    'https://www.daraz.com.np/earphones-headsets/?page=10',
    'https://www.daraz.com.np/earphones-headsets/?page=11',
]
# creating CSV file and writing header data
filename = "products.csv"
f = open(filename, 'w', encoding="utf-8")
fileheaders = 'product_name, product_hash, product_link, product_image_link, date_scraped, product_discount, product_price\n'
f.write(fileheaders)
# scraping engine (using iteration to go through each page)
count = 0
for page in pages:
    # requesting page
    r = requests.get(page)
    # making soup of whole page
    my_soup = soup(r.text, 'html.parser')
    # selecting product containers only
    containers = my_soup.find_all("div",{"class":['sku', '-gallery']})
    try:
        # iterating over each product containers
        for product in containers:
            # choosing if product possess discount or not
            if product.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
                # getting product content
                prod_cont = product.a.find_all("div")
                # getting product name
                product_name = product.a.h2.text.strip().replace(',',' ')
                product_name.replace('\xa0', ' ')
                # getting product's hash value
                product_hash = product['data-sku']
                # getting product link and image link
                product_link = product.a['href']
                product_image_link = prod_cont[0].noscript.img['src']
                # getting discount and price
                product_discount = prod_cont[1].find_all("span")[0].text
                price_mini = prod_cont[1].find_all("span")[1]
                product_price = price_mini.span.find_all("span")[1]['data-price']
                # writing into a CSV file on each iteration of iterations
                f.write(product_name + "," + product_hash + "," + urllib.parse.quote_plus(product_link) + "," + urllib.parse.quote_plus(product_image_link) + "," + time.asctime() + "," + product_discount + "," + product_price + "\n")
        # returns sucess message
        count += 1
        print('Data scraped and written sucessfully from page: ' + str(count))
    except Exception:
        print('Script failed')
        raise
print('Scraping data on earphone/headphones section')

>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
f.close()