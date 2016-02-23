# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:34:41 2013

@author: jaehyek.choi
purpose : 주어진 dbname에서 collectionCalldrop을 원인별로 count해서 
         collectionCalldropCauseCount, collectionCalldropEnvCount 을 생성한다.
"""

from datetime import datetime
from pymongo import MongoClient
import re

# The below list is for just simplifying the ril cause against to long sentence .
listsimplerilcause =[
    "answer error com android internal telephony commandexception",
    "apncontext default setstate failed previous state",
    "apncontext ims setstate failed previous state",
    "apncontext setstate failed for type",
    "broadcast showplmn true plmn 서비스 안됨 showspn false",
    "curspnrule mcurspn mcurplmn 등록이 필요합니다",
    "dataconnectionac getpartialsuccessstatussync error response what when",
    "deactivate data call error com android internal telephony commandexception",
    "dial error com android internal telephony commandexception",
    "exceptcallstate connection video call incoming false state",
    "exceptcallstate connection voice call incoming false state",
    "exceptcallstate connection voice call incoming true state active post",
    "exceptcallstate connection voice call incoming true state disconnecting post dial state not started",
    "exceptcallstate connection voice call incoming true state holding post dial state not started",
    "exceptcallstate connection voice call incoming true state incoming post dial state not started",
    "exceptcallstate connection voice call incoming true state waiting post dial state not started",
    "gsmdc dcactivatingstate onsetupconnectioncompleted result err rilerror",
    "gsmdc err rilerror",
    "gsmdc onsetupconnectioncompleted failed ar exception",
    "gsmdct ondatasetupcomplete error apn ims",
    "gsmdct ondatasetupcomplete error apn internet",
    "gsmdct ondatasetupcomplete error apn lte",
    "gsmsst not normal service plmn 서비스 안됨 spn",
    "in korea showplmn true plmn 등록이 필요합니다",
    "mcurplmn 등록이 필요합니다",
    "mcurplmn 서비스 안됨",
    "broadcast showplmn true plmn 등록이 필요합니다",
    "request get neighboring cell ids error com android internal telephony commandexception",
    "setlinkproperties error clearing linkproperties status result err",
    "screen state error com android internal telephony commandexception"
]

dictsimplerilcause = {
re.compile("apncontext default set reason as .* current state failed") : "apncontext default set reason as ... current state failed",
re.compile("apncontext ims set reason as .* current state failed") : "apncontext ims set reason as ... current state failed",
re.compile("apncontext set reason as .* current state failed") : "apncontext set reason as ... current state failed",
re.compile("dtmf .* error com android internal telephony commandexception .* failure") : "dtmf ... error com android internal telephony commandexception ... failure",
re.compile("ril request cdma .* error com android internal telephony commandexception .*") : "ril request cdma ... error com android internal telephony commandexception ...",
re.compile("ril request get .* error com android internal telephony commandexception .*") : "ril request get ... error com android internal telephony commandexception ..."
}

dictrilcause = {}

# just for ril cuase count for each calldrop
def distinctDoc ( doc ) :
    for ind in range( doc["ril_causecount"] ):
        fullrilcause = doc["ril_cause%s"%(ind)]
        for simplerilcause in listsimplerilcause :
            if simplerilcause in fullrilcause :
                fullrilcause = simplerilcause
                break
        for simplerilcause in dictsimplerilcause:
            fullrilcause = simplerilcause.sub(dictsimplerilcause[simplerilcause], fullrilcause )

        dictrilcause[fullrilcause] = doc["exception_swver"]



def countCalldrop( svr, dbfilename ) :
    mongosvr = MongoClient(svr, 27017)
    mongodb = mongosvr[dbfilename]
    colcalldrop = mongodb["collectionCalldrop"]
    colcalldroprilcount = mongodb["collectionCalldropCauseCount"]
    colcalldropcausecount = mongodb["collectionCalldropEnvCount"]

#    make index for IMEI
#    indexname = "indexIMEI"
#    colcalldrop.ensure_index("IMEI", name = indexname)

    listimei = colcalldrop.distinct("IMEI")
    count = len (listimei)
    lastmsg = "The processed IMEI : %s" % count

    for imei in listimei :
        print "______________call drop_______________________"
        print "IMEI : %s" % imei
        print "the remained count :  %s" % count
        count -= 1

        dictrilcause.clear()

        listdoc = colcalldrop.find({"IMEI":imei})

        for doc in listdoc :
            distinctDoc(doc)

            calldropcause = doc.get("except_cause0", "") + "@"+ doc.get("except_cause1", "")
            queryfind = { "calldropcause":calldropcause}
            doccause = colcalldropcausecount.find_one(queryfind )
            if not doccause :
                colcalldropcausecount.insert( queryfind)
            queryupdate = {}
            queryupdate.update({"total":1})
            queryupdate.update({doc["phone_type"]:1})
            queryupdate.update({doc["model_name"]:1})
            queryupdate.update({doc["exception_swver"]:1})
            queryupdate.update({doc["telphony_state"]:1})
            appsbeforeexception = doc["appsbeforeexception"]
            appsbeforeexception = appsbeforeexception.replace(".", "_")
            appsbeforeexception = appsbeforeexception.replace("/", "@")
            queryupdate.update({appsbeforeexception:1})
            if doc["exception_swver"] == 1 :
                queryupdate.update({"moving":1})
            else:
                queryupdate.update({"movenot":1})
            callmonth = doc["calldate"][:-2]
            queryupdate.update({callmonth:1})

            calltime = doc["calltime"][:2]
            if calltime <= 10 :
                queryupdate.update({"calltime10":1})
            elif calltime <= 14 :
                queryupdate.update({"calltime14":1})
            elif calltime <= 17 :
                queryupdate.update({"calltime17":1})
            elif calltime <= 20 :
                queryupdate.update({"calltime20":1})
            elif calltime <= 23 :
                queryupdate.update({"calltime23":1})

            if doc["cdma_level"] != -1 :
                if doc["cdma_level"] == 1 :
                    queryupdate.update({"cdma_level1":1})
                else:
                    queryupdate.update({"cdma_level2over":1})

            if doc["gsm_level"] != -1 :
                if doc["gsm_level"] == 1 :
                    queryupdate.update({"gsm_level1":1})
                else:
                    queryupdate.update({"gsm_level2over":1})

            if doc["lte_level"] != -1 :
                if doc["lte_level"] == 1 :
                    queryupdate.update({"lte_level1":1})
                else:
                    queryupdate.update({"lte_level2over":1})

            # increment count
            querytotal = { "$inc":queryupdate }
            colcalldropcausecount.update(queryfind, querytotal, safe = True )



        # rilcause count
        for rilcause in dictrilcause :
            queryfind = { "rilcause":rilcause}
            # increment  for  model_name:1, exception_swver : 1 , total:1
            queryupdate = { "$inc":{doc["model_name"]:1, dictrilcause[rilcause]:1, "total":1 } }
            doccause = colcalldroprilcount.find_one(queryfind )
            if not doccause :
                colcalldroprilcount.insert( queryfind)
            colcalldroprilcount.update(queryfind, queryupdate, safe=True )

        if (count % 5000 ) == 0 :
            colcalldropcausecount.create_index("calldropcause" , background=True, drop_dups=True)
            colcalldroprilcount.create_index("rilcause" , background=True, drop_dups=True)

    print lastmsg

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
    countCalldrop(svr, dbfilename )


    endtime = datetime.now()

    print "elasped time is : " +  str(endtime - starttime)