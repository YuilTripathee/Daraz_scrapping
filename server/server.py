import json
from flask import Flask, jsonify, request   # import objects from the Flask model

app = Flask(__name__) # define app using flask
portname = 8090

# products database
with open('../database/dataset.json', 'r', encoding='utf-8') as fp:
    products = json.load(fp)
    fp.close()

# mail subscription list
with open('../database/mailsubscrib.json', 'r+', encoding='utf-8') as fp:
    recipents = json.load(fp)
    fp.close()

# simple API response test   
@app.route('/', methods=['GET'])
def test():
    data = {
        'data' : {
            'provider' : 'Yuil Tripathee',
            'host' : '127.0.0.1',
            'port' : portname
        }
    }
    return jsonify(data)

# products
@app.route('/products/', methods=['GET'])
def product_print():
    return jsonify({ "products" : products})

# category of products
@app.route('/products/category/', methods=['GET'])
def category_print():
    args = request.args
    category = args['category']
    category_data = [product for product in products if product['category'] == category]
    return jsonify({ "category" : category_data})

# individual product
@app.route('/product/', methods=['GET'])
def Indi_Product():
    args = request.args
    sku_data = args['sku']
    product_unit = [product for product in products if product['sku'] == sku_data]
    return jsonify({"product" : product_unit[0]})

# running flask app
if __name__ == '__main__':
    app.run(debug=True, port=portname)
