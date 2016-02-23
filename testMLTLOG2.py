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


LogFileCopy = True

import glob
import shutil
import os

strTempDir = "temp"
diroutput = r'd:\temp3'

def DeleteMLTLOG():
    listlog = glob.glob('*.db')
    if LogFileCopy == False :
        for log in listlog:
            os.remove( log )
    else :
        tempdir = diroutput + "\\" + strTempDir
        if not os.path.exists(tempdir):
            os.makedirs(tempdir)

        ''' move MLT LOG to temp dir '''
        for log in listlog:
            shutil.move(log, tempdir )



def CopyMLTLOG ( logfullpath ) :
    filesrc = logfullpath.replace("MLT_LOG\\", "")
    filesrc = FileDrv + filesrc[1:]
    print "Copying log file from : ", filesrc
    shutil.copy(filesrc, r'.\aa.db')



if not os.path.exists(diroutput):
    os.makedirs(diroutput)

''' goto the diroutput dir to work '''
os.chdir(diroutput)

listlog = glob.glob('*.db')
for logname in listlog :
    print logname
    os.remove(logname)
    #shutil.copy(logname , ".." )


##DeleteMLTLOG()






