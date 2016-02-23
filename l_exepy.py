#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:15:35 2013

@author: jaehyek.choi
다음의 script은 Ubuntu상에서  실행되고,  옵션으로 dirbatchfile을 지정하면, 
해당 dir에 있는 bat 실행파일을 dirworking으로 이동후 수행한다.
이렇게 하는 목적은  ssh terminal으로 접속한 후,  명령을 실행시키고 완료하기 전에, 
ssh connection을 해제하기 위함이다.  즉 connection이 해제되어도  background으로 계속
수행시키는 목적이다.
"""

import time
import glob
import sys
import os 
import os.path
import shutil
import m_email

def runbatch( dirworking ):
    os.chdir(dirworking)
    strtempdir = "temp" 
    if not os.path.exists(strtempdir):
        os.makedirs(strtempdir)
    while (True):    
        listbatch = glob.glob(r"*.bat")
        for batch in listbatch : 
            os.system(batch)
            shutil.move(batch, strtempdir)
        
        print "sleeping for 20sec..."
        time.sleep(20)
    

strdesc = '''
first, move to dirbatchfile dir to monitor  batch file , \n
if batch file,  move to dirworking to execute batch file . 
'''

if __name__ == "__main__":
    import argparse
    dirbatchfile = "."
    dirworking = "."

    cmdlineopt = argparse.ArgumentParser(description=strdesc )
    cmdlineopt.add_argument('-db', action="store", dest="dirbatchfile", default='.',  help='directory in which batch file exist . default = . ' )
    cmdlineopt.add_argument('-dw', action="store", dest="dirworking",  default=".", help='directory in which batch file runs  default = . ' )

    cmdlineresults = cmdlineopt.parse_args()
    
    dirbatchfile = cmdlineresults.dirbatchfile
    dirworking = cmdlineresults.dirworking

    
    ''' goto the batch file dir to monigoring '''
    diroutput = os.path.abspath(dirbatchfile)
    if not os.path.exists(diroutput):
        os.makedirs(diroutput)
    os.chdir(diroutput)

    try:
        runbatch( dirworking )
    except Exception as e  :
        import traceback


        strReportFileName = "Errorexepy_" + ".txt"
        f = open(strReportFileName, "w")
        f.write( "Error Message : \n" )
        f.write( "batch file dir : " +  dirbatchfile + "\n" )
        f.write( traceback.format_exc() )

        f.close()
        
        print "------------- encountng Error during processing ------------------"
        m_email.send_mail("jaehyek.choi@lge.com",["jaehyek.choi@lge.com"], 
                          "Error Counting During HeavyUser", "Error Counting During HeavyUser", 
                          [strReportFileName])
        print "sending the file %s using email " % strReportFileName
    
    
