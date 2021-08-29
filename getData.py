import os,sys
import math
import numpy as np
import json
from smartapi import SmartConnect
import matplotlib.pyplot as plt
def getApiData():
    #or from smartapi.smartConnect import SmartConnect
    #import smartapi.smartExceptions(for smartExceptions)

    #create object of call
    #obj=SmartConnect(api_key="",
                    #optional
                    #access_token = "your access token",
                    #refresh_token = "your refresh_token")
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
        "interval": "ONE_MINUTE",
        "fromdate": "2021-02-08 09:15", 
        "todate": "2021-02-08 10:20"
        }
        hisotricdata = obj.getCandleData(historicParam)
        #print(hisotricdata)
        #{timestamp, open, high, low, close, volume}
        json_object = json.dumps(hisotricdata['data'], indent = 4)
        plt.rcParams.update({'font.size:10'})
        fig, axis = plt.subplots(figsize=(14,7))

    
    except Exception as e:
        print("Historic Api failed: {}".format(e))

    return json_object