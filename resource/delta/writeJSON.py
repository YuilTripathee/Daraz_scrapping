import json       # standard python JSON libary

# class to determine a unit price format
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

# class to determine a unit product format
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
        return '%s' % (self.sku)

# encoder to encode JSON object (dict now) to Python objects
def encodeFromJSON(list):
    new_list = []
    for item in list:
        new_list.append(Product(item))
    return new_list

# decoder to decode Python objects to array of dict (for JSON)
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
            'category' : item.category,
            'link' : item.link,
            'image_link' : item.image_link,
            'date_issued' : item.date_issued,
            'prices' : prices
        }
        new_list.append(product)
    return new_list

# main() function
if __name__ == '__main__':
    # extracting data from internal source
    with open('database/dataset.json', 'r', encoding='utf-8') as fp:
        data_from_file = json.load(fp)    
        encoded_list = encodeFromJSON(data_from_file)
    
    # looping to check if price varies
    items_to_show = []
    for item in encoded_list:
        # kill the loop when item has single price instance and nothing to compare
        if item.prices[-1].id == 1:
            break
        # renders the list of items that has price variation
        if item.prices[-1].price < item.prices[-2].price:
            items = {
                'name' : item.name,
                'image_url' : item.image_link,
                'discount' : item.prices[-1].discount.strip().replace('-',''),
                'new_price' : item.prices[-1].price,
                'old_price' : item.prices[-2].price,
                'link' : item.link
            } 
            items_to_show.append(items)
    
    with open('data_to_send.json', 'w') as fp:
        fp.write(json.dumps(items_to_show, indent=4))
        fp.close()
    