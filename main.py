import json

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'message': 'Index', 'data': None})


@app.route('/send_files', methods=['POST'])
def index():
    file = request.files['file']

    if file:
        filename = secure_filename(file.filename)
        file.save(filename)

        with open(filename, 'r') as f:
            data = json.load(f)

        database_communication = do_stuff_with_data(data)

        if database_communication:
            return jsonify({'success': True, 'message': 'All worked fine'})
        else:
            return jsonify({'success': False, 'message': 'Something went wrong'})

    return jsonify({'success': False, 'message': 'No file'})


