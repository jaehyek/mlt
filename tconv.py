# _*_ coding: utf-8 _*_

'''
Created on 2012. 8. 2.

@author: jaehyek
'''

'''
c:> python tconv.py python tconv.py -s "2012-10-28 00:16:43"
c:> python tconv.py python tconv.py -t 1349869845584
'''



from datetime import datetime, timedelta
import  argparse




def ConvertTimeStampToString ( timestampmilisecond ):
    if timestampmilisecond == None:
        return ""
    strfmt = "%Y-%m-%d %H:%M:%S"
    outdatetime = datetime(1970, 1, 1) + timedelta(hours= 9, milliseconds=timestampmilisecond)
    return outdatetime.strftime(strfmt)

def ConvertDateTimeToMiliSeconds( y, m, d, h = 0 , minute = 0 , s = 0 ):
    daydiff = datetime(y, m, d, h, minute, s) - datetime(1970, 1, 1, 9, 0, 0)
    return int(daydiff.total_seconds()) * 1000L
    
    
strfmt = False
intfmt = False

cmdlineopt = argparse.ArgumentParser(description='convert MLT LOG timestamp to string format or  convert reversely')
cmdlineopt.add_argument('-t', action="store", dest="intfmt", default="",  help='convert timestamp to readable time format. default = False' )
cmdlineopt.add_argument('-s', action="store", dest="strfmt", default="",  help='convert string format type to integer format. default = False ' )

cmdlineresults = cmdlineopt.parse_args()

strfmt = cmdlineresults.strfmt
intfmt = cmdlineresults.intfmt

if len(intfmt) > 0 : 
    print ConvertTimeStampToString(int(intfmt))
    
if len(strfmt) > 0 : 
    l = strfmt.split(" ")
    ymd = l[0]
    hms = l[1]
    list_y_m_d = ymd.split("-")
    list_h_m_s = hms.split(":")
    
    print str(ConvertDateTimeToMiliSeconds(int(list_y_m_d[0]), int(list_y_m_d[1]), int(list_y_m_d[2]), int(list_h_m_s[0]), int(list_h_m_s[1]), int(list_h_m_s[2]) ))
    
    
