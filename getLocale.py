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

def getLoc(locales):
    data = client.geocode(locales)
    return data

def parseJson(data):
    data = pd.DataFrame((flatten(record, '.') for record in data))
    return data



path = set_path()
locales = getList(path)
client = init_client(apk)
data = getLoc(locales)
data = parseJson(data)


