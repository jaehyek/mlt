# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:49:16 2013

@author: jaehyek
"""

#!!! get the MLT LOG list
import pymssql

''' ---------order the SVC data by IMEI -------- '''
def IMEICmp ( a1, a2 ) :
    return cmp ( a1["esn_imei_no"], a2["esn_imei_no"] )



def deleteDuplicateIMEI(listdictmltlogs):
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
                print "esn_imei_no" , dictmltlogs["esn_imei_no"]
                continue
        else:
            listdictmltlogsTemp.append(dictmltlogs)
            dictmltlogsPre = dictmltlogs

    ##restore
    return listdictmltlogsTemp

def getListDictMLTLOGFromServer( model_name, startdate, enddate):
    conn = pymssql.connect(host='10.185.135.57', user='MLT_INF', password='inf_P@ssword', database='LGMLTP', charset="UTF-8" , as_dict=True)
    cur = conn.cursor()

    # 국내 모델만.
    LOGStatement = ''' select * from  dmd_log_m  where ( model_name = '%s' ) and ( cause_cd = 'MDA' or cause_cd = 'MBE'  ) and  base_ymd between '%s' and '%s'  '''
    LOGStatement = LOGStatement % ( model_name, startdate, enddate )
    print "LOGStatement = " , LOGStatement

    cur.execute(LOGStatement)
    listdictmltlogs = cur.fetchall()
    conn.close()

    listdictmltlogs = deleteDuplicateIMEI(listdictmltlogs)

    return listdictmltlogs



