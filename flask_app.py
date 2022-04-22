import json
import requests

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

my_app = Flask(__name__)


@my_app.route('/')
def index():
    return '<a href="http://127.0.0.1:4000/upload_files"><button>SEND</button></a>'


@my_app.route('/upload_files', methods=['POST', 'GET'])
def upload_files():
    data_got_from_front = {
        'forename': 'NAME',
        'surname': 'SURNAME',
        'country': 'GERMANY'
    }

    with open('my_json_file.json', 'w') as f:
        json.dump(data_got_from_front, f)

    r = requests.post('http://127.0.0.1:3000/get_files',
                      files={'file': (
                          'the_json_recieve_name',
                          open('my_json_file.json', 'rb')
                      )}
                      )

    print(r.status_code)  # HTTP Status Code (500, 404, 400, 200 etc.)
    print(r.content)  # The response from API

    return r.content
