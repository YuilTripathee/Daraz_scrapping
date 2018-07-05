<<<<<<< HEAD
# importing request module and beautiful soup module
import requests
from bs4 import BeautifulSoup as soup
import urllib
import urllib.parse

# fetching down the page in web
r = requests.get('https://www.daraz.com.np/earphones-headsets/')

# making a soup
my_soup = soup(r.text, 'html.parser')
containers = my_soup.find_all("div",{"class":['sku', '-gallery']})

# Writing into CSV
filename = "products.csv"
f = open(filename, 'w')

fileheaders = 'product_name, product_hash, product_link, product_image_link, product_discount, product_price\n'

f.write(fileheaders)

# Expoting to the CSV format
try:
    for product in containers:
        if product.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
            prod_cont = product.a.find_all("div")
            product_name = product.a.h2.text.strip().replace(',',' ')
            product_hash = product['data-sku']
            product_link = product.a['href']
            product_image_link = prod_cont[0].noscript.img['src']
            product_discount = prod_cont[1].find_all("span")[0].text
            price_mini = prod_cont[1].find_all("span")[1]
            product_price = price_mini.span.find_all("span")[1]['data-price']
            f.write(product_name.replace('\xa0','') + "," + product_hash + "," + urllib.parse.quote_plus(product_link) + "," + urllib.parse.quote_plus(product_image_link) + "," + product_discount + "," + product_price + "\n")
    f.close()
    print('File written sucessfully')
    pass
except Exception:
    print('Script failed')
    raise
=======
# importing request module and beautiful soup module
import requests
from bs4 import BeautifulSoup as soup
import urllib
import urllib.parse

# fetching down the page in web
r = requests.get('https://www.daraz.com.np/earphones-headsets/')

# making a soup
my_soup = soup(r.text, 'html.parser')
containers = my_soup.find_all("div",{"class":['sku', '-gallery']})

# Writing into CSV
filename = "products.csv"
f = open(filename, 'w')

fileheaders = 'product_name, product_hash, product_link, product_image_link, product_discount, product_price\n'

f.write(fileheaders)

# Expoting to the CSV format
try:
    for product in containers:
        if product.find_all("div")[1].find_all("span")[0]['class'] == ['sale-flag-percent']:
            prod_cont = product.a.find_all("div")
            product_name = product.a.h2.text.strip().replace(',',' ')
            product_hash = product['data-sku']
            product_link = product.a['href']
            product_image_link = prod_cont[0].noscript.img['src']
            product_discount = prod_cont[1].find_all("span")[0].text
            price_mini = prod_cont[1].find_all("span")[1]
            product_price = price_mini.span.find_all("span")[1]['data-price']
            f.write(product_name.replace('\xa0','') + "," + product_hash + "," + urllib.parse.quote_plus(product_link) + "," + urllib.parse.quote_plus(product_image_link) + "," + product_discount + "," + product_price + "\n")
    f.close()
    print('File written sucessfully')
    pass
except Exception:
    print('Script failed')
    raise
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
