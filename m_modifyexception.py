# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 08:25:24 2013

@author: jaehyek.choi
"""

from datetime import datetime
from pymongo import MongoClient
import MltDBDump as dump
import copy

def modifyException( svr, dbfilename ) :
    mongosvr = MongoClient(svr, 27017)
    mongodb = mongosvr[dbfilename]
    colexception = mongodb["collectionException"]
    
    
    cursordoc = colexception.find({})
    count = cursordoc.count()
    lastmsg = "The processed doc : %s" % count 
    
    colexception.ensure_index("_id" )
    
    for doc in cursordoc :
        print "______________modify doc_______________________"
        print "the remained count :  %s" % count
        count -= 1
        
        strexceptioncause = dump.getStrExceptionCause(doc["exception_type"], doc["exception_data"], doc["lastk_log"] )
        dictexceptioncause = dump.getDictExceptionCause(doc["exception_type"],strexceptioncause )
        
        new_doc = copy.deepcopy(doc)
        for i in range(10):
            new_doc.pop( "except_cause%s"%i, 0 )
        new_doc.update(dictexceptioncause )

        dictrilcause = 0
        if (doc["exception_type"] == "exception_calldrop" ) and (len(doc["ril_log"]) > 0 ) : 
            dictrilcause = dump.getDictRilCause( dump.getStrRilCause(doc["ril_log"]))
            for i in range(10):
                new_doc.pop( "ril_cause%s"%i, 0 )
            new_doc.update(dictrilcause)

        new_doc.pop("_id")
        #colexception.update( {"_id": doc["_id"]}, {"$set":new_doc}, multi=False )
        
        del new_doc
        del dictrilcause
        del dictexceptioncause
        
        


    print lastmsg



import  argparse        



if __name__ == "__main__":
    svr = "172.21.26.39"
    dbfilename = "MLTDB"
    cmdlineopt = argparse.ArgumentParser(description='modify the collectionCalldrop from MongoDB MLTDB')
    cmdlineopt.add_argument('-svr', action="store", dest="svr", default="172.21.26.39",  help='Mongo DB server IP. default="172.21.26.39"' )
    cmdlineopt.add_argument('-db', action="store", dest="dbfilename",  default="MLTDB", help='dump the input file,  default= "MLTDB" ' )

    cmdlineresults = cmdlineopt.parse_args()
    svr = cmdlineresults.svr        
    dbfilename = cmdlineresults.dbfilename     
    
    dbfilename = "MLTDBG2"

    starttime = datetime.now()
    modifyException(svr, dbfilename)
    
    endtime = datetime.now()
    
    print "elasped time is : " +  str(endtime - starttime)