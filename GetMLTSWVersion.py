# _*_ coding: utf-8 _*_

'''
Created on 2012. 8. 16.

@author: jaehyek
'''

import os , argparse
# from Crypto.Util.RFC1751 import wordlist




# variables.
diroutput = "."
outputtitle = "GetMLTSWVersion"
outputexcel = outputtitle + ".xlsx"
outputexcelsheetname = outputtitle

if __name__ == '__main__':
    pass

'''
usage : GetMLTSWVersion.py  -o c:\temp_mlt
'''

cmdlineopt = argparse.ArgumentParser(description='get the GetMLTSWVersion  from MLT Server 10.185.135.57')
cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='output directory to put. default = . sample: c:\\temp_mlt' )


cmdlineresults = cmdlineopt.parse_args()

diroutput = cmdlineresults.diroutput



if len(diroutput) == 0 :
    diroutput = "."


statement = "select * from dmm_sw_version"



diroutput = os.path.abspath(diroutput)
if not os.path.exists(diroutput):
    os.makedirs(diroutput)

''' goto the diroutput dir to work '''
os.chdir(diroutput)




import pymssql
conn = pymssql.connect(host='10.185.135.57', user='MLT_INF', password='inf_P@ssword', database='LGMLTP', charset="UTF-8" , as_dict=True)
cur = conn.cursor()

cur.execute(statement)
results = cur.fetchall()
print "Total count = %s " % (len(results))

conn.close()

'''
keys = results[0].keys()
for key in keys:
    if type(key) == type("as"):
        print "'" + key + "', " ,

exit()
'''

''' open the xls file '''
from xlsxcessive.xlsx import Workbook

''' field name '''
fieldnames = [ 'sw_version','creation_dt','creation_id','last_update_dt','update_date','country_cd','last_update_id','model_name' ]


wb = Workbook()
ws = wb.new_sheet(outputexcelsheetname) # insert at the end (default)

rindex = 0
cindex = 0

''' first, insert field name to row0 '''
for fieldname in fieldnames :
    ws.cell(coords=(rindex, cindex,  ), value = fieldname )
    cindex += 1


''' print Symptom Info to excel file '''
rindex = 1
cindex = 0


for record in results:
    for fieldname in fieldnames :
        ws.cell(coords=(rindex, cindex,  ), value = record[fieldname] )
        cindex += 1
    rindex += 1
    cindex = 0
    print  ".",

print " "
curdir = os.path.abspath(os.curdir)

print "Excel Saving : " + curdir + "\\" +  outputexcel
from xlsxcessive.xlsx import save
save(wb,  outputexcel)



print "Processing End ....."
exit()





