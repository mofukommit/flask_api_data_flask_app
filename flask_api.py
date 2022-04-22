import json

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

my_api = Flask(__name__)


@my_api.route('/')
def index():
    return jsonify({'message': 'Index', 'data': None})


@my_api.route('/get_files', methods=['POST'])
def get_files():
    file = request.files['file']

    if file:
        filename = secure_filename(file.filename)
        file.save(filename)

        with open(filename, 'r') as f:
            data = json.load(f)

        return jsonify({'success': True, 'message': 'DONE'})

        #database_communication = do_stuff_with_data(data)

        #if database_communication:
        #    return jsonify({'success': True, 'message': 'All worked fine'})
        #else:
        #    return jsonify({'success': False, 'message': 'Something went wrong'})

    return jsonify({'success': False, 'message': 'No file'})


