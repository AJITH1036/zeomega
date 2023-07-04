from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/hello', methods=['GET'])
def hello():
    response = {'message': 'Hello, world!'}
    return jsonify(response)
 
@app.route('/api/hello', methods=['POST'])
def saveProduct():
      product = {}
      data = request.get_json()
      product.update(data)
      return jsonify(product)


if __name__ == '__main__':
    app.run()
