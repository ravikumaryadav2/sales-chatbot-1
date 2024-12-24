from flask import Flask, request, jsonify
from inventory import get_inventory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/inventory', methods=['GET'])
def inventory():
    return jsonify(get_inventory())

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query')
    inventory = get_inventory()
    results = [product for product in inventory if query.lower() in product['name'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)