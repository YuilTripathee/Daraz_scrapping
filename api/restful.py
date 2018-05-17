import json
from flask import Flask, jsonify, request   # import objects from the Flask model

app = Flask(__name__) # define app using flask

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
            'provider' : 'Yuil Tripathee'
        }
    }
    return jsonify(data)

# products
@app.route('/products/', methods=['GET'])
def product_print():
    return jsonify(products)

# products in cable category
@app.route('/products/cables/', methods=['GET'])
def cable_print():
    cables = []
    for product in products:
        if product['category'] == 'Cables':
            cables.append(product)
    return jsonify(cables)

# products in wireless speakers category
@app.route('/products/wspeakers/', methods=['GET'])
def wspeakers_print():
    wspeakers = []
    for product in products:
        if product['category'] == 'Wireless Speakers':
            wspeakers.append(product)
    return jsonify(wspeakers)

# products in Computers and Gaming category
@app.route('/products/compugame/', methods=['GET'])
def compugame_print():
    compugame = []
    for product in products:
        if product['category'] == 'Computing & Gaming':
            compugame.append(product)
    return jsonify(compugame)

# products in Smartwatches
@app.route('/products/smartwatch/', methods=['GET'])
def smartwatch_print():
    smartwatch = []
    for product in products:
        if product['category'] == 'Smartwatches':
            smartwatch.append(product)
    return jsonify(smartwatch)

# products in Smartwatches
@app.route('/products/VR_Head/', methods=['GET'])
def VR_Head_print():
    VR_Head = []
    for product in products:
        if product['category'] == 'VR Headsets':
            VR_Head.append(product)
    return jsonify(VR_Head)

# # individual product
# @app.route('/product/<string:sku>/', methods=['GET'])
# def product(sku):
#     product_unit = [product for product in products if product['sku'] == sku]
#     return jsonify({"product" : product_unit[0]})

# individual product
@app.route('/product/', methods=['GET'])
def Indi_Product():
    args = request.args
    sku_data = args['sku']
    product_unit = [product for product in products if product['sku'] == sku_data]
    return jsonify({"product" : product_unit[0]})


# running flask app
if __name__ == '__main__':
    app.run(debug=True, port=8080)
