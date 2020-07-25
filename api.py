import simplejson

from data import *
from flask import Flask, request, jsonify

from configs import ArbTab_endpoint


app = Flask(__name__)

@app.route('/',methods=['GET'])
def get_thing():
    toReturn = jsonify(get_all_items())
    return toReturn

@app.route(ArbTab_endpoint ,methods=['GET'])
def get_arbitrage():
    toReturn = get_arb_tab()
    print(type(toReturn))
    return toReturn

# Run Server
if __name__ == '__main__':
    app.run(debug=True)

