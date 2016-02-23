# _*_ coding: utf-8 _*_

'''
Created on 2012. 8. 2.

@author: jaehyek
'''
import os , argparse
from datetime import datetime
import  AnalyzerMLTLOG


def main():
    global diroutput, period, boolAnalyzer, boolCallDump
    dictsymptom = { "symptom_cd":"stop" }

    AnalyzerMLTLOG.setWorkingDir(diroutput)
    AnalyzerMLTLOG.doProcessing(boolProcessingException = boolAnalyzer, boolProcessingCallDump=boolCallDump)
    AnalyzerMLTLOG.writeResultToExcel( dictsymptom, period )

    AnalyzerMLTLOG.closeExcel("F200K_ExceptPath.xlsx", "F220K_CallDrop.xlsx")



if __name__ == '__main__' :
    global diroutput, period, boolAnalyzer, boolCallDump
    
    cmdlineopt = argparse.ArgumentParser(description='get the MLT LOG from MLT Server 10.185.135.57')
    cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='output directory to put MLT log file. default = . sample: c:\\temp_mlt' )
    cmdlineopt.add_argument('-p', action="store", dest="period", default='',  help=' period . example : 20120601-20120630  ' )
    cmdlineopt.add_argument('-aExpt', action="store_true", dest="boolAnalyzer",  default=False, help='Analyzer DB ,  default= Faluse' )
    cmdlineopt.add_argument('-aCall', action="store_true", dest="boolCallDump",  default=False, help='Dump the Call history during analyzer DB ,  default= Faluse' )

    cmdlineresults = cmdlineopt.parse_args()

    diroutput = cmdlineresults.diroutput
    period = cmdlineresults.period
    boolAnalyzer = cmdlineresults.boolAnalyzer
    boolCallDump = cmdlineresults.boolCallDump
    
    if len(diroutput) == 0 :
        diroutput = "."
        
    if len(period) == 0 :
        period = "20130101-20130602"



    starttime =  datetime.now()
    print starttime
    
    main()

    endtime =  datetime.now()
    print endtime
    print " elasped time is : ", endtime - starttime

