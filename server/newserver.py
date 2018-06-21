import sys
import json
import pymysql
import time

# Flask microservice modules
from flask import Flask, jsonify, request
from werkzeug.contrib.cache import SimpleCache

# Flask app and cache declaration
app = Flask(__name__)
cache = SimpleCache()
# Note : apply this in development environment only
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Acquire database config info
with open('../config/DBconf.json', 'r', encoding='utf-8') as fp:
    DB_data = json.load(fp)
    fp.close()

# route to provide info about the backend
@app.route('/api/', methods=['GET'])
def send_info_msg():
    data = {
        'data' : {
            'provider' : 'Product monitoring system',
            'content-type' : 'application/json',
            'host' : 'localhost',
            'server' : 'Werkeug/0.14.1',
            'python_version' : '3.6.5',
            'developer' : 'Yuil Tripathee',
            'date' : time.asctime()
        }
    }
    return jsonify(data)

# Running flask application
if __name__ == '__main__':
    # setting up port with default port settings
    try:
        port = int(sys.argv[1]) # takes the port provided as argument during function call
    except:
        port = 5000 # default port when argument not provided during script call

    # starting server
    app.run(host = '0.0.0.0', port=port, threaded=True)    