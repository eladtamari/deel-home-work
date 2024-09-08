
from flask import Flask
from requests import get
import pymongo


MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def reverse_ip():       
    ip = get_public_ip()
    return reversed(ip)

def get_public_ip():
     ip = get('https://api.ipify.org').content.decode('utf8')
     return ip

def conn_db():
   
    myclient = pymongo.MongoClient('mongodb://root:example@mongo:27017/')
    #myclient = pymongo.MongoClient('mongodb://root:example@localhost:8081/')

    mydb = myclient['IPS']
    mycol = mydb["PUBLIC"]
    mydict = { "MY_IP": "1.2.3.4" }

    x = mycol.insert_one(mydict)

if __name__ == '__main__':
    #conn_db()
    app.run(host="0.0.0.0")
