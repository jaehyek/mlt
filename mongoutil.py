# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:59:35 2013

@author: jaehyek.choi
"""

from pymongo import MongoClient
from bson.objectid import ObjectId




class ClassMongo():
    server = ""
    client = None
    db = None
    collection = None
    booltag = False
    dicttag = {}
    def __init__(self, databasename, collectionname , server="172.21.26.39", tag=""):
        self.server = server
        self.client = MongoClient(self.server, 27017)
        self.db = self.client[databasename]
        self.collection = self.db[collectionname]
        if len(tag) > 0 :
            self.booltag = True
            self.dicttag["tag"] = tag



    def insertdoc(self, doc ):
        if (type(doc)  == list ) or ( type(doc) == dict ) :
            if self.booltag == False:
                self.collection.insert(doc)
            else:
                if ( type(doc) == dict ) :
                    tempdoc = {}
                    tempdoc.update(doc)
                    tempdoc.update(self.dicttag)
                    self.collection.insert(tempdoc)
                    del tempdoc
                else:
                    for smalldoc in doc:
                        tempdoc = {}
                        tempdoc.update(smalldoc)
                        tempdoc.update(self.dicttag)
                        self.collection.insert(tempdoc)
                        del tempdoc
        else:
            raise Exception('mongoClass', 'Ooops not list or dict type')


    def find(self, doc ):
        return self.collection.find( doc )
        
    def count(self, doc ):
        return self.collection.count( doc )
    
    def update(self, doc0, doc1, multiopt=False ):
        self.collection.update(doc0, doc1, multi=multiopt )
        
    def index(self, doc ):
        self.collection.ensureIndex( doc )
        
    def distinct(self, keystring):
        return self.collection.distinct(keystring)
        
    def getObj(self, post_id):
        # Convert from string to ObjectId:
        return self.collection.find_one({'_id': ObjectId(post_id)})

