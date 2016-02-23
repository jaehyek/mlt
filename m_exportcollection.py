# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:32:44 2013

@author: jaehyek.choi

description : Mongo DB 의 collection을 csv으로 출력한다.
"""
import argparse
from datetime import datetime
from pymongo import MongoClient
import re


def exportcollection(svr,dbfilename, csvfilename, collectionname) :
    mongosvr = MongoClient(svr, 27017)
    mongodb = mongosvr[dbfilename]
    colname = mongodb[collectionname]



    cursordoc = colname.find({})
    count = cursordoc.count()
    lastmsg = "The processed collection : %s" % count

    # first, survey the field name across all doc
    setfields =  set()
    for doc in cursordoc :
        print "______________survey the field name _______________________"
        print "the remained count :  %s" % count
        count -= 1

        setfields |= set(doc.keys())

    listfieldname = [ kk for kk in setfields ]
    del setfields

    listfieldname.sort()
    if collectionname == "collectionExceptionCount":
        listfieldname.remove("cause")
        listfieldname.remove("exception_type")
        listfieldname.remove("total")
        listfieldname.append("total")
        listfieldname.append("exception_type")
        listfieldname.append("cause")
    elif collectionname == "collectionCalldropCauseCount" :
        listfieldname.remove("rilcause")
        listfieldname.remove("total")
        listfieldname.append("total")
        listfieldname.append("rilcause")


    f = open(csvfilename, "w" )
    head = ",".join(listfieldname) + " \n"
    f.write(head)

    # remove the curosr
    del cursordoc

    # get the curosr of collection again .
    cursordoc = colname.find({})
    count = cursordoc.count()

    # remove the non-ascii charactor
    recause = re.compile("([^-_a-zA-Z0-9!@#%&=;:~`\$\^\*\(\)\+\[\]\.\{\}\|\?\<\>\\]+|[^\s]+)")
    for doc in cursordoc :
        print "______________write the field value _______________________"
        print "the remained count :  %s" % count
        count -= 1

        strout = ""
        for fieldname in listfieldname :
            strtemp = str(doc.get(fieldname, ""))
            if fieldname == "cause" :
                strtemp = recause.sub("", strtemp)
            elif fieldname == "rilcause":
                strtemp = strtemp.encode('utf-8')
            strout += strtemp + ","
        strout += " \n"
        f.write( strout )

    f.close()

    print lastmsg






if __name__ == "__main__":
    csvfilename = ""
    collectionname = ""
    svr = "172.21.26.39"
    dbfilename = "MLTDB"

    cmdlineopt = argparse.ArgumentParser(description='export the collection  from MongoDB MLTDB to csv file')
    cmdlineopt.add_argument('-csv', action="store", dest="csvfilename", default='',  help='csv file name. default = "" ' )
    cmdlineopt.add_argument('-svr', action="store", dest="svr", default="172.21.26.39",  help='Mongo DB server IP. default="172.21.26.39"' )
    cmdlineopt.add_argument('-col', action="store", dest="collectionname", default="",  help='Mongo DB collection. default=""' )
    cmdlineopt.add_argument('-db', action="store", dest="dbfilename",  default="MLTDB", help='dump the input file,  default= "MLTDB" ' )

    cmdlineresults = cmdlineopt.parse_args()

    csvfilename = cmdlineresults.csvfilename
    collectionname = cmdlineresults.collectionname
    svr = cmdlineresults.svr
    dbfilename = cmdlineresults.dbfilename

    if (len(csvfilename) == 0) or (len(collectionname)== 0) :
        print "please specify the option -csv or -col "
        exit()

    starttime = datetime.now()
    exportcollection(svr,dbfilename, csvfilename, collectionname)
    endtime = datetime.now()

    print "elasped time is : " +  str(endtime - starttime)

