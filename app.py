from flask import Flask,  jsonify, request, render_template

app=Flask(__name__)

import requests
import time
import json
from pymongo import MongoClient

client = MongoClient('mongodb+srv://andrewarpin:Waxer75123@cluster0.2njwl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.Currency
col = db["Currency"]

#BTC
while True:    
    r = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
    if r.status_code == 200:

        data = r.json()
        print(data)  
        db.Currency.insert_one(data)     
        

        curve = {'Task': 'Price'}
        num = 0

        for x in col.find({},{ "_id": 1,"rates": 1}): 
                num += 1                
                a = num
                b = (x['rates']['usd']['value'])    
                convert = b        
                curve[a] = b
        print(curve)                                  
        print(convert)

        @app.route('/')
        def index():
            a = convert
            return render_template('index.html', a = a )


        @app.route('/google-charts/curve-chart')
        def google_pie_chart():  
            data = curve
            return render_template('curve-chart.html', data = data)

        @app.route('/google-charts/barchart')
        def google_barchart():  
            data = curve
            return render_template('barchart.html', data = data)

        if __name__ == "__main__":
            app.run()
        time.sleep(60)  
    else:
            exit()


#GAS PRICES
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

# BTC
# while True:    
#     r = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
#     if r.status_code == 200:
#         data = r.json()
#         print(data)  
#         db.btc.insert_one(data)     
#         time.sleep(60)
#     else:
#         exit()


# for x in col.find({},{ "_id": 1,"time": 1, "bpi": 1}):                 
#         a = (x['time']['updated'])
#         b = (x['bpi']['USD']['rate'])
#         b = b.replace(',','')     
#         curve[a] = float(b)
#print(curve)      
