# importing request module and beautiful soup module
import requests
from bs4 import BeautifulSoup as soup

# fetching down the page in web
r = requests.get('https://www.daraz.com.np/dslr-hybrid-cameras/')

# making a soup
my_soup = soup(r.text, 'html.parser')
containers = my_soup.find_all("div",{"class":['sku', '-gallery']})

# fetching out the output from the soup
output = """"""
output += "Total products : " + str(len(containers)) + '\n\n'
for product in containers:
    output += product.a.text.strip().replace('\xa0', '') + '\n'
    
# writing into the tile
filename = 'output.txt'
fo = open(filename, 'w')
fo.write(output)
print('Output sucessfully written')