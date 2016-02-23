# _*_ coding: utf-8 _*_

'''
Created on 2012. 12. 01.

@author: jaehyek
'''

import os, shutil
from datetime import datetime, timedelta
from pysqlite2 import dbapi2 as sqlite3
import MltDBDump as dump
import mltutils as util
import glob

class classTableCallInOut():
    databasename = "CallInOut.db3"
    strtablename = "tableCallInOut"
    conn = 0 
    cur = 0 
    def __init__(self, databasename ):
        if len( databasename) != 0 :
            self.databasename = databasename
        self.setupDBandTable()
        
    def __del__(self):
        self.conn.close()
        
    def setupDBandTable(self):
        queryCreateTable = '''
        create table if not exists %s (
            model_name VARCHAR(20),
            phone_type VARCHAR(6),
            network_type VARCHAR(30),
            IMEI VARCHAR(20),
            timestamp REAL,
            timediff REAL,
            call_os_ver VARCHAR(20),
            call_sw_ver VARCHAR(30),
            call_inout VARCHAR(10),
            cellmovementcount INTEGER,
            signallowestlevel INTEGER,
            continuecall INTEGER,
            signalgabover2 INTEGER
            )
        ''' % ( self.strtablename )
        self.conn = sqlite3.connect(self.databasename)
        self.cur = self.conn.cursor()
        self.cur.execute(queryCreateTable)
        self.conn.commit()
        
    def updateTableCallInOut( self,  listdictDBDump, listdictBasicSWVer ):
        model_name = listdictBasicSWVer[-1]["model_name"]
        phone_type = listdictBasicSWVer[-1]["phone_type"]
        network_type = listdictBasicSWVer[-1]["network_type"]
        IMEI = listdictBasicSWVer[-1]["IMEI"]
        
        listdictCallInout = []
        self.getListDictCallInOut( listdictCallInout, phone_type,listdictDBDump  )
        querystate = ''' model_name, phone_type, network_type, IMEI, timestamp, timediff,call_os_ver, 
                    call_sw_ver, call_inout, cellmovementcount, signallowestlevel, continuecall, signalgabover2  '''
        qurryvalue = ''' "%s", "%s", "%s", "%s", %s, %s, "%s", "%s", "%s", %s, %s, %s, %s  '''
        querystate = "INSERT INTO " + self.strtablename  + " ( " + querystate + " )  VALUES ( " + qurryvalue + " )" 
        
        for dictCallInout in listdictCallInout :
            timestamp = dictCallInout["timestamp"]
            timediff = dictCallInout["timediff"]
            call_os_ver = dictCallInout["call_os_ver"]
            call_sw_ver = dictCallInout["call_sw_ver"]
            call_inout = dictCallInout["call_inout"]
            cellmovementcount = dictCallInout["cellmovementcount"]
            signallowestlevel = dictCallInout["signallowestlevel"]
            continuecall = dictCallInout["continuecall"]
            signalgabover2 = dictCallInout["signalgabover2"]
            querytemp = querystate
            querytemp = querystate % (model_name, phone_type, network_type, IMEI, timestamp, timediff,call_os_ver, 
                    call_sw_ver, call_inout, cellmovementcount, signallowestlevel, continuecall, signalgabover2 )
            self.cur.execute(querytemp)
            
        self.conn.commit()
        del listdictCallInout
        
        
        
        
    def getListDictCallInOut(self, listdictCallInOut, strPhoneType, listdictDBDump) :
        listdictKeyCallInOut = ["timestamp", "timediff",  "call_os_ver", "call_sw_ver", "call_inout", "cellmovementcount", "signallowestlevel", "continuecall", "signalgabover2" ]
    
        phonetype = 0       # default type : CDMA
        if strPhoneType ==  "GSM" :
            phonetype = 1
    
        callinout = "call_out"
        callstarttimestamp = 0
        calltimestampdiff = 0
        callsigalstrength = 10
        callsigalstrengthLowest = 10
        callmovecount = 0
        callregionID = -1
        callstarting = 0
        save_pre_call_duration = 0
        save_pre_callend_time = 0
        call_continue_retry = 0
        callsignalgabcount = -1
        pre_sigalstrength = 10
        
        sw_ver = ""
        os_ver = ""
    
        for dictDBDump in listdictDBDump :
        
            os_ver = dictDBDump.get("os_ver", os_ver)
            sw_ver = dictDBDump.get("register_svwer", sw_ver)
    
            callstate = dictDBDump.get("callcomm_state", None)
            if callstate != None :
                if callstate == "CALL_STATE_IDLE" :
                    if callstarttimestamp > 0 :
                        calltimestampdiff = dictDBDump.get("timestamp", None) - callstarttimestamp
                        save_pre_call_duration = calltimestampdiff
                        save_pre_callend_time = dictDBDump.get("timestamp", None)
                        callmovecount -= 1
                        if callmovecount < 0 :
                            callmovecount = 0
                        if callsigalstrengthLowest == 10 :      # no signal during calling, if then, replace callsigalstrengthLowest with callsigalstrength
                            callsigalstrengthLowest = -1
                        dicttemp = dict(zip(listdictKeyCallInOut, (callstarttimestamp,calltimestampdiff,os_ver,sw_ver, callinout,callmovecount, callsigalstrengthLowest, call_continue_retry, callsignalgabcount  )))
                        listdictCallInOut.append(dicttemp)
    
                    callinout = "call_out"
                    callstarttimestamp = 0
                    calltimestampdiff = 0
                    callsigalstrengthLowest = 10
                    callmovecount = 0
                    callregionID = -1
                    callstarting = 0
                    call_continue_retry = 0
                    callsignalgabcount = -1
                    pre_sigalstrength = 10
    
                elif callstate == "CALL_STATE_RINGING" :
                    callinout = "call_in"
                    callstarting =1
                elif callstate == "CALL_STATE_OFFHOOK" :
                    # print callinout
                    callstarting =1
                    callstarttimestamp = dictDBDump.get("timestamp", None)
                    difftime = callstarttimestamp - save_pre_callend_time
                    if save_pre_call_duration != 0 and save_pre_call_duration <= (5*1000) and (difftime) <= (5*1000) :
                        call_continue_retry = 1
    
    
            if phonetype == 0 :         # CDMA
                sigalstrength = dictDBDump.get("cdma_level", None)
                if sigalstrength != None :
                    callsigalstrength = sigalstrength
    
                if callstarting == 1  :
                    if sigalstrength != None and callsigalstrengthLowest > sigalstrength :
                        callsigalstrengthLowest = sigalstrength
    
                    if sigalstrength != None and (pre_sigalstrength - sigalstrength) >= 2:
                        callsignalgabcount += 1
    
                    if sigalstrength != None:
                        pre_sigalstrength = sigalstrength
    
                    regionID = dictDBDump.get("cdma_bsid", None)
                    if regionID != None and regionID != -1 and callregionID != regionID :
                        callregionID = regionID
                        callmovecount += 1
            else:                       # GSM
                sigalstrength = dictDBDump.get("gsm_level", None)
                if sigalstrength != None :
                    callsigalstrength = sigalstrength
    
                if callstarting == 1 :
    
                    if sigalstrength != None and callsigalstrengthLowest > sigalstrength :
                        callsigalstrengthLowest = sigalstrength
    
                    if sigalstrength != None and (pre_sigalstrength - sigalstrength) >= 2:
                        callsignalgabcount += 1
    
                    if sigalstrength != None:
                        pre_sigalstrength = sigalstrength
    
                    regionID = dictDBDump.get("gsm_cid", None)
                    if regionID != None and regionID != -1 and callregionID != regionID :
                        callregionID = regionID
                        callmovecount += 1

class classTableException():
    databasename = "exceptionhist.db"
    strtablename = "tableException"
    conn = 0 
    cur = 0
    def __init__( self, databasename ) :
        if len(databasename) != 0 :
            self.databasename = databasename
        self.setupDBandTable()
    
    def __del__(self):
        self.conn.close()
    
    def setupDBandTable(self):
        queryCreateTable = '''
        create table if not exists %s (
            model_name VARCHAR(20),
            phone_type VARCHAR(6),
            network_type VARCHAR(30),
            IMEI VARCHAR(20),
            exception_cause VARCHAR(300),
            exception_swver VARCHAR(100),
            calldate VARCHAR(10),
            calltime VARCHAR(10), 
            calldatetime REAL,
            avail_ram INTEGER,
            appsbeforeexception VARCHAR(200) )
        ''' % ( self.strtablename )
        self.conn = sqlite3.connect(self.databasename)
        self.cur = self.conn.cursor()
        self.cur.execute(queryCreateTable)
        self.conn.commit()
    
    # reverse find from index in  listdictDBDump to determine if columnName have a value.
    #if then, return element of  listdictDBDump
    def rfindColumnValue(self,  index, listdictDBDump, columnName ) :
        while( index >= 0  ) :
            dictDBDump = listdictDBDump[index]
            if dictDBDump.get(columnName, None) != None:
                return dictDBDump
            else:
                index = index -1
        return {}
    
    def getAppBeforeCall(self, calltimestamp, classmltdb ) :
        calltime5minbefore = calltimestamp - ( 5 * 60 * 1000)
        stractivity = ""
        try:
            listdictapp = classmltdb.getlistdictFromTableDuration("recent_act_info",calltime5minbefore, calltimestamp )
            # use the last dict
            apps = listdictapp[-1]["recentpackage_names"]
            
            listrecentActivity = apps.split("\n")
            stractivity = listrecentActivity[0]

        except Exception :
            pass
        
        stractivity = stractivity.encode("utf-8")
        del listdictapp
        return stractivity
    
    def updateTableException( self,  listdictDBDump, listdictBasicSWVer, classmltdb ):
        model_name = listdictBasicSWVer[-1]["model_name"]
        phone_type = listdictBasicSWVer[-1]["phone_type"]
        network_type = listdictBasicSWVer[-1]["network_type"]
        IMEI = listdictBasicSWVer[-1]["IMEI"]

        for index in range(len(listdictDBDump)) :
            dictDBDump = listdictDBDump[index]
            if dictDBDump.get("exception_type", None) != None :
                calldatetime = dictDBDump["timestamp"]
                exception_cause = dictDBDump.get("exception_cause", "unknown" ) 
                if exception_cause == None :
                    exception_cause = "unknown"
                exception_cause = exception_cause.replace('"', "'" )
                exception_swver = dictDBDump.get("exception_swver", "unknown" ) 
                liststrtime = dump.ConvertTimeStampToString(calldatetime).split()
                calldate = "".join( liststrtime[0].split("-"))
                calltime = "".join( liststrtime[1].split(":"))
                
                querystate = " model_name , phone_type ,network_type ,exception_cause ,exception_swver ,IMEI , calldate , calltime ,calldatetime "
                qurryvalue = ' "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", %s ' % ( model_name , 
                        phone_type ,network_type ,exception_cause ,exception_swver ,IMEI , calldate , calltime , calldatetime) 
                
                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "avail_ram" )
                avail_ram = dictDBDump.get("avail_ram", None)
                if avail_ram != None :
                    querystate += " ,avail_ram "
                    qurryvalue += " , %s " % (avail_ram ) 
                
                # get the app name near call drop
                appsbeforeexception = self.getAppBeforeCall(calldatetime, classmltdb )
                if len(appsbeforeexception) > 0 : 
                    querystate += ' ,appsbeforeexception '
                    qurryvalue += ' , "%s" ' % (appsbeforeexception)
                    
                    
                querystate = "INSERT INTO " + self.strtablename  + " ( " + querystate + " )  VALUES ( " + qurryvalue + " )" 
                self.cur.execute( querystate )
            
        self.conn.commit()

        

        
        

class classTableCallDrop():
    databasename = "exceptionhist.db"
    strtablename = "tableCalldrop"
    conn = 0 
    cur = 0
    def __init__( self, databasename ) :
        if len(databasename) != 0 :
            self.databasename = databasename
        self.setupDBandTable()
    
    def __del__(self):
        self.conn.close()
        
    def setupDBandTable(self):
        queryCreateTable = '''
        create table if not exists %s (
            model_name VARCHAR(20),
            phone_type VARCHAR(6),
            network_type VARCHAR(30),
            IMEI VARCHAR(20),
            exception_cause VARCHAR(300),
            exception_swver VARCHAR(100),
            calldate VARCHAR(10),
            calltime VARCHAR(10),
            calldatetime REAL,
            avail_ram INTEGER,
            telephony_datetime REAL,
            telphony_state VARCHAR(30),
            gsm_signal_datetime REAL,
            gsm_level INTEGER,
            gsm_signalstrength INTEGER,
            cdma_signal_datetime REAL,
            cdma_level INTEGER,
            cdma_signalstrength INTEGER,
            lte_signal_datetime REAL,
            lte_level INTEGER,
            lte_signalstrength INTEGER,
            gsm_loc_datetime REAL,
            gsm_cid INTEGER,
            gsm_lac INTEGER,
            gsm_psc INTEGER,
            cdma_loc_datetime REAL,
            cdma_bsid INTEGER,
            cdma_bslat INTEGER,
            cdma_bslong INTEGER,
            cdma_nid INTEGER,
            cdma_sid INTEGER, 
            cellmovement INTEGER, 
            appsbeforeexception VARCHAR(200) )
        ''' % ( self.strtablename )
        self.conn = sqlite3.connect(self.databasename)
        self.cur = self.conn.cursor()
        self.cur.execute(queryCreateTable)
        self.conn.commit()


    # reverse find from index in  listdictDBDump to determine if columnName have a value.
    #if then, return element of  listdictDBDump
    def rfindColumnValue(self,  index, listdictDBDump, columnName ) :
        while( index >= 0  ) :
            dictDBDump = listdictDBDump[index]
            if dictDBDump.get(columnName, None) != None:
                return dictDBDump
            else:
                index = index -1
        return {}
        
    def boolCellMovement(self, calltimestamp, classmltdb ) :
        boolmovement = 0
        calltime5minbefore = calltimestamp - ( 5 * 60 * 1000)
        calltime5minafter = calltimestamp + ( 5 * 60 * 1000)
        
        listdictlocgsm = classmltdb.getlistdictFromTableDuration("gsm_cell_info",calltime5minbefore, calltime5minafter )
        if len(listdictlocgsm) > 0 :
            for dictlocgsm in listdictlocgsm : 
                prev_gsm_cid = dictlocgsm["gsm_cid"]
                prev_gsm_lac = dictlocgsm["gsm_lac"]
                if (prev_gsm_cid != -1 ) and (prev_gsm_lac != -1) :
                    break
            for dictlocgsm in listdictlocgsm : 
                gsm_cid = dictlocgsm["gsm_cid"]
                gsm_lac = dictlocgsm["gsm_lac"]
                if (gsm_cid == -1 ) or (gsm_lac == -1) :
                    continue
                if ((prev_gsm_cid != gsm_cid)  or (prev_gsm_lac != gsm_lac)) : 
                    boolmovement = 1 
                    break
        del listdictlocgsm 
        
        listdictloccdma = classmltdb.getlistdictFromTableDuration("cdma_cell_info",calltime5minbefore, calltime5minafter )
        if len(listdictloccdma) > 0 :
            for dictloccdma in listdictloccdma :
                prev_cdma_bslat = dictloccdma["cdma_bslat"]
                prev_cdma_bslong = dictloccdma["cdma_bslong"]
                if (prev_cdma_bslat != -1 ) and (prev_cdma_bslong != -1) :
                    break
            for dictloccdma in listdictloccdma :
                cdma_bslat = dictloccdma["cdma_bslat"]
                cdma_bslong = dictloccdma["cdma_bslong"]
                if (cdma_bslat == -1 ) or (cdma_bslong == -1) :
                    continue
                if ((prev_cdma_bslat != cdma_bslat)  or (prev_cdma_bslong != cdma_bslong)) : 
                    boolmovement = 1 
                    break
        del listdictloccdma 
        
        return boolmovement
        
    def getAppBeforeCall(self, calltimestamp, classmltdb ) :
        calltime5minbefore = calltimestamp - ( 5 * 60 * 1000)
        stractivity = ""
        try:
            listdictapp = classmltdb.getlistdictFromTableDuration("recent_act_info",calltime5minbefore, calltimestamp )
            # use the last dict
            apps = listdictapp[-1]["recentpackage_names"]
            
            listrecentActivity = apps.split("\n")
            for recentActivity in listrecentActivity : 
                stractivity = recentActivity
                recentpackage = recentActivity.split("/")[0]
                if recentpackage in [ "com.android.contacts" ,"com.android.phone", "com.lge.ltecall" ] : 
                    continue 
                else:
                    break
        except Exception :
            pass
        
        stractivity = stractivity.encode("utf-8")
        del listdictapp
        return stractivity
        

    def updateTableCallDrop( self,  listdictDBDump, listdictBasicSWVer, classmltdb ):
        model_name = listdictBasicSWVer[-1]["model_name"]
        phone_type = listdictBasicSWVer[-1]["phone_type"]
        network_type = listdictBasicSWVer[-1]["network_type"]
        IMEI = listdictBasicSWVer[-1]["IMEI"]

        for index in range(len(listdictDBDump)) :
            dictDBDump = listdictDBDump[index]
            if dictDBDump.get("exception_type", None) == "exception_calldrop" :
                calldatetime = dictDBDump["timestamp"]
                exception_cause = dictDBDump.get("exception_cause", "unknown" ) 
                exception_swver = dictDBDump.get("exception_swver", "unknown" ) 
                liststrtime = dump.ConvertTimeStampToString(calldatetime).split()
                calldate = "".join( liststrtime[0].split("-"))
                calltime = "".join( liststrtime[1].split(":"))
                
                querystate = " model_name , phone_type ,network_type ,exception_cause ,exception_swver ,IMEI , calldate , calltime ,calldatetime "
                qurryvalue = ' "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", %s ' % ( model_name , 
                        phone_type ,network_type ,exception_cause ,exception_swver ,IMEI , calldate , calltime , calldatetime) 
                
                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "avail_ram" )
                avail_ram = dictDBDump.get("avail_ram", None)
                if avail_ram != None :
                    querystate += " ,avail_ram "
                    qurryvalue += " , %s " % (avail_ram ) 
                
                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "telephony_state" )
                telephony_datetime = dictDBDump.get("timestamp", -1)
                telephony_state = dictDBDump.get("telephony_state", "")
                if telephony_datetime != -1 :
                    querystate += " ,telephony_datetime, telphony_state "
                    qurryvalue += ' , %s, "%s" ' % ( telephony_datetime, telephony_state  ) 
                    
                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "gsm_level" )
                gsm_signal_datetime = dictDBDump.get("timestamp", -1)
                gsm_level = dictDBDump.get("gsm_level", -1)
                gsm_signalstrength = dictDBDump.get("gsm_signalstrength", -1)
                if gsm_signal_datetime != -1 :
                    querystate += ' , gsm_signal_datetime, gsm_level, gsm_signalstrength '
                    qurryvalue += ' , %s, %s, %s ' % ( gsm_signal_datetime, gsm_level, gsm_signalstrength)
                
                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "lte_level" )
                lte_signal_datetime = dictDBDump.get("timestamp", -1 )
                lte_level = dictDBDump.get("lte_level", -1 )
                lte_signalstrength = dictDBDump.get("lte_signalstrength", -1 )
                if lte_signal_datetime != -1 :
                    querystate += ' , lte_signal_datetime, lte_level, lte_signalstrength '
                    qurryvalue += ' , %s, %s, %s ' % (  lte_signal_datetime, lte_level, lte_signalstrength)
                    

                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "gsm_cid" )
                gsm_loc_datetime = dictDBDump.get("timestamp", -1 )
                gsm_cid = dictDBDump.get("gsm_cid", -1 )
                gsm_lac = dictDBDump.get("gsm_lac", -1 )
                gsm_psc = dictDBDump.get("gsm_psc", -1 )
                if gsm_loc_datetime != -1 :
                    querystate += ' , gsm_loc_datetime, gsm_cid, gsm_lac, gsm_psc '
                    qurryvalue += ' , %s, %s, %s,%s  ' % ( gsm_loc_datetime, gsm_cid, gsm_lac, gsm_psc )

                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "cdma_level" )
                cdma_signal_datetime = dictDBDump.get("timestamp", -1 )
                cdma_level = dictDBDump.get("cdma_level", -1 )
                cdma_signalstrength = dictDBDump.get("cdma_signalstrength", -1 )
                if cdma_signal_datetime != -1 :
                    querystate += ' , cdma_signal_datetime, cdma_level, cdma_signalstrength  '
                    qurryvalue += ' , %s, %s, %s  ' % ( cdma_signal_datetime, cdma_level, cdma_signalstrength  )

                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "cdma_bsid" )
                cdma_loc_datetime = dictDBDump.get("timestamp", -1 )
                cdma_bsid = dictDBDump.get("cdma_bsid", -1 )
                cdma_bslat = dictDBDump.get("cdma_bslat", -1 )
                cdma_bslong = dictDBDump.get("cdma_bslong", -1 )
                cdma_nid = dictDBDump.get("cdma_nid", -1 )
                cdma_sid = dictDBDump.get("cdma_sid", -1 )
                if cdma_loc_datetime != -1 :
                    querystate += ' , cdma_loc_datetime, cdma_bsid, cdma_bslat, cdma_bslong, cdma_nid,cdma_sid  '
                    qurryvalue += ' , %s, %s, %s,%s, %s, %s  ' % ( cdma_loc_datetime, cdma_bsid, cdma_bslat, cdma_bslong, cdma_nid,cdma_sid)
                    
                # determine  cellmovement
                boolcellmovement = self.boolCellMovement(calldatetime, classmltdb )
                querystate += ' ,cellmovement '
                qurryvalue += ' , %s ' % (boolcellmovement)
                
                # get the app name near call drop
                appsbeforeexception = self.getAppBeforeCall(calldatetime, classmltdb )
                if len(appsbeforeexception) > 0 : 
                    querystate += ' ,appsbeforeexception '
                    qurryvalue += ' , "%s" ' % (appsbeforeexception)
                    
                    
                querystate = "INSERT INTO " + self.strtablename  + " ( " + querystate + " )  VALUES ( " + qurryvalue + " )" 
                self.cur.execute( querystate )
            
        self.conn.commit()

        

''' ---------order the SVC data by IMEI -------- '''
def IMEICmp ( a1, a2 ) :
    return cmp ( a1["esn_imei_no"], a2["esn_imei_no"] )



def deleteDuplicateIMEI(listdictmltlogs):
    ''' ---------replace  IMEI with log_file_name if IMEI == ""  for listdictmltlogs -------- '''
    for dictmltlogs in listdictmltlogs :
        if dictmltlogs["esn_imei_no"] == "" or dictmltlogs["esn_imei_no"] == None :
            dictmltlogs["esn_imei_no"] = dictmltlogs["log_file_name"]


    ''' ---------delete the duplicated IMEI ITEM  for listdictmltlogs -------- '''
    listdictmltlogs.sort(IMEICmp)


    listdictmltlogsTemp = []
    dictmltlogsPre= {}
    dictmltlogsPre["esn_imei_no"] = ""

    for dictmltlogs in listdictmltlogs :
        if dictmltlogs["esn_imei_no"] == dictmltlogsPre["esn_imei_no"]:
                print "esn_imei_no" , dictmltlogs["esn_imei_no"]
                continue
        else:
            listdictmltlogsTemp.append(dictmltlogs)
            dictmltlogsPre = dictmltlogs

    ##restore
    return listdictmltlogsTemp

global logging_logfilepath
logging_logfilepath = ""

def MakeTableExecipton(dbfilename, modelname, period, FileDrv ):
    global logging_logfilepath
    starttime =  datetime.now()

    startdate =  period.split("-")[0]
    enddate = period.split("-")[1]

    #!!! get the MLT LOG list
    import pymssql
    conn = pymssql.connect(host='10.185.135.57', user='MLT_INF', password='inf_P@ssword', database='LGMLTP', charset="UTF-8" , as_dict=True)
    cur = conn.cursor()

    # 국내 모델만.
    LOGStatement = ''' select * from  dmd_log_m  where ( model_name = '%s' ) and ( cause_cd = 'MDA' or cause_cd = 'MBE'  ) and  base_ymd between '%s' and '%s'  '''
    LOGStatement = LOGStatement % ( modelname, startdate, enddate )
    print "LOGStatement = " , LOGStatement

    cur.execute(LOGStatement)
    listdictmltlogs = cur.fetchall()
    conn.close()

    listdictmltlogs = deleteDuplicateIMEI(listdictmltlogs)

    len_mlt = (len(listdictmltlogs))
    msg1 = "MLT LOG Total count = %s " % (len_mlt)
    print msg1

    #!!! setup the CallDrop dB and table
    classcalldrop = classTableCallDrop(dbfilename)
    classcalldrop.setupDBandTable()
    
    classexception = classTableException(dbfilename)
    classexception.setupDBandTable()
    
    classcallinout = classTableCallInOut("callinout.db3")
    classcallinout.setupDBandTable()


    strProcessing =  "**** The remaining count of MLTLOG (%s) : "  % ( len_mlt )

    util.FileDrv = FileDrv
    util.ClearMLTLOG()

    for dictmltlogs in listdictmltlogs:
        print " "
        print strProcessing, len_mlt

        logging_logfilepath = os.path.join(dictmltlogs["log_file_path"] ,  dictmltlogs["log_file_name"])
        util.CopyMLTLOG(logging_logfilepath )
        
        dblist = glob.glob('*.db')
        if len( dblist ) == 0 :
            continue
        dbMLTDBname = dblist[0]
        
        classmltdb = dump.ClassMLTDB( dbMLTDBname )
        if classmltdb.boolTableValied == False:
            continue
            
        count = classmltdb.get_count_byExceptiontype("exception_calldrop")
        
        listdictDBDump = []
        listdictBasicSWVer = []
        classmltdb.get_listDBDump_ListSWVer( listdictDBDump, listdictBasicSWVer )
        
        if count > 0 :
            classcalldrop.updateTableCallDrop(listdictDBDump,listdictBasicSWVer, classmltdb  )
            print "!!!! CallDrop count : %s " % ( count )
        else:
            print "!!!! No CallDrop ... "
        
        if (len(listdictDBDump) > 0) and (len(listdictBasicSWVer) > 0) :
            classexception.updateTableException(listdictDBDump,listdictBasicSWVer, classmltdb  )
            classcallinout.updateTableCallInOut( listdictDBDump,listdictBasicSWVer )
            
        listdictDBDump = None
        listdictBasicSWVer = None
        del classmltdb

        util.DeleteMLTLOG()
        
        len_mlt = len_mlt - 1 

        

    del classcalldrop
    del classexception
    del classcallinout
    del listdictmltlogs


    endtime =  datetime.now()
    print endtime
    msg2 = "elasped time is : " +  str(endtime - starttime)
    print msg2

    strReportFileName = "ReportCallDrop_" + modelname + "_" + period + ".txt"
    f = open(strReportFileName, "w")
    f.write( "Period : " + period + "\n" )
    f.write( "Model Name : " + modelname + "\n" )
    f.write( "DB filename : " + dbfilename + "\n" )
    f.write( "LOGStatement = " + LOGStatement + "\n" )
    f.write( "processing time : " + str(starttime) + "~" + str(endtime) + "\n" )
    f.write( msg2 + "\n" )
    f.write( msg1 + "\n")
    f.close()



def MakeTableExeciptonLocal(dbfilename):
    global logging_logfilepath
    starttime =  datetime.now()
    
    classcalldrop = classTableCallDrop(dbfilename)
    classcalldrop.setupDBandTable()
    
    classexception = classTableException(dbfilename)
    classexception.setupDBandTable()
    
    classcallinout = classTableCallInOut("callinout.db3")
    classcallinout.setupDBandTable()
    
    
    dblist = glob.glob('*.db')
    len_mlt = len(dblist)
    strProcessing =  "**** The remaining count of MLTLOG (%s) : "  % ( len_mlt )
    
    for dbMLTDBname in dblist : 
        print " "
        print strProcessing, len_mlt
        
        logging_logfilepath = dbMLTDBname
        
        classmltdb = dump.ClassMLTDB( dbMLTDBname )
        if classmltdb.boolTableValied == False:
            continue
            
        count = classmltdb.get_count_byExceptiontype("exception_calldrop")
        
        listdictDBDump = []
        listdictBasicSWVer = []
        classmltdb.get_listDBDump_ListSWVer( listdictDBDump, listdictBasicSWVer )
        
        if count > 0 :
            classcalldrop.updateTableCallDrop(listdictDBDump,listdictBasicSWVer, classmltdb  )
            print "!!!! CallDrop count : %s " % ( count )
        else:
            print "!!!! No CallDrop ... "
        
        if (len(listdictDBDump) > 0) and (len(listdictBasicSWVer) > 0) :
            classexception.updateTableException(listdictDBDump,listdictBasicSWVer, classmltdb  )
            classcallinout.updateTableCallInOut( listdictDBDump,listdictBasicSWVer )
        
        del classmltdb
        len_mlt = len_mlt -1 
        
        
    del classcalldrop
    del classexception
    del classcallinout
    del dblist


    endtime =  datetime.now()
    print endtime
    msg2 = "elasped time is : " +  str(endtime - starttime)
    print msg2

    strReportFileName = "ReportCallDrop_" + dbfilename+ ".txt"
    f = open(strReportFileName, "w")
    f.write( "DB filename : " + dbfilename + "\n" )
    f.write( "processing time : " + str(starttime) + "~" + str(endtime) + "\n" )
    f.write( msg2 + "\n" )
    f.close()


'''
c:> python MltDBDump.py -o c:\temp_mlt  -a
'''

if __name__ == "__main__":
    import argparse
    diroutput = "."
    ShutdownAfter = False
    dbfilename = "exceptionhist.db3"
    period = ""
    FileDrv = "Z"
    modelname = ""
    local = False

    cmdlineopt = argparse.ArgumentParser(description='make the call-drop DB')
    cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='working directory . default = . sample: c:\\temp_mlt' )
    cmdlineopt.add_argument('-s', action="store_true", dest="ShutdownAfter",  default=False, help='shutdown system after job finished,  default= Faluse' )
    cmdlineopt.add_argument('-db', action="store", dest="dbfilename",  default="exceptionhist.db3", help='dump the input file,  default= "calldrop.db" ' )
    cmdlineopt.add_argument('-p', action="store", dest="period",  default="", help='period to search,  example : 20120601-20120630' )
    cmdlineopt.add_argument('-d', action="store", dest="FileDrv", default='Z',  help=' Windows File Driver Character of server MLT_LOG directory to be maapped to windows system . example : Z ' )
    cmdlineopt.add_argument('-m', action="store", dest="modelname", default='',  help=' Model name. example: LGF100S  ' )
    cmdlineopt.add_argument('-l', action="store_true", dest="local", default=False,  help=' Operation at local hard   ' )
    cmdlineresults = cmdlineopt.parse_args()


    if len(cmdlineresults.period) == 0 :
        print " Must have the value of period as parameter"        
        exit()
    
    if len(cmdlineresults.modelname) == 0 :
        print " Must have the value of modelname as parameter"        
        exit()
        
    period = cmdlineresults.period
    modelname = cmdlineresults.modelname
    ShutdownAfter = cmdlineresults.ShutdownAfter
    diroutput = cmdlineresults.diroutput
    dbfilename = cmdlineresults.dbfilename        
    FileDrv = cmdlineresults.FileDrv
    local = cmdlineresults.local

    ''' goto the diroutput dir to work '''
    diroutput = os.path.abspath(diroutput)
    if not os.path.exists(diroutput):
        os.makedirs(diroutput)
    os.chdir(diroutput)

    try:
        if local == False:
            MakeTableExecipton( dbfilename, modelname, period,FileDrv )
        else:
            MakeTableExeciptonLocal(dbfilename)
    except Exception as e  : 
        import traceback


        strReportFileName = "ErrorCallDrop_" + modelname + "_" + period + ".txt"
        f = open(strReportFileName, "w")        
        
        f.write( "MLT LOG name : " +  logging_logfilepath + "\n" )
        f.write( "Error Message : \n" )
        f.write( traceback.format_exc() )

        f.close()
        

    if ShutdownAfter == True :
        os.system( "shutdown /s /t 300 ")














