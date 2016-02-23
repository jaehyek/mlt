# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:32:44 2013

@author: jaehyek.choi

description : calldrop관련 , latitude와 longitude을 csv로 출력.
"""
import argparse
from datetime import datetime
from pymongo import MongoClient

# "latitue : 37:23:21.73632"
# "longtitude : 126:55:49.57752"
def SexagesimalToDecimal( str ):
    listsex = str.split(":")
    v = float(listsex[1]) + float(listsex[2])/60 + float(listsex[3])/3600
    return float("%.4f" % v )

dictloc = {}

def calldropcsv(svr, csvfilename) :
    counterr = 0
    mongosvr = MongoClient(svr, 27017)
    mongodb = mongosvr["MLTDB"]
    colcalldrop = mongodb["collectionCalldrop"]
    
    f = open(csvfilename, "w" )    
    head = "imei, model_name, phone_type, dropcause, exception_swver, longitude, latitude \n"
    f.write(head)
        
    colcalldrop.ensure_index("IMEI")
    
    listimei = colcalldrop.distinct("IMEI")
    count = len (listimei)
    lastmsg = "The processed IMEI : %s" % count 
    
    for imei in listimei :
        print "______________call drop location count_______________________"
        print "IMEI : %s" % imei
        print "the remained count :  %s" % count
        count -= 1
        
        listdoc = colcalldrop.find({"IMEI":imei})
        
        dictloc.clear()
        
        for doc in listdoc :
            if (len(doc.get("except_cause3", ""))> 0 ) and (len(doc.get("except_cause4", ""))>0) :
                try :
                    latitude = SexagesimalToDecimal( doc["except_cause3"])
                    longitude = SexagesimalToDecimal( doc["except_cause4"])
                    dropcause = doc.get("except_cause0", "")
                    dictloc.update( { dropcause : (latitude, longitude, doc.get("exception_swver", ""))})
                except:
                    counterr += 1
                    print "Accumulate error  # : %s " % counterr
                    pass
        for dropcause in dictloc : 
            latitude, longitude, exception_swver = dictloc[dropcause]
            
            line = "%s, %s, %s, %s, %s, %s, %s \n" %( imei, doc["model_name"], doc["phone_type"],dropcause,exception_swver, longitude, latitude )
            f.write(line)
            
                
    f.close()
    print lastmsg
    print "Accumulated error  # : %s " % counterr
    
        
    
    



csvfilename = ""
svr = "172.21.26.39"

if __name__ == "__main__":
    
        
    cmdlineopt = argparse.ArgumentParser(description='get the calldrop csv file from MongoDB MLTDB')
    cmdlineopt.add_argument('-csv', action="store", dest="csvfilename", default='calldrop.csv',  help='csv file name. default = calldrop.csv' )
    cmdlineopt.add_argument('-svr', action="store", dest="svr", default="172.21.26.39",  help='Mongo DB server IP. default="172.21.26.39"' )

    cmdlineresults = cmdlineopt.parse_args()
    csvfilename = cmdlineresults.csvfilename
    svr = cmdlineresults.svr

    starttime = datetime.now()
    calldropcsv(svr, csvfilename)
    endtime = datetime.now()
    
    print "elasped time is : " +  str(endtime - starttime)