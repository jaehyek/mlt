# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:32:52 2013

@author: jaehyek.choi
"""

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
re.compile("dtmf .* error com android internal telephony commandexception .*") : "dtmf ... error com android internal telephony commandexception ...",
re.compile("ril request cdma .* error com android internal telephony commandexception .*") : "ril request cdma ... error com android internal telephony commandexception ...",
re.compile("ril request get .* error com android internal telephony commandexception .*") : "ril request get ... error com android internal telephony commandexception ..."
}

dictrilcause = {}
listrilcause = []
# just for ril cuase count for each calldrop
import os
def distinctDoc ( listdoc ) :
    for fullrilcause in listdoc:
        fullrilcause = fullrilcause.rstrip(os.linesep)
        found = 0
        for simplerilcause in listsimplerilcause :
            if simplerilcause in fullrilcause :
                fullrilcause = simplerilcause
                found = 1
                break
        if found == 0 :
            for simplerilcause in dictsimplerilcause:
                if simplerilcause.search( fullrilcause ) :
                    fullrilcause = dictsimplerilcause[simplerilcause]
                    break

        #dictrilcause[fullrilcause] = "exception_swver"
        listrilcause.append(fullrilcause)



listsentence = [
"exceptcallstate connection video call incoming false state",
"exceptcallstate connection voice call incoming false state active post dial state complete dc id active toa norm mo callmode noevp number cli name null call details ljava lang string",
"exceptcallstate connection voice call incoming false state active post dial state complete dc id holding toa norm mo callmode noevp number cli name null call details ljava lang string",
"exceptcallstate connection voice call incoming false state alerting post dial state not started dc id active toa norm mo callmode noevp number cli name null call details ljava lang string",
"exceptcallstate connection voice call incoming false state alerting post dial state not started dc id alerting toa norm mo callmode noevp number cli name null call details ljava lang string",
"exceptcallstate connection voice call incoming false state dialing post dial state not started dc id active toa norm mo callmode noevp number cli name null call details ljava lang string",
"exceptcallstate connection voice call incoming false state dialing post dial state not started dc id alerting toa norm mo callmode noevp number cli name null call details ljava lang string",
"exceptcallstate connection voice call incoming false state dialing post dial state not started dc id dialing toa norm mo callmode noevp number cli name null call details ljava lang string",
"exceptcallstate connection voice call incoming false state disconnecting post dial state complete dc id active toa norm mo callmode noevp number cli name null call details ljava lang string",
"exceptcallstate connection voice call incoming false state disconnecting post dial state complete dc id holding toa norm mo callmode noevp number cli name null call details ljava lang string",
"exceptcallstate connection voice call incoming false state holding post dial state complete dc id active toa norm mo callmode noevp number cli name null call details ljava lang string",
"exceptcallstate connection voice call incoming false state holding post dial state complete dc id holding toa norm mo callmode noevp number cli name null call details ljava lang string",
"exceptcallstate connection voice call incoming true state active post",
"exceptcallstate connection voice call incoming true state disconnecting post dial state not started",
"exceptcallstate connection voice call incoming true state holding post dial state not started",
"exceptcallstate connection voice call incoming true state incoming post dial state not started",
"exceptcallstate connection voice call incoming true state waiting post dial state not started",
"exceptcallstate it does not need to be updated",
"exception during getlastcallfailcause assuming normal disconnect",
"exception in fetching ef csp data com android internal telephony commandexception generic failure",
"exception in fetching ef gid data com android internal telephony commandexception generic failure",
"exception parsing sim record"
]

fi = open("test1.csv", "r")
fo = open("test2.csv", "w" )
listline = fi.readlines()
distinctDoc(listline)
index = 0
for line in listline:
    fo.write(line.rstrip(os.linesep).decode("utf-8") + "," +listrilcause[index].decode("utf-8") + "\n")
    index += 1
    print "..."


fi.close()
fo.close()



