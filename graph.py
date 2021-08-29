
import numpy as np
import json
import matplotlib.pyplot as plt
import datetime as datetime
from smartapi import SmartConnect
import pandas as pd

obj = SmartConnect(api_key="j36iHU6d")
    #login api call
    #T88892", "Sairam@21","j36iHU6d"
data = obj.generateSession("T88892","Sairam@21")
refreshToken = data['data']['refreshToken']

    #fetch the feedtoken
feedToken = obj.getfeedToken()

    #fetch User Profile
    #userProfile = obj.getProfile(refreshToken)
    #print(userProfile)

try:
        historicParam={
        "exchange": "NSE",
        "symboltoken": "3045",
        "interval": "ONE_DAY",
        "fromdate": "2021-02-08 09:30", 
        "todate": "2021-06-08 09:30"
        }
        historical_data = obj.getCandleData(historicParam)
        df = historical_data['data']
        #fig, ax = plt.subplots()
        #ax.plot('date', 'adj_close', data=df)
        #plt.show()
        #df = df[['Date', 'Open', 'High', 'Low', 'Close']]
        #print(df['data'])
        #df = df['Date', 'Open', 'High', 'Low', 'Close']
        #close_price= []
        #date = []
        for x in range(len(df)):
            #close_price.append(df[x][4])
            split_date = df[x][0].split('T')
            #date_object = datetime.datetime.strptime(str(split_date[0]), '%Y-%m-%d').date()
            df[x][0] = pd.to_datetime(split_date[0]) 
# show the plot
        Frame=pd.DataFrame(df, index=None, columns = ['Date', 'Open', 'High','Low','Close', 'Volume'])
        fig, ax = plt.subplots()
        candlestick_ohlc(ax, Frame.values, width = 0.6,
                 colorup = 'green', colordown = 'red', 
                 alpha = 0.8)
        #ax.plot('Date', 'Close', data=Frame)
        plt.show()
        #tuples = [tuple(x) for x in df]
        #print(tuples)
        #fig, ax = plt.subplots()
        #x.plot('date', 'adj_close', data=tuples)
        #plt.show()
        #print(type(date[0]))  
        #datesplit = date[0].split('T')
        #print(datesplit)
        #print(type(datesplit))
        #print(datesplit[0])
        #tim = str(datesplit[0])
        
        #print(type(date_object))
        #rint(date_object)

        #plt.plot_date(dates, values)
        #{timestamp, open, high, low, close, volume}
        #json_object = json.dumps(hisotricdata['data'], indent = 4)
        #plt.rcParams.update({'font.size:10'})
        #fig, axis = plt.subplots(figsize=(14,7))
        #plt.xlabel("price")
        #plt.ylabel("date")
        #plt.plot(data=close_price,label='Closig Price',color='blue')
        #plt.show()
except Exception as e:
        print("Historic Api failed: {}".format(e.message))
    