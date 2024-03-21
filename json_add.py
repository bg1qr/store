import requests,random
from flask import *
import json
app = Flask(__name__)
@app.route('/')
def home():
	#return '<h1>tele : @b_4qr</h1>'
	with open("date.json", "r") as f:
	   	a=f.read()
	   	return a
@app.route('/baqer',methods=["POST","GET"])
def add_json():
    descr=request.args.get('descr')
    price=request.args.get('price')
    name=request.args.get('name')
    id=int("".join(random.choice("1234567890")for i in range(5)))
    with open("date.json", "a") as f:
    	add={ "name": name, "description": descr, "price": price ,"id": id}
    	s=json.dumps(add)
    	f.write(s+",") 	
app.run(host='0.0.0.0', port=8081)    	