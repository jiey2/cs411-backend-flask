import simplejson
 
from data import *
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources=r'/api/*', headers='Content-Type')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/',methods=['GET'])
def get_thing():
    toReturn = jsonify(get_all_items())
    return toReturn

@app.route('/arbitrage' ,methods=['GET'])
@cross_origin()
def get_arbitrage():
    response = {"data": get_arb_tab()}
    # response = jsonify(response)

    return response

@app.route('/item/<string:encodeName>', methods=['GET'])
@cross_origin()
def get_the_item(encodeName):
    response = get_item(encodeName)
    if len(response) == 0:
        return {"found": False}
    else:
        return {
            "found": True,
            "data": response
        }

    

# Run Server
if __name__ == '__main__':
    app.run()

