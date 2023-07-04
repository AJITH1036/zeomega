from flask import Flask,jsonify,render_template
import socket


app= Flask(__name__)
app.debug = True
def connStatus():
   hostname = socket.gethostname()
   host_ip = socket.gethostbyname(hostname)
   return str(hostname),str(host_ip)  
 
@app.route('/index',methods=['GET'])
def template():
    HOSTNAME,IP = connStatus()
    return render_template("index.html",hostname = HOSTNAME,ip = IP  )

if __name__ == '__main__': 
   app.run()