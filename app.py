from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request

app = Flask(__name__)


@app.route('/auth/', methods=['POST'])
def login():
    return "post to /auth/login/ json{username: str}", 200


if __name__ == '__main__':
    app.run(port=5000)
