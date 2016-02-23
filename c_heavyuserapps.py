# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:11:24 2013

@author: jaehyek.choi
headvy user는 하루 8시간을 사용한다고 가정하고, LCD-ON인 경우의 시간을 측정한다.
그리고 해당 MLT DB에서 app list을 추출한다.
"""

import os 
import m_email
from datetime import datetime
import MltDBDump as dump
import mltutils as util
import glob
import mltserver

def getUsedSecsLCDOnSecs(listdictDBDump):
    timestampFirstLCDonTime = 0 
    timestampLastLCDonTime = 0 
    timetotalLCDOnTime = 0
    
    genk = ( kk for kk in range(len(listdictDBDump)))
    
    for index in genk :
        lcdstate = listdictDBDump[index].get("lcd_state", None )
        if lcdstate == None :
            continue 
        if lcdstate == "LCD_ON" :
            timestampFirstLCDonTime = listdictDBDump[index]["timestamp"]
            break
            
    timestampLCDOnStart = timestampFirstLCDonTime
    pre_stateLCD = 1 # meaning LCD ON
    for index in genk :
        lcdstate = listdictDBDump[index].get("lcd_state", None )
        if lcdstate == None :
            continue 
        if (lcdstate == "LCD_OFF") and (pre_stateLCD == 1 ) :
            timetotalLCDOnTime += listdictDBDump[index]["timestamp"] - timestampLCDOnStart
            pre_stateLCD = 0
            timestampLastLCDonTime = listdictDBDump[index]["timestamp"]
            continue 
        if lcdstate == "LCD_ON" : 
            if pre_stateLCD == 0 :
                timestampLCDOnStart = listdictDBDump[index]["timestamp"]
            pre_stateLCD = 1 
            
    del genk
    
#    totalDays = float(timestampLastLCDonTime - timestampFirstLCDonTime ) /( 24 * 60 * 60 * 1000)
#    totalLCDOnHours = float(timetotalLCDOnTime) / ( 60 * 60 * 1000)
    
    totalUsedSecs = float(timestampLastLCDonTime - timestampFirstLCDonTime ) /( 1000)
    totalLCDOnSecs = float(timetotalLCDOnTime) / ( 1000)
       
    return totalUsedSecs, totalLCDOnSecs
    

def processHeavyUserFromMLT(dbMLTDBname, dicttupleappaccum  ):
    classmltdb = dump.ClassMLTDB( dbMLTDBname )
    if classmltdb.boolTableValied == False:
        del classmltdb
        return 0 


    listdictDBDump = []
    listdictBasicSWVer = []
    classmltdb.get_listDBDump_ListSWVer( listdictDBDump, listdictBasicSWVer )

    if ( len(listdictBasicSWVer) == 0 )  or (len(listdictDBDump) == 0 ) :
        del listdictDBDump
        del listdictBasicSWVer
        del classmltdb
        return 0

    totalUsedSecs, totalLCDOnSecs = getUsedSecsLCDOnSecs(listdictDBDump)
    if totalUsedSecs == 0 :
        LCDOnHoursPerDay = 0.0 
    else:
        #LCDOnHoursPerDay = ( totalLCDOnSecs / 60 * 60 ) / (totalUsedSecs / 60 * 60 * 24)
        LCDOnHoursPerDay = float( totalLCDOnSecs * 24 ) / (totalUsedSecs )
        
    intLCDOnHoursPerDay = int(LCDOnHoursPerDay)
    if intLCDOnHoursPerDay == 8 :
        classmltdb.getAppAccumulation(dicttupleappaccum)

    del listdictBasicSWVer
    del listdictDBDump
    del classmltdb
    
    return intLCDOnHoursPerDay

def SaveDictToCSV( dicttupleAppAccumInfo , nameCSV )   :  
    fieldnames = [ "packagename", "total_app_count", "total_run_time(s)", "total_run_count"]
    f = open(nameCSV, "w" )
    f.write( ",".join(fieldnames) + "\n" )
    listkeys = dicttupleAppAccumInfo.keys()
    for packagename in listkeys :
        total_app_count, sum_total_time , sum_total_run_count = dicttupleAppAccumInfo[ packagename ]
        f.write( ",".join([packagename,str(total_app_count),str(sum_total_time),str(sum_total_run_count) ]) + "\n" )
    f.close()
    

global logging_logfilepath
logging_logfilepath = ""
def mltheadvyuserapps( modelname, period,FileDrv):
    global logging_logfilepath
    starttime =  datetime.now()

    startdate =  period.split("-")[0]
    enddate = period.split("-")[1]

    listdictmltlogs = mltserver.getListDictMLTLOGFromServer( modelname, startdate, enddate )

    len_mlt = (len(listdictmltlogs))
    msg1 = "MLT LOG Total count = %s " % (len_mlt)
    print msg1


    strProcessing =  "**** The remaining count of MLTLOG (%s) : "  % ( len_mlt )

    util.FileDrv = FileDrv
    dicttupleappaccum = {}
    listdbnameLCDON8 = []
    listdbnameLCDON7 = []
    listdbnameLCDON6 = []
    listdbnameLCDON5 = []
    
    for dictmltlogs in listdictmltlogs:
        print " "
        print strProcessing, len_mlt
        len_mlt -= 1

        logging_logfilepath = os.path.join(dictmltlogs["log_file_path"] ,  dictmltlogs["log_file_name"])
        util.CopyMLTLOG(logging_logfilepath )

        dbMLTDBname = dictmltlogs["log_file_name"]
        dbMLTDBname = os.path.basename(dbMLTDBname)
        dbMLTDBname = dbMLTDBname.split(".")[0] + ".db"

        dblist = glob.glob(dbMLTDBname)
        if len( dblist ) == 0 :
            continue

        LCDOnHours = processHeavyUserFromMLT(dbMLTDBname, dicttupleappaccum  )
        if LCDOnHours == 8 : 
            listdbnameLCDON8.append( logging_logfilepath)
            # don't delete the MLT DB
            continue
        elif LCDOnHours == 7 : 
            listdbnameLCDON7.append( logging_logfilepath)
        elif LCDOnHours == 6 : 
            listdbnameLCDON6.append( logging_logfilepath)
        elif LCDOnHours == 5 : 
            listdbnameLCDON5.append( logging_logfilepath)

        util.DeleteMLTLOG(dbMLTDBname)

    

    
    print "-------------sending LCDOn8 file List--------------"
    msgLCDOn = "\n".join(listdbnameLCDON8)
    m_email.send_mail("jaehyek.choi@lge.com",["jaehyek.choi@lge.com"], "listdbnameLCDON8", msgLCDOn,  [])

    print "-------------sending LCDOn8 file List--------------"
    msgLCDOn = "\n".join(listdbnameLCDON7)
    m_email.send_mail("jaehyek.choi@lge.com",["jaehyek.choi@lge.com"], "listdbnameLCDON7", msgLCDOn,  [])
    
    print "-------------sending LCDOn8 file List--------------"
    msgLCDOn = "\n".join(listdbnameLCDON6)
    m_email.send_mail("jaehyek.choi@lge.com",["jaehyek.choi@lge.com"], "listdbnameLCDON6", msgLCDOn,  [])    
    
    print "-------------sending LCDOn8 file List--------------"
    msgLCDOn = "\n".join(listdbnameLCDON5)
    m_email.send_mail("jaehyek.choi@lge.com",["jaehyek.choi@lge.com"], "listdbnameLCDON5", msgLCDOn,  [])    

    
    filenameAppAccCSV = "AppAccumulation.csv"
    SaveDictToCSV(dicttupleappaccum, filenameAppAccCSV )
    print "-------------sending CSV ------------"
    m_email.send_mail("jaehyek.choi@lge.com",["jaehyek.choi@lge.com"], 
                      "AppAccumulation.csv", "AppAccumulation.csv", [filenameAppAccCSV])
                      
                      
                      

    endtime =  datetime.now()
    print endtime
    msg2 = "elasped time is : " +  str(endtime - starttime)
    print msg2

    strReportFileName = "ReportHeavyUser_" + modelname + "_" + period + ".txt"
    f = open(strReportFileName, "w")
    f.write( "Period : " + period + "\n" )
    f.write( "Model Name : " + modelname + "\n" )
    f.write( "processing time : " + str(starttime) + "~" + str(endtime) + "\n" )
    f.write( msg2 + "\n" )
    f.write( msg1 + "\n")
    f.close()
    
    del listdictmltlogs
    del dicttupleappaccum




if __name__ == "__main__":
    import argparse
    diroutput = "."
    period = ""
    FileDrv = "Z"
    modelname = ""
    
    
    cmdlineopt = argparse.ArgumentParser(description='make the call-drop DB')
    cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='working directory . default = . sample: c:\\temp_mlt' )
    cmdlineopt.add_argument('-p', action="store", dest="period",  default="", help='period to search,  example : 20120601-20120630' )
    cmdlineopt.add_argument('-m', action="store", dest="modelname", default='',  help=' Model name. example: LGF100S  ' )
    cmdlineopt.add_argument('-d', action="store", dest="FileDrv", default='Z',  help=' Windows File Driver Character of server MLT_LOG directory to be maapped to windows system . example : Z ' )
    
    
    
    cmdlineresults = cmdlineopt.parse_args()
    

    if len(cmdlineresults.period) == 0 :
        print " Must have the value of period as parameter"
        exit()

    if len(cmdlineresults.modelname) == 0 :
        print " Must have the value of modelname as parameter"
        exit()

    period = cmdlineresults.period
    modelname = cmdlineresults.modelname
    diroutput = cmdlineresults.diroutput
    FileDrv = cmdlineresults.FileDrv
    
    ''' goto the diroutput dir to work '''
    diroutput = os.path.abspath(diroutput)
    if not os.path.exists(diroutput):
        os.makedirs(diroutput)
    os.chdir(diroutput)

    try:
        mltheadvyuserapps( modelname, period,FileDrv)
    except Exception as e  :
        import traceback


        strReportFileName = "ErrorHeavyUser_" + modelname + "_" + period + ".txt"
        f = open(strReportFileName, "w")
        f.write( "Error Message : \n" )
        f.write( "MLT LOG name : " +  logging_logfilepath + "\n" )
        f.write( traceback.format_exc() )

        f.close()
        
        print "------------- encountng Error during processing ------------------"
        m_email.send_mail("jaehyek.choi@lge.com",["jaehyek.choi@lge.com"], 
                          "Error Counting During HeavyUser", "Error Counting During HeavyUser", 
                          [strReportFileName])
        print "sending the file %s using email " % strReportFileName
    
    

    
    
    
    

