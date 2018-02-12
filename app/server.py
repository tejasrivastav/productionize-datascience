#!flask/bin/python
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__)))
import json

from flask import render_template
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
from notebook.predict import predict

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    data = request.form.getlist("data[]", type=float)
    return jsonify(predict(data))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
