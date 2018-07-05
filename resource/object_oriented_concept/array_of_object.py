<<<<<<< HEAD
import json

class Price:
    def __init__(self, price_object):
        self.id = price_object['id']
        self.discount = price_object['discount']
        self.price = price_object['price']
        self.date = price_object['date']
        self.currency = price_object['currency']
        pass
    
    def __repr__(self):
        return '%s' % self.id

class Product:
    def __init__(self, data_object):
        self.sku = data_object['sku']
        self.id = data_object['id']
        self.name = data_object['name']
        self.category = data_object['category']
        self.link = data_object['link']
        self.image_link = data_object['image_link']
        self.date_issued = data_object['date_issued']
        self.prices = []
        for item in data_object['prices']:
            unit = Price(item)
            self.prices.append(unit)
            pass
        self.recent_price_id = self.prices[-1].id
    
    def __repr__(self):
        return '%s\t' % (self.sku)

def encodeFromJSON(list):
    new_list = []
    for item in list:
        new_list.append(Product(item))
    return new_list

def decodetoJSON(list):
    new_list = []
    for item in list:
        prices = []
        for price in item.prices:
            price = {
                'id' : price.id,
                'discount' : price.discount,
                'price' : price.price,
                'date' : price.date,
                'currency' : price.currency
            }
            prices.append(price)
        product = {
            'sku' : item.sku,
            'id' : item.id,
            'name' : item.name,
            'link' : item.link,
            'image_link' : item.image_link,
            'date_issued' : item.date_issued,
            'prices' : prices
        }
        new_list.append(product)
    return new_list

if __name__ == '__main__':
    # extracting data from internal source
    with open('data.json', 'r', encoding='utf-8') as fp:
        data_file = json.load(fp)
    
    encoded_list = encodeFromJSON(data_file)
=======
import json

class Price:
    def __init__(self, price_object):
        self.id = price_object['id']
        self.discount = price_object['discount']
        self.price = price_object['price']
        self.date = price_object['date']
        self.currency = price_object['currency']
        pass
    
    def __repr__(self):
        return '%s' % self.id

class Product:
    def __init__(self, data_object):
        self.sku = data_object['sku']
        self.id = data_object['id']
        self.name = data_object['name']
        self.category = data_object['category']
        self.link = data_object['link']
        self.image_link = data_object['image_link']
        self.date_issued = data_object['date_issued']
        self.prices = []
        for item in data_object['prices']:
            unit = Price(item)
            self.prices.append(unit)
            pass
        self.recent_price_id = self.prices[-1].id
    
    def __repr__(self):
        return '%s\t' % (self.sku)

def encodeFromJSON(list):
    new_list = []
    for item in list:
        new_list.append(Product(item))
    return new_list

def decodetoJSON(list):
    new_list = []
    for item in list:
        prices = []
        for price in item.prices:
            price = {
                'id' : price.id,
                'discount' : price.discount,
                'price' : price.price,
                'date' : price.date,
                'currency' : price.currency
            }
            prices.append(price)
        product = {
            'sku' : item.sku,
            'id' : item.id,
            'name' : item.name,
            'link' : item.link,
            'image_link' : item.image_link,
            'date_issued' : item.date_issued,
            'prices' : prices
        }
        new_list.append(product)
    return new_list

if __name__ == '__main__':
    # extracting data from internal source
    with open('data.json', 'r', encoding='utf-8') as fp:
        data_file = json.load(fp)
    
    encoded_list = encodeFromJSON(data_file)
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
    decoded_list = decodetoJSON(encoded_list)