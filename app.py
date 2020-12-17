import datetime
import re

from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request

app = Flask(__name__)


@app.route('/auth/', methods=['GET'])
def auth():
    return "post to /auth/login/ json{username: str}", 200


@app.route('/auth/login/', methods=['POST'])
def login():
    username = password = ''
    json_parse = request.get_json()
    if not isinstance(request.get_json(), dict):
        return "json required", 400
    else:
        if 'username' in json_parse and 'password' in json_parse:
            username = request.get_json()["username"]
            password = request.get_json()["password"]

        if username == 'admin' and password == 'admin':
            non_decimal = re.compile(r'[^\d]+')
            session_id = non_decimal.sub('', str(datetime.datetime.now()))[:20]
            return make_response(jsonify({'sessionid': session_id}), 200)

        return "Invalid username/password supplied", 400


if __name__ == '__main__':
    app.run()
