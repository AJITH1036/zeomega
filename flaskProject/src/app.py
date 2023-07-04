from flask import Flask,json,jsonify,request,Response,abort


app = Flask(__name__)

@app.route('/')
def hello():
    f = open("./data.json","r")
    return f