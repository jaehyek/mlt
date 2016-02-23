# _*_ coding: utf-8 _*_

'''
Created on 2012. 12. 01.

@author: jaehyek
'''

import os
import glob
from datetime import datetime, timedelta
import shutil
from pysqlite2 import dbapi2 as sqlite3
from xlsxcessive.xlsx import Workbook
from xlsxcessive.xlsx import save
import math
import re
import string

# use the following to converet a number to dot "."

_char_class_punct = "[" + re.escape(string.punctuation) + "]"


rehexa = re.compile("0x[0-9a-fA-F]{1,8}")
rehexa1 = re.compile("\s[0-9a-fA-F]{1,15}\s")
redeci = re.compile("\d+")
#resymbol1 = re.compile("[^ A-Za-z]")
resymbol1 = re.compile(_char_class_punct, re.UNICODE ) 
resymbol2 = re.compile("\s+")

def DecryptIMSICode( strEncrypted) :
    if len(strEncrypted) < 4 :
        return ""

    liststr = []
    while ( len(strEncrypted) >= 4 ) :
        liststr.append( strEncrypted[0:4] )
        strEncrypted = strEncrypted[4:]
    strDecrypted = ""
    charbackup = ""
    for str in liststr :
        strOneDigit = str[2:4] + str[0:2]
        nOneDigit = int ( strOneDigit, 16 )
        nDigit = int(math.sqrt(nOneDigit))
        char = unichr(nDigit)
        if len(charbackup) == 0 :
            charbackup = char
        else :
            strDecrypted += char
            strDecrypted += charbackup
            charbackup = ""
    if len(charbackup) > 0 :
        strDecrypted += charbackup

    return strDecrypted


''' ======================================================================'''
''' define some utility '''
def check_table_exception_blobs ( cur ):
    query = "SELECT name FROM sqlite_master WHERE type='table'"
    listTable = list( cur.execute(query))
    if (table_exception_blobs, ) in listTable :
        return True
    else:
        return False




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

''' ---------order the SVC data by IMEI -------- '''
def TimeStampCmp ( a1, a2 ) :
    return cmp ( a1["timestamp"], a2["timestamp"] )


table_app_usage = 't307'
f00n_app_usage = "f002 ,f003, f004"
fields_app_usage = ["timestamp", "evented_app_name", "app_eventid"]
dict_app_event_type = {11:"start foreground", 12:"start background", 13:"start broadcast", 14:"start service", 15:"start provider", 16:"added application", 19:"start other", 20:"end", 31:"resumed", 32:"paused" }


def get_AppUsage_info(listdictDBDump, listdictBasicSWVer, cur, querywhere):
    query_app_usage = "select %s from %s " % (f00n_app_usage,table_app_usage  )
    query_app_usage += querywhere
    cur.execute(query_app_usage)
    listtupleAppUsage = cur.fetchall()

    for tupleAppUsage in listtupleAppUsage :
        timestamp, package, eventid = tupleAppUsage
        if not eventid in [11, 12, 13, 14, 15, 16, 19, 20, 31, 32] :
            continue
        eventid = dict_app_event_type[eventid]
        dicttemp = dict(zip( fields_app_usage, (timestamp,package, eventid )))
        listdictDBDump.append( dicttemp )




table_battery_info = 't308'
f00n_battery_info = "f002 ,f003, f004"
fields_battery_info = ["timestamp", "battery_level", "battery_voltage", "battery_temperature", "battery_healthtype", "battery_chargetype", "battery_plugtype", "battery_present" ]
fields_battery_low_enter = [ "timestamp", "battery_low_enter"]
fields_battery_low_exit = [ "timestamp", "battery_low_exit"]

def get_battery_info (listdictDBDump, listdictBasicSWVer, cur,  querywhere):
    querybattery = "select %s from %s " % (f00n_battery_info, table_battery_info )
    querybattery += querywhere
    cur.execute( querybattery )
    listtupleBatteryInfos = cur.fetchall()


    BATTERY_LEVEL_MASK = 0x000000000000FFFFL;
    BATTERY_VOLTAGE_MASK = 0x00000000FFFF0000L;
    BATTERY_TEMPERATURE_MASK = 0x0000FFFF00000000L;
    BATTERY_HEALTH_MASK = 0x000F000000000000L;
    BATTERY_SATUS_MASK = 0x00F0000000000000L;
    #BATTERY_PLUG_TYPE_MASK = 0x0F00000000000000L;
    BATTERY_PLUG_TYPE_MASK = 0x0300000000000000L;    # for mask value adjustment due to abnormal value
    BATTERY_PRESENT_MASK = 0x7000000000000000L;

    BATTERY_VOLTAGE_SHIFT = 16;
    BATTERY_TEMPERATURE_SHIFT = 32;
    BATTERY_HEALTH_SHIFT = 48;
    BATTERY_STATUS_SHIFT = 52;
    BATTERY_PLUG_TYPE_SHIFT = 56;
    BATTERY_PRESENT_SHIFT = 60;

    dictbatteryhealth = {  1:"Unknown", 2:"Good", 3:"OverHeat", 4:"Dead", 5:"OverVoltage", 6:"UnspecifiedFailure", 7:"Cold"}
    dictbatterycharging = {1:"Unknown", 2:"Charging", 3:"Discharging", 4:"NotCharging", 5:"Full"}
    dictbatteryplugtype = {0:"None", 1:"AC", 2:"USB", 3:"None" }


    for tupleBatteryInfo in listtupleBatteryInfos:
        timestamp, battery_eventid, battery_value = tupleBatteryInfo
        if battery_eventid == 11 :
            battery_level = battery_value & BATTERY_LEVEL_MASK
            battery_voltage = ((battery_value & BATTERY_VOLTAGE_MASK) >> BATTERY_VOLTAGE_SHIFT) / 1000
            battery_temperature = ((battery_value & BATTERY_TEMPERATURE_MASK) >> BATTERY_TEMPERATURE_SHIFT ) / 10
            battery_health = (battery_value & BATTERY_HEALTH_MASK) >> BATTERY_HEALTH_SHIFT
            battery_charging = (battery_value & BATTERY_SATUS_MASK) >> BATTERY_STATUS_SHIFT
            battery_plugtype = (battery_value & BATTERY_PLUG_TYPE_MASK) >> BATTERY_PLUG_TYPE_SHIFT
            battery_present = (battery_value & BATTERY_PRESENT_MASK) >> BATTERY_PRESENT_SHIFT

            battery_health = dictbatteryhealth[battery_health]
            battery_charging = dictbatterycharging[battery_charging]
            battery_plugtype = dictbatteryplugtype[battery_plugtype]

            dicttemp = dict(zip(fields_battery_info, (timestamp, battery_level, battery_voltage,battery_temperature,battery_health, battery_charging, battery_plugtype, battery_present  )))


        elif battery_eventid == 12  :
            dicttemp = dict(zip(fields_battery_low_enter, (timestamp, 1 )))

        elif battery_eventid == 13  :
            dicttemp = dict(zip(fields_battery_low_exit, (timestamp, 1 )))

        listdictDBDump.append( dicttemp )


def CalcRSSILevel( signal_type,  nSignalStrength):
    nRSSILevel = -1
    if signal_type == 23:  # "GSM"
        if nSignalStrength <= 2 or nSignalStrength == 99: nRSSILevel = 0
        elif nSignalStrength >= 12: nRSSILevel = 4
        elif nSignalStrength >= 8: nRSSILevel = 3
        elif nSignalStrength >= 5: nRSSILevel = 2
        else: nRSSILevel = 1
    elif signal_type == 21 :  # "CDMA"
        nLevelDbm = 0
        if nSignalStrength >= -75: nLevelDbm = 4
        elif nSignalStrength >= -85: nLevelDbm = 3
        elif nSignalStrength >= -95: nLevelDbm = 2
        elif nSignalStrength >= -100: nLevelDbm = 1
        else: nLevelDbm = 0
        nRSSILevel = nLevelDbm
    elif signal_type == 22 :  # "EVDO"
        nLevelEvdoDbm = 0
        if nSignalStrength >= -65: nLevelEvdoDbm = 4
        elif nSignalStrength >= -75: nLevelEvdoDbm = 3
        elif nSignalStrength >= -90: nLevelEvdoDbm = 2
        elif nSignalStrength >= -105: nLevelEvdoDbm = 1
        else: nLevelEvdoDbm = 0
        nRSSILevel = nLevelEvdoDbm
    elif signal_type == 24 :  # "LTE"
        nLevelLTEDbm = 0
        if nSignalStrength >= -65: nLevelLTEDbm = 4
        elif nSignalStrength >= -75: nLevelLTEDbm = 3
        elif nSignalStrength >= -90: nLevelLTEDbm = 2
        elif nSignalStrength >= -105: nLevelLTEDbm = 1
        else: nLevelLTEDbm = 0
        nRSSILevel = nLevelLTEDbm

    return nRSSILevel


table_signal_level_info = 't309'
f00n_signal_level_info = "f002 ,f003, f004"
fields_cdma_level_info = ["timestamp", "cdma_level", "cdma_signalstrength" ]
fields_evdo_level_info = ["timestamp", "evdo_level", "evdo_signalstrength"]
fields_gsm_level_info = ["timestamp", "gsm_level", "gsm_signalstrength"]
fields_lte_level_info = ["timestamp", "lte_level", "lte_signalstrength"]


def get_signal_level_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ):
    querysignalstrength = "select %s  from %s " % (f00n_signal_level_info, table_signal_level_info )
    querysignalstrength += querywhere
    cur.execute(querysignalstrength)
    listtuplesignalstrength = cur.fetchall()


    SIGNAL_CDMA = 21
    SIGNAL_EVDO = 22
    SIGNAL_GSM = 23
    SIGNAL_LTE = 24

    for tuplesignalstrength in listtuplesignalstrength :
        timestamp, signaltype, signalstrength = tuplesignalstrength
        if not signaltype in [ SIGNAL_CDMA, SIGNAL_EVDO, SIGNAL_GSM, SIGNAL_LTE ] :
            continue
        signallevel = CalcRSSILevel(signaltype, signalstrength )
        if signaltype == SIGNAL_CDMA :
            dicttemp = dict(zip(fields_cdma_level_info, (timestamp, signallevel, signalstrength )))
        elif signaltype == SIGNAL_EVDO :
            dicttemp = dict(zip(fields_evdo_level_info, (timestamp, signallevel , signalstrength )))
        elif signaltype == SIGNAL_GSM :
            dicttemp = dict(zip(fields_gsm_level_info, (timestamp, signallevel , signalstrength )))
        elif signaltype == SIGNAL_LTE :
            dicttemp = dict(zip(fields_lte_level_info, (timestamp, signallevel , signalstrength )))

        listdictDBDump.append( dicttemp )



table_telephony_info = 't310'
f00n_telephony_info = "f002 ,f003, f004"
fields_telephony_state_info = ["timestamp", "telephony_state"]
fields_datacomm_state_info = ["timestamp", "datacomm_state"]
fields_callcomm_state_info = ["timestamp", "callcomm_state"]


def get_telephony_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ):

    querytelephony = "select %s from %s " % (f00n_telephony_info, table_telephony_info )
    querytelephony += querywhere
    cur.execute( querytelephony )
    listtupleTelePhonyInfos = cur.fetchall()

    dictServiceState = { 0:"STATE_IN_SERVICE", 1:"STATE_OUT_OF_SERVICE", 2:"STATE_EMERGENCY_ONLY", 3:"STATE_POWER_OFF" }
    dictDataCommState = { 0:"DATA_DISCONNECTED", 1:"DATA_CONNECTING", 2:"DATA_CONNECTED", 3:"DATA_SUSPENDED" }
    dictCallState  = { 0:"CALL_STATE_IDLE", 1:"CALL_STATE_RINGING", 2:"CALL_STATE_OFFHOOK" }

    SERVICE_STATE = 31
    DATA_STATE = 32
    CALL_STATE = 33

    for tupleTelePhonyInfos in listtupleTelePhonyInfos :
        timestamp, statetype, statevalue = tupleTelePhonyInfos
        if statevalue == -1 :
            continue
        if not statetype in [ SERVICE_STATE, DATA_STATE, CALL_STATE] :
            continue

        if statetype == SERVICE_STATE :
            statevalue = dictServiceState[statevalue]
            dicttemp = dict(zip(fields_telephony_state_info, (timestamp, statevalue )))
        elif statetype == DATA_STATE :
            statevalue = dictDataCommState[statevalue]
            dicttemp = dict(zip(fields_datacomm_state_info, (timestamp, statevalue )))
        elif statetype == CALL_STATE :
            statevalue = dictCallState[statevalue]
            dicttemp = dict(zip(fields_callcomm_state_info, (timestamp, statevalue )))

        listdictDBDump.append( dicttemp )


table_cdmacell_info = 't311'
f00n_cdmacell_info = "f002 ,f003, f004, f005, f006, f007 "
fields_cdmacell_info = ["timestamp", "cdma_bsid", "cdma_bslat", "cdma_bslong", "cdma_nid", "cdma_sid"]
def get_cdmacell_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ):
    querycdmacell = "select %s from %s " % (f00n_cdmacell_info, table_cdmacell_info )
    querycdmacell += querywhere
    cur.execute( querycdmacell )
    listtupleCDMACellInfos = cur.fetchall()

    for tupleCDMACellInfos in listtupleCDMACellInfos :
        dicttemp = dict(zip(fields_cdmacell_info, tupleCDMACellInfos))
        listdictDBDump.append( dicttemp )


table_gsmcell_info = 't312'
f00n_gsmcell_info = "f002 ,f003, f004, f005 "
fields_gsmcell_info = ["timestamp", "gsm_cid", "gsm_lac", "gsm_psc"]
def get_gsmcell_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ):

    querygsmcell = "select %s from %s " % (f00n_gsmcell_info, table_gsmcell_info )
    querygsmcell += querywhere
    cur.execute( querygsmcell )
    listtupleGSMCellInfos = cur.fetchall()

    for tupleGSMCellInfos in listtupleGSMCellInfos :
        dicttemp = dict(zip(fields_gsmcell_info, tupleGSMCellInfos))
        listdictDBDump.append( dicttemp )




table_connectivity_info = 't313'
f00n_connectivity_info = "f002 ,f003, f004"
fields_earjack_state = ["timestamp", "earjack_state"]
fields_gps_state = ["timestamp", "gps_state"]
fields_gpsstatus_state = ["timestamp", "gpsstatus_state"]
fields_usbta_state = ["timestamp", "usbta_state"]
fields_ums_state = ["timestamp", "ums_state"]


def get_connectivity_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ):

    queryconnectivity = "select %s from %s " % (f00n_connectivity_info, table_connectivity_info )
    queryconnectivity += querywhere
    cur.execute( queryconnectivity )
    listtupleConnectivityInfos = cur.fetchall()

    EARJACK_TYPE = 21
    GPS_TYPE = 41
    GPSSTATUS_TYPE = 42
    USBTA_TYPE = 51
    UMS_TYPE = 61

    dictEarJackState = { -1:"EARJACK_STATE_UNKNOWN", 0:"EARJACK_STATE_UNPLUGGED", 1:"EARJACK_STATE_PLUGGED" }
    dictGPSState = { 0:"GPS_STATUS_UNKNOWN", 1:"GPS_STATUS_STARTED", 2:"GPS_STATUS_STOPPED" }

    dictGPSStatusState  = { 1:"GPS_EVENT_STARTED", 2:"GPS_EVENT_STOPPED", 3:"GPS_EVENT_FIRST_FIX", 4:"GPS_EVENT_SATELLITE_STATUS", 5:"GPS_FIX_CHANGED" }
    dictUSBTAState  = { 0 :"BATTERY_PLUGGED_NONE", 1:"BATTERY_PLUGGED_AC", 2:"BATTERY_PLUGGED_USB" }
    dictUMSState  = {  1:"UMS_ON", 2:"UMS_OFF" }

    for tupleConnectivityInfos in listtupleConnectivityInfos :
        timestamp, statetype, statevalue = tupleConnectivityInfos
        if not statetype in [EARJACK_TYPE, GPS_TYPE, GPSSTATUS_TYPE, USBTA_TYPE, UMS_TYPE ] :
            continue

        if statetype == EARJACK_TYPE :
            statevalue = dictEarJackState[statevalue]
            dicttemp = dict(zip(fields_earjack_state, (timestamp, statevalue )))
        elif statetype == GPS_TYPE :
            statevalue = dictGPSState[statevalue]
            dicttemp = dict(zip(fields_gps_state, (timestamp, statevalue )))
        elif statetype == GPSSTATUS_TYPE :
            statevalue = dictGPSStatusState[statevalue]
            dicttemp = dict(zip(fields_gpsstatus_state, (timestamp, statevalue )))
        elif statetype == USBTA_TYPE :
            statevalue = dictUSBTAState[statevalue]
            dicttemp = dict(zip(fields_usbta_state, (timestamp, statevalue )))
        elif statetype == UMS_TYPE :
            statevalue = dictUMSState[statevalue]
            dicttemp = dict(zip(fields_ums_state, (timestamp, statevalue )))

        listdictDBDump.append( dicttemp )



table_bluetooth_info = 't317'
f00n_bluetooth_info = "f002 ,f003, f004"
fields_bt_adapter_state = ["timestamp", "bt_adapter_state"]
fields_bt_headset_state = ["timestamp", "bt_headset_state"]
fields_bt_a2dp_state = ["timestamp", "bt_a2dp_state"]
fields_bt_pbap_state = ["timestamp", "bt_pbap_state"]
fields_bt_device_state = ["timestamp", "bt_device_state"]
fields_bt_bond_state = ["timestamp", "bt_bond_state"]


def get_bluetooth_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ):

    querybluetooth = "select %s from %s " % (f00n_bluetooth_info, table_bluetooth_info )
    querybluetooth += querywhere
    cur.execute( querybluetooth )
    listtupleBluetoothInfos = cur.fetchall()

    BT_ADAPTER_TYPE = 11
    BT_HEADSET_TYPE = 12
    BT_A2DP_TYPE = 13
    BT_PBAP_TYPE = 14
    BT_DEVICE_TYPE = 15
    BT_BOND_TYPE = 16

    dictAdapterState = { -1:"STATE_UNKNOWN",  10:"STATE_OFF", 11:"STATE_TURNING_ON", 12:"STATE_ON", 13:"STATE_TURNING_OFF" }
    dictHeadsetState = { -1:"BT_STATE_ERROR", 0:"BT_STATE_DISCONNECTED", 1:"BT_STATE_CONNECTING", 2:"BT_STATE_CONNECTED" }
    dictA2DPState = { -1:"BT_STATE_ERROR", 0:"BT_STATE_DISCONNECTED", 1:"BT_STATE_CONNECTING", 2:"BT_STATE_CONNECTED", 3:"BT_STATE_DISCONNECTING", 4:"BT_STATE_PLAYING" }
    dictPBAPState = { -1:"BT_STATE_ERROR", 0:"BT_STATE_DISCONNECTED", 1:"BT_STATE_CONNECTING", 2:"BT_STATE_CONNECTED" }
    dictDeviceState = { 5:"BT_STATE_ACL_CONNECTED", 6:"BT_STATE_ACL_DISCONNECTED", 7:"BT_STATE_ACL_DISCONNECT_REQUESTED" }
    dictBondState = { -1:"BT_BOND_STATE_UNKNOWN", 10:"BT_BOND_STATE_NONE", 11:"BT_BOND_STATE_BONDING", 12:"BT_BOND_STATE_BONDED" }


    for tupleBluetoothInfos in listtupleBluetoothInfos :
        timestamp, statetype, statevalue = tupleBluetoothInfos

        if not statetype in [BT_ADAPTER_TYPE, BT_HEADSET_TYPE, BT_A2DP_TYPE, BT_PBAP_TYPE, BT_DEVICE_TYPE,BT_BOND_TYPE  ] :
            continue

        if statetype == BT_ADAPTER_TYPE :
            statevalue = dictAdapterState[statevalue]
            dicttemp = dict(zip(fields_bt_adapter_state, (timestamp, statevalue )))
        elif statetype == BT_HEADSET_TYPE :
            statevalue = dictHeadsetState[statevalue]
            dicttemp = dict(zip(fields_bt_headset_state, (timestamp, statevalue )))
        elif statetype == BT_A2DP_TYPE :
            statevalue = dictA2DPState[statevalue]
            dicttemp = dict(zip(fields_bt_a2dp_state, (timestamp, statevalue )))
        elif statetype == BT_PBAP_TYPE :
            statevalue = dictPBAPState[statevalue]
            dicttemp = dict(zip(fields_bt_pbap_state, (timestamp, statevalue )))
        elif statetype == BT_DEVICE_TYPE :
            statevalue = dictDeviceState[statevalue]
            dicttemp = dict(zip(fields_bt_device_state, (timestamp, statevalue )))
        elif statetype == BT_BOND_TYPE :
            statevalue = dictBondState[statevalue]
            dicttemp = dict(zip(fields_bt_bond_state, (timestamp, statevalue )))

        listdictDBDump.append( dicttemp )


table_wifi_info = 't318'
f00n_wifi_info = "f002 ,f003, f004"
fields_wifi_state = ["timestamp", "wifi_state"]
fields_wifinetwork_state = ["timestamp", "wifinetwork_state"]

def get_wifi_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ):

    querywifi = "select %s from %s " % (f00n_wifi_info, table_wifi_info )
    querywifi += querywhere
    cur.execute( querywifi )
    listtupleWIFIInfos = cur.fetchall()

    WIFISTATE_TYPE = 31
    WIFINETWORK_TYPE = 32

    dictWIFIState = { -1:"WI_UNKNOWN", 0:"WI_DISABLING", 1:"WI_DISABLED", 2:"WI_ENABLING", 3:"WI_ENABLED", 4:"WI_FAILED" }
    dictWIFINetworkState = { -1:"WINET_UNKNOWN", 0:"WINET_DISABLING", 1:"WINET_DISABLED", 2:"WINET_ENABLING", 3:"WINET_ENABLED", 4:"WINET_FAILED" }


    for tupleWIFIInfos in listtupleWIFIInfos :
        timestamp, statetype, statevalue = tupleWIFIInfos

        if not statetype in [WIFISTATE_TYPE, WIFINETWORK_TYPE] :
            continue

        if statetype == WIFISTATE_TYPE :
            statevalue = dictWIFIState[statevalue]
            dicttemp = dict(zip(fields_wifi_state, (timestamp, statevalue )))
        elif statetype == WIFINETWORK_TYPE :
            statevalue = dictWIFINetworkState[statevalue]
            dicttemp = dict(zip(fields_wifinetwork_state, (timestamp, statevalue )))

        listdictDBDump.append( dicttemp )

table_power_info = 't314'
f00n_power_info = "f002 ,f003"
fields_power_info = ["timestamp", "power_state"]

def get_power_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ):

    querypower = "select %s from %s " % (f00n_power_info, table_power_info )
    querypower += querywhere
    cur.execute( querypower )
    listtuplePowerInfos = cur.fetchall()

    for tuplePowerInfos in listtuplePowerInfos :
        timestamp ,  statetype = tuplePowerInfos
        if statetype == 51 :
            POWER_STATE = "POWER_ON"
        elif statetype == 52 :
            POWER_STATE = "POWER_OFF"
        elif statetype == 53 :
            POWER_STATE = "RESTART_MPT"

        dicttemp = dict(zip(fields_power_info, (timestamp, POWER_STATE )))
        listdictDBDump.append( dicttemp )



table_lcd_info = 't315'
f00n_lcd_info = "f002 ,f003"
fields_lcd_info = ["timestamp", "lcd_state"]

def get_lcd_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ):

    querylcd = "select %s from %s " % (f00n_lcd_info, table_lcd_info )
    querylcd += querywhere
    cur.execute( querylcd )
    listtupleLCDInfos = cur.fetchall()

    for tupleLCDInfos in listtupleLCDInfos :
        timestamp ,  statetype = tupleLCDInfos
        if statetype == 61 :
            LCD_STATE = "LCD_ON"
        elif statetype == 62 :
            LCD_STATE = "LCD_OFF"

        dicttemp = dict(zip(fields_lcd_info, (timestamp, LCD_STATE )))
        listdictDBDump.append( dicttemp )


table_resource_info = 't316'
f00n_resource_info = "f002 ,f003, f004"
fields_resource_info = ["timestamp", "cpu_usage", "avail_ram"]

def get_resource_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ):

    queryresource = "select %s from %s " % (f00n_resource_info, table_resource_info )
    queryresource += querywhere
    cur.execute(queryresource )
    listtupleResourceInfos = cur.fetchall()

    for tupleResourceInfos in listtupleResourceInfos :
        timestamp, cpu_usage, avail_ram = tupleResourceInfos

        dicttemp = dict(zip(fields_resource_info, (timestamp, cpu_usage, avail_ram )))
        listdictDBDump.append( dicttemp )


table_recentAct_info = 't325'
f00n_recentAct_info = "f002 ,f003"
fields_recentAct_info = ["timestamp", "recentpackage_names"]

def get_recentAct_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ):

    queryrecent = "select %s from %s " % (f00n_recentAct_info, table_recentAct_info )
    queryrecent += querywhere
    cur.execute(queryrecent)
    listtuplerecent = cur.fetchall()

    for tuplerecent in listtuplerecent :
        timestamp, package_names = tuplerecent

        dicttemp = dict(zip(fields_recentAct_info, (timestamp, package_names)))
        listdictDBDump.append( dicttemp )


table_external_media_info = 't326'
f00n_external_media_info = "f002 ,f003"
fields_external_media_info = ["timestamp", "externalmedia_state"]

def get_External_Media_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ) :

    queryExternal = "select %s  from %s " % (f00n_external_media_info, table_external_media_info )
    queryExternal += querywhere
    cur.execute(queryExternal)
    listtupleExternal = cur.fetchall()

    dictstate = { 1:"BAD_REMOVAL", 2:"NOFS", 3:"SHARED", 4:"UNMOUNTABLE", 5:"SCAN_STARTED" , 6:"SCAN_FINISHED"}

    for tupleExternal in listtupleExternal :
        timestamp, externalmedia_state = tupleExternal
        if not externalmedia_state in [ 1, 2, 3, 4, 5, 6 ] :
            continue
        externalmedia_state = dictstate[externalmedia_state]

        dicttemp = dict(zip(fields_external_media_info, (timestamp, externalmedia_state)))
        listdictDBDump.append( dicttemp )

table_data_act_info = 't327'
f00n_data_act_info = "f002 ,f003, f004"
fields_data_act_info = ["timestamp", "dataact_state"]

def get_data_activity_info(listdictDBDump, listdictBasicSWVer, cur,querywhere ):

    querydataact = "select %s  from %s " % (f00n_data_act_info, table_data_act_info )
    querydataact += querywhere
    cur.execute(querydataact)
    listtupledataact = cur.fetchall()

    DATA_NONE = 0
    DATA_IN = 1
    DATA_OUT = 2
    DATA_INOUT = 3
    DATA_DORMANT = 4

    dictstate = {DATA_NONE:"DATA_NONE", DATA_IN:"DATA_IN", DATA_OUT:"DATA_OUT", DATA_INOUT:"DATA_INOUT", DATA_DORMANT:"DATA_DORMANT" }

    for tupledataact in listtupledataact :
        timestamp, statetype, statevalue = tupledataact

        if not statevalue in [ DATA_NONE, DATA_IN, DATA_OUT, DATA_INOUT, DATA_DORMANT ] :
            continue
        statevalue = dictstate[statevalue]

        dicttemp = dict(zip(fields_data_act_info, (timestamp, statevalue)))
        listdictDBDump.append( dicttemp )


fields_basic_swver = ["timestamp","os_ver", "register_svwer", "phone_type", "network_type", "IMEI"]

table_basic_info = 't301'
fields_basic_info =["basic_timestamp", "IMEI", "serial_no", "os_ver", "hw_ver", "last_sw_ver", "model_name", "build_no", "registration_timestamp", "phone_type", "network_type","mpt_version"]
f00n_basic_info = "f002, f003, f006, f007, f008, f009, f010, f011, f013, f014, f015, f021 "
dict_network_type = {0:"NETWORK_TYPE_UNKNOWN",1:"NETWORK_TYPE_GPRS",2:"NETWORK_TYPE_EDGE",3:"NETWORK_TYPE_UMTS",4:"NETWORK_TYPE_CDMA",5:"NETWORK_TYPE_EVDO_0",6:"NETWORK_TYPE_EVDO_A",7:"NETWORK_TYPE_1xRTT",8:"NETWORK_TYPE_HSDPA",9:"NETWORK_TYPE_HSUPA",10:"NETWORK_TYPE_HSPA",11:"NETWORK_TYPE_IDEN",12:"NETWORK_TYPE_EVDO_B",13:"NETWORK_TYPE_LTE",14:"NETWORK_TYPE_EHRPD" }
dict_phone_type = { 0:None, 1:"GSM", 2:"CDMA", 3:"SIP" }
def get_basic_info(listdictDBDump, listdictBasicSWVer, cur, querywhere ) :

    query_basic_info = "SELECT %s from %s order by f002 asc " % (f00n_basic_info, table_basic_info )
    cur.execute(query_basic_info)
    listtupleBasicInfo = cur.fetchall()

    for tupleBasicInfo in listtupleBasicInfo :
        dicttempBasicInfo = dict(zip (fields_basic_info, tupleBasicInfo ))
        if dicttempBasicInfo["registration_timestamp"] == None :
            continue
        dicttempBasicSWVer = {}
        dicttempBasicSWVer["timestamp"]  = dicttempBasicInfo["basic_timestamp"]
        dicttempBasicSWVer["register_svwer"]  = dicttempBasicInfo["last_sw_ver"]
        dicttempBasicSWVer["os_ver"]  = dicttempBasicInfo["os_ver"]
        dicttempBasicSWVer["model_name"]  = dicttempBasicInfo["model_name"]

        dicttempBasicSWVer["phone_type"] = dict_phone_type.get(dicttempBasicInfo["phone_type"], None)
        dicttempBasicSWVer["network_type"] = dict_network_type.get(dicttempBasicInfo["network_type"], None)
        if (len(dicttempBasicInfo["IMEI"]) > 20 ) and ( len(dicttempBasicInfo["IMEI"]) % 4  == 0 ) :
            dicttempBasicSWVer["IMEI"] = DecryptIMSICode(dicttempBasicInfo["IMEI"]).strip()
        else :
            dicttempBasicSWVer["IMEI"] = dicttempBasicInfo["IMEI"]
        listdictBasicSWVer.append( dicttempBasicSWVer )
        listdictDBDump.append( dicttempBasicSWVer )


    if len(listdictBasicSWVer) == 0 :
        dicttempBasicInfo = dict(zip (fields_basic_info, listtupleBasicInfo[-1] ))
        dicttempBasicSWVer = {}
        dicttempBasicSWVer["timestamp"]  = ConvertDateTimeToMiliSeconds(2011, 7, 1)
        dicttempBasicSWVer["register_svwer"]  = dicttempBasicInfo["last_sw_ver"]
        dicttempBasicSWVer["os_ver"]  = dicttempBasicInfo["os_ver"]
        dicttempBasicSWVer["model_name"]  = dicttempBasicInfo["model_name"]
        dicttempBasicSWVer["phone_type"] = dict_phone_type.get(dicttempBasicInfo["phone_type"], None)
        dicttempBasicSWVer["network_type"] = dict_network_type.get(dicttempBasicInfo["network_type"], None)
        dicttempBasicSWVer["IMEI"] = dicttempBasicInfo["IMEI"]

        listdictBasicSWVer.append( dicttempBasicSWVer )

    del dicttempBasicSWVer



delimitor = "@@"
def getStrExceptionCause( exceptiontype, strExceptionInfo, strException_lastk_log ) :

    if exceptiontype != "exception_Kernel_LastK" and (strExceptionInfo == None or len( strExceptionInfo ) == 0 ):
        return "unknown"
    elif exceptiontype == "exception_Kernel_LastK" and ( len(strException_lastk_log) == 0 ) :
        return "unknown"

    # exception_framework
    if exceptiontype == "exception_framework" :
        liststrret = strExceptionInfo.split(">>>")
        liststrret = liststrret[1].split("<<<")
        strret = liststrret[0].strip()
        if " " in strret :
            strret = "unknown"
        return strret

    # exception_app_fatal
    elif exceptiontype == "exception_app_fatal" :
        index = strExceptionInfo.find("FATAL EXCEPTION")
        if index >= 0 :
            strret = "unknown"
            try:
                strlist = strExceptionInfo.splitlines()
                strret = strlist[1].split(":")[0].strip()
                
            except:
                pass
            return redeci.sub('', strret)
        else:
            return "unknown"

    # exception_anr
    elif exceptiontype == "exception_anr" :
        index = strExceptionInfo.find("ANR in ")
        if index >= 0   :
            strret = "unknown"
            try:
                strret =  delimitor.join(strExceptionInfo.splitlines()[:2] )
            except:
                pass
            return strret
        else:
            return "unknown"

    # exception_calldrop
    elif exceptiontype == "exception_calldrop" :
        strret = ""
        strExceptionInfo = strExceptionInfo.lower()
        if strExceptionInfo.find("calldrop reason") == -1  :
            liststrCalldrop = DecryptIMSICode( strExceptionInfo ).strip().split(";")
            listret = []
            try :
                strret += "Calldrop Reason : " + liststrCalldrop[0]

                if liststrCalldrop[1] == "1" :
                    strret += ",Incoming Call"
                else :
                    strret += ",Outgoing Call"

                listret.append(strret)

                if liststrCalldrop[2] == "2" :
                    strret = "Provider : Passive"
                elif liststrCalldrop[2] == "1" :
                    strret = "Provider : Network"
                elif liststrCalldrop[2] == "0" :
                    strret = "Provider : GPS"
                else:
                    strret = "Provider : None"

                listret.append(strret)

                listret.append("Latitue :" + liststrCalldrop[3] )
                listret.append("Longtitude :" + liststrCalldrop[4] )

            except:
                pass

            return delimitor.join(listret )
        else :
            liststrCalldrop = strExceptionInfo.lower().strip().splitlines()
            listret = []
            try :
                listret.append(liststrCalldrop[0].strip())
                listret.append(liststrCalldrop[1].strip())
                listret.append(liststrCalldrop[5].strip())
                listret.append(liststrCalldrop[6].strip())
                listret.append(liststrCalldrop[7].strip())
            except:
                pass
            return delimitor.join( listret )


    # exception_Kernel_LastK
    elif exceptiontype == "exception_Kernel_LastK" :
        liststr_lastk_log = strException_lastk_log.splitlines()

        liststrneg = [ "except", " fail", " cannot", " error ", "could not", " denied", " collapse", "fatal", "severe" ]
        listret = []
        try:
            for str_lastk_log in liststr_lastk_log:
                strlast = str_lastk_log.lower()
                for strneg in liststrneg :
                    if  (strneg in strlast) and ("no errors" not in  strlast):
                        strtemp = ("".join(strlast.split("]")[1:])).strip()
                        # replace a number with dot.
                        strtemp = resymbol2.sub(' ', redeci.sub(' ', rehexa1.sub(' ', rehexa.sub(' ', resymbol1.sub('  ',strtemp )))))
                        listret.append(strtemp.strip())

        except:
            pass
        return delimitor.join(listret )

    else:
        return "unknown"

def getDictExceptionCause (exceptiontype, exceptionstr ):
    if len(exceptionstr) == 0 :
        return {"except_causecount":0 }
    dicttemp = {}
    index = 0
    try:
        if exceptiontype == "exception_calldrop" :
            for cause in exceptionstr.split(delimitor):
                dicttemp["except_cause%s"%(index)] = cause
                index += 1
        elif exceptiontype == "exception_anr" :
            for cause in exceptionstr.split(delimitor):
                dicttemp["except_cause%s"%(index)] = cause
                index += 1
        elif exceptiontype == "exception_app_fatal" :
            for cause in exceptionstr.split(delimitor):
                dicttemp["except_cause%s"%(index)] = cause
                index += 1
        elif exceptiontype == "exception_framework" :
            dicttemp["except_cause0"] = exceptionstr

        elif exceptiontype == "exception_Kernel_LastK" :
            ret = {}
            for cause in exceptionstr.split(delimitor):
                ret.setdefault(cause, []).append(1)

            for key in ret.keys():
                ret[key] = ret[key].count(1)

            k = ret.keys()
            v = ret.values()
            s = sorted(zip(v, k), reverse = True )

            for count, cause in s :
                dicttemp["except_cause%s"%(index)] = cause
                index += 1
                if index == 10 :
                    break

        else:
            pass
    except:
        pass
    
    dicttemp["except_causecount"] = len(dicttemp)
    return dicttemp

def getStrRilCause(ril_log):
    liststr_ril_log = ril_log.splitlines()

    liststrneg = ["except", " fail", " cannot", "error", "could not", " denied", "collapse", "fatal", "severe", u"등록이 필요합니다", u"서비스 안됨" ]
    listret = []
    try:
        for str_ril_log in liststr_ril_log:
            strril = str_ril_log.lower()
            for strneg in liststrneg :
                if strneg in strril :
                    # replace a number with dot.
                    #cause = resymbol2.sub('.', resymbol1.sub('.', redeci.sub('.', strril.split("): ")[1]  )))
                    cause = resymbol2.sub(' ', redeci.sub(' ', rehexa1.sub(' ', rehexa.sub(' ', resymbol1.sub('  ',strril.split("): ")[1] )))))
                    listret.append(cause.strip())
    except:
        pass
    
    return delimitor.join(listret )
    
def getDictRilCause(ril_log): 
    if len(ril_log) == 0 :
        return {"ril_causecount":0}
        
    dicttemp = {}
    index = 0
    try:
        ret = {}
        for cause in ril_log.split(delimitor):
            ret.setdefault(cause, []).append(1)

        for key in ret.keys():
            ret[key] = ret[key].count(1)

        k = ret.keys()
        v = ret.values()
        s = sorted(zip(v, k), reverse = True )

        for count, cause in s :
            dicttemp["ril_cause%s"%(index)] = cause
            index += 1
            if index == 10 :
                break
    except:
        pass
    dicttemp["ril_causecount"] = len(dicttemp)
    return dicttemp
    
    

table_exception_blobs = 't320'
f00n_exception_blobs = "f002 ,f007, f003, f013, f006"
fields_exception_blobs = [ "timestamp", "exception_type", "exception_cause", "exception_swver",  "ril_log"]
dict_exception_type = { 1:"exception_cp", 2:"exception_kernel", 3:"exception_framework", 4:"exception_app_fatal", 5:"exception_app_reset", 6:"exception_lockup", 7:"exception_anr",8:"exception_calldrop",13:"exception_Kernel_LastK" }

def getListDictException(listdictDBDump, listdictBasicSWVer, cur, querywhere ) :

    if len(listdictBasicSWVer) == 0 :
        print "Please call the get_basic_info first to make the listdictBasicSWVer , and  processing exits "
        exit()

    query_exception_blobs = "SELECT %s from %s " % (f00n_exception_blobs, table_exception_blobs )
    query_exception_blobs += querywhere
    cur.execute(query_exception_blobs)
    listtupleExceptionBlobs = cur.fetchall()

    for tupleExceptionBlob in listtupleExceptionBlobs:
        timestamp, exceptiontype, exception_data, exception_lastk_log, ril_log = tupleExceptionBlob

        ## skip the lock-up exception info. because that lock-up info is recoded after reboot due to not recording during locking-up.
        if exceptiontype == 6 :
            continue

        exceptiontype = dict_exception_type[ exceptiontype]
        exception_cause = getStrExceptionCause( exceptiontype, exception_data, exception_lastk_log )
        
        if (exceptiontype == "exception_calldrop") and (len(ril_log) > 0) : 
            #ril_log = getStrRilCause(ril_log)
            pass
        else:
            ril_log = ""


        ## find the exception SW ver
        exception_swver = ""
        for dictBasicSWVer in listdictBasicSWVer :
            if dictBasicSWVer["timestamp"]  <= timestamp :
                exception_swver = dictBasicSWVer["register_svwer"]

        dicttemp = dict(zip (fields_exception_blobs, (timestamp, exceptiontype, exception_cause, exception_swver, ril_log) ))
        listdictDBDump.append( dicttemp )

def get_count_byExceptiontype( cur, exceptiontype ) :
    for key in dict_exception_type.keys() :
        if dict_exception_type[key] == exceptiontype :
            break
    query_count_execption = "SELECT count(*) from t320 where f007 = %s " % (key )
    cur.execute(query_count_execption)
    count = cur.fetchall()

    return count[0][0]



f008_exception_blobs = "f002 ,f003,  f006, f007, f011, f013"
fields_exception_allblobs = [ "timestamp", "exception_data", "ril_log","exception_type", "traces_log", "lastk_log" ]
def getListDictExceptionInfoRaw(cur, querywhere):
    listdictDBDump = []
    try:
        query_exception_blobs = "SELECT %s from %s " % (f008_exception_blobs, table_exception_blobs )
        query_exception_blobs += querywhere
        cur.execute(query_exception_blobs)
        listtupleExceptionBlobs = cur.fetchall()

        for tupleExceptionBlob in listtupleExceptionBlobs:
            dicttemp = dict(zip (fields_exception_allblobs,tupleExceptionBlob))
            dicttemp["exception_type"] = dict_exception_type[ dicttemp["exception_type"]]
            listdictDBDump.append( dicttemp )
    except Exception :
        pass

    return listdictDBDump





#f008_exception_blobs = "f002 ,f003, f004, f005, f006, f007, f008, f009, f010, f011, f012, f013"
#fields_exception_allblobs = [ "timestamp", "exception_data", "blob_data", "blob_data2", "ril_log","exception_type", "file_size", "file_size2", "ril_size", "traces_log", "traces_size", "last-k_log" ]
#def getListDictExceptionInfoRaw(listdictDBDump, cur, querywhere):
#    query_exception_blobs = "SELECT %s from %s " % (f008_exception_blobs, table_exception_blobs )
#    query_exception_blobs += querywhere
#    cur.execute(query_exception_blobs)
#    listtupleExceptionBlobs = cur.fetchall()
#
#    blob_name = "blob"
#    blob2_name = "blob2"
#    index = 0
#    for tupleExceptionBlob in listtupleExceptionBlobs:
#        dicttemp = dict(zip (fields_exception_allblobs,tupleExceptionBlob))
#        dicttemp["exception_type"] = dict_exception_type[ dicttemp["exception_type"]]
#
#        tempblob_name = blob_name + str(index) + ".db"
#        tempblob2_name = blob2_name + str(index) + ".db"
#
#        with open(tempblob_name, 'wb') as dbFile:
#            dbFile.write(dicttemp["blob_data"])
#            dbFile.close()
#
#        with open(tempblob2_name, 'wb') as dbFile2:
#            dbFile2.write(dicttemp["blob_data2"])
#            dbFile2.close()
#
#        listdictDBDump.append( dicttemp )
#

table_AppAccum_info = "t305"
f00n_AppAccum_info = "f003, f004, f005"     # packagename, total_time_ms, total_run_count
def get_App_Accumulation (cur, dicttupleappaccum) :
    query_app_accum = "select %s from %s" % (f00n_AppAccum_info,table_AppAccum_info  )
    cur.execute(query_app_accum)
    listtupleAppAccum = cur.fetchall()

    for tupleAppAccum in listtupleAppAccum :
        packagename, total_time_ms, total_run_count = tupleAppAccum
        sum_app_count, sum_total_time , sum_total_run_count  = dicttupleappaccum.get( packagename, (0,0,0))
        sum_app_count += 1
        sum_total_time += total_time_ms / 1000
        sum_total_run_count += total_run_count
        dicttupleappaccum[ packagename ] = (sum_app_count, sum_total_time, sum_total_run_count)





table_app_history = 't304'
f00n_app_history = "f002 ,f003, f004, f005, f006"
#fields_app_history = [ "timestamp", "managed_app_name", "timestamp_install", "timestamp_delete", "last_version"]
fields_app_history = [ "timestamp", "app_name_install", "app_name_delete" ]

def get_app_history_info(listdictDBDump, listdictBasicSWVer, cur, querywhere ) :

    query_app_history = "SELECT %s from %s " % (f00n_app_history, table_app_history )
    #query_app_history += querywhere
    cur.execute(query_app_history)
    listtupleapphistory = cur.fetchall()

    for tupleapphistory in listtupleapphistory :
        timestamp, app_name, timestamp_install, timestamp_delete, last_version = tupleapphistory
        if timestamp_install != None and timestamp_install != 0 :
            dicttemp = dict(zip (fields_app_history, (timestamp_install, app_name, "") ))
            listdictDBDump.append( dicttemp )

        if timestamp_delete != None and timestamp_delete != 0 :
            dicttemp = dict(zip (fields_app_history, (timestamp_delete, "", app_name) ))
            listdictDBDump.append( dicttemp )


table_rooting = 't303'
f00n_rooting = "f002 ,f003"
fields_rooting = [ "timestamp", "rootingapp_name"]

def get_rooting(listdictDBDump, listdictBasicSWVer, cur, querywhere ) :

    query_rooting = "SELECT %s from %s " % (f00n_rooting, table_rooting )
    query_rooting += querywhere
    cur.execute(query_rooting)
    listtuplerooting = cur.fetchall()

    for tuplerooting in listtuplerooting :
        dicttemp = dict(zip (fields_rooting, tuplerooting ))
        listdictDBDump.append( dicttemp )


## determine if the lock-up is happpened .
## condition : power-on/off is not paired .  that is , power-on is marked as log,  power-off is not marked as log.
##           : the battery level is  less than  20% , this is to determine if battery is enforecd to be taken-off .
def searchaddlockup( listdictDBDump, listdictBasicSWVer, cur, querywhere ):


    listdictDBDump.sort(cmp = TimeStampCmp, reverse=True )
    listdicttemp = []

    PowerOnState = 0
    powerOnBatteryLevel = 0
    powerOffBatteryLevel = 0
    powerOfftimestamp = 0


    powerTempBatteryLevel = 0


    for dictDBDump in listdictDBDump :
        battery_level = dictDBDump.get("battery_level", None)
        if battery_level != None :
            if PowerOnState == 0 :
                powerOnBatteryLevel = battery_level
            elif powerOffBatteryLevel == 0 :
                powerOffBatteryLevel = battery_level
            else:
                powerTempBatteryLevel = battery_level

            continue

        power_state = dictDBDump.get("power_state", None)

        if power_state == None :
            if PowerOnState == 1 and powerOfftimestamp == 0 :
                powerOfftimestamp = dictDBDump.get("timestamp", None)
            continue

        if power_state == "RESTART_MPT" :
            continue

        if power_state == "POWER_ON" :
            # print "Power:On time is "  +  ConvertTimeStampToString(timestamp)
            if PowerOnState ==1 and powerOffBatteryLevel != 0 :
                # two  power-on without power-off
                # print " powerOnBatteryLevel: " +  str(powerOnBatteryLevel)
                # print " powerOffBatteryLevel: " +  str(powerOffBatteryLevel)
                if (powerOnBatteryLevel - powerOffBatteryLevel) < 20 :
                    dicttemp = {}
                    dicttemp["timestamp"] = powerOfftimestamp
                    dicttemp["exception_type"] = "exception_lockup"
                    exception_swver = ""
                    for dictBasicSWVer in listdictBasicSWVer :
                        if dictBasicSWVer["timestamp"]  <= powerOfftimestamp :
                            exception_swver = dictBasicSWVer["register_svwer"]
                    dicttemp["exception_swver"] = exception_swver

                    listdicttemp.append(dicttemp)
                powerOnBatteryLevel = powerTempBatteryLevel

            PowerOnState = 1
            powerOffBatteryLevel = 0
            powerOfftimestamp = 0

            continue

        if PowerOnState == 1 :
            if  power_state == "POWER_OFF" :      # normal power off
                # print "Power:Off time is "  +  ConvertTimeStampToString(timestamp)
                PowerOnState = 0
                powerOnBatteryLevel = 0
                powerOffBatteryLevel = 0
                powerOfftimestamp = 0
                continue


    listdictDBDump += listdicttemp
    listdicttemp = []







def getlatesttimestampamongtable(cur) :
    TimeStampBase = ConvertDateTimeToMiliSeconds(2011, 7, 1)
    listtablename = [
        "t307", "t308", "t310", "t313", "t317", "t318", "t314",
        "t315", "t326", "t327", "t301", "t320" ]
    ## t303(rooting), t316(resource ) , t304(app_history)
    ## t309(acc_signal_strength), t325(acc_recent_activity) won't be checked because that these table is rapid burn out,
    ## their  start pointer of record is  updated to the latest time. that makes the view range of data short.

    querywhere = "select f002 from %s where f002 > %s order by f002 asc "
    timestamp = 0
    for tablename in listtablename :
        querytemp = querywhere % (tablename, TimeStampBase )
        cur.execute(querytemp)
        tupletimestamp = cur.fetchone()

        tablenameShort = tablename

        if tupletimestamp == None :
            continue

        if tupletimestamp[0] > timestamp :
            timestamp = tupletimestamp[0]

    print ">>>> Shortest table name : " , tablenameShort
    return timestamp


def buildupDBDumpSWver( listdictDBDump, listdictBasicSWVer, cur, querywhere ) :
    try:
        get_AppUsage_info( listdictDBDump, listdictBasicSWVer, cur, querywhere)
        get_battery_info( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        get_signal_level_info( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        get_telephony_info( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        get_cdmacell_info( listdictDBDump, listdictBasicSWVer, cur, querywhere)
        get_gsmcell_info( listdictDBDump, listdictBasicSWVer, cur, querywhere)

        get_connectivity_info( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        get_bluetooth_info( listdictDBDump, listdictBasicSWVer, cur, querywhere)

        get_wifi_info( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        get_power_info( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        get_lcd_info( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        get_resource_info( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        get_recentAct_info( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        get_External_Media_info( listdictDBDump, listdictBasicSWVer, cur, querywhere )

        get_data_activity_info( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        get_basic_info( listdictDBDump, listdictBasicSWVer, cur, querywhere)

        getListDictException( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        get_app_history_info( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        get_rooting( listdictDBDump, listdictBasicSWVer, cur, querywhere )

        ## do searching the exception "lock-up' after gathering of every infomation
        searchaddlockup( listdictDBDump, listdictBasicSWVer, cur, querywhere )
        listdictDBDump.sort(cmp = TimeStampCmp )
    except Exception:
        listdictDBDump =[]
        listdictBasicSWVer = []




class   ClassMLTDB :
    MLTDBFilename = ""
    conn = 0
    cur = 0
    boolTableValied = True
    timestampbeginpoint = 0
    def __init__( self, MLTDBFilename ) :
        self.MLTDBFilename = MLTDBFilename

        try:
            self.conn = sqlite3.connect(self.MLTDBFilename)
            self.cur = self.conn.cursor()

            ''' check if t320 table is exist, if then, keep processing.  '''
            if check_table_exception_blobs(self.cur) == False:
                print "!!!! No Exception Blobs, DB skip"
                self.boolTableValied = False

            ## get the latest timestamp among the start point of each table
            self.timestampbeginpoint = getlatesttimestampamongtable(self.cur)
        except :
            pass

    def __del___(self):
        if self.conn != 0:
            self.conn.close()

    def get_count_byExceptiontype( self, exception_name ):
        if self.cur != 0 :
            return get_count_byExceptiontype( self.cur, exception_name)
        else:
            return 0

    def get_listDBDump_ListSWVer (self, out_listdictDBDump, out_listdictBasicSWVer):
        if self.cur != 0 :
            querywhere = " where f002 >= %s " % ( self.timestampbeginpoint )
            buildupDBDumpSWver(out_listdictDBDump, out_listdictBasicSWVer, self.cur, querywhere )

    def getlistdictFromTableDuration( self, strtablename, timestampstart, timestampend ):
        listdictoutput = []
        if self.cur != 0 :
            querywhere = " where f002 >= %s and f002 < %s " % (timestampstart, timestampend )
            if strtablename == "cdma_cell_info" :
                get_cdmacell_info( listdictoutput, "", self.cur,querywhere )
            elif strtablename == "gsm_cell_info" :
                get_gsmcell_info( listdictoutput, "", self.cur,querywhere )
            elif strtablename == "recent_act_info" :
                get_recentAct_info( listdictoutput, "", self.cur,querywhere )

            listdictoutput.sort(cmp =TimeStampCmp )

        return listdictoutput


    def getListBasicInfo(self ):
        if self.cur != 0 :
            querywhere = " where f002 >= %s " % ( self.timestampbeginpoint )
            listdictDBDump = []
            listdictBasicSWVer = []
            get_basic_info( listdictDBDump, listdictBasicSWVer, self.cur, querywhere)
            return listdictBasicSWVer


    def getListDictExceptionInfoRaw(self ):
        if self.cur != 0 :
            querywhere = " where f002 >= %s " % ( self.timestampbeginpoint )
            return getListDictExceptionInfoRaw(self.cur, querywhere  )
            
    def getAppAccumulation ( self,dicttupleappaccum ):
        if self.cur != 0 :
            return get_App_Accumulation(self.cur, dicttupleappaccum )
        



class classCallDropDetail():

    def __init__( self ) :
        pass

    # reverse find from index in  listdictDBDump to determine if columnName have a value.
    #if then, return element of  listdictDBDump
    def rfindColumnValue(self,  index, listdictDBDump, columnName ) :
        while( index >= 0  ) :
            dictDBDump = listdictDBDump[index]
            if dictDBDump.get(columnName, None) != None:
                return dictDBDump
            else:
                index = index -1
        return {}

    def boolCellMovement(self, calltimestamp, classmltdb ) :
        boolmovement = 0
        calltime5minbefore = calltimestamp - ( 5 * 60 * 1000)
        calltime5minafter = calltimestamp + ( 5 * 60 * 1000)

        listdictlocgsm = classmltdb.getlistdictFromTableDuration("gsm_cell_info",calltime5minbefore, calltime5minafter )
        if len(listdictlocgsm) > 0 :
            for dictlocgsm in listdictlocgsm :
                prev_gsm_cid = dictlocgsm["gsm_cid"]
                prev_gsm_lac = dictlocgsm["gsm_lac"]
                if (prev_gsm_cid != -1 ) and (prev_gsm_lac != -1) :
                    break
            for dictlocgsm in listdictlocgsm :
                gsm_cid = dictlocgsm["gsm_cid"]
                gsm_lac = dictlocgsm["gsm_lac"]
                if (gsm_cid == -1 ) or (gsm_lac == -1) :
                    continue
                if ((prev_gsm_cid != gsm_cid)  or (prev_gsm_lac != gsm_lac)) :
                    boolmovement = 1
                    break
        del listdictlocgsm

        listdictloccdma = classmltdb.getlistdictFromTableDuration("cdma_cell_info",calltime5minbefore, calltime5minafter )
        if len(listdictloccdma) > 0 :
            for dictloccdma in listdictloccdma :
                prev_cdma_bslat = dictloccdma["cdma_bslat"]
                prev_cdma_bslong = dictloccdma["cdma_bslong"]
                if (prev_cdma_bslat != -1 ) and (prev_cdma_bslong != -1) :
                    break
            for dictloccdma in listdictloccdma :
                cdma_bslat = dictloccdma["cdma_bslat"]
                cdma_bslong = dictloccdma["cdma_bslong"]
                if (cdma_bslat == -1 ) or (cdma_bslong == -1) :
                    continue
                if ((prev_cdma_bslat != cdma_bslat)  or (prev_cdma_bslong != cdma_bslong)) :
                    boolmovement = 1
                    break
        del listdictloccdma

        return boolmovement

    def getAppBeforeCall(self, calltimestamp, classmltdb ) :
        calltime5minbefore = calltimestamp - ( 5 * 60 * 1000)
        stractivity = ""
        try:
            listdictapp = classmltdb.getlistdictFromTableDuration("recent_act_info",calltime5minbefore, calltimestamp )
            # use the last dict
            apps = listdictapp[-1]["recentpackage_names"]

            listrecentActivity = apps.split("\n")
            for recentActivity in listrecentActivity :
                stractivity = recentActivity
                recentpackage = recentActivity.split("/")[0]
                if recentpackage in [ "com.android.contacts" ,"com.android.phone", "com.lge.ltecall" ] :
                    continue
                else:
                    break
        except Exception :
            pass

        stractivity = stractivity.encode("utf-8")
        if len(stractivity) == 0 :
            stractivity = "none"
        del listdictapp
        return stractivity


    def getListDictCallDropDetail( self,  listdictDBDump, listdictBasicSWVer, classmltdb ):
        model_name = listdictBasicSWVer[-1]["model_name"]
        phone_type = listdictBasicSWVer[-1]["phone_type"]
        network_type = listdictBasicSWVer[-1]["network_type"]
        IMEI = listdictBasicSWVer[-1]["IMEI"]

        dictbase = {}
        dictbase.update([("model_name", model_name),("phone_type", phone_type),("network_type", network_type), ("IMEI", IMEI)])

        ret = []
        for index in range(len(listdictDBDump)) :
            dictDBDump = listdictDBDump[index]
            if dictDBDump.get("exception_type", None) == "exception_calldrop" :
                dicttemp = {}
                dicttemp.update( dictbase.copy())

                dicttemp["exception_type"] = "exception_calldrop"
                dicttemp["exception_cause"] = dictDBDump.get("exception_cause", "unknown" )
                dicttemp["ril_log"] = dictDBDump.get("ril_log", "unknown" )
                dicttemp["exception_swver"] = dictDBDump.get("exception_swver", "unknown" )

                dicttemp["timestamp"] = dictDBDump["timestamp"]
                calldatetime = dictDBDump["timestamp"]
                liststrtime = ConvertTimeStampToString(calldatetime).split()
                calldate = "".join( liststrtime[0].split("-"))
                calltime = "".join( liststrtime[1].split(":"))
                dicttemp["calldate"] = calldate
                dicttemp["calltime"] = calltime


                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "avail_ram" )
                dicttemp["avail_ram"] = dictDBDump.get("avail_ram", None)


                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "telephony_state" )
                dicttemp["telephony_datetime"] = dictDBDump.get("timestamp", -1)
                dicttemp["telphony_state"] = dictDBDump.get("telephony_state", "")

                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "gsm_level" )
                dicttemp["gsm_signal_datetime"] = dictDBDump.get("timestamp", -1)
                dicttemp["gsm_level"] = dictDBDump.get("gsm_level", -1)
                dicttemp["gsm_signalstrength"] = dictDBDump.get("gsm_signalstrength", -1)


                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "lte_level" )
                dicttemp["lte_signal_datetime"] = dictDBDump.get("timestamp", -1 )
                dicttemp["lte_level"] = dictDBDump.get("lte_level", -1 )
                dicttemp["lte_signalstrength"] = dictDBDump.get("lte_signalstrength", -1 )


                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "gsm_cid" )
                dicttemp["gsm_loc_datetime"] = dictDBDump.get("timestamp", -1 )
                dicttemp["gsm_cid"] = dictDBDump.get("gsm_cid", -1 )
                dicttemp["gsm_lac"] = dictDBDump.get("gsm_lac", -1 )
                dicttemp["gsm_psc"] = dictDBDump.get("gsm_psc", -1 )

                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "cdma_level" )
                dicttemp["cdma_signal_datetime"] = dictDBDump.get("timestamp", -1 )
                dicttemp["cdma_level"] = dictDBDump.get("cdma_level", -1 )
                dicttemp["cdma_signalstrength"] = dictDBDump.get("cdma_signalstrength", -1 )


                dictDBDump = self.rfindColumnValue( index, listdictDBDump, "cdma_bsid" )
                dicttemp["cdma_loc_datetime"] = dictDBDump.get("timestamp", -1 )
                dicttemp["cdma_bsid"] = dictDBDump.get("cdma_bsid", -1 )
                dicttemp["cdma_bslat"] = dictDBDump.get("cdma_bslat", -1 )
                dicttemp["cdma_bslong"] = dictDBDump.get("cdma_bslong", -1 )
                dicttemp["cdma_nid"] = dictDBDump.get("cdma_nid", -1 )
                dicttemp["cdma_sid"] = dictDBDump.get("cdma_sid", -1 )

                # determine  cellmovement
                boolcellmovement = self.boolCellMovement(calldatetime, classmltdb )
                dicttemp["cellmovement"] = boolcellmovement

                # get the app name near call drop
                appsbeforeexception = self.getAppBeforeCall(calldatetime, classmltdb )
                dicttemp["appsbeforeexception"] = appsbeforeexception

                ret.append( dicttemp)
        return ret






def writeResultToExcel(listdictDBDump, wb, ws ):
    sumfieldnames = ["timestamp", "timediff"]

    sumfieldnames += fields_exception_blobs[1:]

    sumfieldnames += fields_power_info[1:]

    sumfieldnames += fields_lcd_info[1:]

    sumfieldnames += fields_battery_info[1:]

    sumfieldnames += fields_data_act_info[1:]

    sumfieldnames += fields_app_usage[1:]

    sumfieldnames += fields_app_history[1:]
    sumfieldnames += fields_resource_info[1:]

    sumfieldnames += fields_wifi_state[1:]
    sumfieldnames += fields_wifinetwork_state[1:]

    sumfieldnames += fields_telephony_state_info[1:]
    sumfieldnames += fields_datacomm_state_info[1:]
    sumfieldnames += fields_callcomm_state_info[1:]

    sumfieldnames += fields_cdmacell_info[1:]
    sumfieldnames += fields_gsmcell_info[1:]

    sumfieldnames += fields_cdma_level_info[1:]
    sumfieldnames += fields_evdo_level_info[1:]
    sumfieldnames += fields_gsm_level_info[1:]
    sumfieldnames += fields_lte_level_info[1:]


    sumfieldnames += fields_earjack_state[1:]
    sumfieldnames += fields_gps_state[1:]
    sumfieldnames += fields_gpsstatus_state[1:]
    sumfieldnames += fields_usbta_state[1:]
    sumfieldnames += fields_ums_state[1:]

    sumfieldnames += fields_bt_adapter_state[1:]
    sumfieldnames += fields_bt_headset_state[1:]
    sumfieldnames += fields_bt_a2dp_state[1:]
    sumfieldnames += fields_bt_pbap_state[1:]
    sumfieldnames += fields_bt_device_state[1:]
    sumfieldnames += fields_bt_bond_state[1:]



    sumfieldnames += fields_external_media_info[1:]
    sumfieldnames += fields_recentAct_info[1:]

    sumfieldnames += fields_rooting[1:]

    sumfieldnames += fields_basic_swver[1:]

    sumfieldnames += fields_battery_low_enter[1:]
    sumfieldnames += fields_battery_low_exit[1:]


    ''' ============================================================  '''
    ''' first, insert field name to row0 '''
    rindex = 0
    cindex = 0
    for fieldname in sumfieldnames :
        ws.cell(coords=(rindex, cindex,  ),  value = fieldname )
        if fieldname == "timestamp" or fieldname == "exception_type" :
            ws.col(index=cindex, width=20)
        else :
            ws.col(index=cindex, width=12)
        cindex += 1

    ''' print MLT Log info to excel file '''
    rindex = 1
    cindex = 0



    TimeStampPrevious = listdictDBDump[0]["timestamp"]

    for dictDBDump in listdictDBDump :
        for fieldname in sumfieldnames :
            if fieldname.find("timestamp") >= 0 :
                ws.cell(coords=(rindex, cindex,  ), value = ConvertTimeStampToString(dictDBDump.get(fieldname,None ) ) )
            elif fieldname.find("timediff") >= 0 :
                ntimediffseconds = (dictDBDump["timestamp"] - TimeStampPrevious)/1000
                strtimedelta = "%s" % (timedelta(seconds=ntimediffseconds))
                ws.cell(coords=(rindex, cindex,  ), value = strtimedelta )
            else:
                ws.cell(coords=(rindex, cindex,  ), value = dictDBDump.get(fieldname, None) )
            cindex += 1
        TimeStampPrevious = dictDBDump["timestamp"]
        rindex += 1
        cindex = 0


def doDumping(workdir, filename, boolusetimestamp2011 = False ):

    diroutput = os.path.abspath(workdir)
    if not os.path.exists(diroutput):
        os.makedirs(diroutput)

    ''' goto the diroutput dir to work '''
    os.chdir(diroutput)

    dblist = []
    if len(filename) != 0 :
        dblist.append(filename)
    else:
        dblist = glob.glob('*.db')

    if len( dblist ) == 0 :
        return

    for dbfilename in dblist:
        ## save the Excel Output to the Excel file
        #tempfilenamelist = dbfilename.split(".")
        #excelfilename = tempfilenamelist[0] + ".xlsx"
        excelfilename = os.path.splitext(dbfilename)[0] + ".xlsx"


        ## if exist , return
        if os.path.exists( excelfilename ) == True :
            print "** Excel file is exist  : ", excelfilename
            continue

        print " "
        print "MLT DB Dumpping  : " + dbfilename

        ''' rename the DB file name to 'temp.db' because theat sqlite3.connect can't handle the hangul file name . '''
        tempdbname = '___processing.db'
        shutil.copy(dbfilename, tempdbname )
        conn = sqlite3.connect(tempdbname)
        ''' check if t320 table is exist, if then, keep processing.  '''
        if check_table_exception_blobs(conn) == False:
            conn.close()
            print "No Exception Blobs, DB skip"
            os.remove( tempdbname )
            continue
        cur = conn.cursor()

        ##---------------------------------------------------------------------------------------------------------
        ## get the latest timestamp among the start point of each table

        if boolusetimestamp2011 == True :
            timestampbeginpoint = ConvertDateTimeToMiliSeconds(2011, 7, 1)
        else :
            timestampbeginpoint = getlatesttimestampamongtable(cur)

        # print "timestampbeginpoint : ", ConvertTimeStampToString ( timestampbeginpoint )

        querywhere = " where f002 >= %s " % ( timestampbeginpoint )

        listdictDBDump = []
        listdictBasicSWVer = []

        buildupDBDumpSWver(listdictDBDump, listdictBasicSWVer, cur, querywhere )

        ## write the result to the Excel module
        wb = Workbook()
        ws = wb.new_sheet("MLT_DUMP" )
        print "write the dump stuff to excel"
        writeResultToExcel(listdictDBDump, wb, ws )

        listdictDBDump = []
        listdictBasicSWVer = []


        print "Excel Saving : " + excelfilename
        save(wb,  excelfilename )
        print "Excel Saved : " + excelfilename

        ws = None
        wb = None


        ## finish the processing
        ##---------------------------------------------------------------------------------------------------------
        conn.close()
        os.remove( tempdbname )

    dblist = []


def doTest(workdir, filename, boolusetimestamp2011 = False ):

    diroutput = os.path.abspath(workdir)
    if not os.path.exists(diroutput):
        os.makedirs(diroutput)

    ''' goto the diroutput dir to work '''
    os.chdir(diroutput)

    dblist = []
    if len(filename) != 0 :
        dblist.append(filename)
    else:
        dblist = glob.glob('*.db')

    if len( dblist ) == 0 :
        return

    for dbfile in dblist :
        classmlt = ClassMLTDB(dbfile)

        listdictDBDump = classmlt.getListDictExceptionInfoRaw()

    del dblist





'''
c:> python MltDBDump.py -o c:\temp_mlt  -a
'''

if __name__ == "__main__":
    import argparse
    diroutput = "."
    ShutdownAfter = False
    dumpall = False
    filename = ""

    cmdlineopt = argparse.ArgumentParser(description='dump MLT DB into Excel file')
    cmdlineopt.add_argument('-o', action="store", dest="diroutput", default='.',  help='outputing and working directory . default = . sample: c:\\temp_mlt' )
    cmdlineopt.add_argument('-s', action="store_true", dest="ShutdownAfter",  default=False, help='shutdown system after job finished,  default= Faluse' )
    cmdlineopt.add_argument('-a', action="store_true", dest="dumpall",  default=False, help='dump all DB content to Excel without calculating viewing timestamp,  default= Faluse' )
    cmdlineopt.add_argument('-f', action="store", dest="filename",  default="", help='dump the input file,  default= "" ' )

    cmdlineresults = cmdlineopt.parse_args()

    diroutput = cmdlineresults.diroutput
    ShutdownAfter = cmdlineresults.ShutdownAfter
    dumpall = cmdlineresults.dumpall
    filename = cmdlineresults.filename

    doDumping ( diroutput, filename, dumpall )
#    doTest ( diroutput, filename, dumpall )

    if ShutdownAfter == True :
        os.system( "shutdown /s /t 300 ")














