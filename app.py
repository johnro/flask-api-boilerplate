from flask import Flask, jsonify, request

app = Flask(__name__)

fruits = [
    { 
        'fruit': 'Mango', 
        'amount': 2 
    }
]


@app.route('/fruits')
def get_fruits():
    return jsonify(fruits)


@app.route('/fruits', methods=['POST'])
def add_fruit():
    fruits.append(request.get_json())
    return '', 204