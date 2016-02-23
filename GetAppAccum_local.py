# _*_ coding: utf-8 _*_

'''
Created on 2012. 10. 30.
@author: jaehyek
'''

import os , argparse
from datetime import datetime
import shutil


'''
c:> python GetAppAccum.py -o c:\temp_mlt -m "LGF160L LGF160S LGF160K" -s
'''


# variables.
diroutput = "."
modelname = ""
ShutdownAfter = False


if __name__ == '__main__':
    pass

starttime =  datetime.now()
print starttime



cmdlineopt = argparse.ArgumentParser(description='get the MLT LOG from MLT Server 10.185.135.57')
cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='output directory to put MLT log file. default = . sample: c:\\temp_mlt' )
cmdlineopt.add_argument('-m', action="store", dest="modelname", default='',  help=' Model name. example: F100S  ' )
cmdlineopt.add_argument('-s', action="store_true", dest="ShutdownAfter",  default=False, help='shutdown system after job finished,  default= Faluse' )

cmdlineresults = cmdlineopt.parse_args()

diroutput = cmdlineresults.diroutput
modelname = cmdlineresults.modelname
ShutdownAfter = cmdlineresults.ShutdownAfter



# ==================================================================================
''' variable initialization for test of F100L '''
diroutput = "D:\\temp_F240L_DOA\\mltlogs"
modelname = "F220K"
ShutdownAfter = False
# ==================================================================================


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

import glob

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
f00n_AppAccum_info = "f003, f004, f005"     # packagename, total_time_ms, total_count 

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
        print "_____ Reading DBFiles : ", str(countDB)
        cur = conn.cursor()
        
        query_app_accum = "select %s from %s" % (f00n_AppAccum_info,table_AppAccum_info  )
        cur.execute(query_app_accum)
        listtupleAppAccum = cur.fetchall()
        
        for tupleAppAccum in listtupleAppAccum :
            packagename, total_time_ms, total_count = tupleAppAccum
            sum_total_time , sum_total_count  = dicttupleappaccum.get( packagename, (0,0))
            sum_total_time += total_time_ms / 1000
            sum_total_count += total_count
            dicttupleappaccum[ packagename ] = (sum_total_time, sum_total_count)
        
        conn.close()
        shutil.move( tempdbname, dbfilename )
        
        


''' MLT LOG field name '''
fieldnames = ['log_no',  'model_name',   'esn_imei_no',  'serial_no',  'os_version', 'sw_version',  'hw_version',  'base_ymd',  'cust_symptom_cd',   'country_cd',  'log_file_path',  'log_file_name',   'svc_cd',    'rooting_count', 'input_imei_no',  'buyer_cd',   'buyer_model_name',     'update_count',   'phone_type',    'registration',   'process_ymd'  ]






''' ========================= MLT App Accumulation ======================================='''
''' Build the summary of Application Acculation  '''



dicttupleAppAccumInfo = {}


    
getAppAccumation(dicttupleAppAccumInfo)

''' create the excel file and save the   dicttupleAppAccumInfo '''

from xlsxcessive.xlsx import Workbook
from xlsxcessive.xlsx import save

wb = Workbook()
ws = wb.new_sheet("AppAccum") # insert at the end (default)

rindex = 0
cindex = 0

fieldnames = [ "packagename", "total_time(s)", "total_count", "avg_time(s)" ]
  
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
    sum_total_time , sum_total_count = dicttupleAppAccumInfo[ packagename ] 
    AppName = GetAppList.dictPackageToAppName.get( packagename, packagename)
    ws.cell(coords=(rindex, cindex,  ),  value = AppName )
    cindex += 1
    ws.cell(coords=(rindex, cindex,  ),  value = sum_total_time )
    cindex += 1
    ws.cell(coords=(rindex, cindex,  ),  value = sum_total_count )
    cindex += 1
    if sum_total_count != 0 :
        ws.cell(coords=(rindex, cindex,  ),  value = sum_total_time/sum_total_count )
    else :
        ws.cell(coords=(rindex, cindex,  ),  value = 0 )
    rindex += 1 
    cindex = 0 
    print ".",
    
print "."    
    
''' save the  AppAccum'''

excelExceptPath = "AppAccum" + "_" +  modelname + ".xlsx"
print "Saving ressult to Excel file : ", excelExceptPath
save(wb,  excelExceptPath )
print "Saved...."


''' ====================================================================================='''




endtime =  datetime.now()
print endtime
print " elasped time is : ", endtime - starttime

print "Proces End ....."

Jobfinished()












