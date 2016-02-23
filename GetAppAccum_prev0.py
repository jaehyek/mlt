# _*_ coding: utf-8 _*_

'''
Created on 2012. 10. 30.
@author: jaehyek
'''

import os , argparse
from datetime import datetime
import shutil


'''
c:> python GetAppAccum.py -o D:\\temp_MLT_F200 -m "LG-F200L LG-F200S LG-F200K" -p 20120101-20130220 -d Z
'''


# variables.
diroutput = "."
modelname = ""
period = ""
FileDrv = "Z"
LogFileCopy = False
ShutdownAfter = False
SavingHeadName = ""


if __name__ == '__main__':
    pass

starttime =  datetime.now()
print starttime



cmdlineopt = argparse.ArgumentParser(description='get the MLT LOG from MLT Server 10.185.135.57')
cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='output directory to put MLT log file. default = . sample: c:\\temp_mlt' )
cmdlineopt.add_argument('-m', action="store", dest="modelname", default='',  help=' Model name. example: F100S  ' )
cmdlineopt.add_argument('-p', action="store", dest="period", default='',  help=' period . example : 20120601-20120630  ' )
cmdlineopt.add_argument('-d', action="store", dest="FileDrv", default='Z',  help=' Windows File Driver Character of server MLT_LOG directory to be maapped to windows system . example : Z ' )
cmdlineopt.add_argument('-n', action="store", dest="SavingHeadName", default='',  help=' indicate the file head name for result saving after processing  example : model ' )
cmdlineopt.add_argument('-l', action="store_true", dest="LogFileCopy",  default=False, help='copy MLT Log db file to output directory default= Faluse' )
cmdlineopt.add_argument('-s', action="store_true", dest="ShutdownAfter",  default=False, help='shutdown system after job finished,  default= Faluse' )

cmdlineresults = cmdlineopt.parse_args()

diroutput = cmdlineresults.diroutput
modelname = cmdlineresults.modelname
period = cmdlineresults.period
FileDrv = cmdlineresults.FileDrv
LogFileCopy = cmdlineresults.LogFileCopy
ShutdownAfter = cmdlineresults.ShutdownAfter
SavingHeadName = cmdlineresults.SavingHeadName




''' variable initialization for test of F100L '''
# period = "20121001-20130220"
# diroutput = "D:\\temp_MLT_F200"
# modelname = "LG-F180L LG-F180S LG-F180K"
# FileDrv = "Z"
# LogFileCopy = True
# ShutdownAfter = True

# period = "20120316-20130316"
# diroutput = "D:\\temp_MLT_F240_AppAcc"
# modelname = "LGF240L LGF240S LGF240K"
# FileDrv = "Z"
# LogFileCopy = False
# ShutdownAfter = False

''' variable initialization for test of F100S'''
##period = "20120705-20120815"
##diroutput = "D:\\temp_MLT_F100"
##modelname = "LGF100S"


'''
. IP :\\10.185.135.57\mlt_log_guest --> \10.185.135.115\mlt_log_guest
. ID : mlt_inf01
.  Password  inf_P@ssword
'''


if len(modelname) == 0 :
    print "No Model Name"
    exit()

if len(period) == 0 :
    print "No period"
    exit()

if len(FileDrv) == 0 :
    print "No File Drv Name"
    exit()

if len(diroutput) == 0 :
    diroutput = "."

import os
def Jobfinished ():
    if ShutdownAfter == False :
        exit()
    else:
        os.system( "shutdown /s /t 300 ")

diroutput = os.path.abspath(diroutput)
if not os.path.exists(diroutput):
    os.makedirs(diroutput)

''' goto the diroutput dir to work '''
os.chdir(diroutput)



modellist = modelname.split(' ')
modelcount = len(modellist)
modelstatementA = ""
modelstatementB = ""
modelstatementSVC = ""
excelsavingname = ""
for model in modellist :
    modelstatementA += "a.model_name = " + "'" +  model + "' "
    modelstatementB += "b.model_name = " + "'" +  model + "' "
    modelstatementSVC += "model_name = " + "'" +  model + "' "
    excelsavingname += model
    modelcount -= 1
    if ( modelcount > 0 ) :
        modelstatementA += " or "
        modelstatementB += " or "
        modelstatementSVC += " or "
        excelsavingname += "_"




''' extract the period to startdate and enddate. '''
startdate =  period.split("-")[0]
enddate = period.split("-")[1]

strTempDir = "temp"


import glob
import shutil


def ClearMLTLOG():
    listlog = glob.glob('*.db')
    for log in listlog:
        os.remove( log )


def DeleteMLTLOG():
    listlog = glob.glob('*.db')
    if LogFileCopy == False :
        for log in listlog:
            os.remove( log )
    else :
        tempdir = diroutput + "\\" + strTempDir
        if not os.path.exists(tempdir):
            os.makedirs(tempdir)

        ''' move MLT LOG to temp dir '''
        for log in listlog:
            shutil.move(log, tempdir )

import zipfile
def CopyMLTLOG ( logfullpath ) :
    filesrc = logfullpath.replace("MLT_LOG\\", "")
    filesrc = FileDrv + filesrc[1:]
    if os.path.isfile(filesrc) :
        print "Copying log file from : ", filesrc
        shutil.copy(filesrc, r'.')
    else :
        # try to check the zip file and extract it 
        filesrczip = filesrc[:-2] + "zip"
        if os.path.isfile(filesrczip) :
            print "Copying log file from : ", filesrczip
            shutil.copy(filesrczip, r'.')
            filesrczip = os.path.basename(filesrczip)
            z = zipfile.ZipFile(filesrczip)
            z.extractall()
            z = None
            listzfile = glob.glob('*.zip')
            for zfile in listzfile :
                try:
                    os.remove(zfile)
                except Exception :
                    print "======= Can't remove the file ======== \n ", zfile
        else:
            print "!!!    DB file does not exist : ", filesrc, filesrczip


# LOGstatement = '''
# select  *
# from    dmr_basic_info
# where   1=1
# and ( %s)
# and     input_imei_no in (    select input_imei_no
                            # from    dmr_service_history
                            # where   1=1
                            # and ( %s )
							# and receipt_ymd between '%s' and '%s'
                            # group by input_imei_no
                        # )
# '''

'''
receipt_ymd 은 수리 접수일자이다. 일본향은 수리접수일자와 log 받은 날짜가 많이 다르다(1개월 이상 ). 
그러므로 log 받은 날짜인 base_ymd을 사용하는 것이 맞다.
'''

LOGstatement = ''' select  * from  dmd_log_m where  (%s) and base_ymd between '%s' and '%s'  '''

LOGstatement = LOGstatement % ( modelstatementSVC, startdate, enddate )

print "LOGstatement = ",  LOGstatement

import pymssql
conn = pymssql.connect(host='10.185.135.57', user='MLT_INF', password='inf_P@ssword', database='LGMLTP', charset="UTF-8" , as_dict=True)
cur = conn.cursor()


cur.execute(LOGstatement)
listdictmltlogs = cur.fetchall()
print "MLT LOG Total count = %s " % (len(listdictmltlogs))

if len(listdictmltlogs) == 0 :
    print "LOG Total count = 0, exit "
    exit()


conn.close()



table_exception_blobs = 't320'
''' define some utility '''
def check_table_exception_blobs ( conn ):
    query = "SELECT name FROM sqlite_master WHERE type='table'"
    listTable = list( conn.execute(query))
    if (table_exception_blobs, ) in listTable :
        return True
    else:
        return False

from pysqlite2 import dbapi2 as sqlite3

table_AppAccum_info = "t305"
f00n_AppAccum_info = "f003, f004, f005"     # packagename, total_time_ms, total_run_count

countDB = 0
def getAppAccumation ( dicttupleappaccum ):
    global countDB
    dblist = glob.glob('*.db')

    for dbfilename in dblist:
        print "Extracting DB : " + dbfilename

        ''' rename the DB file name to 'temp.db' because theat sqlite3 can't handle the hangul file name . '''
        tempdbname = '___processing.db'
        shutil.move(dbfilename, tempdbname )
        conn = sqlite3.connect(tempdbname)
        ''' check if t320 table is exist, if then, keep processing.  '''
        if check_table_exception_blobs(conn) == False:
            conn.close()
            print "No Exception Blobs, DB skip"
            shutil.move( tempdbname, dbfilename )
            continue
        countDB += 1
        # print "_____ Reading DBFiles : ", str(countDB)
        cur = conn.cursor()

        query_app_accum = "select %s from %s" % (f00n_AppAccum_info,table_AppAccum_info  )
        cur.execute(query_app_accum)
        listtupleAppAccum = cur.fetchall()

        for tupleAppAccum in listtupleAppAccum :
            packagename, total_time_ms, total_run_count = tupleAppAccum
            sum_app_count, sum_total_time , sum_total_run_count  = dicttupleappaccum.get( packagename, (0,0,0))
            sum_app_count += 1
            sum_total_time += total_time_ms / 1000
            sum_total_run_count += total_run_count
            dicttupleappaccum[ packagename ] = (sum_app_count, sum_total_time, sum_total_run_count)

        conn.close()
        shutil.move( tempdbname, dbfilename )




''' MLT LOG field name '''
# fieldnames = ['log_no',  'model_name',   'esn_imei_no',  'serial_no',  'os_version', 'sw_version',  'hw_version',  'base_ymd',  'cust_symptom_cd',   'country_cd',  'log_file_path',  'log_file_name',   'svc_cd',    'rooting_count', 'input_imei_no',  'buyer_cd',   'buyer_model_name',     'update_count',   'phone_type',    'registration',   'process_ymd'  ]
fieldnames = ['model_name', 'base_ymd', 'log_file_name', 'log_file_path','country_cd','description','creation_dt','esn_imei_no','moa_type','buyer_cd','last_update_dt','log_no','cust_symptom_cd' ]



''' ---------order the SVC data by IMEI -------- '''
def IMEICmp ( a1, a2 ) :
    return cmp ( a1["esn_imei_no"], a2["esn_imei_no"] )


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
            continue
    else:
        listdictmltlogsTemp.append(dictmltlogs)
        dictmltlogsPre = dictmltlogs

## restore
listdictmltlogs = listdictmltlogsTemp

print "MLT LOG Total count after sorting  = %s " % (len(listdictmltlogs))



''' ========================= MLT App Accumulation ======================================='''
''' Build the summary of Application Acculation  '''

ClearMLTLOG()

logcount = len(listdictmltlogs)
strProcessing =  "**** The remaining count of MLTLOG (%s) : "  % ( logcount )

# dictlistAppAccumInfo = { "com.lge.camera": [total_time_ms, total_run_count, total_app_count], "com.android.settings": [total_time_ms, total_run_count, total_app_count] }
dicttupleAppAccumInfo = {}


for dictmltlogs in listdictmltlogs:
    print strProcessing, logcount
    ''' copy the log file to current directory. '''
    CopyMLTLOG( dictmltlogs["log_file_path"] + "\\" + dictmltlogs["log_file_name"])

    ''' process the gathered log file at current dir '''
    getAppAccumation(dicttupleAppAccumInfo)
    # print "____ the length of dicttupleAppAccumInfo : " , str(len(dicttupleAppAccumInfo))
    ''' delete the processed log file '''
    DeleteMLTLOG()
    logcount = logcount - 1



''' create the excel file and save the   dicttupleAppAccumInfo '''

from xlsxcessive.xlsx import Workbook
from xlsxcessive.xlsx import save

wb = Workbook()
ws = wb.new_sheet(period) # insert at the end (default)

rindex = 0
cindex = 0

fieldnames = [ "packagename", "total_app_count", "total_run_time(s)", "total_run_count", "avg_time(s)" ]

''' first, insert field name to row0 '''
for fieldname in fieldnames :
    ws.cell(coords=(rindex, cindex,  ),  value = fieldname )
    ws.col(index=cindex, width=50)
    cindex += 1

rindex = 1
cindex = 0

listkeys = dicttupleAppAccumInfo.keys()
import GetAppList 
for packagename in listkeys :
    total_app_count, sum_total_time , sum_total_run_count = dicttupleAppAccumInfo[ packagename ]
    AppName = GetAppList.dictPackageToAppName.get( packagename, packagename)
    ws.cell(coords=(rindex, cindex,  ),  value = AppName )
    cindex += 1
    ws.cell(coords=(rindex, cindex,  ),  value = total_app_count )
    cindex += 1
    ws.cell(coords=(rindex, cindex,  ),  value = sum_total_time )
    cindex += 1
    ws.cell(coords=(rindex, cindex,  ),  value = sum_total_run_count )
    cindex += 1
    if sum_total_run_count != 0 :
        ws.cell(coords=(rindex, cindex,  ),  value = sum_total_time/sum_total_run_count )
    else :
        ws.cell(coords=(rindex, cindex,  ),  value = 0 )
    rindex += 1
    cindex = 0
    print ".",

print "."

''' save the  AppAccum'''
if SavingHeadName == "" :
    excelExceptPath = excelsavingname + "_" + "AppAccum" + "_" +  period + ".xlsx"
else:
    excelExceptPath =  SavingHeadName + "_" + "AppAccum" + "_" +  period + ".xlsx"

print "Saving ressult to Excel file : ", excelExceptPath
save(wb,  excelExceptPath )
print "Saved...."


''' ====================================================================================='''

if LogFileCopy == False :
    print "Process End ....."
    endtime =  datetime.now()
    print endtime
    print " elasped time is : ", endtime - starttime
    Jobfinished()


''' copy the MLT LOG file from temp dir to current dir . '''

tempdir = diroutput + "\\" + strTempDir
listlog = glob.glob(tempdir + "\\" + '*.db')

''' move MLT LOG to temp dir '''
for log in listlog:
    shutil.move(log, "." )

''' remove the temp dir . '''
shutil.rmtree( strTempDir, True)


endtime =  datetime.now()
print endtime
print " elasped time is : ", endtime - starttime

print "Proces End ....."

Jobfinished()












