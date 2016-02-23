# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:40:44 2013

@author: jaehyek.choi
"""

from datetime import datetime
from pymongo import MongoClient




svr = "172.21.26.39"
databasename = "TestDDB"
collectionname = "kkkk"


client = MongoClient(svr, 27017)
db = client[databasename]
collection = db[collectionname]
tempdoc = { "aaa": 111, "bbb":"asdfasdfas", "ccc":{"kk": 1234 }}
collection.insert(tempdoc)

docfind = { "aaa":111 }
listret = collection.find(docfind )
print listret[0]["aaa"]