# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:34:41 2013

@author: jaehyek.choi
"""

from datetime import datetime
from pymongo import MongoClient
     
    


def countDistinctIMEI( svr ) :
    mongosvr = MongoClient(svr, 27017)
    mongodb = mongosvr["MLTDB"]
    colexcept = mongodb["collectionException"]

    dictmodel = {}


    # make index for IMEI
    #indexname = "indexIMEI"
    colexcept.ensure_index("IMEI" )
    
    listimei = colexcept.distinct("IMEI")
    count = len (listimei)
    lastmsg = "The processed IMEI : %s" % count 
    

    for imei in listimei :
        print "_____________________________________"
        print "IMEI : %s" % imei
        print "the remained count :  %s" % count
        count -= 1

   
        listdoc = colexcept.find({"IMEI":imei})
        for doc in listdoc :
            dictmodel.setdefault( doc["model_name"], []).append(1)
            break
    
    for model_name in dictmodel :
        dictmodel[model_name] = len(dictmodel[model_name])


    print dictmodel  
    print lastmsg
    

import  argparse        

svr = "172.21.26.39"

if __name__ == "__main__":
    cmdlineopt = argparse.ArgumentParser(description='get the calldrop csv file from MongoDB MLTDB')
    cmdlineopt.add_argument('-svr', action="store", dest="svr", default="172.21.26.39",  help='Mongo DB server IP. default="172.21.26.39"' )

    cmdlineresults = cmdlineopt.parse_args()
    svr = cmdlineresults.svr
    
    starttime = datetime.now()
    countDistinctIMEI(svr)
    endtime = datetime.now()
    
    print "elasped time is : " +  str(endtime - starttime)