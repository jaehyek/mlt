# _*_ coding: utf-8 _*_

'''
Created on 2012. 7. 6.

@author: jaehyek
'''

import os , argparse
# from Crypto.Util.RFC1751 import wordlist




# variables.
diroutput = "."
outputtitle = "GetMLTTableFieldNames"
outputexcel = outputtitle + ".xlsx"
outputexcelsheetname = outputtitle

if __name__ == '__main__':
    pass

'''
usage : GetMLTTableFieldNames.py  -o c:\temp_mlt
'''

cmdlineopt = argparse.ArgumentParser(description='get the MLT Table and Field Name from MLT Server 10.185.135.57')
cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='output directory to put . default = . sample: c:\\temp_mlt' )


cmdlineresults = cmdlineopt.parse_args()

diroutput = cmdlineresults.diroutput



if len(diroutput) == 0 :
    diroutput = "."

# the below statement is to get the table list
statement = "SELECT Distinct TABLE_NAME FROM information_schema.TABLES"



diroutput = os.path.abspath(diroutput)
if not os.path.exists(diroutput):
    os.makedirs(diroutput)

''' goto the diroutput dir to work '''
os.chdir(diroutput)


''' open the xls file '''
from xlsxcessive.xlsx import Workbook

''' field name '''

wb = Workbook()
ws = wb.new_sheet(outputexcelsheetname) # insert at the end (default)

rindex = 0
cindex = 0



import pymssql
conn = pymssql.connect(host='10.185.135.57', user='MLT_INF', password='inf_P@ssword', database='LGMLTPM', charset="UTF-8" , as_dict=True)
cur = conn.cursor()

cur.execute(statement)
results = cur.fetchall()


tablenamelist = []
for tabledic in results:
    tablenamelist.append(tabledic["TABLE_NAME"])


print "Table Total count = %s " % (len(results))

  
for tablename in tablenamelist :
    statement_fieldlist = "select * from " + tablename
    try:
        cur.execute(statement_fieldlist)
    except Exception:
        print "Can't receive Field information from ", tablename
        continue
        
    ''' print table name row0  '''
    ws.cell(coords=(rindex, cindex,  ), value = tablename )
    # if tablename == u"dmr_basic_info" :
        # ws.col(cindex + 1 , width=50)
    rindex += 1
    print tablename,  
    
    fieldic = cur.fetchone()
    if ( fieldic != None):
        fieldlist = fieldic.keys()
        for fieldname in fieldlist:
            if type(fieldname) == type("asd"):
                ws.cell(coords=(rindex, cindex,  ), value = fieldname )
                rindex += 1
            print ".",
    rindex = 0
    cindex +=1
    print "."

conn.close()


curdir = os.path.abspath(os.curdir)

print "Excel Saving : " + curdir + "\\" +  outputexcel
from xlsxcessive.xlsx import save
save(wb,  outputexcel)



print "Processing End ....."
exit()












