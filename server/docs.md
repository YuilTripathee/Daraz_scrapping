# RESTful API documentation

## Project Structure Summary
The project basically scraps the contents from web and gives the client products having reasonable pricing. We have the following scripts:
1.  `main.py` : scrapping script 
2.  `writeJSON.py` : script to detect changes in prices of product.
3.  `writeHTML.py` : script to generate HTML5 page for rendering products having price drop.  
4.  `sendmail.py` : email client scipt send email for notifying products having price drop.
5.  `sendToDB.py` : script to send the data in database.
6.  `iDB.py` : interactive console to execute SQL queries to the connected database server.
7.  `getch.py` : hold the console to notify for the task to be automated.

## Local JSON data structure summary
The data structure in local database (working during runtime):
1. `config.json` : configuration file for scrapping contents.
2. `dataset.json` : mail local database (all the scraped data written into JSON).
3. `DBconf.json` : configuration file for database (host, port, authentication credentials)
4. `mailsubscrib.json` : list of notification subscribers.
5. `serializable.p` : serializable format (pickle) data from `dataset.json`.

## Host and port
```python
host_port = 'http://localhost://8080/'
```

## Accessing API
 Operation | Procedure (REST API link) 
| --------- | ----------|
| To access all products | `host_port/products/` |
| To access products under a paricular category | `host_port/products/category/?category='category` Here, category are of following types: `Cables`, `Wireless Speakers`, `Computing & Gaming`, `Smartwatches`, `VR Headsets`, etc. 
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