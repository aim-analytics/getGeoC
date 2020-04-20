# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:26:25 2020

@author: csun
"""



from geocodio import GeocodioClient
from flatten_json import flatten
import pandas as pd
import os

apk = '' #insert API Key

#def limit check for simplicity set a hard limit check when batch process, it will cancel if length is greater than limit with out initilazing call to REST API 
#alternative is to iterate and check if index is greater than limit
limit = 101

#initialize path
def set_path():
    direct = r''
    name = "locale.csv"
    path = os.path.join(direct,name)
    print(path)
    return path

#initialize locations
def getList(path):
    df=pd.read_csv(path)
    locales=df['Location'].tolist()
    return locales

#initialize geocodio client

def init_client(apk):
    client = GeocodioClient(apk)
    return client

def parseJson(data):
    data = pd.DataFrame((flatten(record, '.') for record in data))
    return data

def getLoc(locales):
    if len(locales) <= limit:
        data = client.geocode(locales)
        df=parseJson(data)
        return data, df
    else: 
        print("Are you sure you want to drop money???")





path = set_path()
locales = getList(path)
client = init_client(apk)
data, df = getLoc(locales)

