from flask import Flask, request, jsonify
import commands
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/hello")
def hello():
    out = commands.getoutput('python print-hello.py')
    return out

    
@app.route("/run01", methods=['GET','POST'])
def run01():
    json_data = json.loads(request.data)
    # return jsonify(json_data)
    return json_data

    


@app.route("/run02")
def run02():
    return 'this is run02'


@app.route('/api/auth')
def auth():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    return jsonify(token=generate_token(email, password))