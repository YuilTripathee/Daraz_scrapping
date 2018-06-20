# importing request module and beautiful soup module
import requests
from bs4 import BeautifulSoup as soup
import urllib
import urllib.parse

# fetching down the page in web
r = requests.get('https://www.daraz.com.np/phones-tablets/')

# making a soup
my_soup = soup(r.text, 'html.parser')
containers = my_soup.find_all("div",{"class":['sku', '-gallery']})

# Writing into CSV
filename = "products.csv"
f = open(filename, 'w')

fileheaders = 'product_brand, product_name, product_hash, product_link, product_image_link, product_discount, product_price, product_review\n'

f.write(fileheaders)

# return brand name of the product
def get_product_brand(product):
    for container in product.h2.find_all("span"):
        if container['class'][0] == 'brand':
            brand = container.text
    return brand

# return brand name of the product
def get_product_name(product):
    for container in product.h2.find_all("span"):
        if container['class'][0] == 'name':
            name = container.text
    return name

# return the reviews of the product
def get_review(product_container):
    try:
        for container in product_container:
            if container['class'][0] == 'total-ratings':
                return container.text
    except:
        return 0

# return the image link of the product
def get_image_link(product_container):
    try:
        for container in product_container:
            if container['class'][0] == 'image-wrapper':
                return container.img["data-src"]
    except:
        pass

# checks the product discount
def check_discount(product):
    try:
        for container in product.find_all("span"):
            if container['class'][0] == 'sale-flag-percent':
                return True
    except:
        return False

# returns the price details
def get_price_details(product_container):
    try:
        for container in product_container:
            if container['class'][0] == 'price-container':
                product_discount = container.find_all("span")[0].text
                price_mini = container.find_all("span")[1]
                product_price = price_mini.span.find_all("span")[1]['data-price']
                break
        return product_discount, product_price
    except:
        pass

# Expoting to the CSV format
try:
    for product in containers:
        if check_discount(product):
            product_brand = get_product_brand(product)
            product_name = get_product_name(product)
            product_hash = product['data-sku']
            product_link = product.a['href']
            product_container = product.a.find_all("div")
            product_image_link = get_image_link(product_container)
            product_discount, product_price = get_price_details(product_container)
            product_review = get_review(product_container)
            print('\n')
            print("Brand\t: ", product_brand)
            print("Name\t: ", product_name)
            print("SKU\t: ", product_hash)
            print("URL\t: ", product_link)
            print("Image\t: ", product_image_link)
            print("Disc\t: ", product_discount)
            print("Review\t: ", product_review)
            # f.write(product_brand + product_name.replace(',','') + "," + product_hash + "," + urllib.parse.quote_plus(product_link) + "," + urllib.parse.quote_plus(product_image_link) + "," + product_discount + "," + product_price + product_review + "\n")
            # print("Product written")
        else:
            print('No discount')
    print('File written sucessfully')
except Exception:
    print('Script failed')
    raise
 
'''
    NEW DATA MODELS TO CRAWL:
        1. BRAND
        2. REVIEWS
'''