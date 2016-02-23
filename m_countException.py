# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:34:41 2013

@author: jaehyek.choi
purpose : 주어진 dbname에서 collectionExceoption을 종류별로 count해서 
         collectionExceptionCount을 생성한다.
"""

from datetime import datetime
from pymongo import MongoClient
import m_email
import mltutils as util


setlastk = set()
setcalldrop = set()
setanr = set()
setappfatal = set()
setframework = set()

dictcountCalldropByModel = {}
dictcountKernelLastkByModel = {}
dictcountANRByModel = {}
dictcountFrameworkByModel = {}
dictcountAppFatalByModel = {}

dictcountIMEIByModel = {}


def distinctDoc ( doc ) :
    if doc["exception_type"] == "exception_calldrop"  :
        dictcountCalldropByModel.setdefault(doc["model_name"], []).append(1)
        setcalldrop.add(doc.get("except_cause0", "") + "@" + doc.get("except_cause1", "") )
    elif doc["exception_type"] == "exception_Kernel_LastK"  :
        dictcountKernelLastkByModel.setdefault(doc["model_name"], []).append(1)
        for ind in range( doc.get("except_causecount", 0) ):
            setlastk.add( doc["except_cause%s"%(ind)])
    elif doc["exception_type"] == "exception_anr"  :
        dictcountANRByModel.setdefault(doc["model_name"], []).append(1)
        setanr.add(doc.get("except_cause0", ""))
    elif doc["exception_type"] == "exception_framework"  :
        dictcountFrameworkByModel.setdefault(doc["model_name"], []).append(1)
        setframework.add(doc.get("except_cause0", ""))
    elif doc["exception_type"] == "exception_app_fatal"  :
        dictcountAppFatalByModel.setdefault(doc["model_name"], []).append(1)
        setappfatal.add(doc.get("except_cause0", "") + "@" + doc.get("except_cause1", "") )


def countException( svr, dbfilename ) :
    mongosvr = MongoClient(svr, 27017)
    mongodb = mongosvr[dbfilename]
    colexcept = mongodb["collectionException"]
    colexceptcount = mongodb["collectionExceptionCount"]

    # make index for IMEI
    #indexname = "indexIMEI"
    colexcept.ensure_index("IMEI" )


    listimei = colexcept.distinct("IMEI")
    total = len (listimei)
    count = total
    lastmsg = "The processed IMEI : %s" % total

    for imei in listimei :
        print "_____________________________________"
        print "IMEI : %s" % imei
        print "the remained count :  %s" % count
        count -= 1


        setlastk.clear()
        setcalldrop.clear()
        setanr.clear()
        setappfatal.clear()
        setframework.clear()

        listdoc = colexcept.find({"IMEI":imei})

        #count IMEI by Model
        dictcountIMEIByModel.setdefault(listdoc[0]["model_name"], []).append(1)


        for doc in listdoc :
            distinctDoc(doc)

        queryupdate = {doc["model_name"]:1, doc["register_svwer"]:1, "total":1  }
        querytotal = { "$inc":queryupdate }

        # exception_Kernel_LastK
        for causeone in setlastk :
            queryfind = { "exception_type":"exception_Kernel_LastK", "cause":causeone}
            doccause = colexceptcount.find_one(queryfind )
            if not doccause :
                colexceptcount.insert( queryfind)
            colexceptcount.update(queryfind, querytotal, safe=True )


        # exception_calldrop
        for causeone in setcalldrop :
            queryfind = { "exception_type":"exception_calldrop", "cause":causeone}
            doccause = colexceptcount.find_one(queryfind )
            if not doccause :
                colexceptcount.insert( queryfind)
            colexceptcount.update(queryfind, querytotal, safe=True )

        # exception_anr
        for causeone in setanr :
            queryfind = { "exception_type":"exception_anr", "cause":causeone}
            doccause = colexceptcount.find_one(queryfind )
            if not doccause :
                colexceptcount.insert( queryfind)
            colexceptcount.update(queryfind, querytotal, safe=True )

        # exception_framework
        for causeone in setframework :
            queryfind = { "exception_type":"exception_framework", "cause":causeone}
            doccause = colexceptcount.find_one(queryfind )
            if not doccause :
                colexceptcount.insert( queryfind)
            colexceptcount.update(queryfind, querytotal, safe=True )

        # exception_app_fatal
        for causeone in setappfatal :
            queryfind = { "exception_type":"exception_app_fatal", "cause":causeone}
            doccause = colexceptcount.find_one(queryfind )
            if not doccause :
                colexceptcount.insert( queryfind)
            colexceptcount.update(queryfind, querytotal, safe=True )

        if (count % 5000 ) == 0 :
            colexceptcount.create_index([("cause", 1),("exception_type", 1)] , background=True, drop_dups=True)


    #count the number of IMEI by exception type
    for model_name in dictcountCalldropByModel :
        dictcountCalldropByModel[model_name] = dictcountCalldropByModel[model_name].count(1)
    for model_name in dictcountKernelLastkByModel :
        dictcountKernelLastkByModel[model_name] = dictcountKernelLastkByModel[model_name].count(1)
    for model_name in dictcountANRByModel :
        dictcountANRByModel[model_name] = dictcountANRByModel[model_name].count(1)
    for model_name in dictcountFrameworkByModel :
        dictcountFrameworkByModel[model_name] = dictcountFrameworkByModel[model_name].count(1)
    for model_name in dictcountAppFatalByModel :
        dictcountAppFatalByModel[model_name] = dictcountAppFatalByModel[model_name].count(1)

    for model_name in dictcountIMEIByModel:
        dictcountIMEIByModel[model_name] = dictcountIMEIByModel[model_name].count(1)

    from cStringIO import StringIO
    import sys

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()


    print "---------exception count by Exceptoin Type ---------"
    strnameIMEIcount = "CountByException.csv"

    print "Calldrop: " + str(dictcountCalldropByModel)
    print "KernelLastk: " + str(dictcountKernelLastkByModel)
    print "ANR : " + str(dictcountANRByModel)
    print "Framework: " + str(dictcountFrameworkByModel)
    print "AppFatal: " + str(dictcountAppFatalByModel)
    print "---------IMEI count by Exceptoin Type ---------"
    print "IMEI By Model : " + str(dictcountIMEIByModel)
    print lastmsg

    sys.stdout = old_stdout
    stremailbody =  mystdout.getvalue()
    print stremailbody

    listtemp = []
    listtemp.append(dictcountCalldropByModel )
    listtemp.append(dictcountKernelLastkByModel )
    listtemp.append(dictcountANRByModel )
    listtemp.append(dictcountFrameworkByModel )
    listtemp.append(dictcountAppFatalByModel )
    listtemp.append(dictcountIMEIByModel )
    
    util.SaveListDictToCSV( listtemp, strnameIMEIcount)
    del listtemp
    print "-----------------------------------------------"
    m_email.send_mail("jaehyek.choi@lge.com",["jaehyek.choi@lge.com"], 
                      "Exception count by exception type", stremailbody,
                      [strnameIMEIcount])
    print "sending the file %s using email " % strnameIMEIcount


import  argparse



if __name__ == "__main__":
    svr = "172.21.26.39"
    dbfilename = "MLTDB"

    cmdlineopt = argparse.ArgumentParser(description='get the calldrop csv file from MongoDB MLTDB')
    cmdlineopt.add_argument('-svr', action="store", dest="svr", default="172.21.26.39",  help='Mongo DB server IP. default="172.21.26.39"' )
    cmdlineopt.add_argument('-db', action="store", dest="dbfilename",  default="MLTDB", help='dump the input file,  default= "MLTDB" ' )

    cmdlineresults = cmdlineopt.parse_args()
    svr = cmdlineresults.svr
    dbfilename = cmdlineresults.dbfilename

    starttime = datetime.now()
    countException(svr, dbfilename)
    endtime = datetime.now()

    print "elasped time is : " +  str(endtime - starttime)