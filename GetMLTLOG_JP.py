# _*_ coding: utf-8 _*_

'''
Created on 2012. 7. 6.

@author: jaehyek
'''

import os , argparse
import AnalyzerMLTLOG
import GetMLTSymptomInfo
from datetime import datetime
import shutil


'''
c:> python GetMLTLOG.py -o c:\temp_mlt -m "LGF160L LGF160S LGF160K" -p 20120511-20120705 -d Z -l -s
'''


# variables.
diroutput = "."
modelname = ""
period = ""
FileDrv = "Z"
LogFileCopy = False
ShutdownAfter = False

if __name__ == '__main__':
    pass

starttime =  datetime.now()
print starttime



cmdlineopt = argparse.ArgumentParser(description='get the MLT LOG from MLT Server 10.185.135.57')
cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='output directory to put MLT log file. default = . sample: c:\\temp_mlt' )
cmdlineopt.add_argument('-m', action="store", dest="modelname", default='',  help=' Model name. example: F100S  ' )
cmdlineopt.add_argument('-p', action="store", dest="period", default='',  help=' period . example : 20120601-20120630  ' )
cmdlineopt.add_argument('-d', action="store", dest="FileDrv", default='Z',  help=' Windows File Driver Character of server MLT_LOG directory to be maapped to windows system . example : Z ' )
cmdlineopt.add_argument('-l', action="store_true", dest="LogFileCopy",  default=False, help='copy MLT Log db file to output directory default= Faluse' )
cmdlineopt.add_argument('-s', action="store_true", dest="ShutdownAfter",  default=False, help='shutdown system after job finished,  default= Faluse' )


cmdlineresults = cmdlineopt.parse_args()

diroutput = cmdlineresults.diroutput
modelname = cmdlineresults.modelname
period = cmdlineresults.period
FileDrv = cmdlineresults.FileDrv
LogFileCopy = cmdlineresults.LogFileCopy
ShutdownAfter = cmdlineresults.ShutdownAfter





''' variable initialization for test of F100L '''
period = "20120601-20120912"
diroutput = "D:\\temp_MLT_F100"
modelname = "L05D"
LogFileCopy = True

''' variable initialization for test of F100S'''
##period = "20120705-20120815"
##diroutput = "D:\\temp_MLT_F100"
##modelname = "LGF100S"


'''
. IP :\\10.185.135.57\mlt_log_guest
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




def CopyMLTLOG ( logfullpath ) :
    filesrc = logfullpath.replace("MLT_LOG\\", "")
    filesrc = FileDrv + filesrc[1:]
    print "Copying log file from : ", filesrc
    shutil.copy(filesrc, '.')




ServiceStatement = "select * from  dmr_service_history  where ( %s )  and  receipt_ymd between '%s' and '%s'   "
ServiceStatement = ServiceStatement % ( modelstatementSVC,  startdate, enddate )
print "ServiceStatement = " , ServiceStatement

##LOGstatement = "select * from dmr_basic_info a join  dmr_service_history b on a.esn_imei_no = b.esn_imei_no where ( %s ) and ( %s ) and b.close_dt_rtn_dt >= a.base_ymd  and  a.base_ymd between '%s' and '%s' and a.esn_imei_no IS NOT NULL  "
LOGstatement = '''
select  *
from    dmr_basic_info
where   1=1
and ( %s)
and     esn_imei_no in (    select esn_imei_no
                            from    dmr_service_history
                            where   1=1
                            and ( %s )
							and receipt_ymd between '%s' and '%s'
                            group by esn_imei_no
                        )
'''

LOGstatement = LOGstatement % ( modelstatementSVC,modelstatementSVC,  startdate, enddate )

print "LOGstatement = ",  LOGstatement




import pymssql
conn = pymssql.connect(host='10.185.135.57', user='MLT_INF', password='inf_P@ssword', database='LGMLTP', charset="UTF-8" , as_dict=True)
cur = conn.cursor()




GetMLTSymptomInfo.initializeMLTSymptomInfo(cur)

cur.execute(ServiceStatement)
listdictSVClogs = cur.fetchall()
print "MLT SVC Total count = %s " % (len(listdictSVClogs))

if len(listdictSVClogs) == 0 :
    print "SVC Total count = 0, exit "
    exit()



cur.execute(LOGstatement)
listdictmltlogs = cur.fetchall()
print "MLT LOG Total count = %s " % (len(listdictmltlogs))

if len(listdictmltlogs) == 0 :
    print "LOG Total count = 0, exit "
    exit()


conn.close()



''' open the xls file '''
from xlsxcessive.xlsx import Workbook
from xlsxcessive.xlsx import save

''' MLT SVC field name '''
SVCfieldnames = ['serial_no','interface_ymd','creation_id','section_cd','receipt_ymd','symptom_cd','defect_type','receipt_no','purc_date','data_type','source_system','creation_dt','cause_cd','esn_imei_no','repair_cd','close_dt_rtn_dt','last_update_dt','symptom_org_cd','corp_cd','last_update_id','model_name','unique_id']


''' MLT LOG field name '''
##fieldnames = ['log_no',  'model_name',   'esn_imei_no',  'serial_no',  'os_version', 'sw_version',  'hw_version',  'base_ymd',  'cust_symptom_cd',  'symptom_cd',  'cause_cd',   'symptom_org_cd' ,  'close_dt_rtn_dt',   'section_cd',   'moa_type', 'country_cd',  'log_file_path',  'log_file_name',  'mapp_sw_version' , 'svc_cd',  'receipt_no',  'rooting_count', 'input_imei_no',  'buyer_cd',  'corp_cd',   'buyer_model_name',  'interface_ymd',  'receipt_ymd',  'defect_type',  'purc_date',  'data_type',   'defect_id',  'update_count',  'repair_cd',  'phone_type',    'registration',   'process_ymd'  ]
##fieldnames = ['log_no',  'model_name',   'esn_imei_no',  'serial_no',  'os_version', 'sw_version',  'hw_version',  'base_ymd',  'cust_symptom_cd',   'cause_cd',   'close_dt_rtn_dt',   'section_cd',   'moa_type', 'country_cd',  'log_file_path',  'log_file_name',  'mapp_sw_version' , 'svc_cd',  'receipt_no',  'rooting_count', 'input_imei_no',  'buyer_cd',  'corp_cd',   'buyer_model_name',  'interface_ymd',  'receipt_ymd',  'defect_type',  'purc_date',  'data_type',   'defect_id',  'update_count',  'repair_cd',  'phone_type',    'registration',   'process_ymd'  ]
fieldnames = ['log_no',  'model_name',   'esn_imei_no',  'serial_no',  'os_version', 'sw_version',  'hw_version',  'base_ymd',  'cust_symptom_cd',   'country_cd',  'log_file_path',  'log_file_name',   'svc_cd',    'rooting_count', 'input_imei_no',  'buyer_cd',   'buyer_model_name',     'update_count',   'phone_type',    'registration',   'process_ymd'  ]


''' ---------order the SVC data by IMEI -------- '''
def IMEICmp ( a1, a2 ) :
    return cmp ( a1["esn_imei_no"], a2["esn_imei_no"] )



''' ---------delete the duplicated IMEI ITEM  for listdictSVClogs -------- '''
listdictSVClogs.sort(IMEICmp)

listdictSVClogsTemp = []
dictSVClogsPre = {}
dictSVClogsPre["esn_imei_no"] = ""
for dictSVClogs in listdictSVClogs :
    if dictSVClogs["esn_imei_no"] == dictSVClogsPre["esn_imei_no"] :
        continue
    else :
        listdictSVClogsTemp.append(dictSVClogs)
        dictSVClogsPre =dictSVClogs
## restore
listdictSVClogs = listdictSVClogsTemp

print "MLT SVC Total count after sorting  = %s " % (len(listdictSVClogs))

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


''' -------- order the mlt log by cust_symptom_cd -------------- '''
def symptomcmp( a1, a2 ):
    return cmp ( a1["cust_symptom_cd"], a2["cust_symptom_cd"] )

listdictmltlogs.sort(symptomcmp)




''' +++++++++++++++++++++++++ SVC +++++++++++++++++++++++++++++++++++ '''
''' Build the summary of model of the SVC  '''
wb = Workbook()
ws = wb.new_sheet(period) # insert at the end (default)

rindex = 0
cindex = 0


''' first, insert field name to row0 '''
for fieldname in SVCfieldnames :
    ws.cell(coords=(rindex, cindex,  ),  value = fieldname )
    cindex += 1

''' print SVC info  to excel file '''
rindex = 1
cindex = 0



for dictSVClogs in listdictSVClogs:
    for fieldname in SVCfieldnames :
        if fieldname == 'symptom_cd' :
            ws.cell(coords=(rindex, cindex,  ),  value = GetMLTSymptomInfo.mapSymptomCodeToName(dictSVClogs[fieldname]) )
        else:
            ws.cell(coords=(rindex, cindex,  ),  value = dictSVClogs[fieldname] )

        cindex += 1

    rindex += 1
    cindex = 0
    print  ".",

print " "
curdir = os.path.abspath(os.curdir)
excelsummary = excelsavingname + "_" + "SVCsummary" + "_" +  period + ".xlsx"
print "Excel Saving : " + curdir + "\\" +  excelsummary

save(wb,  excelsummary )

wb = 0



''' ========================= MLT LOG ======================================='''
''' Build the summary of model of the MLT  '''

wb = Workbook()
ws = wb.new_sheet(period) # insert at the end (default)

rindex = 0
cindex = 0

''' first, insert field name to row0 '''
for fieldname in fieldnames :
    ws.cell(coords=(rindex, cindex,  ),  value = fieldname )
    cindex += 1


''' print mltinfos to excel file '''
rindex = 1
cindex = 0

mltpath =""
mltfile = ""
listmltpathfile = []

for dictmltlogs in listdictmltlogs:
    for fieldname in fieldnames :
        if fieldname == 'cust_symptom_cd' :
            ws.cell(coords=(rindex, cindex,  ),  value = GetMLTSymptomInfo.mapSymptomCodeToName(dictmltlogs[fieldname]) )
        else:
            ws.cell(coords=(rindex, cindex,  ),  value = dictmltlogs[fieldname] )
        if( fieldname == 'log_file_name'):
            mltfile = dictmltlogs[fieldname]
        if( fieldname == 'log_file_path'):
            mltpath = dictmltlogs[fieldname]
        cindex += 1

    listmltpathfile.append(mltpath + "\\" + mltfile )
    rindex += 1
    cindex = 0
    print  ".",

print " "
curdir = os.path.abspath(os.curdir)
excelsummary = excelsavingname + "_" + "LOGsummary" + "_" +  period + ".xlsx"
print "Excel Saving : " + curdir + "\\" +  excelsummary
from xlsxcessive.xlsx import save
save(wb,  excelsummary )



''' ====================================================================================='''
''' Build the Exception Path Excel of Models
The list of MLTLOG is sorted by cust_symptom_cd, also can process the bunch of log of the same symptom code.
Of cause, each of log can be processed.

'''

previousSymptomCode = listdictmltlogs[0]["cust_symptom_cd"]
dictpreviousAdditionalBaicInfo = {}
dictpreviousAdditionalBaicInfo["cust_symptom_cd"] = GetMLTSymptomInfo.mapSymptomCodeToName( previousSymptomCode )
for dictmltlogs in listdictmltlogs:
    if previousSymptomCode == dictmltlogs["cust_symptom_cd"]:
        ''' copy the log file to current directory. '''
        CopyMLTLOG( dictmltlogs["log_file_path"] + "\\" + dictmltlogs["log_file_name"])
    else:
        ''' process the gathered log file at current dir '''
        AnalyzerMLTLOG.setWorkingDir(".")
        AnalyzerMLTLOG.doProcessing()
        AnalyzerMLTLOG.writeResultToExcel( dictpreviousAdditionalBaicInfo )
        ''' delete the processed log file '''
        DeleteMLTLOG()
        ''' update the SymptomCode '''
        previousSymptomCode = dictmltlogs["cust_symptom_cd"]
        dictpreviousAdditionalBaicInfo = {}
        dictpreviousAdditionalBaicInfo["cust_symptom_cd"] = GetMLTSymptomInfo.mapSymptomCodeToName( previousSymptomCode )
        ''' copy the log file to current directory. '''
        CopyMLTLOG( dictmltlogs["log_file_path"] + "\\" + dictmltlogs["log_file_name"])

''' process the last gathered log file at current dir '''
AnalyzerMLTLOG.setWorkingDir(".")
AnalyzerMLTLOG.doProcessing()
AnalyzerMLTLOG.writeResultToExcel( dictpreviousAdditionalBaicInfo )
DeleteMLTLOG()

''' save the  ExceptPath'''
excelExceptPath = excelsavingname + "_" + "ExceptPath" + "_" +  period + ".xlsx"
print "Saving ressult to Excel file : ", excelExceptPath
AnalyzerMLTLOG.closeExcel(excelExceptPath)
print "Saved...."




''' ====================================================================================='''

if LogFileCopy == False :
    print "Process End ....."
    endtime =  datetime.now()
    print endtime
    print " elasped time is : ", endtime - starttime
    Jobfinished()


''' ====================================================================================='''
''' MLT LOG File copy '''

'''
  : from F:\MLT_LOG\20120628\MLT_DB_3524540504182150_LG-F160S_20120628_114855763_(490646).db
               in form of Z:\20120628\MLT_DB_3524540504182150_LG-F160S_20120628_114855763_(490646).db
               that is ,   remove the "MLT_LOG|

copycount = len (listmltpathfile )

print "Copying log files to local dir ................."
for filefullname in listmltpathfile :
    CopyMLTLOG( filefullname )
    print copycount, " copying file from " + filefullname
    copycount -= 1


'''

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












