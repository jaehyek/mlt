# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:04:42 2013

@author: jaehyek.choi

purpose : 주어진 모델명/기간을 바탕으로 mlt DB에서 log을 추출해서 mongo DB에 저장한다.
          생성되는  collection은 : collectionException, collectionCalldrop 
"""

import os
from datetime import datetime
import MltDBDump as dump
import mltutils as util
import glob
import mongoutil
import mltserver

def processCalldropExceptFromMLT (dbMLTDBname, classmongocalldrop,classmongoexcept ):

    classmltdb = dump.ClassMLTDB( dbMLTDBname )
    if classmltdb.boolTableValied == False:
        del classmltdb
        return


    count = classmltdb.get_count_byExceptiontype("exception_calldrop")

    listdictDBDump = []
    listdictBasicSWVer = []
    classmltdb.get_listDBDump_ListSWVer( listdictDBDump, listdictBasicSWVer )

    if ( len(listdictBasicSWVer) == 0 )  or (len(listdictDBDump) == 0 ) :
        del listdictDBDump
        del listdictBasicSWVer
        del classmltdb
        return

    ## save the call drop
    if count == 0:
        print "!!!! No CallDrop ... "
    else:
        print "!!!! CallDrop count : %s " % ( count )
        classcalldrop = dump.classCallDropDetail()
        listdictcalldropdetail = classcalldrop.getListDictCallDropDetail(listdictDBDump,listdictBasicSWVer,classmltdb  )
        for dictcalldropdetail in listdictcalldropdetail :
            dictcalldropcause = dump.getDictExceptionCause(dictcalldropdetail["exception_type"], dictcalldropdetail["exception_cause"] )
            dictrilcause = dump.getDictRilCause( dump.getStrRilCause(dictcalldropdetail["ril_log"] ))
            dicttemp = {}
            dicttemp.update(dictcalldropdetail )
            dicttemp.update(dictcalldropcause )
            dicttemp.update(dictrilcause )
            classmongocalldrop.insertdoc(dicttemp)
            del dicttemp
            del dictcalldropcause
        del listdictcalldropdetail
        del classcalldrop


    ## save only the Exception
    listdictExceptionInfoRaw = classmltdb.getListDictExceptionInfoRaw(  )

    for dictExceptionInfoRaw in listdictExceptionInfoRaw :
        dicttemp = {}
        dicttemp.update(listdictBasicSWVer[-1])
        dicttemp.update(dictExceptionInfoRaw)
        strexceptioncause = dump.getStrExceptionCause(dictExceptionInfoRaw["exception_type"], dictExceptionInfoRaw["exception_data"], dictExceptionInfoRaw["lastk_log"] )
        dictexceptioncause = dump.getDictExceptionCause(dictExceptionInfoRaw["exception_type"],strexceptioncause )
        dicttemp.update(dictexceptioncause)

        if (dictExceptionInfoRaw["exception_type"] == "exception_calldrop" ) and (len(dictExceptionInfoRaw["ril_log"]) > 0 ) :
            strrilcause = dump.getStrRilCause(dictExceptionInfoRaw["ril_log"])
            dictrilcause = dump.getDictRilCause( strrilcause)
            dicttemp.update(dictrilcause)

        classmongoexcept.insertdoc( dicttemp )
        del dicttemp
        del dictexceptioncause

    del listdictBasicSWVer
    del listdictDBDump
    del listdictExceptionInfoRaw

    del classmltdb


global logging_logfilepath
logging_logfilepath = ""

def MakeCollectionExecipton( svrMongo, dbfilename, modelname, period, FileDrv, booltag=False ):
    global logging_logfilepath
    starttime =  datetime.now()

    startdate =  period.split("-")[0]
    enddate = period.split("-")[1]

    listdictmltlogs = mltserver.getListDictMLTLOGFromServer( modelname, startdate, enddate )

    len_mlt = (len(listdictmltlogs))
    msg1 = "MLT LOG Total count = %s " % (len_mlt)
    print msg1

    if booltag==True :
        tag = modelname + "_" + startdate[:6]
    else:
        tag = ""

    classmongoexcept = mongoutil.ClassMongo( dbfilename, "collectionException", svrMongo, tag )
    classmongocalldrop = mongoutil.ClassMongo( dbfilename, "collectionCalldrop", svrMongo, tag)

    strProcessing =  "**** The remaining count of MLTLOG (%s) : "  % ( len_mlt )

    util.FileDrv = FileDrv

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

        processCalldropExceptFromMLT(dbMLTDBname, classmongocalldrop,classmongoexcept  )

        util.DeleteMLTLOG()

    del listdictmltlogs

    del classmongoexcept
    del classmongocalldrop


    endtime =  datetime.now()
    print endtime
    msg2 = "elasped time is : " +  str(endtime - starttime)
    print msg2

    strReportFileName = "ReportCallDrop_" + modelname + "_" + period + ".txt"
    f = open(strReportFileName, "w")
    f.write( "Period : " + period + "\n" )
    f.write( "Model Name : " + modelname + "\n" )
    f.write( "DB filename : " + dbfilename + "\n" )
    f.write( "processing time : " + str(starttime) + "~" + str(endtime) + "\n" )
    f.write( msg2 + "\n" )
    f.write( msg1 + "\n")
    f.close()



def MakeCollectionExeciptonLocal( svrMongo, dbfilename, booltag=False):
    global logging_logfilepath
    starttime =  datetime.now()

    if booltag == True :
        tag = str(starttime)
    else:
        tag = ""

    classmongoexcept = mongoutil.ClassMongo( dbfilename, "collectionException", svrMongo, tag)
    classmongocalldrop = mongoutil.ClassMongo( dbfilename, "collectionCalldrop", svrMongo, tag )

    dblist = glob.glob('*.db')
    len_mlt = len(dblist)

    strProcessing =  "**** The remaining count of MLTLOG (%s) : "  % ( len_mlt )

    for dbMLTDBname in dblist :
        print "--> processing %s \n" % (dbMLTDBname)
        print strProcessing, len_mlt
        len_mlt -= 1

        logging_logfilepath = dbMLTDBname

        processCalldropExceptFromMLT(dbMLTDBname, classmongocalldrop,classmongoexcept  )

    del dblist

    del classmongoexcept
    del classmongocalldrop


    endtime =  datetime.now()
    print endtime
    msg2 = "elasped time is : " +  str(endtime - starttime)
    print msg2

    strReportFileName = "ReportMongoException_" + dbfilename+ ".txt"
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
    dbfilename = "MLTDB"
    period = ""
    FileDrv = "Z"
    modelname = ""
    local = False
    booltag = False
    svrMongo = "172.21.26.39"

    cmdlineopt = argparse.ArgumentParser(description='extract MLT LOG, and create 2 collection : collectionException, collectionCalldrop')
    cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='working directory . default = . sample: c:\\temp_mlt' )
    cmdlineopt.add_argument('-s', action="store_true", dest="ShutdownAfter",  default=False, help='shutdown system after job finished,  default= Faluse' )
    cmdlineopt.add_argument('-db', action="store", dest="dbfilename",  default="MLTDB", help='dump the input file,  default= "MLTDB" ' )
    cmdlineopt.add_argument('-p', action="store", dest="period",  default="", help='period to search,  example : 20120601-20120630' )
    cmdlineopt.add_argument('-svr', action="store", dest="svrMongo",  default="172.21.26.39", help='MongoDB Server IP' )
    cmdlineopt.add_argument('-d', action="store", dest="FileDrv", default='Z',  help=' Windows File Driver Character of server MLT_LOG directory to be maapped to windows system . example : Z ' )
    cmdlineopt.add_argument('-m', action="store", dest="modelname", default='',  help=' Model name. example: LGF100S  ' )
    cmdlineopt.add_argument('-l', action="store_true", dest="local", default=False,  help=' Operation at local hard   ' )
    cmdlineopt.add_argument('-t', action="store_true", dest="booltag", default=False,  help=' taggable for each document  ' )

    cmdlineresults = cmdlineopt.parse_args()


    if cmdlineresults.local != True :
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
    svrMongo = cmdlineresults.svrMongo
    booltag = cmdlineresults.booltag

    ''' goto the diroutput dir to work '''
    diroutput = os.path.abspath(diroutput)
    if not os.path.exists(diroutput):
        os.makedirs(diroutput)
    os.chdir(diroutput)

    try:
        if local == False:
            MakeCollectionExecipton( svrMongo, dbfilename, modelname, period,FileDrv, booltag )
        else:
            MakeCollectionExeciptonLocal(svrMongo, dbfilename, booltag)
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


