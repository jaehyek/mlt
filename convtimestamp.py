# _*_ coding: utf-8 _*_
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:  ConvertTimeStampToString
#
# Author:      jaehyek.choi
#
# Created:     13-09-2012
# Copyright:   (c) jaehyek.choi 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from datetime import datetime, timedelta
import argparse


'''
c:> python convtimestamp.py -t 1342386542568
'''

cmdlineopt = argparse.ArgumentParser(description='convert the MLT DB Timestamp to the readable string')
cmdlineopt.add_argument('-t', action="store", dest="timestamp", default='',  help=' MLT Time Stamp ' )

cmdlineresults = cmdlineopt.parse_args()

timestamp = cmdlineresults.timestamp
timestamp = int(timestamp)



def ConvertTimeStampToString ( timestampmilisecond ):
    if timestampmilisecond == None:
        return ""
    strfmt = "%Y-%m-%d %H:%M:%S"
    outdatetime = datetime(1970, 1, 1) + timedelta(hours= 9, milliseconds=timestampmilisecond)
    return outdatetime.strftime(strfmt)

def ConvertDateTimeToMiliSeconds( y, m, d, h = 0 , minute = 0 , s = 0 ):
    daydiff = datetime(y, m, d, h, minute, s) - datetime(1970, 1, 1, 9, 0, 0)
    return int(daydiff.total_seconds()) * 1000L
'''
print ConvertTimeStampToString(1340751010888)
print ConvertDateTimeToMiliSeconds(2012, 6, 26, 22, 50, 10)
exit()
--> result---
2012-06-26 22:50:10
1340751010000

'''

print ConvertTimeStampToString(timestamp)