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
c:> python GetMLTLOG3.py -o c:\temp_mlt -m "LGF160L LGF160S LGF160K" -p 20120511-20120705 -d Z -l -s
'''


# variables.
diroutput = "."
modelname = ""
period = ""
FileDrv = "Z"
ShutdownAfter = False
boolDBCopy = False
boolSymptomPartial = False
boolDBDump = False
boolAnalyzer = False
boolCallDump = False
FileNameHeader = "MLT"

if __name__ == '__main__':
    pass

starttime =  datetime.now()
print starttime



cmdlineopt = argparse.ArgumentParser(description='get the MLT LOG from MLT Server 10.185.135.57')
cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='output directory to put MLT log file. default = . sample: c:\\temp_mlt' )
cmdlineopt.add_argument('-m', action="store", dest="modelname", default='',  help=' Model name. example: F100S  ' )
cmdlineopt.add_argument('-p', action="store", dest="period", default='',  help=' period . example : 20120601-20120630  ' )
cmdlineopt.add_argument('-d', action="store", dest="FileDrv", default='Z',  help=' Windows File Driver Character of server MLT_LOG directory to be maapped to windows system . example : Z ' )
cmdlineopt.add_argument('-fh', action="store", dest="FileNameHeader", default='MLT',  help=' indicate the file name header of output  . example : MLT ' )
cmdlineopt.add_argument('-s', action="store_true", dest="ShutdownAfter",  default=False, help='shutdown system after job finished,  default= Faluse' )
cmdlineopt.add_argument('-aExpt', action="store_true", dest="boolAnalyzer",  default=False, help='Analyzer DB ,  default= Faluse' )
cmdlineopt.add_argument('-aCall', action="store_true", dest="boolCallDump",  default=False, help='Dump the Call history during analyzer DB ,  default= Faluse' )
cmdlineopt.add_argument('-sp', action="store_true", dest="boolSymptomPartial",  default=False, help='Process DB according to the wanted symptom code table,  default= Faluse' )
cmdlineopt.add_argument('-DBCopy', action="store_true", dest="boolDBCopy",  default=False, help='Copy DB after analyzing,  default= Faluse' )
cmdlineopt.add_argument('-DBDump', action="store_true", dest="boolDBDump",  default=False, help='dump the DB into excel file for data viewer,  default= Faluse' )


cmdlineresults = cmdlineopt.parse_args()

diroutput = cmdlineresults.diroutput
modelname = cmdlineresults.modelname
period = cmdlineresults.period
FileDrv = cmdlineresults.FileDrv
ShutdownAfter = cmdlineresults.ShutdownAfter
boolDBCopy = cmdlineresults.boolDBCopy
boolDBDump = cmdlineresults.boolDBDump
boolSymptomPartial = cmdlineresults.boolSymptomPartial
boolAnalyzer = cmdlineresults.boolAnalyzer
boolCallDump = cmdlineresults.boolCallDump
FileNameHeader = cmdlineresults.FileNameHeader

exit()

''' variable initialization for test of F100L '''
# period = "20121001-20121104"
# diroutput = "D:\\temp_MLT_F200"
# modelname = "LGF200L LGF200S LGF200K"
# FileDrv = "Z"
# boolDBCopy = True
# ShutdownAfter = True
#boolDBDump = True


# period = "20121021-20121031"
# diroutput = "D:\\temp_MLT_F180"
# modelname = "LGF180L LGF180S LGF180K"
# FileDrv = "Z"
# boolDBCopy = True
# ShutdownAfter = True
#boolDBDump = True

''' variable initialization for test of F100S'''
# period = "20120316-20130316"
# diroutput = "D:\\temp_MLT_F240_lockup"
# modelname = "LGF240S LGF240K LGF240L"
# boolDBCopy = False
# boolSymptomPartial = True 
# boolDBDump = False 
# boolAnalyzer = True
'''
. IP :\\10.185.135.57\mlt_log_guest
. ID : mlt_inf01
.  Password  inf_P@ssword
. 
. 10.185.135.57 : 가공을 하기 위해 준비된 server
. 10.185.135.115 : 가공을 하기 전의 data을 모아 두기 위한 server 
                   해당 table 들은 ODS의 확장자가 붙어 있다. 
                   log file 들도 여기에 있다.
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


modelstatementSVC = ""

for model in modellist :
    modelstatementSVC += "ss.model_name = " + "'" +  model + "' "
    modelcount -= 1
    if ( modelcount > 0 ) :
        modelstatementSVC += " or "


''' extract the period to startdate and enddate. '''
startdate =  period.split("-")[0]
enddate = period.split("-")[1]

strTempDir = "temp"


import pymssql
conn = pymssql.connect(host='10.185.135.57', user='MLT_INF', password='inf_P@ssword', database='LGMLTP', charset="UTF-8" , as_dict=True)
cur = conn.cursor()

## MDA : S/W(소프트웨어)
## MBE : 정상(Tesk OK/재현불)
        
ServiceStatement = ''' select ss.*, cc.cause_desc, yy.symptom_desc 
from  dwt_service_h ss , dwt_cause_m cc, dwt_symptom_m yy   where 
( %s )   and  
( ss.cause_cd = 'MDA' or ss.cause_cd = 'MBE'  ) and  
ss.cause_cd = cc.cause_cd and 
ss.symptom_cd = yy.symptom_cd and 
ss.receipt_ymd between '%s' and '%s'  '''


ServiceStatement = ServiceStatement % ( modelstatementSVC,  startdate, enddate )
print "ServiceStatement = " , ServiceStatement


cur.execute(ServiceStatement)
listdictSVCHist = cur.fetchall()
print "MLT SVC Total count = %s " % (len(listdictSVCHist))

if len(listdictSVCHist) == 0 :
    print "SVC History count = 0, exit "
    exit()


print " "



LOGStatement = '''
select  *
from    dmr_basic_info
where   1=1
and ( %s)
and     esn_imei_no in (    select esn_imei_no
                            from    dmr_service_history
                            where   1=1
                            and ( %s )
                            and   (  cause_cd = 'MDA' or cause_cd = 'MBE'  )
                            and base_ymd between '%s' and '%s'
                            group by esn_imei_no
                        )
'''

LOGStatement = ''' select ss.*, cc.cause_desc, yy.symptom_desc 
from  dmd_log_m ss , dwt_cause_m cc, dwt_symptom_m yy  where 
( %s )   and  
( ss.cause_cd = 'MDA' or ss.cause_cd = 'MBE'  ) and  
ss.cause_cd = cc.cause_cd and 
ss.symptom_cd = yy.symptom_cd and 
ss.base_ymd between '%s' and '%s'  '''


LOGStatement = LOGStatement % ( modelstatementSVC,  startdate, enddate )
print "LOGStatement = " , LOGStatement


cur.execute(LOGStatement)
listdictmltlogs = cur.fetchall()
print "MLT LOG Total count = %s " % (len(listdictmltlogs))

if len(listdictmltlogs) == 0 :
    print "LOG Total count = 0, exit "
    exit()


if boolSymptomPartial == True :  
    import GetMLTLOG3_FilterSympton
    filterstatement = " and ( "
    for dictFilteringSympton in GetMLTLOG3_FilterSympton.listdictFilteringSympton : 
        if dictFilteringSympton["Filtering_YN"] == "Y":
            filterstatement += " ss.symptom_cd = '" + dictFilteringSympton["symptom_cd"] + "' or "
        PartialLOGStatement = LOGStatement + filterstatement + " 1 != 1 ) "
    print " "
    print PartialLOGStatement
    cur.execute(PartialLOGStatement)
    listdictpartialmltlogs = cur.fetchall()
    print "Partial MLT LOG Total count = %s " % (len(listdictpartialmltlogs))
    
conn.close()
print " "


''' ---------order the SVC data by IMEI -------- '''
def IMEICmp ( a1, a2 ) :
    return cmp ( a1["esn_imei_no"], a2["esn_imei_no"] )



''' ---------replace  IMEI with log_file_name if IMEI == ""  for listdictSVCHist -------- '''
for dictSVClogs in listdictSVCHist :
    if dictSVClogs["esn_imei_no"] == "" or dictSVClogs["esn_imei_no"] == None :
        dictSVClogs["esn_imei_no"] = dictSVClogs["model_name"] + dictSVClogs["prod_serial_no"]

''' ---------delete the duplicated IMEI ITEM  for listdictSVCHist -------- '''
listdictSVCHist.sort(IMEICmp)

listdictSVCHistTemp = []
dictSVClogsPre = {}
dictSVClogsPre["esn_imei_no"] = ""
for dictSVClogs in listdictSVCHist :
    if dictSVClogs["esn_imei_no"] == dictSVClogsPre["esn_imei_no"] :
        continue
    else :
        listdictSVCHistTemp.append(dictSVClogs)
        dictSVClogsPre =dictSVClogs
## restore
listdictSVCHist = listdictSVCHistTemp

print "MLT SVC Total count after sorting  = %s " % (len(listdictSVCHist))



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
            print "esn_imei_no" , dictSVClogs["esn_imei_no"]
            continue
    else:
        listdictmltlogsTemp.append(dictmltlogs)
        dictmltlogsPre = dictmltlogs

##restore
listdictmltlogs = listdictmltlogsTemp

print "MLT LOG Total count after sorting  = %s " % (len(listdictmltlogs))


''' -------- order the mlt log by symptom_cd -------------- '''
def symptomcmp( a1, a2 ):
    return cmp ( a1["symptom_cd"], a2["symptom_cd"] )

listdictmltlogs.sort(symptomcmp)





''' open the xls file '''
from xlsxcessive.xlsx import Workbook
from xlsxcessive.xlsx import save


    
''' MLT SVC field name '''
SVCHistfieldnames = [
'model_name',
'receipt_ymd',
'receipt_ymweek',
'outgo_sw_version',
'symptom_desc',
'product_ymd',
'affiliate_short_name',
'cause_desc',
'warranty_type',
'esn_imei_no' ]




''' +++++++++++++++++++++++++ SVC +++++++++++++++++++++++++++++++++++ '''
''' Build the summary of model of the SVC  '''
wb = Workbook()
ws = wb.new_sheet("SVC_" +  period) # insert at the end (default)

rindex = 0
cindex = 0


''' first, insert field name to row0 '''
for fieldname in SVCHistfieldnames :
    ws.cell(coords=(rindex, cindex,  ),  value = fieldname )
    cindex += 1

''' print SVC info  to excel file '''
rindex = 1
cindex = 0



for dictSVClogs in listdictSVCHist:
    for fieldname in SVCHistfieldnames :
        if  fieldname == "receipt_ymweek" :
            strymd = dictSVClogs["receipt_ymd"].encode("utf-8")
            strday = strymd[-2:]
            intday = int(strday)
            if intday <= 7 :
                strh = strymd[:-2] + "w1"
            elif intday <= 14 :
                strh = strymd[:-2] + "w2"
            elif intday <= 21 :
                strh = strymd[:-2] + "w3"
            else :
                strh = strymd[:-2] + "w4"

            ws.cell(coords=(rindex, cindex,  ),  value = strh )
        else:
            ws.cell(coords=(rindex, cindex,  ),  value = dictSVClogs[fieldname] )

        cindex += 1

    rindex += 1
    cindex = 0
    print  ".",

print " "
curdir = os.path.abspath(os.curdir)
excelsummary = FileNameHeader + "_" + "SVCsummary" + "_" +  period + ".xlsx"

print "Excel Saving : " + curdir + "\\" +  excelsummary

save(wb,  excelsummary )

wb = 0

''' MLT LOG field name '''
LOGHistfieldnames = [
'model_name',
'base_ymd',
'receipt_ymweek',
'outgo_sw_version',
'outgo_hw_version',
'svc_sw_version',
'svc_hw_version',
'symptom_desc',
'cause_desc',
'esn_imei_no',
'log_file_name', 
'log_file_path']

''' ========================= MLT LOG ======================================='''
''' Build the summary of model of the MLT  '''

wb = Workbook()
ws = wb.new_sheet(period) # insert at the end (default)

rindex = 0
cindex = 0

''' first, insert field name to row0 '''
for fieldname in LOGHistfieldnames :
    ws.cell(coords=(rindex, cindex,  ),  value = fieldname )
    cindex += 1


''' print mltinfos to excel file '''
rindex = 1
cindex = 0

mltpath =""
mltfile = ""
listmltpathfile = []

for dictmltlogs in listdictmltlogs:
    for fieldname in LOGHistfieldnames :
        if  fieldname == "receipt_ymweek" :
            strymd = dictmltlogs["base_ymd"].encode("utf-8")
            strday = strymd[-2:]
            intday = int(strday)
            if intday <= 7 :
                strh = strymd[:-2] + "w1"
            elif intday <= 14 :
                strh = strymd[:-2] + "w2"
            elif intday <= 21 :
                strh = strymd[:-2] + "w3"
            else :
                strh = strymd[:-2] + "w4"

            dictmltlogs["receipt_ymweek"] = strh

            ws.cell(coords=(rindex, cindex,  ),  value = strh )
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
excelsummary = FileNameHeader + "_" + "LOGsummary" + "_" +  period + ".xlsx"

print "Excel Saving : " + curdir + "\\" +  excelsummary
from xlsxcessive.xlsx import save
save(wb,  excelsummary )


if boolDBCopy == False  and boolAnalyzer == False and boolCallDump == False :
    print "Process End ....."
    endtime =  datetime.now()
    print endtime
    print " elasped time is : ", endtime - starttime
    Jobfinished()



''' ====================================================================================='''
''' Build the Exception Path Excel of Models
The list of MLTLOG is sorted by cust_symptom_cd, also can process the bunch of log of the same symptom code.
Of cause, each of log can be processed.

'''


import glob
import shutil


def ClearMLTLOG():
    listlog = glob.glob('*.db')
    for log in listlog:
        os.remove( log )


def DeleteMLTLOG():
    listlog = glob.glob('*.db')
    if boolDBCopy == False :
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



        



ClearMLTLOG()

if boolDBDump == True :
    import MltDBDump
    
if boolSymptomPartial == True : 
    listdictmltlogs = listdictpartialmltlogs
    print "__________________________________________________________________ "
    print "==== replace listdictmltlogs with listdictpartialmltlogs ========= "

logcount = len(listdictmltlogs)
strProcessing =  "**** The remaining count of MLTLOG (%s) : "  % ( logcount )

for dictmltlogs in listdictmltlogs:
    print " "
    print strProcessing, logcount
    # if logcount > 117 :
        # print dictmltlogs["log_file_name"]
        # logcount = logcount - 1
        # continue
    dictAdditionalBaicInfo = {}
    dictAdditionalBaicInfo["symptom_desc"] = dictmltlogs["symptom_desc"]
    dictAdditionalBaicInfo["base_ymd"] = dictmltlogs["base_ymd"]

    CopyMLTLOG( os.path.join(dictmltlogs["log_file_path"] , dictmltlogs["log_file_name"]))
    
    if boolDBDump == True :
            MltDBDump.doDumping(".", "" )

    if boolAnalyzer == True or boolCallDump == True:
        ''' process the gathered log file at current dir '''
        AnalyzerMLTLOG.setWorkingDir(".")
        AnalyzerMLTLOG.doProcessing(boolProcessingException = boolAnalyzer, boolProcessingCallDump = boolCallDump)
        AnalyzerMLTLOG.writeResultToExcel( dictAdditionalBaicInfo, period )
        
        ''' delete the processed log file '''
    DeleteMLTLOG()
    logcount = logcount - 1




''' save the  ExceptPath'''
excelExceptPath = FileNameHeader + "_" + "ExceptPath" + "_" +  period + ".xlsx"
excelCallDrop = FileNameHeader + "_" + "CallDrop" + "_" +  period + ".xlsx"

print "Saving ressult to Excel file : ", excelExceptPath, " " , excelCallDrop
AnalyzerMLTLOG.closeExcel(excelExceptPath, excelCallDrop)
print "Saved...."




''' ====================================================================================='''

if boolDBCopy == False :
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












