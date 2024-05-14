from flask import Flask, jsonify, request

app = Flask (__name__)


purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de compra 1',
        'items': [ 
            {
                'id':1,
                'description':'Item do pedido 1',
                'price': 20.00

            }
        ]
    }  
 ]


# GET purchase_order
# GET purchase_order por id
# GET purchase_order por item
# POST purchase_order
# POST purchase order item

@app.route('/')
def home():
    return "Hello World!!"

@app.route('/purchase_orders')
def get_purchase_order():
    return jsonify(purchase_orders)


@app.route('/purchase_orders/<int:id>')
def get_purchase_order_by_id(id):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po)
    return jsonify({'message':'Objeto nao encontrado'})


@app.route('/purchase_orders', methods= ['POST'])
def create_purchase_order():
    request_data = request.get_json()
    purchase_order = {
        'id': request_data['id'],
        'description': request_data['description'],
        'items':[]
    }
    purchase_orders.append(purchase_order)
    return jsonify(purchase_order)



@app.route('/purchase_orders/<int:id>/items', method= ['POST'])
def create_purchase_orders_item(id):
    req_data = request.get_json()

    for po in purchase_orders:
        if po['id'] == id:
            po['items'].append({
                'id':req_data['id'],
                'description':req_data['description'],
                'price':req_data['price']
            })
            return jsonify(po)
    
    return jsonify({'message':'pedido {} nao encontrado'.format(id)})


app.run(port= 5000)