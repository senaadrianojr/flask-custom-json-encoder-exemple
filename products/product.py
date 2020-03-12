from app import app, mongo
from flask_negotiate import produces


@app.route('/products', methods=['GET'])
@produces('application/json')
def get():

    data = mongo.db.products.find()

    return {'content': list(data)}, 200
