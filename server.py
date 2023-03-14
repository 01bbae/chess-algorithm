from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello():
    if request.method == 'POST':
        return 'Hello, World!'
