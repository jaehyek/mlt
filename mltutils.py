# _*_ coding: utf-8 _*_

'''
Created on 2012. 12. 01.

@author: jaehyek
'''


import glob
import shutil
import os
import platform
import zipfile

strTempDir = "temp"
boolDBCopy = False
FileDrv = "Z"

def ClearMLTLOG():
    listlog = glob.glob('*.db')
    for log in listlog:
        os.remove( log )


def DeleteMLTLOG(dbfilename = None):
    listlog = []
    if dbfilename != None :
        listlog.append(dbfilename)
    else:
        listlog = glob.glob('*.db')
        
    try:
        if boolDBCopy == False :
            for log in listlog:
                os.remove( log )
        else :
            diroutput = os.path.abspath( os.curdir)
            tempdir = os.path.join(diroutput , strTempDir)
            if not os.path.exists(tempdir):
                os.makedirs(tempdir)
    
            ''' move MLT LOG to temp dir '''
            for log in listlog:
                shutil.move(log, tempdir )
    except:
        print "Can't operate DeleteMLTLOG \n"
        pass



def CopyMLTLOG ( logfullpath ) :
    osname = platform.system()
    filesrc = logfullpath.replace("MLT_LOG\\", "")
    if osname == 'Windows':        
        filesrc = FileDrv + filesrc[1:]
    else:
        filesrc = os.path.join(FileDrv, filesrc[3:])
        
    if os.path.isfile(filesrc) :
        print "Copying log file from : ", filesrc
        shutil.copy(filesrc, r'.')
    else :
        # try to check the zip file and extract it 
        filesrczip = filesrc[:-2] + "zip"
        if os.path.isfile(filesrczip) :
            print "Copying log file from : ", filesrczip
            shutil.copy(filesrczip, r'.')
            filesrczip = os.path.basename(filesrczip)
            z = zipfile.ZipFile(filesrczip)
            z.extractall()
            z = None
            listzfile = glob.glob('*.zip')
            for zfile in listzfile :
                try:
                    os.remove(zfile)
                except Exception :
                    print "======= Can't remove the file ======== \n ", zfile
        else:
            print "!!!    DB file does not exist : ", filesrc, filesrczip



def SaveListDictToCSV( listdictdoc , nameCSV )   :
    '''  convert listdictdoc to file type CSV  '''
    
    #first extract the key list from listdictdoc 
    keyset = set()
    for dictdoc in listdictdoc :
        keyset.update( dictdoc.keys())
    
    listkey = list(keyset)    
    f = open(nameCSV, "w")
    #print listkey
    f.write( ",".join([str(kk) for kk in listkey]) + "\n" )
    
    #print values of key for each dict 
    for dictdoc in listdictdoc : 
        listtemp = []
        for key in listkey :
            listtemp.append( str(dictdoc.get(key,"" )))
        f.write( ",".join([kk for kk in listtemp]) + "\n" )
    f.close()
    
    

        

if __name__ == "__main__":
    listtemp = []
#    listtemp.append({u'LG-F200L': 1111, u'LG-F240K': 3331, u'LG-F240L': 839, u'LG-F200K': 7287, u'LG-F180L': 7190, u'LG-F160L': 1, u'LG-F180K': 7132, u'LG-F220K': 312, u'LG-F180S': 7254, u'LG-F260S': 2657, u'LG-F240S': 5789, u'LG-F200S': 7173} )
#    listtemp.append({u'LG-F200L': 13805, u'LG-F240K': 8405, u'LG-F240L': 17671, u'LG-F260S': 2622, u'LG-F200K': 14410, u'LG-F180L': 54689, u'SHV-E210S': 2, u'LG-F160L': 9, u'unknown': 3, u'LG-F180K': 27847, u'SHW-M250S': 1, u'optimus g': 5, u'\x04tX ': 4, u'LG-F220K': 1079, u'LG-F180S': 32460, u'GT-9000L': 2, u'LG-F240S': 11312, u'LG-F200S': 13842})
#    listtemp.append({u'LG-F200L': 36814, u'optimus g': 2, u'LG-F240L': 11173, u'LG-F260S': 2246, u'LG-F200K': 19998, u'LG-F180L': 50150, u'unknown': 4, u'LG-F180K': 22638, u'LG-F240K': 6365, u'LG-F220K': 760, u'LG-F180S': 22289, u'GT-9000L': 7, u'LG-F240S': 9479, u'LG-F200S': 24205})
#    listtemp.append({u'LG-F200L': 24027, u'optimus g': 7, u'LG-F240L': 24378, u'LG-F260S': 2479, u'LG-F200K': 19711, u'LG-F180L': 41043, u'SHV-E210S': 4, u'LG-F160L': 21, u'unknown': 4, u'LG-F180K': 20263, u'SHW-M250S': 15, u'LG-F240K': 11552, u'\x04tX ': 12, u'LG-F220K': 846, u'LG-F180S': 23623, u'SHV-E21OS': 10, u'LG-F240S': 15439, u'LG-F200S': 21058})
#    listtemp.append({u'LG-F200L': 25700, u'SHV-E21': 36, u'optimus g': 15, u'LG-F240L': 29271, u'GT-9000L': 4, u'LG-F160L': 3, u'LG-F200K': 21319, u'LG-F180L': 43315, u'LG-F240': 34, u'unknown': 3, u'LG-F180K': 20486, u'SHW-M250S': 3, u'LG-F240K': 12328, u'\x04tX ': 9, u'LG-F220K': 1409, u'LG-F180S': 22888, u'SHV-E21OS': 27, u'LG-F260S': 4925, u'LG-F240S': 19629, u'LG-F200S': 24273})
    
    listtemp.append({u'LG-F320L': 1, u'LG-F320K': 222, u'LG-F320S': 363})
    listtemp.append({u'LG-F320L': 965, u'LG-F320K': 466, u'LG-F320S': 862})
    listtemp.append({u'LG-F320L': 299, u'LG-F320S': 384, u'LG-F320K': 168})
    listtemp.append({u'LG-F320L': 1024, u'LG-F320K': 578, u'LG-F320S': 995})
    listtemp.append({u'LG-F320L': 1426, u'LG-F320K': 844, u'LG-F320S': 1352})
    
    SaveListDictToCSV(listtemp, "test.csv")
    











