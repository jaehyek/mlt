# _*_ coding: utf-8 _*_
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jaehyek.choi
#
# Created:     12-09-2012
# Copyright:   (c) jaehyek.choi 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


import pymssql
conn = pymssql.connect(host='10.185.135.57', user='MLT_INF', password='inf_P@ssword', database='LGMLTPM', charset="UTF-8" , as_dict=True)
cur = conn.cursor()

statement = '''select count( * ) from    dmd_log_m where 
(model_name='LGE971' or 
model_name='LGLS696' or 
model_name='LGLS840' or 
model_name='LGLS860' or 
model_name='LGLW770' or 
model_name='LGMS695' or 
model_name='LGMS770' or 
model_name='LGMS840' or 
model_name='LGMS870' or 
model_name='LGP769BK' or 
model_name='LGP769BKGO' or 
model_name='LGUS730' or 
model_name='LGVS840' or 
model_name='LGVS840P' or 
model_name='LGVS840SS' or 
model_name='LGVS920' or 
model_name='LGVS930' or 
model_name='LGVS930SS' or 
model_name='LGVS950' or 
model_name='LGVS950SS' or 
model_name='LGP769' or 
model_name='VS930 4G' or 
model_name='VS950 4G' ) and 
receipt_ymd between '20121201' and '20130326'



'''


cur.execute(statement)
listdict = cur.fetchall()

print listdict
exit()

print "MLT LOG Total count = %s " % (len(listdict))


if len(listdict) == 0 :
    print "LOG Total count = 0, exit "
    exit()


conn.close()

for name  in listdict :
    print name 



