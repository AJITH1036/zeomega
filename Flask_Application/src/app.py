from flask import Flask,jsonify,render_template
import socket

app= Flask(__name__)


def connStatus():
   hostname = socket.gethostname()
   host_ip = socket.gethostbyname(hostname)
   return str(hostname),str(host_ip)

@app.route('/')
def hello():
    return "<h3>Hello world</h3>"


@app.route('/health',methods=['GET'])
def health():
    return jsonify(
        status="UP"
    )   
 
@app.route('/index',methods=['GET'])
def template():
    HOSTNAME,IP = connStatus()
    return render_template("index.html",hostname = HOSTNAME,ip = IP  )

