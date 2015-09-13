from flask import Blueprint, jsonify

data_controller = Blueprint('data_controller', __name__)

@data_controller.route('/data')
def data():
    data = {
        'hello' : 'world',
        'number' : 42
    }
    return jsonify(data)
