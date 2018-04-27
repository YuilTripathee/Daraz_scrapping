# importing request module and beautiful soup module
import requests
from bs4 import BeautifulSoup as soup
import urllib
import urllib.parse

# fetching down the page in web
r = requests.get('https://www.daraz.com.np/dslr-hybrid-cameras/')

# making a soup
my_soup = soup(r.text, 'html.parser')
containers = my_soup.find_all("div",{"class":['sku', '-gallery']})

# # fetching out the output from the soup
# output = """"""
# output += "Total products : " + str(len(containers)) + '\n\n'
# for product in containers:
#     output += product.a.text.strip().replace('\xa0', '') + '\n'
    
# # writing into the text file
# filename = 'output.txt'
# fo = open(filename, 'w')
# fo.write(output)
# print('Output sucessfully written')

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
            product_name = product.a.h2.text.strip().replace('\xa0','')
            product_hash = product['data-sku']
            product_link = product.a['href']
            product_image_link = prod_cont[0].noscript.img['src']
            product_discount = prod_cont[1].find_all("span")[0].text
            price_mini = prod_cont[1].find_all("span")[1]
            product_price = price_mini.span.find_all("span")[1]['data-price']
            # print('Name of product :\n'+ product_name)
            # print('Product hash value :\n' + product_hash)
            # print('Product Link:\n' + product_link)
            # print('Product Image Link:\n' + product_image_link)
            # print('Product Discount:\n' + product_discount)
            # print('Product Price:\n' + product_price)
            # print('\n')
            f.write(product_name + "," + product_hash + "," + urllib.parse.quote_plus(product_link) + "," + urllib.parse.quote_plus(product_image_link) + "," + product_discount + "," + product_price + "\n")
            pass
    else:
        print('\nNo discount product\n')
        pass
    f.close()
    print('File written sucessfully')
    pass
except Exception:
    print('Script failed')
    raise
