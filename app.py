from flask import Flask,  jsonify, request, render_template

app=Flask(__name__)

import requests
import time
import json
from pymongo import MongoClient


client = MongoClient('mongodb+srv://andrewarpin:Waxer75123@cluster0.2njwl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.btc
col = db["btc"]

#for x in col.find_one():
for x in col.find({},{ "_id": 0, "bpi": 1}):
  print(x)


@app.route('/')
def index():
     return render_template('index.html')


@app.route('/google-charts/pie-chart')
def google_pie_chart():
    data = {'Task' : 'Hours per Day', 'Work' : 11, 'Eat' : 2, 'Commute' : 2, 'Watch TV' : 2,'Sleep' : 7}
    return render_template('pie-chart.html', data=data)

if __name__ == "__main__":
    app.run()

# url = "https://gas-price.p.rapidapi.com/europeanCountries"

# headers = {
#     'x-rapidapi-host': "gas-price.p.rapidapi.com",
#     'x-rapidapi-key': "1073c61132msh7612d5fb34baeebp1b7e84jsnaec026a057ec"
#     }
    
# while True:    
#     response = requests.request("GET", url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         print(data)  
#         db.CanadaGas.insert_one(data)     
#         time.sleep(86400)
#     else:
#         exit()







