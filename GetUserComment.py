# _*_ coding: utf-8 _*_

'''
Created on 2012. 12. 13.

@author: jaehyek
'''

import os , argparse
# from Crypto.Util.RFC1751 import wordlist


# variables.
diroutput = "."
period = ""




if __name__ == '__main__':
    pass

'''
usage : GetUserComments.py  -o c:\temp_mlt -p 20120511-20120705
'''

cmdlineopt = argparse.ArgumentParser(description='get the MLT Table and Field Name from MLT Server 10.185.135.57')
cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='output directory to put . default = . sample: c:\\temp_mlt' )
cmdlineopt.add_argument('-p', action="store", dest="period", default='',  help=' period . example : 20120601-20120630  ' )

cmdlineresults = cmdlineopt.parse_args()

diroutput = cmdlineresults.diroutput
period = cmdlineresults.period

outputtitle = "GetUserComments"
outputexcel = outputtitle + "_" +  period + ".xlsx"
outputexcelsheetname = outputtitle



if len(diroutput) == 0 :
    diroutput = "."



diroutput = os.path.abspath(diroutput)
if not os.path.exists(diroutput):
    os.makedirs(diroutput)

''' goto the diroutput dir to work '''
os.chdir(diroutput)

startdate =  period.split("-")[0]
enddate = period.split("-")[1]

querystartdate = startdate[4:6] + "/" + startdate[6:] + "/" + startdate[0:4]
queryenddate = enddate[4:6] + "/" + enddate[6:] + "/" + enddate[0:4]

querystatement = " select * from dmr_service_decision a where a.creation_dt >= '%s' and a.creation_dt < '%s' "
querystatement = querystatement %  (querystartdate, queryenddate)
print "querystatement : ", querystatement


import pymssql
conn = pymssql.connect(host='10.185.135.57', user='MLT_INF', password='inf_P@ssword', database='LGMLTP', charset="UTF-8" , as_dict=True)
cur = conn.cursor()

cur.execute(querystatement)
listdictUserComments = cur.fetchall()

if len(listdictUserComments) == 0 :
    print "results length : 0 "
    exit()


fieldnames = [  "creation_dt", "model_name", "symptom_cd", "UserComment","UserSymptomTime", "UserFrequency","decision_cmt", "decision_dt",  "log_file_name", "engineer_id","creation_id",  "svc_cd", "attribute2", "attribute3", "country_cd", "attribute1", "attribute4",
                "attribute5",  "decision_result", "last_update_dt", "symptom_org_cd",  "decision_id", "replay_yn", "last_update_id" ]



''' open the xls file '''
from xlsxcessive.xlsx import Workbook

''' field name '''

wb = Workbook()
ws = wb.new_sheet("UserComments")

rindex = 0
cindex = 0

''' first, insert field name to row0 '''
for fieldname in fieldnames :
    ws.cell(coords=(rindex, cindex,  ),  value = fieldname )
    cindex += 1

''' print SVC info  to excel file '''
rindex = 1
cindex = 0

UserComment = ""
UserSymptomTime = ""
UserFrequency = ""


for dictUserComments in listdictUserComments:
    for fieldname in fieldnames :
        if fieldname == "model_name" :
            name = dictUserComments.get("log_file_name", None)
            namelist = name.split("_")
            if name.find("LG") < 0 :
                ws.cell(coords=(rindex, cindex,  ), value = "Unknown"  )
            else:
                ws.cell(coords=(rindex, cindex,  ), value = namelist[3]  )
        elif fieldname == "UserComment" :
            comment = dictUserComments.get("decision_cmt", None).decode("utf-8")
            commentlist = comment.splitlines()
            listtemp = commentlist[0].split(":")
            if len(listtemp) >= 2 :
                ws.cell(coords=(rindex, cindex,  ), value = listtemp[1] )
            else :
                ws.cell(coords=(rindex, cindex,  ), value = "" )

            listtemp = commentlist[1].split(":")
            if len(listtemp) >= 2 :
                UserSymptomTime = listtemp[1]
            else :
                UserSymptomTime = ""
                
            listtemp = commentlist[2].split(":")
            if len(listtemp) >= 2 :
                UserFrequency = listtemp[1]
            else :
                UserFrequency = ""
                
        elif fieldname == "UserSymptomTime" :
            ws.cell(coords=(rindex, cindex,  ), value = UserSymptomTime )               
            
        elif fieldname == "UserFrequency" :
            ws.cell(coords=(rindex, cindex,  ), value = UserFrequency )
            


        else:
            ws.cell(coords=(rindex, cindex,  ), value = dictUserComments.get(fieldname, None) )
        cindex += 1
    rindex += 1
    cindex = 0



conn.close()


curdir = os.path.abspath(os.curdir)

print "Excel Saving : " + curdir + "\\" +  outputexcel
from xlsxcessive.xlsx import save
save(wb,  outputexcel)



print "Processing End ....."
exit()












