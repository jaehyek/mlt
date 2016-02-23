# _*_ coding: utf-8 _*_

'''
Created on 2012. 12. 01.

@author: jaehyek
'''


import win32com.client as win32
import os
import glob

def fillcolorrecentpackagenames():
    global excel, wb, ws
    global dicthead, longcolumns, longrows
    
    cindex = dicthead[ "recentpackage_names" ] 
    ws.Columns(cindex).Interior.Pattern = win32.constants.xlSolid
    ws.Columns(cindex).Interior.PatternColorIndex = win32.constants.xlAutomatic
    ws.Columns(cindex).Interior.Color = 65535
    
def fillcoloreventedappname():
    global excel, wb, ws
    global dicthead, longcolumns, longrows
    
    cindex = dicthead[ "evented_app_name" ] 
    
    ws.Columns(cindex).Interior.Pattern = win32.constants.xlSolid
    ws.Columns(cindex).Interior.PatternColorIndex = win32.constants.xlAutomatic
    ws.Columns(cindex).Interior.Color = 5296274
    
    cindex = dicthead[ "app_eventid" ] 
    ws.Columns(cindex).Interior.Pattern = win32.constants.xlSolid
    ws.Columns(cindex).Interior.PatternColorIndex = win32.constants.xlAutomatic
    ws.Columns(cindex).Interior.Color = 5296274
    
def fillcolorexceptiontype():
    global excel, wb, ws
    global dicthead, longcolumns, longrows
    
    cindex = dicthead[ "exception_type" ] 
    
    RangeWhole = ws.Range( ws.Cells(1,1), ws.Cells(longrows,longcolumns) )
    
   
    RangeWhole.AutoFilter(Field = cindex, Criteria1="exception_lockup" )
    RangeVisual = RangeWhole.SpecialCells(win32.constants.xlCellTypeVisible) 
    RangeVisual.Interior.Pattern = win32.constants.xlSolid
    RangeVisual.Interior.PatternColorIndex = win32.constants.xlAutomatic
    RangeVisual.Interior.Color = 13209
    RangeWhole.AutoFilter( Field = cindex)
    
    RangeWhole.AutoFilter(Field = cindex, Criteria1="exception_Kernel_LastK" )
    RangeVisual = RangeWhole.SpecialCells(win32.constants.xlCellTypeVisible) 
    RangeVisual.Interior.Pattern = win32.constants.xlSolid
    RangeVisual.Interior.PatternColorIndex = win32.constants.xlAutomatic
    RangeVisual.Interior.Color = 8950780
    RangeWhole.AutoFilter( Field = cindex)

    RangeWhole.AutoFilter(Field = cindex, Criteria1="exception_calldrop" )
    RangeVisual = RangeWhole.SpecialCells(win32.constants.xlCellTypeVisible) 
    RangeVisual.Interior.Pattern = win32.constants.xlSolid
    RangeVisual.Interior.PatternColorIndex = win32.constants.xlAutomatic
    RangeVisual.Interior.Color = 8950780
    RangeWhole.AutoFilter(Field = cindex )

    RangeWhole.AutoFilter(Field = cindex, Criteria1="exception_framework" )
    RangeVisual = RangeWhole.SpecialCells(win32.constants.xlCellTypeVisible) 
    RangeVisual.Interior.Pattern = win32.constants.xlSolid
    RangeVisual.Interior.PatternColorIndex = win32.constants.xlAutomatic
    RangeVisual.Interior.Color = 8950780
    RangeWhole.AutoFilter(Field = cindex )


    
    RangeWhole = 0
    RangeVisual = 0
    
def fillcolorBatteryChargeType():
    global excel, wb, ws
    global dicthead, longcolumns, longrows
    
    cindex = dicthead[ "battery_chargetype" ] 
    #
    RangeWhole = ws.Range( ws.Cells(1,1), ws.Cells(longrows,longcolumns) )
    RangeSelect = ws.Range( ws.Cells(2,cindex), ws.Cells(longrows,cindex) )
    
    #
    RangeWhole.AutoFilter(Field = cindex, Criteria1="Charging" )
    visualcount =   RangeWhole.SpecialCells(win32.constants.xlCellTypeVisible).Count / longcolumns - 1 
    if visualcount > 0 : 
        RangeSelect.Select()
        excel.Selection.Interior.Pattern = win32.constants.xlSolid
        excel.Selection.Interior.PatternColorIndex = win32.constants.xlAutomatic
        excel.Selection.Interior.Color = 16711935
    RangeWhole.AutoFilter(Field = cindex )
    
    RangeSelect = 0 
    RangeWhole = 0

def fillcolorBatteryTemprature():
    global excel, wb, ws
    global dicthead, longcolumns, longrows
    
    cindex = dicthead[ "battery_temperature" ] 
    #
    RangeWhole = ws.Range( ws.Cells(1,1), ws.Cells(longrows,longcolumns) )
    RangeSelect = ws.Range( ws.Cells(2,cindex), ws.Cells(longrows,cindex) )
    
    #
    RangeWhole.AutoFilter(Field = cindex, Criteria1=">=40" )
    visualcount =   RangeWhole.SpecialCells(win32.constants.xlCellTypeVisible).Count / longcolumns - 1 
    if visualcount > 0 : 
        RangeSelect.Select()
        excel.Selection.Interior.Pattern = win32.constants.xlSolid
        excel.Selection.Interior.PatternColorIndex = win32.constants.xlAutomatic
        excel.Selection.Interior.Color = 255
    RangeWhole.AutoFilter(Field = cindex )
    
    RangeSelect = 0 
    RangeWhole = 0

def fillcolorBatteryLevel():
    global excel, wb, ws
    global dicthead, longcolumns, longrows
    
    cindex = dicthead[ "battery_level" ] 
    #
    RangeWhole = ws.Range( ws.Cells(1,1), ws.Cells(longrows,longcolumns) )
    RangeSelect = ws.Range( ws.Cells(2,cindex), ws.Cells(longrows,cindex) )
    
    #
    RangeWhole.AutoFilter(Field = cindex, Criteria1="<=5" )
    visualcount =   RangeWhole.SpecialCells(win32.constants.xlCellTypeVisible).Count / longcolumns - 1 
    if visualcount > 0 : 
        RangeSelect.Select()
        excel.Selection.Interior.Pattern = win32.constants.xlSolid
        excel.Selection.Interior.PatternColorIndex = win32.constants.xlAutomatic
        excel.Selection.Interior.Color = 255
    RangeWhole.AutoFilter(Field = cindex )
    

    RangeSelect = 0 
    RangeWhole = 0

def fillcolorLCDOnOff():
    global excel, wb, ws
    global dicthead, longcolumns, longrows
    
    cindex = dicthead[ "lcd_state" ] 
    #
    RangeWhole = ws.Range( ws.Cells(1,1), ws.Cells(longrows,longcolumns) )
    RangeSelect = ws.Range( ws.Cells(2,cindex), ws.Cells(longrows,cindex) )
    
    #
    RangeWhole.AutoFilter(Field = cindex, Criteria1="LCD_ON" )
    visualcount =   RangeWhole.SpecialCells(win32.constants.xlCellTypeVisible).Count / longcolumns - 1 
    if visualcount > 0 : 
        RangeSelect.Select()
        excel.Selection.Interior.Pattern = win32.constants.xlSolid
        excel.Selection.Interior.PatternColorIndex = win32.constants.xlAutomatic
        excel.Selection.Interior.Color = 15773696
    RangeWhole.AutoFilter(Field = cindex )

    RangeWhole.AutoFilter(Field = cindex, Criteria1="LCD_OFF" )
    visualcount =   RangeWhole.SpecialCells(win32.constants.xlCellTypeVisible).Count / longcolumns - 1 
    if visualcount > 0 : 
        RangeSelect.Select()
        excel.Selection.Interior.Pattern = win32.constants.xlSolid
        excel.Selection.Interior.PatternColorIndex = win32.constants.xlAutomatic
        excel.Selection.Interior.Color = 5066061
    RangeWhole.AutoFilter(Field = cindex )    
    
    RangeSelect = 0 
    RangeWhole = 0

def fillcolorPowerOnOff():
    global excel, wb, ws
    global dicthead, longcolumns, longrows
    
    cindex = dicthead[ "power_state" ] 
    #
    RangeWhole = ws.Range( ws.Cells(1,1), ws.Cells(longrows,longcolumns) )
    RangeSelect = ws.Range( ws.Cells(2,cindex), ws.Cells(longrows,cindex) )
    
    #
    RangeWhole.AutoFilter(Field = cindex, Criteria1="POWER_ON" )
    visualcount =   RangeWhole.SpecialCells(win32.constants.xlCellTypeVisible).Count / longcolumns - 1 
    if visualcount > 0 : 
        RangeSelect.Select()
        excel.Selection.Interior.Pattern = win32.constants.xlSolid
        excel.Selection.Interior.PatternColorIndex = win32.constants.xlAutomatic
        excel.Selection.Interior.Color = 255
    RangeWhole.AutoFilter(Field = cindex )

    RangeWhole.AutoFilter(Field = cindex, Criteria1="POWER_OFF" )
    visualcount =   RangeWhole.SpecialCells(win32.constants.xlCellTypeVisible).Count / longcolumns - 1 
    if visualcount > 0 : 
        RangeSelect.Select()
        excel.Selection.Interior.Pattern = win32.constants.xlSolid
        excel.Selection.Interior.PatternColorIndex = win32.constants.xlAutomatic
        excel.Selection.Interior.Color = 0
    RangeWhole.AutoFilter(Field = cindex )    
    
    RangeSelect = 0 
    RangeWhole = 0

def doDumpPost(workdir, filename ):
    global excel, wb, ws
    global dicthead, longcolumns, longrows
    savedir = os.getcwd()
    diroutput = os.path.abspath(workdir)
    if not os.path.exists(diroutput):
        os.makedirs(diroutput)

    ''' goto the diroutput dir to work '''
    os.chdir(diroutput)

    dblist = []
    if len(filename) != 0 :
        dblist.append(filename)
    else:
        dblist = glob.glob('*.xlsx')
        
    if len( dblist ) == 0 :
        print "No Excel file was found. "
        return 

    
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    for xlsfilename in dblist:
        
        print "MLT DB DumpPost  : " + xlsfilename
        
        xlsfilename = os.path.join( diroutput, xlsfilename )
        wb = excel.Workbooks.Open(xlsfilename)
        ws = wb.Worksheets("MLT_DUMP")
        
        longcolumns = ws.Range("A1").CurrentRegion.Columns.Count
        longrows = ws.Range("A1").CurrentRegion.Rows.Count
        print "column No : ", longcolumns
        print "Row No : ", longrows
        
        # get the column head value 
        dicthead = {}
        for cindex in range(1, longcolumns + 1 ) :
            dicthead [ ws.Cells(1,cindex).Value ] = cindex
            
            
        fillcolorexceptiontype()
        print ".",         
        fillcolorBatteryLevel()
        print ".", 
        fillcolorPowerOnOff()
        print ".", 
        fillcolorLCDOnOff()
        print ".", 

        fillcolorBatteryTemprature()
        print ".", 
        fillcolorBatteryChargeType()
        print ".", 
        fillcoloreventedappname()
        print ".", 
        fillcolorrecentpackagenames()
        print "."


        # delete the color of head line
        ws.Range( ws.Cells(1,1), ws.Cells(1,longcolumns) ).Interior.Pattern = win32.constants.xlNone
        
        #첫줄 틀 고정.
        excel.ActiveWindow.SplitColumn = 0 
        excel.ActiveWindow.SplitRow = 1
        excel.ActiveWindow.FreezePanes = True
        
        # Zoom mode : 30%
        excel.ActiveWindow.Zoom = 30
        
        wb.Save()
        excel.Workbooks.Close()
        
        ws = None
        wb = None
    
    excel.Application.Quit()
    excel = None
    dblist = []
    os.chdir(savedir)

'''
c:> python MltDBDump.py -o c:\temp_mlt  -a 
'''

if __name__ == "__main__":
    import argparse
    diroutput = "."
    ShutdownAfter = False
    filename = ""
    
    cmdlineopt = argparse.ArgumentParser(description='dump MLT DB into Excel file')
    cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='outputing and working directory . default = . sample: c:\\temp_mlt' )
    cmdlineopt.add_argument('-s', action="store_true", dest="ShutdownAfter",  default=False, help='shutdown system after job finished,  default= Faluse' )
    cmdlineopt.add_argument('-f', action="store", dest="filename",  default="", help='dump the input file,  default= "" ' )

    cmdlineresults = cmdlineopt.parse_args()

    diroutput = cmdlineresults.diroutput
    ShutdownAfter = cmdlineresults.ShutdownAfter
    filename = cmdlineresults.filename

    doDumpPost ( diroutput, filename )
    
    if ShutdownAfter == True :
        os.system( "shutdown /s /t 300 ")
    
    












