# _*_ coding: utf-8 _*_

'''
Created on 2012. 12. 28.

@author: jaehyek
'''

import os , argparse



'''
c:> python cf.py -f excel.csv -c 3 -a textsearch -o modeltext
'''



class SeqFile :
    def __init__(self, fname ):
        self.file = open(fname)
    def close(self):
        self.file.close()
    def __iter__(self):
        return self
    def checkpairQuoteMark(self, line):
        countfind = 0
        index = 0
        index = line.find('"', index)
        while( index  != -1 ):
            index += 1
            countfind += 1
            index = line.find('"', index)

        boolpaired = True
        if (countfind % 2 ) == 1 :
            boolpaired = False

        return boolpaired

    def next(self):
        global boolcsvfile
        if boolcsvfile == False:
            line = self.file.readline()
            if not line : raise StopIteration
        else:
            line = ""
            while(1):
                linetemp = self.file.readline()

                if not linetemp :
                    raise StopIteration
                line += linetemp
                if self.checkpairQuoteMark(line) == True :
                    break

        return line

def CSVLinesplit(line, delimiter ) :

    listtempstr = line.split(delimiter)
    liststr = []
    strsave = ""
    for tempstr in listtempstr :
        if len(tempstr) == 0 :
            liststr.append("")
            continue

        if tempstr[0] == '"' :
            if tempstr[-1] == '"' :
                liststr.append(tempstr)
            else:
                strsave = tempstr[1::] + ","
        elif tempstr[-1] == '"' :
            strsave += tempstr[0:-1]
            liststr.append(strsave)
            strsave = ""
        else:
            if len(strsave) > 0 :
                strsave += tempstr + ","
            else:
                liststr.append(tempstr)

    return liststr

def findStrInField(strSrc, strPattern) :
    liststrword = strPattern.lower().split()
    print strSrc
    liststratom1 = []
    liststratom2 = []
    for strword in liststrword :
        listatom1 = strword.split("(")
        if len(listatom1) == 1 :
            liststratom1.append(strword)
            continue
        for atom1 in listatom1[0:-1] :
            liststratom1.append(atom1)
            liststratom1.append("(")
        liststratom1.append(listatom1[-1])


    for strword in liststratom1 :
        listatom2 = strword.split(")")
        if len(listatom2) == 1 :
            liststratom2.append(strword)
            continue
        for atom1 in listatom2[0:-1] :
            liststratom2.append(atom1)
            liststratom2.append(")")
        liststratom2.append(listatom2[-1])


    posSearch = 0
    listresult = []
    for atom in liststratom2 :
        if len(atom) == 0 or atom == "(" or atom == ")" or atom == "and" or atom == "or" or atom == "not" :
            listresult.append(atom)
            continue
        if atom[0] == "~" :
            if posSearch >= 0 :
                posSearch = strSrc.find(atom[1:], posSearch)
            else:
                posSearch = -1
        else:
            posSearch = strSrc.find(atom)

        if posSearch >= 0 :
            listresult.append("True")
        else:
            listresult.append("False")

    strEvalBefore = ""
    for atom in listresult :
        strEvalBefore +=  atom + " "

    # print strEvalBefore, ":" , eval(strEvalBefore)

    return eval(strEvalBefore)

def findtextInStr( StrTarget, Str_Search ) :
    liststrSearch = Str_Search.split()
    result = -1
    for StrSearch in liststrSearch :
        index = StrTarget.find(StrSearch)
        if index >= 0 :
            result = index

    return result


def findtextInline(line):
    global boolcsvfile
    # make the text list
    line = line.lower()
    boolfound = False

    if len(delimiter) >= 0 :

        if boolcsvfile == True :
            liststr = CSVLinesplit(line, delimiter)
        else:
            liststr = line.split(delimiter)


        if len(textinfile ) > 0 :
            for str in liststr :
                if findStrInField(str.lower(), textinfile) >= 0 :
                    boolfound = True

        else:
            boolfound = findStrInField( liststr[textindex], textsearch )
            if len(modeltext) > 0 :
                boolfound = boolfound and findStrInField( liststr[modelindex], modeltext )

    else:
        boolfound =  findStrInField(line, textinfile)

    return boolfound

def convertXLS2CSV(filename ):
    import time
    import win32com.client

    xlApp = win32com.client.Dispatch('Excel.Application')

    xlWb = xlApp.Workbooks.Open(filename)
    filename_out = ""
    if filename[-5:] == ".xlsx" :
        filename_out = filename.split('.xlsx')[0] + '.csv'
    else:
        filename_out = filename.split('.xls')[0] + '.csv'

    xlWb.SaveAs( filename_out, FileFormat=6)

    xlApp.Quit()
    time.sleep(2) # give Excel time to quit, otherwise files may be locked

    return filename_out





# variables.
modeltext = ""
modelindex = -1
textsearch = ""
textindex = -1
filename = ""
regular=False
delimiter = ""
textinfile = ""
boolcsvfile = False

boolcsvout = False

if __name__ == '__main__':

    cmdlineopt = argparse.ArgumentParser(description='find text in CSV type filename')
    cmdlineopt.add_argument('-ms', action="store", dest="modeltext", default="",  help='second colomn text list seperated by space to find ' )
    cmdlineopt.add_argument('-mc', action="store", dest="modelindex", default="",  help='second colomn number to find ' )
    cmdlineopt.add_argument('-ts', action="store", dest="textsearch", default="",  help='first column text list seperated by space to find ' )
    cmdlineopt.add_argument('-tc', action="store", dest="textindex", default="",  help='first column number to find ' )
    cmdlineopt.add_argument('-f', action="store", dest="filename", default="",  help='file name to find ' )
    cmdlineopt.add_argument('-req', action="store_true", dest="regular", default=False,  help='boolean value to use the regular exepression ' )
    cmdlineopt.add_argument('-del', action="store", dest="delimiter", default="",  help='delimiter to seperate a sentence ' )
    cmdlineopt.add_argument('-txt', action="store", dest="textinfile", default="",  help='text to just find , with no reference to column ' )
    cmdlineopt.add_argument('-csv', action="store_true", dest="boolcsvout", default="",  help=' csv file name for saving result ' )


    cmdlineresults = cmdlineopt.parse_args()

    modeltext = cmdlineresults.modeltext
    modelindex = cmdlineresults.modelindex
    textsearch = cmdlineresults.textsearch
    textindex = cmdlineresults.textindex
    filename = cmdlineresults.filename
    regular = cmdlineresults.regular
    delimiter = cmdlineresults.delimiter
    textinfile = cmdlineresults.textinfile
    boolcsvout = cmdlineresults.boolcsvout

    filename = r"D:\temp10\CIC0128.csv"
    textsearch = "전환"
    textindex = "5"
    boolcsvout = False

    Hread = None
    Hwrite = None



    if len(filename) == 0 :
        print "No input filename"
        exit()

    # textsearch �� textinfile �� �� �� �ϳ��� search�Ѵ�.
    if (len(textsearch) == 0  and len(textinfile) != 0 ) or (len(textsearch) != 0  and len(textinfile) == 0 ) :
        pass
    else:
        print "No text to find, or two text to find "
        exit()

    if len(textinfile) != 0 :
        textinfile = textinfile.lower()


    if len(textsearch) != 0 :
        textsearch = textsearch.lower()
        if len(textindex) < 0 :
            print "No column 0 indexing to find"
            exit()
        else:
            textindex = int(textindex)
            if len(modeltext) != 0 :
                modeltext = modeltext.lower()
                if len(modelindex) < 0 :
                    print "No column 1 indexing to find"
                    exit()
                else:
                    modelindex = int(modelindex)


    filename = filename.lower()
    if filename[-4:] == ".xls"  or filename[-5:] == ".xlsx" :
        filename = convertXLS2CSV(filename)



    if filename[-4:] == ".csv":
        boolcsvfile = True
        delimiter = ","

    Hread = SeqFile(filename)
    LineNO = 1
    FoundCount = 0

    if boolcsvfile == True :
        if boolcsvout == True and len(textsearch) > 0  :
            fileoutput = filename.split(".")[0] + ".csv"
            Hwrite = open( fileoutput, "w" )

            # composite  the head line of column line
            line = '"' + textsearch + '",' +  Hread.next()
            Hwrite.write(line)
        else:
            Hread.next()



    for line in Hread :

        boolout = findtextInline(line)

        if Hwrite != None :
            if boolout == True :
                FoundCount += 1
                line = 'O,' +  line
            else :
                line = 'X,' +  line

            Hwrite.write(line)
        else:
            if boolout == True :
                print LineNO,"]],",  line,
                FoundCount += 1

        LineNO += 1




    Hread.close()
    if Hwrite != None :
        Hwrite.close()


    print " "
    print "===== Total Found Count :",     FoundCount


# 1.	# You must have Python for Windows (I used 2.6) and pywin32 extensions
# 2.	# installed and Excel 2007 on a Windows PC
# 3.	# Put this script into the dir where all the .XLSX files are and then cd to that dir
# 4.	# Usage:  c:\python26\python.exe xls2csv.py
# 5.
# 6.	import glob
# 7.	import os
# 8.	import time
# 9.	import win32com.client
# 10.
# 11.	xlsx_files = glob.glob('*.xlsx')
# 12.
# 13.	if len(xlsx_files) == 0:
# 14.	    raise RuntimeError('No XLSX files to convert.')
# 15.
# 16.	xlApp = win32com.client.Dispatch('Excel.Application')
# 17.
# 18.	for file in xlsx_files:
# 19.	    xlWb = xlApp.Workbooks.Open(os.path.join(os.getcwd(), file))
# 20.	    xlWb.SaveAs(os.path.join(os.getcwd(), file.split('.xlsx')[0] +
# 21.	'.csv'), FileFormat=6)
# 22.
# 23.	xlApp.Quit()
# 24.	time.sleep(2) # give Excel time to quit, otherwise files may be locked
# 25.
# 26.	# Uncomment the two lines below if you want the script to remove
# 27.	# the orig .xlsx files when done
# 28.
# 29.	#for file in xlsx_files:
# 30.	#    os.unlink(file)


