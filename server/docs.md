# RESTful API documentation

## Project Structure Summary
The project basically scraps the contents from web and gives the client products having reasonable pricing. We have the following scripts:
1.  `scrapper.py` : scrapping script 

## Host and port
```python
host_port = 'http://localhost://8090/'
```

## Accessing API
 Operation | Procedure (REST API link) 
| --------- | ----------|
| To access all products | `host_port/products/` |
| To access products under a paricular category | `host_port/products/category/?category='category` Here, category are of category id in integer` i.e. 1, 2, 3... 
| To access individual product | `host_port/product/?sku='sku content'` |

## Output format
### For individual product
#### Command
```js
http://localhost:8080/product/?sku=AC014EL02H18WNAFAMZ
```
#### Output
```json
{
  "product": {
    "category": "Computing & Gaming", 
    "date_issued": "Tue May 15 11:56:49 2018", 
    "id": 35, 
    "image_link": "https://np.daraz.io/QeKz0soJGKTGqwy1lpvvXlVwtRg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/04/154/1.jpg?5576", 
    "link": "https://www.daraz.com.np/acer-e5-476g-i5-7th-gen-4gb1tb2gb-14-nvidia-geforce-mx-130-2gb-ddr5-graphics-laptop-black-45140.html", 
    "name": "Acer E5-476G I5 7th Gen 4GB/1TB/2GB 14\" NVIDIA Geforce MX 130 2GB DDR5 Graphics Laptop - Black", 
    "prices": [
      {
        "currency": "NPR", 
        "date": "Tue May 15 11:56:49 2018", 
        "discount": "-13%", 
        "id": 1, 
        "price": 63945
      }, 
      {
        "currency": "NPR", 
        "date": "Tue May 15 11:58:19 2018", 
        "discount": "-13%", 
        "id": 2, 
        "price": 63945
      }
    ], 
    "sku": "AC014EL02H18WNAFAMZ"
  }
}
```