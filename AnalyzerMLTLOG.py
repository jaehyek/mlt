# _*_ coding: utf-8 _*_

'''
Created on 2012. 8. 2.

@author: jaehyek
'''

import os
import glob
from datetime import datetime, timedelta
import shutil
import MltDBDump
'''
===========================================================================
 caution : the return value of "cursor.execute("query") is  list of tuple .
'''
from pysqlite2 import dbapi2 as sqlite3

''' open the xls file '''

from xlsxcessive.xlsx import Workbook


''' -----------------------------------------------------------------------------------------------------
The below code is defined in  MLT Viewer source code for IMSI encription

            public static String DecryptIMSICode(String _strEncrypted)
            {
                String strDecrypted = "";

                int nDigitBackup = -1;
                while (_strEncrypted.Length > 0)
                {
                    String strOneDigit = _strEncrypted.Substring(2, 2) + _strEncrypted.Substring(0, 2);
                    int nDigit = Convert.ToInt32(strOneDigit, 16); //CFun.ConvertHexStringToInt(strOneDigit);

                    nDigit = (int)Math.Sqrt((double)nDigit);
                    if (nDigitBackup == -1)
                    {
                        nDigitBackup = nDigit;
                    }
                    else
                    {
                        strDecrypted += Char.ConvertFromUtf32(nDigit);  //(nDigit - '0');
                        strDecrypted += Char.ConvertFromUtf32(nDigitBackup);  //(nDigitBackup - '0');
                        nDigitBackup = -1;
                    }

                    _strEncrypted = _strEncrypted.Substring(4);
                }

                if (nDigitBackup != -1)
                    strDecrypted += Char.ConvertFromUtf32(nDigitBackup); //nDigitBackup;

                return strDecrypted;
            }
---------------------------------------------------------------------------------------------------------'''
import math

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







''' -----------------------------------------------------------------------------------------------------
The below code is defined in  MLT Viewer source code for Datetime Converting .

            public static DateTime CvrtToDateTime(Int64 TimeStamp)
            {
                DateTime t = new DateTime(1970, 1, 1).AddSeconds((Double)(TimeStamp / 1000));
                return t;
            }

            public static String CvrtToDateTimeString(Int64 _nTimeStamp, bool _bShowMillSec = false)
            {
                String strTime = "";
                if (_nTimeStamp == 0)
                    return strTime;

                DateTime t = new DateTime(1970, 1, 1).AddMilliseconds((Double)(_nTimeStamp));
                t = t.AddHours(9);

                if (_bShowMillSec)
                    strTime = t.ToString("yyyy-MM-dd HH:mm:ss.fff");
                else
                    strTime = t.ToString("yyyy-MM-dd HH:mm:ss");


                return strTime;
            }
---------------------------------------------------------------------------------------------------------'''




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
    return cmp ( a1[0], a2[0] )

def TimeStampCmpDict ( a1, a2 ) :
    return cmp ( a1["timestamp"], a2["timestamp"] )

''' ======================================================================'''
''' define the table name and field name'''
table_basic_info = 't301'
fields_basic_info =["basic_timestamp", "IMEI", "serial_no", "os_ver", "hw_ver", "last_sw_ver", "model_name", "build_no", "registration_timestamp", "phone_type", "network_type","mpt_version"]
f00n_basic_info = "f002, f003, f006, f007, f008, f009, f010, f011, f013, f014, f015, f021 "
dict_network_type = {0:"NETWORK_TYPE_UNKNOWN",1:"NETWORK_TYPE_GPRS",2:"NETWORK_TYPE_EDGE",3:"NETWORK_TYPE_UMTS",4:"NETWORK_TYPE_CDMA",5:"NETWORK_TYPE_EVDO_0",6:"NETWORK_TYPE_EVDO_A",7:"NETWORK_TYPE_1xRTT",8:"NETWORK_TYPE_HSDPA",9:"NETWORK_TYPE_HSUPA",10:"NETWORK_TYPE_HSPA",11:"NETWORK_TYPE_IDEN",12:"NETWORK_TYPE_EVDO_B",13:"NETWORK_TYPE_LTE",14:"NETWORK_TYPE_EHRPD" }
dict_phone_type = { 0:None, 1:"GSM", 2:"CDMA", 3:"SIP" }

table_exception_blobs = 't320'
fields_exception_blobs = [ "except_timestamp", "exception_type", "exception_cause", "exception_timediff", "exception_swver"]
f00n_exception_blobs = "f002 ,f007, f003, f013"
dict_exception_type = { 1:"exception_cp", 2:"exception_kernel", 3:"exception_framework", 4:"exception_app_fatal", 5:"exception_app_reset", 6:"exception_lockup", 7:"exception_anr",8:"exception_calldrop",13:"exception_Kernel_LastK" }

fields_App1_10min_Overlap = ["app1_10min_overlap" ]
fields_App_timediff1 = ["app_timediff1"]
fields_App_timediff2 = ["app_timediff2"]
fields_App_timediff3 = ["app_timediff3"]


table_app_usage = 't307'
f00n_app_usage = "f002 ,f003, f004"
fields_app_usage10min = ["app_timestamp10min", "AppName10min", "app_eventid10min"]
fields_app_usage1 = ["app_timestamp1", "AppName1", "app_eventid1"]
fields_app_usage2 = ["app_timestamp2", "AppName2", "app_eventid2"]
fields_app_usage3 = ["app_timestamp3", "AppName3", "app_eventid3"]
dict_app_event_type = {11:"start foreground", 12:"start background", 13:"start broadcast", 14:"start service", 15:"start provider", 16:"added application", 19:"start other", 20:"end", 31:"resumed", 32:"paused" }


table_battery_info = 't308'
f00n_battery_info = "f002 ,f003, f004"
fields_battery_info1 = ["battery_level1", "battery_voltage1", "battery_temperature1", "battery_health1", "battery_charging1", "battery_plugtype1", "battery_plugtype_count1", "battery_low_enter_count1", "battery_low_exit_count1", "battery_level_judge1", "battery_temperature_judge1"]
fields_battery_info2 = ["battery_level2", "battery_voltage2", "battery_temperature2", "battery_health2", "battery_charging2", "battery_plugtype2", "battery_plugtype_count2", "battery_low_enter_count2", "battery_low_exit_count2", "battery_level_judge2", "battery_temperature_judge2"]
fields_battery_info3 = ["battery_level3", "battery_voltage3", "battery_temperature3", "battery_health3", "battery_charging3", "battery_plugtype3", "battery_plugtype_count3", "battery_low_enter_count3", "battery_low_exit_count3", "battery_level_judge3", "battery_temperature_judge3"]
fields_battery_info10min = ["battery_level10min", "battery_voltage10min", "battery_temperature10min", "battery_health10min", "battery_charging10min", "battery_plugtype10min", "battery_plugtype_count10min", "battery_low_enter_count10min", "battery_low_exit_count10min", "battery_level_judge10min", "battery_temperature_judge10min"]





table_telephony_info = 't310'
f00n_telephony_info = "f002 ,f003, f004"
fields_telephony_info10min = ["telephony_STATE_OUT_OF_SERVICE_count10min",
                          "telephony_STATE_EMERGENCY_ONLY_count10min",
                          "telephony_STATE_POWER_OFF_count10min",
                          "telephony_DATA_DISCONNECTED_count10min",
                          "telephony_DATA_CONNECTED_count10min",
                          "telephony_DATA_SUSPENDED_count10min",
                          "telephony_CALL_STATE_RINGING_count10min",
                          "telephony_CALL_STATE_OFFHOOK_count10min",
                          "telephony_SERVICE_STATE10min",
                          "telephony_DATACOMM_STATE10min",
                          "telephony_TELEPHONY_CALL_STATE10min" ]

fields_telephony_info1 = ["telephony_STATE_OUT_OF_SERVICE_count1",
                          "telephony_STATE_EMERGENCY_ONLY_count1",
                          "telephony_STATE_POWER_OFF_count1",
                          "telephony_DATA_DISCONNECTED_count1",
                          "telephony_DATA_CONNECTED_count1",
                          "telephony_DATA_SUSPENDED_count1",
                          "telephony_CALL_STATE_RINGING_count1",
                          "telephony_CALL_STATE_OFFHOOK_count1",
                          "telephony_SERVICE_STATE1",
                          "telephony_DATACOMM_STATE1",
                          "telephony_TELEPHONY_CALL_STATE1" ]

fields_telephony_info2 = ["telephony_STATE_OUT_OF_SERVICE_count2",
                          "telephony_STATE_EMERGENCY_ONLY_count2",
                          "telephony_STATE_POWER_OFF_count2",
                          "telephony_DATA_DISCONNECTED_count2",
                          "telephony_DATA_CONNECTED_count2",
                          "telephony_DATA_SUSPENDED_count2",
                          "telephony_CALL_STATE_RINGING_count2",
                          "telephony_CALL_STATE_OFFHOOK_count2",
                          "telephony_SERVICE_STATE2",
                          "telephony_DATACOMM_STATE2",
                          "telephony_TELEPHONY_CALL_STATE2" ]

fields_telephony_info3 = ["telephony_STATE_OUT_OF_SERVICE_count3",
                          "telephony_STATE_EMERGENCY_ONLY_count3",
                          "telephony_STATE_POWER_OFF_count3",
                          "telephony_DATA_DISCONNECTED_count3",
                          "telephony_DATA_CONNECTED_count3",
                          "telephony_DATA_SUSPENDED_count3",
                          "telephony_CALL_STATE_RINGING_count3",
                          "telephony_CALL_STATE_OFFHOOK_count3",
                          "telephony_SERVICE_STATE3",
                          "telephony_DATACOMM_STATE3",
                          "telephony_TELEPHONY_CALL_STATE3" ]


table_connectivity_info = 't313'
f00n_connectivity_info = "f002 ,f003, f004"
fields_connectivity_info10min = ["connectivity_EARJACK_STATE_UNPLUGGED_count10min",
                             "connectivity_EARJACK_STATE_PLUGGED_count10min",
                             "connectivity_GPS_STATUS_STARTED_count10min",
                             "connectivity_GPS_STATUS_STOPPED_count10min",
                             "connectivity_BATTERY_PLUGGED_AC_count10min",
                             "connectivity_BATTERY_PLUGGED_USB_count10min",
                             "connectivity_UMS_ON_count10min",
                             "connectivity_UMS_OFF_count10min",
                             "connectivity_EARJAcK_STATE10min",
                             "connectivity_GPS_STATE10min",
                             "connectivity_GPSSTATUS_STATE10min",
                             "connectivity_USBTA_STATE10min",
                             "connectivity_UMS_STATE10min"]

fields_connectivity_info1 = ["connectivity_EARJACK_STATE_UNPLUGGED_count1",
                             "connectivity_EARJACK_STATE_PLUGGED_count1",
                             "connectivity_GPS_STATUS_STARTED_count1",
                             "connectivity_GPS_STATUS_STOPPED_count1",
                             "connectivity_BATTERY_PLUGGED_AC_count1",
                             "connectivity_BATTERY_PLUGGED_USB_count1",
                             "connectivity_UMS_ON_count1",
                             "connectivity_UMS_OFF_count1",
                             "connectivity_EARJAcK_STATE1",
                             "connectivity_GPS_STATE1",
                             "connectivity_GPSSTATUS_STATE1",
                             "connectivity_USBTA_STATE1",
                             "connectivity_UMS_STATE1"]


fields_connectivity_info2 = ["connectivity_EARJACK_STATE_UNPLUGGED_count2",
                             "connectivity_EARJACK_STATE_PLUGGED_count2",
                             "connectivity_GPS_STATUS_STARTED_count2",
                             "connectivity_GPS_STATUS_STOPPED_count2",
                             "connectivity_BATTERY_PLUGGED_AC_count2",
                             "connectivity_BATTERY_PLUGGED_USB_count2",
                             "connectivity_UMS_ON_count2",
                             "connectivity_UMS_OFF_count2",
                             "connectivity_EARJAcK_STATE2",
                             "connectivity_GPS_STATE2",
                             "connectivity_GPSSTATUS_STATE2",
                             "connectivity_USBTA_STATE2",
                             "connectivity_UMS_STATE2"]

fields_connectivity_info3 = ["connectivity_EARJACK_STATE_UNPLUGGED_count3",
                             "connectivity_EARJACK_STATE_PLUGGED_count3",
                             "connectivity_GPS_STATUS_STARTED_count3",
                             "connectivity_GPS_STATUS_STOPPED_count3",
                             "connectivity_BATTERY_PLUGGED_AC_count3",
                             "connectivity_BATTERY_PLUGGED_USB_count3",
                             "connectivity_UMS_ON_count3",
                             "connectivity_UMS_OFF_count3",
                             "connectivity_EARJAcK_STATE3",
                             "connectivity_GPS_STATE3",
                             "connectivity_GPSSTATUS_STATE3",
                             "connectivity_USBTA_STATE3",
                             "connectivity_UMS_STATE3"]


table_bluetooth_info = 't317'
f00n_bluetooth_info = "f002 ,f003, f004"
fields_bluetooth_info10min = [   "bluetooth_BT_ADAPTER_OFF_count10min",
                             "bluetooth_BT_ADAPTER_ON_count10min",
                             "bluetooth_BT_HEADSET_DISCONNECTED_count10min",
                             "bluetooth_BT_HEADSET_CONNECTED_count10min",
                             "bluetooth_BT_A2DP_DISCONNECTED_count10min",
                             "bluetooth_BT_A2DP_CONNECTED_count10min",
                             "bluetooth_BT_A2DP_PLAYING_count10min",
                             "bluetooth_BT_PBAP_DISCONNECTED_count10min",
                             "bluetooth_BT_PBAP_CONNECTED_count10min",
                             "bluetooth_BT_DEVICE_DISCONNECTED_count10min",
                             "bluetooth_BT_DEVICE_CONNECTED_count10min",
                             "bluetooth_BT_DEVICE_DISCONNECTED_REQ_count10min",
                             "bluetooth_BT_BOND_NONE_count10min",
                             "bluetooth_BT_BOND_BONDED_count10min",
                             "bluetooth_ADAPTER_STATE10min",
                             "bluetooth_HEADSET_STATE10min",
                             "bluetooth_A2DP_STATE10min",
                             "bluetooth_PBAP_STATE10min",
                             "bluetooth_DEVICE_STATE10min",
                             "bluetooth_BOND_STATE10min" ]

fields_bluetooth_info1 = [   "bluetooth_BT_ADAPTER_OFF_count1",
                             "bluetooth_BT_ADAPTER_ON_count1",
                             "bluetooth_BT_HEADSET_DISCONNECTED_count1",
                             "bluetooth_BT_HEADSET_CONNECTED_count1",
                             "bluetooth_BT_A2DP_DISCONNECTED_count1",
                             "bluetooth_BT_A2DP_CONNECTED_count1",
                             "bluetooth_BT_A2DP_PLAYING_count1",
                             "bluetooth_BT_PBAP_DISCONNECTED_count1",
                             "bluetooth_BT_PBAP_CONNECTED_count1",
                             "bluetooth_BT_DEVICE_DISCONNECTED_count1",
                             "bluetooth_BT_DEVICE_CONNECTED_count1",
                             "bluetooth_BT_DEVICE_DISCONNECTED_REQ_count1",
                             "bluetooth_BT_BOND_NONE_count1",
                             "bluetooth_BT_BOND_BONDED_count1",
                             "bluetooth_ADAPTER_STATE1",
                             "bluetooth_HEADSET_STATE1",
                             "bluetooth_A2DP_STATE1",
                             "bluetooth_PBAP_STATE1",
                             "bluetooth_DEVICE_STATE1",
                             "bluetooth_BOND_STATE1" ]

fields_bluetooth_info2 = [   "bluetooth_BT_ADAPTER_OFF_count2",
                             "bluetooth_BT_ADAPTER_ON_count2",
                             "bluetooth_BT_HEADSET_CONNECTED_count2",
                             "bluetooth_BT_HEADSET_DISCONNECTED_count2",
                             "bluetooth_BT_A2DP_DISCONNECTED_count2",
                             "bluetooth_BT_A2DP_CONNECTED_count2",
                             "bluetooth_BT_A2DP_PLAYING_count2",
                             "bluetooth_BT_PBAP_DISCONNECTED_count2",
                             "bluetooth_BT_PBAP_CONNECTED_count2",
                             "bluetooth_BT_DEVICE_DISCONNECTED_count2",
                             "bluetooth_BT_DEVICE_CONNECTED_count2",
                             "bluetooth_BT_DEVICE_DISCONNECTED_REQ_count2",
                             "bluetooth_BT_BOND_NONE_count2",
                             "bluetooth_BT_BOND_BONDED_count2",
                             "bluetooth_ADAPTER_STATE2",
                             "bluetooth_HEADSET_STATE2",
                             "bluetooth_A2DP_STATE2",
                             "bluetooth_PBAP_STATE2",
                             "bluetooth_DEVICE_STATE2",
                             "bluetooth_BOND_STATE2" ]

fields_bluetooth_info3 = [   "bluetooth_BT_ADAPTER_OFF_count3",
                             "bluetooth_BT_ADAPTER_ON_count3",
                             "bluetooth_BT_HEADSET_CONNECTED_count3",
                             "bluetooth_BT_HEADSET_DISCONNECTED_count3",
                             "bluetooth_BT_A3DP_DISCONNECTED_count3",
                             "bluetooth_BT_A3DP_CONNECTED_count3",
                             "bluetooth_BT_A3DP_PLAYING_count3",
                             "bluetooth_BT_PBAP_DISCONNECTED_count3",
                             "bluetooth_BT_PBAP_CONNECTED_count3",
                             "bluetooth_BT_DEVICE_DISCONNECTED_count3",
                             "bluetooth_BT_DEVICE_CONNECTED_count3",
                             "bluetooth_BT_DEVICE_DISCONNECTED_REQ_count3",
                             "bluetooth_BT_BOND_NONE_count3",
                             "bluetooth_BT_BOND_BONDED_count3",
                             "bluetooth_ADAPTER_STATE3",
                             "bluetooth_HEADSET_STATE3",
                             "bluetooth_A2DP_STATE3",
                             "bluetooth_PBAP_STATE3",
                             "bluetooth_DEVICE_STATE3",
                             "bluetooth_BOND_STATE3" ]

table_wifi_info = 't318'
f00n_wifi_info = "f002 ,f003, f004"
fields_wifi_info10min = [   "wifi_WIFI_STATE_DISABLED_count10min",
                        "wifi_WIFI_STATE_ENABLED_count10min",
                        "wifi_WIFI_STATE_FAILED_count10min",
                        "wifi_WIFI_NETWORK_STATE_DISABLED_count10min",
                        "wifi_WIFI_NETWORK_STATE_ENABLED_count10min",
                        "wifi_WIFI_NETWORK_STATE_FAILED_count10min",
                        "wifi_WIFI_STATE10min",
                        "wifi_WIFI_NETWORK_STATE10min"]

fields_wifi_info1 = [   "wifi_WIFI_STATE_DISABLED_count1",
                        "wifi_WIFI_STATE_ENABLED_count1",
                        "wifi_WIFI_STATE_FAILED_count1",
                        "wifi_WIFI_NETWORK_STATE_DISABLED_count1",
                        "wifi_WIFI_NETWORK_STATE_ENABLED_count1",
                        "wifi_WIFI_NETWORK_STATE_FAILED_count1",
                        "wifi_WIFI_STATE1",
                        "wifi_WIFI_NETWORK_STATE1"]


fields_wifi_info2 = [   "wifi_WIFI_STATE_DISABLED_count2",
                        "wifi_WIFI_STATE_ENABLED_count2",
                        "wifi_WIFI_STATE_FAILED_count2",
                        "wifi_WIFI_NETWORK_STATE_DISABLED_count2",
                        "wifi_WIFI_NETWORK_STATE_ENABLED_count2",
                        "wifi_WIFI_NETWORK_STATE_FAILED_count2",
                        "wifi_WIFI_STATE2",
                        "wifi_WIFI_NETWORK_STATE2"]

fields_wifi_info3 = [   "wifi_WIFI_STATE_DISABLED_count3",
                        "wifi_WIFI_STATE_ENABLED_count3",
                        "wifi_WIFI_STATE_FAILED_count3",
                        "wifi_WIFI_NETWORK_STATE_DISABLED_count3",
                        "wifi_WIFI_NETWORK_STATE_ENABLED_count3",
                        "wifi_WIFI_NETWORK_STATE_FAILED_count3",
                        "wifi_WIFI_STATE3",
                        "wifi_WIFI_NETWORK_STATE3"]

table_power_info = 't314'
f00n_power_info = "f002 ,f003"
fields_power_info10min = [  "power_POWER_ON_count10min","power_POWER_OFF_count10min", "power_POWER_STATE10min" ]
fields_power_info1 = [  "power_POWER_ON_count1","power_POWER_OFF_count1", "power_POWER_STATE1" ]
fields_power_info2 = [  "power_POWER_ON_count2","power_POWER_OFF_count2", "power_POWER_STATE2"  ]
fields_power_info3 = [  "power_POWER_ON_count3","power_POWER_OFF_count3", "power_POWER_STATE3"  ]


table_lcd_info = 't315'
f00n_lcd_info = "f002 ,f003"
fields_lcd_info10min = [  "lcd_LCD_ON_count10min","lcd_LCD_OFF_count10min", "lcd_LCD_STATE10min" ]
fields_lcd_info1 = [  "lcd_LCD_ON_count1","lcd_LCD_OFF_count1", "lcd_LCD_STATE1" ]
fields_lcd_info2 = [  "lcd_LCD_ON_count2","lcd_LCD_OFF_count2", "lcd_LCD_STATE2" ]
fields_lcd_info3 = [  "lcd_LCD_ON_count3","lcd_LCD_OFF_count3", "lcd_LCD_STATE3" ]

table_resource_info = 't316'
f00n_resource_info = "f002 ,f003, f004"
fields_resource_info10min = [  "resource_CPU_90_OVER_count10min","resource_AVAIL_RAM_AVG10min","resource_AVAIL_RAM_AVG_10min0M_count10min", "CPU_Usage_90_Over_judge10min", "Avail_Ram_STATE_10min0M_judge10min"]
fields_resource_info1 = [  "resource_CPU_90_OVER_count1","resource_AVAIL_RAM_AVG1","resource_AVAIL_RAM_AVG_10M_count1", "CPU_Usage_90_Over_judge1", "Avail_Ram_STATE_10M_judge1"]
fields_resource_info2 = [  "resource_CPU_90_OVER_count2","resource_AVAIL_RAM_AVG2","resource_AVAIL_RAM_AVG_10M_count2", "CPU_Usage_90_Over_judge2", "Avail_Ram_STATE_10M_judge2"]
fields_resource_info3 = [  "resource_CPU_90_OVER_count3","resource_AVAIL_RAM_AVG3","resource_AVAIL_RAM_AVG_10M_count3", "CPU_Usage_90_Over_judge3", "Avail_Ram_STATE_10M_judge3"]

table_recentAct_info = 't325'
f00n_recentAct_info = "f002 ,f003"
fields_recentAct_info10min = [  "recentAct_Activity10min_1",
                            "recentAct_Activity10min_10",
                            "recentAct_Activity10min_11",
                            "recentAct_Activity10min_12",
                            "recentAct_Activity10min_13",
                            "recentAct_Activity10min_14",
                            "recentAct_Activity10min_15",
                            "recentAct_Activity10min_16",
                            "recentAct_Activity10min_17",
                            "recentAct_Activity10min_18",
                            "recentAct_Activity10min_19" ]

fields_recentAct_info1 = [  "recentAct_ActivityList1",
                            "recentAct_ActivityList10",
                            "recentAct_ActivityList11",
                            "recentAct_ActivityList12",
                            "recentAct_ActivityList13",
                            "recentAct_ActivityList14",
                            "recentAct_ActivityList15",
                            "recentAct_ActivityList16",
                            "recentAct_ActivityList17",
                            "recentAct_ActivityList18",
                            "recentAct_ActivityList19" ]


fields_recentAct_info2 = [  "recentAct_ActivityList2",
                            "recentAct_ActivityList20",
                            "recentAct_ActivityList21",
                            "recentAct_ActivityList22",
                            "recentAct_ActivityList23",
                            "recentAct_ActivityList24",
                            "recentAct_ActivityList25",
                            "recentAct_ActivityList26",
                            "recentAct_ActivityList27",
                            "recentAct_ActivityList28",
                            "recentAct_ActivityList29" ]

fields_recentAct_info3 = [  "recentAct_ActivityList3",
                            "recentAct_ActivityList30",
                            "recentAct_ActivityList31",
                            "recentAct_ActivityList32",
                            "recentAct_ActivityList33",
                            "recentAct_ActivityList34",
                            "recentAct_ActivityList35",
                            "recentAct_ActivityList36",
                            "recentAct_ActivityList37",
                            "recentAct_ActivityList38",
                            "recentAct_ActivityList39" ]

table_external_media_info = 't326'
f00n_external_media_info = "f002 ,f003"
fields_external_media_info10min = [  "externalM_STATE10min", "externalM_BAD_REMOVAL_count10min", "externalM_NOFS_count10min" , "externalM_SHARED_count10min", "externalM_UNMOUNTABLE_count10min" , "externalM_SCAN_STARTED_count10min", "externalM_SCAN_FINISHED_count10min"  ]
fields_external_media_info1 = [  "externalM_STATE1", "externalM_BAD_REMOVAL_count1", "externalM_NOFS_count1" , "externalM_SHARED_count1", "externalM_UNMOUNTABLE_count1" , "externalM_SCAN_STARTED_count1", "externalM_SCAN_FINISHED_count1"  ]
fields_external_media_info2 = [  "externalM_STATE2", "externalM_BAD_REMOVAL_count2", "externalM_NOFS_count2" , "externalM_SHARED_count2", "externalM_UNMOUNTABLE_count2" , "externalM_SCAN_STARTED_count2", "externalM_SCAN_FINISHED_count2"  ]
fields_external_media_info3 = [  "externalM_STATE3", "externalM_BAD_REMOVAL_count3", "externalM_NOFS_count3" , "externalM_SHARED_count3", "externalM_UNMOUNTABLE_count3" , "externalM_SCAN_STARTED_count3", "externalM_SCAN_FINISHED_count3"  ]


table_data_act_info = 't327'
f00n_data_act_info = "f002 ,f003, f004"
fields_data_act_info10min = [  "dataact_STATE10min", "dataact_ACTIVITY_NONE_count10min", "dataact_ACTIVITY_IN_count10min", "dataact_ACTIVITY_OUT_count10min", "dataact_ACTIVITY_INOUT_count10min" , "dataact_ACTIVITY_DORMANT_count10min"  ]
fields_data_act_info1 = [  "dataact_STATE1", "dataact_ACTIVITY_NONE_count1", "dataact_ACTIVITY_IN_count1", "dataact_ACTIVITY_OUT_count1", "dataact_ACTIVITY_INOUT_count1" , "dataact_ACTIVITY_DORMANT_count1"  ]
fields_data_act_info2 = [  "dataact_STATE2", "dataact_ACTIVITY_NONE_count2", "dataact_ACTIVITY_IN_count2", "dataact_ACTIVITY_OUT_count2", "dataact_ACTIVITY_INOUT_count2" , "dataact_ACTIVITY_DORMANT_count2"  ]
fields_data_act_info3 = [  "dataact_STATE3", "dataact_ACTIVITY_NONE_count3", "dataact_ACTIVITY_IN_count3", "dataact_ACTIVITY_OUT_count3", "dataact_ACTIVITY_INOUT_count3" , "dataact_ACTIVITY_DORMANT_count3"  ]




table_signal_level_info = 't309'
f00n_signal_level_info = "f002 ,f003, f004"
fields_signal_level_info10min = [ "singal_STATE10min", "signal_LEVEL10min", "signal_level_CDMA_count10min", "signal_level_EVDO_count10min", "signal_level_GSM_count10min",  "signal_level_LTE_count10min" ]
fields_signal_level_info1 = [ "singal_STATE1", "signal_LEVEL1", "signal_level_CDMA_count1", "signal_level_EVDO_count1", "signal_level_GSM_count1",  "signal_level_LTE_count1" ]
fields_signal_level_info2 = [ "singal_STATE2", "signal_LEVEL2", "signal_level_CDMA_count2", "signal_level_EVDO_count2", "signal_level_GSM_count2",  "signal_level_LTE_count2" ]
fields_signal_level_info3 = [ "singal_STATE3", "signal_LEVEL3", "signal_level_CDMA_count3", "signal_level_EVDO_count3", "signal_level_GSM_count3",  "signal_level_LTE_count3" ]
fields_sum_signal_level = [ "Sum_signal_level_CDMA", "Sum_signal_level_EVDO", "Sum_signal_level_GSM",  "Sum_signal_level_LTE" ]



fields_SeqEvent10min = [
    "SeqEvent10min_s00",
    "SeqEvent10min_s01",
    "SeqEvent10min_s02",
    "SeqEvent10min_s03",
    "SeqEvent10min_s04",
    "SeqEvent10min_s05",
    "SeqEvent10min_s06",
    "SeqEvent10min_s07",
    "SeqEvent10min_s08",
    "SeqEvent10min_s09",
    "SeqEvent10min_s10",
    "SeqEvent10min_s11",
    "SeqEvent10min_s12",
    "SeqEvent10min_s13",
    "SeqEvent10min_s14",
    "SeqEvent10min_s15",
    "SeqEvent10min_s16",
    "SeqEvent10min_s17",
    "SeqEvent10min_s18",
    "SeqEvent10min_s19",
    "SeqEvent10min_s20",
    "SeqEvent10min_s21",
    "SeqEvent10min_s22",
    "SeqEvent10min_s23",
    "SeqEvent10min_s24",
    "SeqEvent10min_s25",
    "SeqEvent10min_s26",
    "SeqEvent10min_s27",
    "SeqEvent10min_s28",
    "SeqEvent10min_s29",
    "SeqEvent10min_s30",
    "SeqEvent10min_s31",
    "SeqEvent10min_s32",
    "SeqEvent10min_s33",
    "SeqEvent10min_s34",
    "SeqEvent10min_s35",
    "SeqEvent10min_s36",
    "SeqEvent10min_s37",
    "SeqEvent10min_s38",
    "SeqEvent10min_s39",
    "SeqEvent10min_s40",
    "SeqEvent10min_s41",
    "SeqEvent10min_s42",
    "SeqEvent10min_s43",
    "SeqEvent10min_s44",
    "SeqEvent10min_s45",
    "SeqEvent10min_s46",
    "SeqEvent10min_s47",
    "SeqEvent10min_s48",
    "SeqEvent10min_s49",
    "SeqEvent10min_s50",
    "SeqEvent10min_s51",
    "SeqEvent10min_s52",
    "SeqEvent10min_s53",
    "SeqEvent10min_s54",
    "SeqEvent10min_s55",
    "SeqEvent10min_s56",
    "SeqEvent10min_s57",
    "SeqEvent10min_s58",
    "SeqEvent10min_s59",
    "SeqEvent10min_s60",
    "SeqEvent10min_s61",
    "SeqEvent10min_s62",
    "SeqEvent10min_s63",
    "SeqEvent10min_s64",
    "SeqEvent10min_s65",
    "SeqEvent10min_s66",
    "SeqEvent10min_s67",
    "SeqEvent10min_s68",
    "SeqEvent10min_s69",
    "SeqEvent10min_s70",
    "SeqEvent10min_s71",
    "SeqEvent10min_s72",
    "SeqEvent10min_s73",
    "SeqEvent10min_s74",
    "SeqEvent10min_s75",
    "SeqEvent10min_s76",
    "SeqEvent10min_s77",
    "SeqEvent10min_s78",
    "SeqEvent10min_s79",
    "SeqEvent10min_s80",
    "SeqEvent10min_s81",
    "SeqEvent10min_s82",
    "SeqEvent10min_s83",
    "SeqEvent10min_s84",
    "SeqEvent10min_s85",
    "SeqEvent10min_s86",
    "SeqEvent10min_s87",
    "SeqEvent10min_s88",
    "SeqEvent10min_s89",
    "SeqEvent10min_s90",
    "SeqEvent10min_s91",
    "SeqEvent10min_s92",
    "SeqEvent10min_s93",
    "SeqEvent10min_s94",
    "SeqEvent10min_s95",
    "SeqEvent10min_s96",
    "SeqEvent10min_s97",
    "SeqEvent10min_s98",
    "SeqEvent10min_s99",
    "SeqEvent10min_s100",
    "SeqEvent10min_s101",
    "SeqEvent10min_s102",
    "SeqEvent10min_s103",
    "SeqEvent10min_s104",
    "SeqEvent10min_s105",
    "SeqEvent10min_s106",
    "SeqEvent10min_s107",
    "SeqEvent10min_s108",
    "SeqEvent10min_s109",
    "SeqEvent10min_s110",
    "SeqEvent10min_s111",
    "SeqEvent10min_s112",
    "SeqEvent10min_s113",
    "SeqEvent10min_s114",
    "SeqEvent10min_s115",
    "SeqEvent10min_s116",
    "SeqEvent10min_s117",
    "SeqEvent10min_s118",
    "SeqEvent10min_s119",
    "SeqEvent10min_s120",
    "SeqEvent10min_s121",
    "SeqEvent10min_s122",
    "SeqEvent10min_s123",
    "SeqEvent10min_s124",
    "SeqEvent10min_s125",
    "SeqEvent10min_s126",
    "SeqEvent10min_s127",
    "SeqEvent10min_s128",
    "SeqEvent10min_s129",
    "SeqEvent10min_s130",
    "SeqEvent10min_s131",
    "SeqEvent10min_s132",
    "SeqEvent10min_s133",
    "SeqEvent10min_s134",
    "SeqEvent10min_s135",
    "SeqEvent10min_s136",
    "SeqEvent10min_s137",
    "SeqEvent10min_s138",
    "SeqEvent10min_s139",
    "SeqEvent10min_s140",
    "SeqEvent10min_s141",
    "SeqEvent10min_s142",
    "SeqEvent10min_s143",
    "SeqEvent10min_s144",
    "SeqEvent10min_s145",
    "SeqEvent10min_s146",
    "SeqEvent10min_s147",
    "SeqEvent10min_s148",
    "SeqEvent10min_s149"
 ]

fields_SeqApp10min = [
    "SeqApp10min_s00",
    "SeqApp10min_s01",
    "SeqApp10min_s02",
    "SeqApp10min_s03",
    "SeqApp10min_s04",
    "SeqApp10min_s05",
    "SeqApp10min_s06",
    "SeqApp10min_s07",
    "SeqApp10min_s08",
    "SeqApp10min_s09",
    "SeqApp10min_s10",
    "SeqApp10min_s11",
    "SeqApp10min_s12",
    "SeqApp10min_s13",
    "SeqApp10min_s14",
    "SeqApp10min_s15",
    "SeqApp10min_s16",
    "SeqApp10min_s17",
    "SeqApp10min_s18",
    "SeqApp10min_s19"
 ]

fields_SeqAction10min = [
    "SeqAction10min_s00",
    "SeqAction10min_s01",
    "SeqAction10min_s02",
    "SeqAction10min_s03",
    "SeqAction10min_s04",
    "SeqAction10min_s05",
    "SeqAction10min_s06",
    "SeqAction10min_s07",
    "SeqAction10min_s08",
    "SeqAction10min_s09",
    "SeqAction10min_s10",
    "SeqAction10min_s11",
    "SeqAction10min_s12",
    "SeqAction10min_s13",
    "SeqAction10min_s14",
    "SeqAction10min_s15",
    "SeqAction10min_s16",
    "SeqAction10min_s17",
    "SeqAction10min_s18",
    "SeqAction10min_s19",
    "SeqAction10min_s20",
    "SeqAction10min_s21",
    "SeqAction10min_s22",
    "SeqAction10min_s23",
    "SeqAction10min_s24",
    "SeqAction10min_s25",
    "SeqAction10min_s26",
    "SeqAction10min_s27",
    "SeqAction10min_s28",
    "SeqAction10min_s29",
    "SeqAction10min_s30",
    "SeqAction10min_s31",
    "SeqAction10min_s32",
    "SeqAction10min_s33",
    "SeqAction10min_s34",
    "SeqAction10min_s35",
    "SeqAction10min_s36",
    "SeqAction10min_s37",
    "SeqAction10min_s38",
    "SeqAction10min_s39",
    "SeqAction10min_s40",
    "SeqAction10min_s41",
    "SeqAction10min_s42",
    "SeqAction10min_s43",
    "SeqAction10min_s44",
    "SeqAction10min_s45",
    "SeqAction10min_s46",
    "SeqAction10min_s47",
    "SeqAction10min_s48",
    "SeqAction10min_s49",
    "SeqAction10min_s50",
    "SeqAction10min_s51",
    "SeqAction10min_s52",
    "SeqAction10min_s53",
    "SeqAction10min_s54",
    "SeqAction10min_s55",
    "SeqAction10min_s56",
    "SeqAction10min_s57",
    "SeqAction10min_s58",
    "SeqAction10min_s59",
    "SeqAction10min_s60",
    "SeqAction10min_s61",
    "SeqAction10min_s62",
    "SeqAction10min_s63",
    "SeqAction10min_s64",
    "SeqAction10min_s65",
    "SeqAction10min_s66",
    "SeqAction10min_s67",
    "SeqAction10min_s68",
    "SeqAction10min_s69",
    "SeqAction10min_s70",
    "SeqAction10min_s71",
    "SeqAction10min_s72",
    "SeqAction10min_s73",
    "SeqAction10min_s74",
    "SeqAction10min_s75",
    "SeqAction10min_s76",
    "SeqAction10min_s77",
    "SeqAction10min_s78",
    "SeqAction10min_s79",
    "SeqAction10min_s80",
    "SeqAction10min_s81",
    "SeqAction10min_s82",
    "SeqAction10min_s83",
    "SeqAction10min_s84",
    "SeqAction10min_s85",
    "SeqAction10min_s86",
    "SeqAction10min_s87",
    "SeqAction10min_s88",
    "SeqAction10min_s89",
    "SeqAction10min_s90",
    "SeqAction10min_s91",
    "SeqAction10min_s92",
    "SeqAction10min_s93",
    "SeqAction10min_s94",
    "SeqAction10min_s95",
    "SeqAction10min_s96",
    "SeqAction10min_s97",
    "SeqAction10min_s98",
    "SeqAction10min_s99"
 ]

fields_AppInstallException = ["exception_AppInstall", "exception_AppDeleted" ]
fields_AppInstall10min = ["AppInstall10min", "AppDeleted10min" ]


''' ======================================================================'''
''' define some utility '''
def check_table_exception_blobs ( conn ):
    query = "SELECT name FROM sqlite_master WHERE type='table'"
    listTable = list( conn.execute(query))
    if (table_exception_blobs, ) in listTable :
        return True
    else:
        return False


def getLatestApp(cur, querywhere):
    query_app_usage = "select %s from %s " % (f00n_app_usage,table_app_usage  )
    query_app_usage += querywhere
    cur.execute(query_app_usage)
    listtupleAppUsage = cur.fetchall()
    listtupleAppUsage.sort(reverse=True)

    retstr = "NoApp"
    for tupleAppUsage in listtupleAppUsage :
        ''' treat the only type  "start foreground" "start background"  "resumed"  "paused" '''
        ''' timestamp, package, eventid = tupleAppUsage '''
        if not  tupleAppUsage[2] in [11, 31] :
            continue
        retstr = tupleAppUsage[1]
    return retstr



'''--------------------------------------------------------------------------------------------------- '''
'''  MLT Viewer���� ����� int64������ �� �ǹ̵�
            public const Int64 PACKED_BATTERY_LEVEL_MASK = 0x000000000000FFFFL;
            public const Int64 PACKED_BATTERY_VOLTAGE_MASK = 0x00000000FFFF0000L;
            public const Int64 PACKED_BATTERY_TEMPERATURE_MASK = 0x0000FFFF00000000L;
            public const Int64 PACKED_BATTERY_HEALTH_MASK = 0x000F000000000000L;
            public const Int64 PAKCED_BATTERY_SATUS_MASK = 0x00F0000000000000L;
            public const Int64 PACKED_BATTERY_PLUG_TYPE_MASK = 0x0F00000000000000L;
            public const Int64 PACKED_BATTERY_PRESENT_MASK = 0x7000000000000000L;

            public const int PACKED_BATTERY_VOLTAGE_SHIFT = 16;
            public const int PACKED_BATTERY_TEMPERATURE_SHIFT = 32;
            public const int PACKED_BATTERY_HEALTH_SHIFT = 48;
            public const int PACKED_BATTERY_STATUS_SHIFT = 52;
            public const int PACKED_BATTERY_PLUG_TYPE_SHIFT = 56;
            public const int PACKED_BATTERY_PRESENT_SHIFT = 60;

            {
                BatteryCore.nLevel = (int)(BatteryInfo & PACKED_BATTERY_LEVEL_MASK);
                BatteryCore.nVoltage(mV) = (int)((int)(BatteryInfo & PACKED_BATTERY_VOLTAGE_MASK) >> PACKED_BATTERY_VOLTAGE_SHIFT);
                BatteryCore.nTemperature(��) = (int)((BatteryInfo & PACKED_BATTERY_TEMPERATURE_MASK) >> PACKED_BATTERY_TEMPERATURE_SHIFT) / 10;
                BatteryCore.eBatteryStatus_Health = (EBatteryStatus_Health)((BatteryInfo & PACKED_BATTERY_HEALTH_MASK) >> PACKED_BATTERY_HEALTH_SHIFT);
                    eBatteryStatus_Health_Unknown = 1,
                    eBatteryStatus_Health_Good = 2,
                    eBatteryStatus_Health_OverHeat = 3,
                    eBatteryStatus_Health_Dead = 4,
                    eBatteryStatus_Health_OverVoltage = 5,
                    eBatteryStatus_Health_UnspecifiedFailure = 6,
                    eBatteryStatus_Health_Cold = 7,
                BatteryCore.eBatteryStatus_Charging = (EBatteryStatus_Charging)((BatteryInfo & PAKCED_BATTERY_SATUS_MASK) >> PACKED_BATTERY_STATUS_SHIFT);
                    eBatteryStatus_Charging_Unknown = 1,
                    eBatteryStatus_Charging_Charging = 2,
                    eBatteryStatus_Charging_Discharging = 3,
                    eBatteryStatus_Charging_NotCharging = 4,
                    eBatteryStatus_Charging_Full = 5,
                BatteryCore.eBatteryStatus_PlugType = (EBatteryStatus_PlugType)((BatteryInfo & PACKED_BATTERY_PLUG_TYPE_MASK) >> PACKED_BATTERY_PLUG_TYPE_SHIFT);
                    eBatteryStatus_PlugType_None = 0,
                    eBatteryStatus_PlugType_AC = 1,
                    eBatteryStatus_PlugType_USB = 2,
                BatteryCore.bPresent = (bool)(((BatteryInfo & PACKED_BATTERY_PRESENT_MASK) >> PACKED_BATTERY_PRESENT_SHIFT) == 1);
            }
'''
'''--------------------------------------------------------------------------------------------------- '''


''' return battery info if changed '''
def get_battery_info (cur,  querywhere):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min
    querybattery = "select %s from %s " % (f00n_battery_info, table_battery_info )
    querybattery += querywhere
    cur.execute( querybattery )
    listtupleBatteryInfos = cur.fetchall()
    listtupleBatteryInfos.sort(reverse=True)

    BATTERY_LEVEL_MASK = 0x000000000000FFFFL
    BATTERY_VOLTAGE_MASK = 0x00000000FFFF0000L
    BATTERY_TEMPERATURE_MASK = 0x0000FFFF00000000L
    BATTERY_HEALTH_MASK = 0x000F000000000000L
    BATTERY_SATUS_MASK = 0x00F0000000000000L
    #BATTERY_PLUG_TYPE_MASK = 0x0F00000000000000L
    BATTERY_PLUG_TYPE_MASK = 0x0300000000000000L    # for mask value adjustment due to abnormal value
    BATTERY_PRESENT_MASK = 0x7000000000000000L

    BATTERY_VOLTAGE_SHIFT = 16
    BATTERY_TEMPERATURE_SHIFT = 32
    BATTERY_HEALTH_SHIFT = 48
    BATTERY_STATUS_SHIFT = 52
    BATTERY_PLUG_TYPE_SHIFT = 56
    BATTERY_PRESENT_SHIFT = 60

    dictbatteryhealth = {  1:"Health_Unknown", 2:"Health_Good", 3:"Health_OverHeat", 4:"Health_Dead", 5:"Health_OverVoltage", 6:"Health_UnspecifiedFailure", 7:"Health_Cold"}
    dictbatterycharging = {1:"Charging_Unknown", 2:"Charging_Charging", 3:"Charging_Discharging", 4:"Charging_NotCharging", 5:"Charging_Full"}
    dictbatteryplugtype = {0:"PlugType_None", 1:"PlugType_AC", 2:"PlugType_USB", 3:"PlugType_None" }

    ''' just get the last recode of eventid == 11, define each item. '''


    battery_level = None
    battery_voltage = None
    battery_temperature = None
    battery_health = None
    battery_charging = None
    battery_plugtype = None
    battery_present = None

    battery_low_enter_count = 0
    battery_low_exit_count = 0

    batterystatus_firstscanned = False

    for tupleBatteryInfo in listtupleBatteryInfos:
        battery_eventid, battery_value = tupleBatteryInfo[1], tupleBatteryInfo[2]
        if battery_eventid == 11 and batterystatus_firstscanned == False:
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

            batterystatus_firstscanned = True

        elif battery_eventid == 12  :
            battery_low_enter_count += 1

        elif battery_eventid == 13  :
            battery_low_exit_count += 1


    battery_plugtype_count = 0

    temp_plugtype = battery_plugtype

    for tupleBatteryInfo in listtupleBatteryInfos:
        battery_eventid, battery_value = tupleBatteryInfo[1], tupleBatteryInfo[2]
        if battery_eventid == 11 :
            if temp_plugtype != ( dictbatteryplugtype[(battery_value & BATTERY_PLUG_TYPE_MASK) >> BATTERY_PLUG_TYPE_SHIFT ] ):
                battery_plugtype_count += 1
                temp_plugtype =  dictbatteryplugtype[(battery_value & BATTERY_PLUG_TYPE_MASK) >> BATTERY_PLUG_TYPE_SHIFT ]


    battery_level_judge = None
    if battery_level != None and battery_level <11 :
        battery_level_judge = 1


    battery_temperature_judge = None
    if battery_temperature != None and battery_temperature > 40  :
        battery_temperature_judge = 1


    ''' gather the 10min  scenario '''
    if bGatheringSeqEvent10min == True :
        prevlistBatteryInfo = []
        for tupleBatteryInfo in listtupleBatteryInfos:
            battery_timestamp, battery_eventid, battery_value = tupleBatteryInfo
            if battery_eventid == 11 :
                TenMinBattery =  "Battery:" + dictbatteryplugtype[(battery_value & BATTERY_PLUG_TYPE_MASK) >> BATTERY_PLUG_TYPE_SHIFT ]
            elif battery_eventid == 12 :
                TenMinBattery = "Battery:LowEnter"
            elif battery_eventid == 13 :
                TenMinBattery = "Battery:LowExit"

            listlistSeqEvent10min.append( [battery_timestamp, TenMinBattery] )


            # '''save the action items '''
            # if battery_eventid == 11 :
                # if len(prevlistBatteryInfo) == 0 or  prevBatteryInfo[1] == TenMinBattery :
                    # prevBatteryInfo = [battery_timestamp, TenMinBattery]
                    # continue
                # elif prevBatteryInfo[1] != TenMinBattery :
                    # listlistSeqAction10min.append( prevBatteryInfo )
                    # prevBatteryInfo = [battery_timestamp, TenMinBattery]
        # ''' save the last prevBatteryInfo  '''
        # if battery_eventid == 11 and len(prevlistBatteryInfo) > 0 :
            # listlistSeqAction10min.append( prevBatteryInfo )


    return battery_level, battery_voltage, battery_temperature, battery_health, battery_charging, battery_plugtype, battery_plugtype_count, battery_low_enter_count, battery_low_exit_count, battery_level_judge, battery_temperature_judge

def get_LastUSBTAconnectivity_info(cur,querywhere ):
    querybattery = "select %s from %s " % (f00n_battery_info, table_battery_info )
    querybattery += querywhere
    cur.execute( querybattery )
    listtupleBatteryInfos = cur.fetchall()
    listtupleBatteryInfos.sort(reverse=True)

    retstr = "PlugType_None"
    dictbatteryplugtype = {0:"PlugType_None", 1:"PlugType_AC", 2:"PlugType_USB", 3:"PlugType_None" }

    BATTERY_PLUG_TYPE_MASK = 0x0300000000000000L
    BATTERY_PLUG_TYPE_SHIFT = 56

    for tupleBatteryInfo in listtupleBatteryInfos:
        battery_eventid, battery_value = tupleBatteryInfo[1], tupleBatteryInfo[2]
        if battery_eventid == 11 :
            battery_plugtype = (battery_value & BATTERY_PLUG_TYPE_MASK) >> BATTERY_PLUG_TYPE_SHIFT
            retstr = dictbatteryplugtype[battery_plugtype]
            break

    return retstr

def get_BatteryLevel_info(cur,querywhere ):
    querybattery = "select %s from %s " % (f00n_battery_info, table_battery_info )
    querybattery += querywhere
    cur.execute( querybattery )
    listtupleBatteryInfos = cur.fetchall()

    listlistBatteryLevel = []
    BATTERY_LEVEL_MASK = 0x000000000000FFFFL

    for tupleBatteryInfo in listtupleBatteryInfos:
        timestamp, battery_eventid, battery_value = tupleBatteryInfo
        if battery_eventid == 11 :
            battery_level = battery_value & BATTERY_LEVEL_MASK
            listlistBatteryLevel.append ( [timestamp, battery_level] )

    return listlistBatteryLevel



## get the App list when  voltage level drop to 5 % during 10 minute  = -5 / ( 10 * 60 )  =  0.0083 --> -9 slope
## get the App list when  Temperature level raised to 45 degree during 5 minutes
def getCurrentThermalApp ( cur, querywhere ) :
    querybattery = "select %s from %s " % (f00n_battery_info, table_battery_info )
    querybattery += querywhere
    cur.execute( querybattery )
    listtupleBatteryInfos = cur.fetchall()
    listtupleBatteryInfos.sort()

    BATTERY_LEVEL_MASK = 0x000000000000FFFFL
    BATTERY_VOLTAGE_MASK = 0x00000000FFFF0000L
    BATTERY_TEMPERATURE_MASK = 0x0000FFFF00000000L
    BATTERY_HEALTH_MASK = 0x000F000000000000L
    BATTERY_SATUS_MASK = 0x00F0000000000000L
    #BATTERY_PLUG_TYPE_MASK = 0x0F00000000000000L
    BATTERY_PLUG_TYPE_MASK = 0x0300000000000000L    # for mask value adjustment due to abnormal value
    BATTERY_PRESENT_MASK = 0x7000000000000000L

    BATTERY_VOLTAGE_SHIFT = 16
    BATTERY_TEMPERATURE_SHIFT = 32
    BATTERY_HEALTH_SHIFT = 48
    BATTERY_STATUS_SHIFT = 52
    BATTERY_PLUG_TYPE_SHIFT = 56
    BATTERY_PRESENT_SHIFT = 60


    batterykeys =  [ "battery_timestamp", "battery_level", "battery_temperature", "batterylevel_slope" ]
    ##  battery_timestamp : 8 sec unit.
    ##  battery_level     : 4 level unit
    ##  battery_temperature : 2 degree unit

    listdictbatteryleveltemp = []
    previoustimestamp = 0
    for tupleBatteryInfo in listtupleBatteryInfos:
        timestamp, battery_eventid, battery_value = tupleBatteryInfo

        if battery_eventid == 11 :
            ## converet time unit from milisecond to second, and  make time  8 second step.
            timestamp = (( timestamp / 1000 ) >> 3 ) << 3
            if timestamp > previoustimestamp :
                battery_level = (battery_value & BATTERY_LEVEL_MASK ) & 0xfffc
                battery_temperature = (((battery_value & BATTERY_TEMPERATURE_MASK) >> BATTERY_TEMPERATURE_SHIFT ) / 10) & 0xfffe
                listdictbatteryleveltemp.append( dict(zip(batterykeys, (timestamp,battery_level, battery_temperature, 0 ))) )

            previoustimestamp = timestamp

    listtupleBatteryInfos = []

    if len(listdictbatteryleveltemp) == 0 :
        return 0, "", 0, ""

    # calculate the battery slope at each timestamp
    previoustimestamp = 0
    previousbatterylevel = listdictbatteryleveltemp[0]["battery_level"]
    for dictbatteryleveltemp in listdictbatteryleveltemp :
        timestamp = dictbatteryleveltemp["battery_timestamp"]
        battery_level = dictbatteryleveltemp["battery_level"]
        battery_slope = ((battery_level - previousbatterylevel ) * 1000 ) / ( timestamp - previoustimestamp )
        dictbatteryleveltemp["batterylevel_slope"] = battery_slope
        previoustimestamp = timestamp
        previousbatterylevel = battery_level

    ## search the time period with which battery_slope is under -9
    begintimestamp = 0   # meaning that it is beginning point to calculate
    endtimestamp = 0

    boolDuringCalcalute = False
    CHECKSLOPEVALUE = -9

    retLevelApplist = ""
    retLevelAppCount = 0

    # print "battery level processing .... "
    for dictbatteryleveltemp in listdictbatteryleveltemp :
        battery_slope = dictbatteryleveltemp["batterylevel_slope"]
        # print ConvertTimeStampToString(dictbatteryleveltemp["battery_timestamp"] * 1000 ) + "," + str(dictbatteryleveltemp["battery_level"]) + "," + str(battery_slope)
        if battery_slope > CHECKSLOPEVALUE :
            if begintimestamp != 0 and endtimestamp != 0 :
                ## check the 10 minute duration of voltage level.
                if (endtimestamp - begintimestamp ) > ( 10 * 60 ) :
                    # print "LLLL endtimestamp - begintimestamp : " + ConvertTimeStampToString(endtimestamp * 1000 ) + "," + ConvertTimeStampToString(begintimestamp * 1000 )
                    # begintimestamp is  advanced during 1 minute because the caused app is launched in advance
                    querywhere = " where  f002 > %s and f002 <= %s " % ((begintimestamp - 60) * 1000 , endtimestamp * 1000 )
                    retLevelApplist += getLatestApp ( cur , querywhere ) + ","
                    retLevelAppCount += 1

            begintimestamp = 0
            endtimestamp = 0
            continue
        else :
            if begintimestamp == 0 :
                begintimestamp = dictbatteryleveltemp["battery_timestamp"]
                continue
            else :
                endtimestamp = dictbatteryleveltemp["battery_timestamp"]
                continue



    ## search the time period with which temperature is over 40
    begintimestamp = 0   # meaning that it is beginning point to calculate
    endtimestamp = 0
    boolDuringCalcalute = False

    retTemperatureApplist = ""
    retTemperatureAppCount = 0

    CHECKTEMPERATURE = 40

    # print "termperature processing .... "
    for dictbatteryleveltemp in listdictbatteryleveltemp :
        temp_value = dictbatteryleveltemp["battery_temperature"]
        # print ConvertTimeStampToString(dictbatteryleveltemp["battery_timestamp"] * 1000 ) + "," + str(temp_value)
        if temp_value < CHECKTEMPERATURE :
            if begintimestamp != 0 and endtimestamp != 0 :
                ## check the 5 minute duration of temperature.
                if (endtimestamp - begintimestamp ) > ( 5 * 60 ) :
                    # print "TTTT endtimestamp - begintimestamp : " + ConvertTimeStampToString(endtimestamp * 1000 ) + "," + ConvertTimeStampToString(begintimestamp * 1000 )
                    # begintimestamp is  advanced during 1 minute because the caused app is launched in advance
                    querywhere = " where  f002 > %s and f002 <= %s" % ((begintimestamp - 60) * 1000 , endtimestamp * 1000 )
                    retTemperatureApplist += getLatestApp ( cur , querywhere ) + ","
                    retTemperatureAppCount += 1
            begintimestamp = 0
            endtimestamp = 0
            continue
        else :
            if begintimestamp == 0 :
                begintimestamp = dictbatteryleveltemp["battery_timestamp"]
                continue
            else :
                endtimestamp = dictbatteryleveltemp["battery_timestamp"]
                continue

    return retLevelAppCount, retLevelApplist, retTemperatureAppCount, retTemperatureApplist

def getBatteryLevelDropCountDuringLCDOff(listdictDBDump) :
    listdictDBDump.sort(cmp=TimeStampCmpDict)

    totaldiffsum = 0
    totaldiffcount = 0

    count4diff = 0
    count6diff = 0
    count8diff = 0
    count10diff = 0
    count12diff = 0

    BatteryLevelOn = 0
    BatteryLevelOff = 0
    LCD_ON = 0
    LCD_OFF = 0
    for dictDBDump in listdictDBDump :
        value = dictDBDump.get("power_state", None)
        if value == "POWER_ON" :
            BatteryLevelOn = 0
            BatteryLevelOff = 0
            LCD_ON = 0
            LCD_OFF = 0
            continue

        value = dictDBDump.get("lcd_state", None)
        if value != None :
            if value == "LCD_ON" :
                LCD_ON = 1
                continue
            elif value == "LCD_OFF" :
                LCD_OFF = 1
                continue

        value = dictDBDump.get("battery_level", None)
        if value != None :
            if LCD_OFF == 1 and BatteryLevelOff == 0 :
                BatteryLevelOff = value
                continue
            elif LCD_OFF == 1 and LCD_ON == 1 and BatteryLevelOff > 0 :
                BatteryLeveldiff = BatteryLevelOff - value

                if BatteryLeveldiff > 0 :
                    totaldiffsum += BatteryLeveldiff
                    totaldiffcount += 1

                if BatteryLeveldiff > 4 :
                    count4diff += 1
                    if BatteryLeveldiff > 6 :
                        count6diff += 1
                        if BatteryLeveldiff > 8 :
                            count8diff += 1
                            if BatteryLeveldiff > 10 :
                                count10diff += 1
                                if BatteryLeveldiff > 12 :
                                    count12diff += 1

                BatteryLevelOn = 0
                BatteryLevelOff = 0
                LCD_ON = 0
                LCD_OFF = 0
                continue
    totalavr = 0
    if  totaldiffcount != 0 :
        totalavr = float(totaldiffsum )/ float(totaldiffcount)
    return totalavr, count4diff,count6diff,count8diff,count10diff,count12diff




def get_telephony_info(cur,querywhere ):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min
    querytelephony = "select count(f001) from %s " % (table_telephony_info )
    querytelephony += querywhere

    ''' get the count of STATE_OUT_OF_SERVICE '''
    additionalwhere = " and f003 = 31 and f004 = 1"
    cur.execute(querytelephony + additionalwhere )
    STATE_OUT_OF_SERVICE_count = cur.fetchall()[0][0]

    ''' get the count of STATE_EMERGENCY_ONLY '''
    additionalwhere = " and f003 = 31 and f004 = 2"
    cur.execute(querytelephony + additionalwhere )
    STATE_EMERGENCY_ONLY_count = cur.fetchall()[0][0]

    ''' get the count of STATE_POWER_OFF '''
    additionalwhere = " and f003 = 31 and f004 = 3"
    cur.execute(querytelephony + additionalwhere )
    STATE_POWER_OFF_count = cur.fetchall()[0][0]

    ''' get the count of DATA_DISCONNECTED '''
    additionalwhere = " and f003 = 32 and f004 = 0"
    cur.execute(querytelephony + additionalwhere )
    DATA_DISCONNECTED_count = cur.fetchall()[0][0]

    ''' get the count of DATA_CONNECTED '''
    additionalwhere = " and f003 = 32 and f004 = 2"
    cur.execute(querytelephony + additionalwhere )
    DATA_CONNECTED_count = cur.fetchall()[0][0]

    ''' get the count of DATA_SUSPENDED '''
    additionalwhere = " and f003 = 32 and f004 = 3"
    cur.execute(querytelephony + additionalwhere )
    DATA_SUSPENDED_count = cur.fetchall()[0][0]

    ''' get the count of CALL_STATE_RINGING '''
    additionalwhere = " and f003 = 33 and f004 = 1"
    cur.execute(querytelephony + additionalwhere )
    CALL_STATE_RINGING_count = cur.fetchall()[0][0]

    ''' get the count of  CALL_STATE_OFFHOOK '''
    additionalwhere = " and f003 = 33 and f004 = 2"
    cur.execute(querytelephony + additionalwhere )
    CALL_STATE_OFFHOOK_count = cur.fetchall()[0][0]

    querytelephony = "select %s from %s " % (f00n_telephony_info, table_telephony_info )
    querytelephony += querywhere
    cur.execute( querytelephony )
    listtupleTelePhonyInfos = cur.fetchall()
    listtupleTelePhonyInfos.sort(reverse=True)

    TELEPHONY_SERVICE_STATE = None
    TELEPHONY_DATACOMM_STATE = None
    TELEPHONY_CALL_STATE = None

    dictServiceState = { 0:"STATE_IN_SERVICE", 1:"STATE_OUT_OF_SERVICE", 2:"STATE_EMERGENCY_ONLY", 3:"STATE_POWER_OFF" }
    dictDataCommState = { 0:"DATA_DISCONNECTED", 1:"DATA_CONNECTING", 2:"DATA_CONNECTED", 3:"DATA_SUSPENDED" }
    dictCallState  = { 0:"CALL_STATE_IDLE", 1:"CALL_STATE_RINGING", 2:"CALL_STATE_OFFHOOK" }

    for tupleTelePhonyInfos in listtupleTelePhonyInfos :
        timestamp, statetype, statevalue = tupleTelePhonyInfos
        if statevalue == -1 :
            continue
        if TELEPHONY_SERVICE_STATE != None and TELEPHONY_DATACOMM_STATE != None and TELEPHONY_CALL_STATE != None :
            break
        if TELEPHONY_SERVICE_STATE == None and statetype == 31 :
            TELEPHONY_SERVICE_STATE = dictServiceState[statevalue]
        if TELEPHONY_DATACOMM_STATE == None and statetype == 32 :
            TELEPHONY_DATACOMM_STATE = dictDataCommState[statevalue]
        if TELEPHONY_CALL_STATE == None and statetype == 33 :
            TELEPHONY_CALL_STATE = dictCallState[statevalue]

    ''' gather the 10min's scenario '''
    if bGatheringSeqEvent10min == True :
        for tupleTelePhonyInfos in listtupleTelePhonyInfos :
            timestamp, statetype, statevalue = tupleTelePhonyInfos
            if statevalue == -1 :
                continue

            if statetype == 31 :
                TenMinPhoneStatus = "TelePhone:" + dictServiceState[statevalue]
            elif statetype == 32 :
                TenMinPhoneStatus = "TelePhone:" + dictDataCommState[statevalue]
            elif statetype == 33 :
                TenMinPhoneStatus = "TelePhone:" + dictCallState[statevalue]
                listlistSeqAction10min.append(  [timestamp, TenMinPhoneStatus] )

            listlistSeqEvent10min.append( [timestamp, TenMinPhoneStatus] )

    return (STATE_OUT_OF_SERVICE_count, STATE_EMERGENCY_ONLY_count, STATE_POWER_OFF_count,
            DATA_DISCONNECTED_count, DATA_CONNECTED_count, DATA_SUSPENDED_count,
            CALL_STATE_RINGING_count, CALL_STATE_OFFHOOK_count, TELEPHONY_SERVICE_STATE, TELEPHONY_DATACOMM_STATE, TELEPHONY_CALL_STATE   )

def BuildupCallDump(listdictCallDump, strPhoneType, listdictDBDump) :
    global listdictKeyCallDump

    listdictDBDump.sort(cmp=TimeStampCmpDict)

    phonetype = 0       # default type : CDMA
    if strPhoneType ==  "GSM" :
        phonetype = 1

    callinout = "call_out"
    callstarttimestamp = 0
    calltimestampdiff = 0
    callsigalstrength = 10
    callsigalstrengthLowest = 10
    callmovecount = 0
    callregionID = -1
    callstarting = 0
    save_pre_call_duration = 0
    save_pre_callend_time = 0
    call_continue_retry = 0
    callsignalgabcount = -1
    pre_sigalstrength = 10
    
    sw_ver = ""
    os_ver = ""

    for dictDBDump in listdictDBDump :
    
        os_ver = dictDBDump.get("os_ver", os_ver)
        
        sw_ver = dictDBDump.get("exception_swver", sw_ver)
        sw_ver = dictDBDump.get("register_svwer", sw_ver)
            
        temp_exception = dictDBDump.get("exception_type", None)
        if temp_exception == "exception_calldrop" :
            temp_timestamp = dictDBDump.get("timestamp", None)
            dicttemp = dict(zip(listdictKeyCallDump, (temp_timestamp,0,os_ver, sw_ver,"call_drop",-1, -1, -1, -1  )))
            listdictCallDump.append(dicttemp)
            continue

        callstate = dictDBDump.get("callcomm_state", None)
        if callstate != None :
            if callstate == "CALL_STATE_IDLE" :
                if callstarttimestamp > 0 :
                    calltimestampdiff = dictDBDump.get("timestamp", None) - callstarttimestamp
                    save_pre_call_duration = calltimestampdiff
                    save_pre_callend_time = dictDBDump.get("timestamp", None)
                    callmovecount -= 1
                    if callmovecount < 0 :
                        callmovecount = 0
                    if callsigalstrengthLowest == 10 :      # no signal during calling, if then, replace callsigalstrengthLowest with callsigalstrength
                        callsigalstrengthLowest = callsigalstrength
                    dicttemp = dict(zip(listdictKeyCallDump, (callstarttimestamp,calltimestampdiff,os_ver,sw_ver, callinout,callmovecount, callsigalstrengthLowest, call_continue_retry, callsignalgabcount  )))
                    listdictCallDump.append(dicttemp)

                callinout = "call_out"
                callstarttimestamp = 0
                calltimestampdiff = 0
                callsigalstrengthLowest = 10
                callmovecount = 0
                callregionID = -1
                callstarting = 0
                call_continue_retry = 0
                callsignalgabcount = -1
                pre_sigalstrength = 10

            elif callstate == "CALL_STATE_RINGING" :
                callinout = "call_in"
                callstarting =1
            elif callstate == "CALL_STATE_OFFHOOK" :
                # print callinout
                callstarting =1
                callstarttimestamp = dictDBDump.get("timestamp", None)
                difftime = callstarttimestamp - save_pre_callend_time
                if save_pre_call_duration != 0 and save_pre_call_duration <= (5*1000) and (difftime) <= (5*1000) :
                    call_continue_retry = 1


        if phonetype == 0 :         # CDMA
            sigalstrength = dictDBDump.get("cdma_level", None)
            if sigalstrength != None :
                callsigalstrength = sigalstrength

            if callstarting == 1  :
                if sigalstrength != None and callsigalstrengthLowest > sigalstrength :
                    callsigalstrengthLowest = sigalstrength

                if sigalstrength != None and (pre_sigalstrength - sigalstrength) >= 2:
                    callsignalgabcount += 1

                if sigalstrength != None:
                    pre_sigalstrength = sigalstrength

                regionID = dictDBDump.get("cdma_bsid", None)
                if regionID != None and regionID != -1 and callregionID != regionID :
                    callregionID = regionID
                    callmovecount += 1
        else:                       # GSM
            sigalstrength = dictDBDump.get("gsm_level", None)
            if sigalstrength != None :
                callsigalstrength = sigalstrength

            if callstarting == 1 :

                if sigalstrength != None and callsigalstrengthLowest > sigalstrength :
                    callsigalstrengthLowest = sigalstrength

                if sigalstrength != None and (pre_sigalstrength - sigalstrength) >= 2:
                    callsignalgabcount += 1

                if sigalstrength != None:
                    pre_sigalstrength = sigalstrength

                regionID = dictDBDump.get("gsm_cid", None)
                if regionID != None and regionID != -1 and callregionID != regionID :
                    callregionID = regionID
                    callmovecount += 1

def BuildupCallDrop(listdictCallDrop, strPhoneType, listdictDBDump) :
    global listdictKeyCallDrop

    listdictDBDump.sort(cmp=TimeStampCmpDict)
    
    prev_cdma_lat = 0 
    prev_cdma_long = 0 
    
    prev_gsm_cid = 0 
    prev_gsm_lac = 0 
    
    for dictDBDump in listdictDBDump :
    
        cdma_bsid = dictDBDump.get("cdma_bsid", None)
        if cdma_bsid != None :
            if cdma_bsid == -1 :
                continue 
            else : 
                prev_cdma_lat = dictDBDump.get("cdma_bslat", None)
                prev_cdma_long = dictDBDump.get("cdma_bslong", None)
                continue 
                
        tempvalue = dictDBDump.get("gsm_cid", None)
        if tempvalue != None :
            prev_gsm_cid = dictDBDump.get("gsm_cid", None)
            prev_gsm_lac = dictDBDump.get("gsm_lac", None)
            if prev_gsm_cid == -1  or prev_gsm_lac == -1 :
                prev_gsm_cid = 0 
                prev_gsm_lac = 0
                continue 
            else : 
                continue 
                
        excpt_calldrop = dictDBDump.get("exception_type", None)
        if excpt_calldrop == "exception_calldrop" : 
            timestamp = dictDBDump.get("timestamp", None)
            dicttemp = dict(zip(listdictKeyCallDrop, (timestamp,"",prev_cdma_lat,prev_cdma_long, prev_gsm_cid, prev_gsm_lac  )))
            listdictCallDrop.append(dicttemp)

    
    
def get_connectivity_info(cur,querywhere ):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min
    queryconnectivity = "select count(f001) from %s " % (table_connectivity_info )
    queryconnectivity += querywhere

    ''' get the count of EARJACK_STATE_UNPLUGGED '''
    additionalwhere = " and f003 = 21 and f004 = 0"
    cur.execute(queryconnectivity + additionalwhere )
    count_EARJACK_STATE_UNPLUGGED = cur.fetchall()[0][0]

    ''' get the count of EARJACK_STATE_PLUGGED '''
    additionalwhere = " and f003 = 21 and f004 = 1"
    cur.execute(queryconnectivity + additionalwhere )
    count_EARJACK_STATE_PLUGGED = cur.fetchall()[0][0]

    ''' get the count of GPS_STATUS_STARTED '''
    additionalwhere = " and f003 = 41 and f004 = 1"
    cur.execute(queryconnectivity + additionalwhere )
    count_GPS_STATUS_STARTED = cur.fetchall()[0][0]

    ''' get the count of GPS_STATUS_STOPPED '''
    additionalwhere = " and f003 = 41 and f004 = 2"
    cur.execute(queryconnectivity + additionalwhere )
    count_GPS_STATUS_STOPPED = cur.fetchall()[0][0]

    ''' get the count of BATTERY_PLUGGED_AC '''
    additionalwhere = " and f003 = 51 and f004 = 1"
    cur.execute(queryconnectivity + additionalwhere )
    count_BATTERY_PLUGGED_AC = cur.fetchall()[0][0]

    ''' get the count of BATTERY_PLUGGED_USB '''
    additionalwhere = " and f003 = 51 and f004 = 2"
    cur.execute(queryconnectivity + additionalwhere )
    count_BATTERY_PLUGGED_USB = cur.fetchall()[0][0]

    ''' get the count of UMS_ON '''
    additionalwhere = " and f003 = 61 and f004 = 1"
    cur.execute(queryconnectivity + additionalwhere )
    count_UMS_ON = cur.fetchall()[0][0]

    ''' get the count of  UMS_OFF '''
    additionalwhere = " and f003 = 61 and f004 = 2"
    cur.execute(queryconnectivity + additionalwhere )
    count_UMS_OFF = cur.fetchall()[0][0]

    '''----------------------------------------------------------'''
    queryconnectivity = "select %s from %s " % (f00n_connectivity_info, table_connectivity_info )
    queryconnectivity += querywhere
    cur.execute( queryconnectivity )
    listtupleConnectivityInfos = cur.fetchall()
    listtupleConnectivityInfos.sort(reverse=True)

    COMM_EARJAcK_STATE = None
    COMM_GPS_STATE = None
    COMM_GPSSTATUS_STATE = None
    COMM_USBTA_STATE = None
    COMM_UMS_STATE = None

    dictEarJackState = { -1:"EARJACK_STATE_UNKNOWN", 0:"EARJACK_STATE_UNPLUGGED", 1:"EARJACK_STATE_PLUGGED" }
    dictGPSState = { 0:"GPS_STATUS_UNKNOWN", 1:"GPS_STATUS_STARTED", 2:"GPS_STATUS_STOPPED" }

    dictGPSStatusState  = { 1:"GPS_EVENT_STARTED", 2:"GPS_EVENT_STOPPED", 3:"GPS_EVENT_FIRST_FIX", 4:"GPS_EVENT_SATELLITE_STATUS", 5:"GPS_FIX_CHANGED" }
    dictUSBTAState  = { 0 :"BATTERY_PLUGGED_NONE", 1:"BATTERY_PLUGGED_AC", 2:"BATTERY_PLUGGED_USB" }
    dictUMSState  = {  1:"UMS_ON", 2:"UMS_OFF" }

    for tupleConnectivityInfos in listtupleConnectivityInfos :
        timestamp, statetype, statevalue = tupleConnectivityInfos
        if COMM_EARJAcK_STATE != None and COMM_GPS_STATE != None and COMM_GPSSTATUS_STATE != None and COMM_USBTA_STATE != None and COMM_UMS_STATE != None :
            break
        if COMM_EARJAcK_STATE == None and statetype == 21 :
            COMM_EARJAcK_STATE = dictEarJackState[statevalue]
        if COMM_GPS_STATE == None and statetype == 41 :
            COMM_GPS_STATE = dictGPSState[statevalue]
        if COMM_GPSSTATUS_STATE == None and statetype == 42 :
            COMM_GPSSTATUS_STATE = dictGPSStatusState[statevalue]
        if COMM_USBTA_STATE == None and statetype == 51 :
            COMM_USBTA_STATE = dictUSBTAState[statevalue]
        if COMM_UMS_STATE == None and statetype == 61 :
            COMM_UMS_STATE = dictUMSState[statevalue]

    ''' gather the 10min's scenario '''
    if bGatheringSeqEvent10min == True :
        for tupleConnectivityInfos in listtupleConnectivityInfos :
            timestamp, statetype, statevalue = tupleConnectivityInfos

            if statetype == 21 :
                TenMinConnect = "connect:" + dictEarJackState[statevalue]
            elif statetype == 41 :
                TenMinConnect = "connect:" + dictGPSState[statevalue]
            elif statetype == 42 :
                TenMinConnect = "connect:" + dictGPSStatusState[statevalue]
            elif statetype == 51 :
                TenMinConnect = "connect:" + dictUSBTAState[statevalue]
            elif statetype == 61 :
                TenMinConnect = "connect:" + dictUMSState[statevalue]

            listlistSeqEvent10min.append( [timestamp, TenMinConnect] )
            if statetype in [21, 41, 51, 61] :
                listlistSeqAction10min.append( [timestamp, TenMinConnect] )


    return (count_EARJACK_STATE_UNPLUGGED, count_EARJACK_STATE_PLUGGED, count_GPS_STATUS_STARTED,
            count_GPS_STATUS_STOPPED, count_BATTERY_PLUGGED_AC,count_BATTERY_PLUGGED_USB,
            count_UMS_ON, count_UMS_OFF,  COMM_EARJAcK_STATE, COMM_GPS_STATE, COMM_GPSSTATUS_STATE, COMM_USBTA_STATE, COMM_UMS_STATE   )





def get_bluetooth_info(cur,querywhere ):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min
    querybluetooth = "select count(f001) from %s " % (table_bluetooth_info )
    querybluetooth += querywhere

    ''' get the count of bluetooth_BT_ADAPTER_OFF_count '''
    additionalwhere = " and f003 = 11 and f004 = 13"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_ADAPTER_OFF = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_ADAPTER_ON_count '''
    additionalwhere = " and f003 = 11 and f004 = 11"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_ADAPTER_ON = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_HEADSET_DISCONNECTED_count '''
    additionalwhere = " and f003 = 12 and f004 = 0"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_HEADSET_DISCONNECTED = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_HEADSET_CONNECTED_count '''
    additionalwhere = " and f003 = 12 and f004 = 2"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_HEADSET_CONNECTED = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_A2DP_DISCONNECTED_count '''
    additionalwhere = " and f003 = 13 and f004 = 0"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_A2DP_DISCONNECTED = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_A2DP_CONNECTED_count '''
    additionalwhere = " and f003 = 13 and f004 = 2"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_A2DP_CONNECTED = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_A2DP_PLAYING_count '''
    additionalwhere = " and f003 = 13 and f004 = 4"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_A2DP_PLAYING = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_PBAP_DISCONNECTED_count '''
    additionalwhere = " and f003 = 14 and f004 = 0"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_PBAP_DISCONNECTED = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_PBAP_CONNECTED_count '''
    additionalwhere = " and f003 = 14 and f004 = 2"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_PBAP_CONNECTED = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_DEVICE_DISCONNECTED_count '''
    additionalwhere = " and f003 = 15 and f004 = 6"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_DEVICE_DISCONNECTED = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_DEVICE_CONNECTED_count '''
    additionalwhere = " and f003 = 15 and f004 = 5"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_DEVICE_CONNECTED = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_DEVICE_DISCONNECTED_REQ_count '''
    additionalwhere = " and f003 = 15 and f004 = 7"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_DEVICE_DISCONNECTED_REQ = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_BOND_NONE_count '''
    additionalwhere = " and f003 = 16 and f004 = 10"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_BOND_NONE = cur.fetchall()[0][0]

    ''' get the count of bluetooth_BT_BOND_BONDED_count '''
    additionalwhere = " and f003 = 16 and f004 = 12"
    cur.execute(querybluetooth + additionalwhere )
    count_BT_BOND_BONDED = cur.fetchall()[0][0]

    '''----------------------------------------------------------'''
    querybluetooth = "select %s from %s " % (f00n_bluetooth_info, table_bluetooth_info )
    querybluetooth += querywhere
    cur.execute( querybluetooth )
    listtupleBluetoothInfos = cur.fetchall()
    listtupleBluetoothInfos.sort(reverse=True)

    BLUETOOTH_ADAPTER_STATE = None
    BLUETOOTH_HEADSET_STATE = None
    BLUETOOTH_A2DP_STATE = None
    BLUETOOTH_PBAP_STATE = None
    BLUETOOTH_DEVICE_STATE = None
    BLUETOOTH_BOND_STATE = None

    dictAdapterState = { -1:"STATE_UNKNOWN",  10:"STATE_OFF", 11:"STATE_TURNING_ON", 12:"STATE_ON", 13:"STATE_TURNING_OFF" }
    dictHeadsetState = { -1:"BT_STATE_ERROR", 0:"BT_STATE_DISCONNECTED", 1:"BT_STATE_CONNECTING", 2:"BT_STATE_CONNECTED" }
    dictA2DPState = { -1:"BT_STATE_ERROR", 0:"BT_STATE_DISCONNECTED", 1:"BT_STATE_CONNECTING", 2:"BT_STATE_CONNECTED", 3:"BT_STATE_DISCONNECTING", 4:"BT_STATE_PLAYING" }
    dictPBAPState = { -1:"BT_STATE_ERROR", 0:"BT_STATE_DISCONNECTED", 1:"BT_STATE_CONNECTING", 2:"BT_STATE_CONNECTED" }
    dictDeviceState = { 5:"BT_STATE_ACL_CONNECTED", 6:"BT_STATE_ACL_DISCONNECTED", 7:"BT_STATE_ACL_DISCONNECT_REQUESTED" }
    dictBondState = { -1:"BT_BOND_STATE_UNKNOWN", 10:"BT_BOND_STATE_NONE", 11:"BT_BOND_STATE_BONDING", 12:"BT_BOND_STATE_BONDED" }


    for tupleBluetoothInfos in listtupleBluetoothInfos :
        timestamp, statetype, statevalue = tupleBluetoothInfos

        if BLUETOOTH_ADAPTER_STATE != None and BLUETOOTH_HEADSET_STATE != None and BLUETOOTH_A2DP_STATE != None and BLUETOOTH_PBAP_STATE != None and BLUETOOTH_DEVICE_STATE != None and BLUETOOTH_BOND_STATE != None :
            break
        if BLUETOOTH_ADAPTER_STATE == None and statetype == 11 :
            BLUETOOTH_ADAPTER_STATE = dictAdapterState[statevalue]
        if BLUETOOTH_HEADSET_STATE == None and statetype == 12 :
            BLUETOOTH_HEADSET_STATE = dictHeadsetState[statevalue]
        if BLUETOOTH_A2DP_STATE == None and statetype == 13 :
            BLUETOOTH_A2DP_STATE = dictA2DPState[statevalue]
        if BLUETOOTH_PBAP_STATE == None and statetype == 14 :
            BLUETOOTH_PBAP_STATE = dictPBAPState[statevalue]
        if BLUETOOTH_DEVICE_STATE == None and statetype == 15 :
            BLUETOOTH_DEVICE_STATE = dictDeviceState[statevalue]
        if BLUETOOTH_BOND_STATE == None and statetype == 16 :
            BLUETOOTH_BOND_STATE = dictBondState[statevalue]

    ''' gather the 10min's scenario '''
    if bGatheringSeqEvent10min == True :
        for tupleBluetoothInfos in listtupleBluetoothInfos :
            timestamp, statetype, statevalue = tupleBluetoothInfos

            if statetype == 11 :
                TenMinBluetooth = "Bluetooth:" + dictAdapterState[statevalue]
            elif statetype == 12 :
                TenMinBluetooth = "Bluetooth:" + dictHeadsetState[statevalue]
            elif statetype == 13 :
                TenMinBluetooth = "Bluetooth:" + dictA2DPState[statevalue]
            elif statetype == 14 :
                TenMinBluetooth = "Bluetooth:" + dictPBAPState[statevalue]
            elif statetype == 15 :
                TenMinBluetooth = "Bluetooth:" + dictDeviceState[statevalue]
            elif statetype == 16 :
                if not statevalue in [10, 11, 12] :
                    continue
                TenMinBluetooth = "Bluetooth:" + dictBondState[statevalue]

            listlistSeqEvent10min.append( [timestamp, TenMinBluetooth] )
            listlistSeqAction10min.append( [timestamp, TenMinBluetooth] )


    return (count_BT_ADAPTER_OFF, count_BT_ADAPTER_ON,
            count_BT_HEADSET_DISCONNECTED, count_BT_HEADSET_CONNECTED,
            count_BT_A2DP_DISCONNECTED, count_BT_A2DP_CONNECTED, count_BT_A2DP_PLAYING,
            count_BT_PBAP_DISCONNECTED, count_BT_PBAP_CONNECTED,
            count_BT_DEVICE_DISCONNECTED, count_BT_DEVICE_CONNECTED,  count_BT_DEVICE_DISCONNECTED_REQ,
            count_BT_BOND_NONE, count_BT_BOND_BONDED, BLUETOOTH_ADAPTER_STATE,BLUETOOTH_HEADSET_STATE,
        BLUETOOTH_A2DP_STATE, BLUETOOTH_PBAP_STATE,BLUETOOTH_DEVICE_STATE,BLUETOOTH_BOND_STATE  )


def get_wifi_info(cur,querywhere ):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min
    querywifi = "select count(f001) from %s " % (table_wifi_info )
    querywifi += querywhere

    ''' get the count of wifi_WIFI_STATE_DISABLED_count1 '''
    additionalwhere = " and f003 = 31 and f004 = 1"
    cur.execute(querywifi + additionalwhere )
    count_WIFI_STATE_DISABLED = cur.fetchall()[0][0]

    ''' get the count of wifi_WIFI_STATE_ENABLED_count1 '''
    additionalwhere = " and f003 = 31 and f004 = 3"
    cur.execute(querywifi + additionalwhere )
    count_WIFI_STATE_ENABLED = cur.fetchall()[0][0]

    ''' get the count of wifi_WIFI_STATE_FAILED_count1 '''
    additionalwhere = " and f003 = 31 and f004 = 4"
    cur.execute(querywifi + additionalwhere )
    count_WIFI_STATE_FAILED = cur.fetchall()[0][0]

    ''' get the count of wifi_WIFI_NETWORK_STATE_DISABLED_count1 '''
    additionalwhere = " and f003 = 32 and f004 = 1"
    cur.execute(querywifi + additionalwhere )
    count_WIFI_NETWORK_STATE_DISABLED = cur.fetchall()[0][0]

    ''' get the count of wifi_WIFI_NETWORK_STATE_ENABLED_count1 '''
    additionalwhere = " and f003 = 32 and f004 = 3"
    cur.execute(querywifi + additionalwhere )
    count_WIFI_NETWORK_STATE_ENABLED = cur.fetchall()[0][0]

    ''' get the count of wifi_WIFI_NETWORK_STATE_FAILED_count1 '''
    additionalwhere = " and f003 = 32 and f004 = 4"
    cur.execute(querywifi + additionalwhere )
    count_WIFI_NETWORK_STATE_FAILED = cur.fetchall()[0][0]

    '''----------------------------------------------------------'''
    querywifi = "select %s from %s " % (f00n_wifi_info, table_wifi_info )
    querywifi += querywhere
    cur.execute( querywifi )
    listtupleWIFIInfos = cur.fetchall()
    listtupleWIFIInfos.sort(reverse=True)

    WIFI_STATE = None
    WIFI_NETWORK_STATE = None

    dictWIFIState = { -1:"WIFI_STATE_UNKNOWN", 0:"WIFI_STATE_DISABLING", 1:"WIFI_STATE_DISABLED", 2:"WIFI_STATE_ENABLING", 3:"WIFI_STATE_ENABLED", 4:"WIFI_STATE_FAILED" }
    dictWIFINetworkState = { -1:"WIFI_STATE_UNKNOWN", 0:"WIFI_STATE_DISABLING", 1:"WIFI_STATE_DISABLED", 2:"WIFI_STATE_ENABLING", 3:"WIFI_STATE_ENABLED", 4:"WIFI_STATE_FAILED" }


    for tupleWIFIInfos in listtupleWIFIInfos :
        timestamp, statetype, statevalue = tupleWIFIInfos

        if WIFI_STATE != None and WIFI_NETWORK_STATE != None :
            break
        if WIFI_STATE == None and statetype == 31 :
            WIFI_STATE = dictWIFIState[statevalue]
        if WIFI_NETWORK_STATE == None and statetype == 31 :
            WIFI_NETWORK_STATE = dictWIFINetworkState[statevalue]

    ''' gather the 10min's scenario '''
    if bGatheringSeqEvent10min == True :
        for tupleWIFIInfos in listtupleWIFIInfos :
            timestamp, statetype, statevalue = tupleWIFIInfos

            if statetype == 31 :
                TenMinWIFI = "WIFI:" + dictWIFIState[statevalue]
            elif statetype == 32 :
                TenMinWIFI = "WIFI:" + dictWIFINetworkState[statevalue]

            listlistSeqEvent10min.append( [timestamp, TenMinWIFI] )
            if statetype == 31 :
                listlistSeqAction10min.append( [timestamp, TenMinWIFI] )

    return (count_WIFI_STATE_DISABLED,count_WIFI_STATE_ENABLED, count_WIFI_STATE_FAILED,
            count_WIFI_NETWORK_STATE_DISABLED,count_WIFI_NETWORK_STATE_ENABLED, count_WIFI_NETWORK_STATE_FAILED,
        WIFI_STATE, WIFI_NETWORK_STATE )


def get_LastWIFIState(cur,querywhere ):
    querywifi = "select %s from %s " % (f00n_wifi_info, table_wifi_info )
    querywifi += querywhere
    cur.execute( querywifi )
    listtupleWIFIInfos = cur.fetchall()
    listtupleWIFIInfos.sort(reverse=True)

    dictWIFIState = { -1:"WIFI_STATE_UNKNOWN", 0:"WIFI_STATE_DISABLING", 1:"WIFI_STATE_DISABLED", 2:"WIFI_STATE_ENABLING", 3:"WIFI_STATE_ENABLED", 4:"WIFI_STATE_FAILED" }

    WIFI_STATE = "WIFI_STATE_UNKNOWN"

    for tupleWIFIInfos in listtupleWIFIInfos :
        timestamp, statetype, statevalue = tupleWIFIInfos

        if statetype != 31 :
            continue

        if statetype == 31 :
            WIFI_STATE = dictWIFIState[statevalue]
            break
    return WIFI_STATE





def get_power_info(cur,querywhere ):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min
    querypower = "select count(f001) from %s " % (table_power_info )
    querypower += querywhere

    ''' get the count of power_POWER_ON_count1 '''
    additionalwhere = " and f003 = 51 "
    cur.execute(querypower + additionalwhere )
    count_POWER_ON = cur.fetchall()[0][0]

    ''' get the count of power_POWER_OFF_count1 '''
    additionalwhere = " and f003 = 52 "
    cur.execute(querypower + additionalwhere )
    count_POWER_OFF = cur.fetchall()[0][0]

    '''----------------------------------------------------------'''
    querypower = "select %s from %s " % (f00n_power_info, table_power_info )
    querypower += querywhere
    cur.execute( querypower )
    listtuplePowerInfos = cur.fetchall()
    listtuplePowerInfos.sort(reverse=True)

    POWER_STATE = None

    for tuplePowerInfos in listtuplePowerInfos :
        timestamp ,  statetype = tuplePowerInfos
        if statetype == 51 :
            POWER_STATE = "POWER_ON"
            break
        if statetype == 52 :
            POWER_STATE = "POWER_OFF"
            break
        if statetype == 53 :
            continue

    ''' gather the 10min's scenario '''
    if bGatheringSeqEvent10min == True :
        for tuplePowerInfos in listtuplePowerInfos :
            timestamp ,  statetype = tuplePowerInfos

            if statetype == 51 :
                TenMinPower = "Power:On"
            elif statetype == 52 :
                TenMinPower = "Power:Off"
            elif statetype == 53 :
                TenMinPower = "Power:MLT_restart"
            else :
                continue

            listlistSeqEvent10min.append( [timestamp, TenMinPower] )
            if statetype in [51, 52] :
                listlistSeqAction10min.append( [timestamp, TenMinPower] )

    return ( count_POWER_ON, count_POWER_OFF,POWER_STATE )

def get_lcd_info(cur,querywhere ):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min
    querylcd = "select count(f001) from %s " % (table_lcd_info )
    querylcd += querywhere

    ''' get the count of lcd_LCD_ON_count1 '''
    additionalwhere = " and f003 = 61 "
    cur.execute(querylcd + additionalwhere )
    count_LCD_ON = cur.fetchall()[0][0]

    ''' get the count of lcd_LCD_OFF_count1 '''
    additionalwhere = " and f003 = 62 "
    cur.execute(querylcd + additionalwhere )
    count_LCD_OFF = cur.fetchall()[0][0]

    '''----------------------------------------------------------'''
    querylcd = "select %s from %s " % (f00n_lcd_info, table_lcd_info )
    querylcd += querywhere
    cur.execute( querylcd )
    listtupleLCDInfos = cur.fetchall()

    LCD_STATE = None

    listtupleLCDInfos.sort(reverse=True)



    for tupleLCDInfos in listtupleLCDInfos :
        timestamp ,  statetype = tupleLCDInfos
        if statetype == 61 :
            LCD_STATE = "LCD_ON"
            break
        if statetype == 62 :
            LCD_STATE = "LCD_OFF"
            break
        else  :
            continue

    ''' gather the 10min's scenario '''
    if bGatheringSeqEvent10min == True :
        for tupleLCDInfos in listtupleLCDInfos :
            timestamp ,  statetype = tupleLCDInfos

            if statetype == 61 :
                TenMinLCD = "LCD:On"
            elif statetype == 62 :
                TenMinLCD = "LCD:Off"
            listlistSeqEvent10min.append( [timestamp, TenMinLCD] )
            listlistSeqAction10min.append( [timestamp, TenMinLCD] )

    return ( count_LCD_ON, count_LCD_OFF, LCD_STATE )





def get_resource_info(cur,querywhere ):
    queryresource = "select count(f001) from %s " % (table_resource_info )
    queryresource += querywhere

    ''' get the count of resource_CPU_90_OVER_count1 '''
    additionalwhere = " and f003 >= 90 "
    cur.execute(queryresource + additionalwhere )
    CPU_90_OVER_count = cur.fetchall()[0][0]

    queryresource = "select AVG(f004) from %s " % (table_resource_info )
    queryresource += querywhere

    ''' get the count of resource_AVAIL_RAM_AVG1 '''
    cur.execute(queryresource  )
    AVAIL_RAM_AVG = cur.fetchall()[0][0]

    queryresource = "select count(f001) from %s " % (table_resource_info )
    queryresource += querywhere

    ''' get the count of resource_AVAIL_RAM_AVG_10M_count '''
    additionalwhere = " and f004 < 10000 "
    cur.execute(queryresource + additionalwhere )
    resource_AVAIL_RAM_AVG_10M_count = cur.fetchall()[0][0]



    '''----------------------------------------------------------'''
    queryresource = "select %s from %s " % (f00n_resource_info, table_resource_info )
    queryresource += querywhere

    cur.execute(queryresource )
    listtupleResourceInfos = cur.fetchall()


    CPU_Usage_90_Over_judge = 0
    Avail_Ram_STATE_10M_judge = 0

    if len(listtupleResourceInfos) > 0 :
        listtupleResourceInfos.sort(reverse=True)

        timestamp, CPU_Usage_STATE, Avail_Ram_STATE = listtupleResourceInfos[0]

        if CPU_Usage_STATE > 90 :
            CPU_Usage_90_Over_judge = 1
        else :
            CPU_Usage_90_Over_judge = 0

        if Avail_Ram_STATE < 10000 :
            Avail_Ram_STATE_10M_judge = 1
        else :
            Avail_Ram_STATE_10M_judge = 0



    return ( CPU_90_OVER_count, AVAIL_RAM_AVG, resource_AVAIL_RAM_AVG_10M_count, CPU_Usage_90_Over_judge, Avail_Ram_STATE_10M_judge )

''' save the previous routine for later modification.
def get_recentAct_info(cur,querywhere ):
    queryrecent = "select %s from %s " % (f00n_recentAct_info, table_recentAct_info )
    queryrecent += querywhere
    cur.execute(queryrecent)
    listtuplerecent = cur.fetchall()

    retRecentActivityText =""
    listRecentActivityText = ["", "", "", "", "", "", "", "", "", "" ]
    previousActivity = ""

    index = 0

    if len(listtuplerecent) > 0 :

        listtuplerecent.sort(reverse=True)

        for tuplerecent in listtuplerecent :
            recentlist = tuplerecent[1].split("\n")

            ret = recentlist[0].encode("utf-8")
            if previousActivity == ret:
                continue

            listRecentActivityText[index] = ret
            previousActivity = ret
            index = index + 1
            if index > 10 :
                break

        for recentitem in listRecentActivityText :
            if recentitem != "":
                retRecentActivityText += "<" + recentitem

    return retRecentActivityText , listRecentActivityText[0], listRecentActivityText[1], listRecentActivityText[2],
           listRecentActivityText[3], listRecentActivityText[4], listRecentActivityText[5],
           listRecentActivityText[6], listRecentActivityText[7], listRecentActivityText[8],
           listRecentActivityText[9]
'''

def get_recentAct_info(cur,querywhere ):
    global listrecentActivity
    listrecentActivity = []
    queryrecent = "select %s from %s " % (f00n_recentAct_info, table_recentAct_info )
    queryrecent += querywhere
    cur.execute(queryrecent)
    listtuplerecent = cur.fetchall()

    if len(listtuplerecent) == 0 :
        return "", "", "", "", "", "", "", "", "", "", ""

    retRecentActivityText =""
    listRecentActivityText = ["", "", "", "", "", "", "", "", "", "" ]

    listtuplerecent.sort(reverse=True)

    tuplerecent = listtuplerecent[0]

    listrecentActivity = tuplerecent[1].split("\n")
    countrecent = len(listrecentActivity)

    temprecent = listrecentActivity[0].encode("utf-8")
    listRecentActivityText[0] = temprecent
    retRecentActivityText += temprecent

    for i in range(1, countrecent) :
        temprecent = listrecentActivity[i].encode("utf-8")
        listRecentActivityText[i] = temprecent
        retRecentActivityText += " < " + temprecent


    return retRecentActivityText , listRecentActivityText[0], listRecentActivityText[1], listRecentActivityText[2], \
           listRecentActivityText[3], listRecentActivityText[4], listRecentActivityText[5], \
           listRecentActivityText[6], listRecentActivityText[7], listRecentActivityText[8], listRecentActivityText[9]


def get_External_Media_info(cur,querywhere ):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min
    queryExternal = "select %s  from %s " % (f00n_external_media_info, table_external_media_info )
    queryExternal += querywhere
    cur.execute(queryExternal)
    listtupleExternal = cur.fetchall()
    if len(listtupleExternal) == 0 :
        return "", 0,0,0,0,0,0

    listtupleExternal.sort(reverse=True)

    count_BAD_REMOVAL = 1
    count_NOFS = 2
    count_SHARED = 3
    count_UNMOUNTABLE = 4
    count_SCAN_STARTED = 5
    count_SCAN_FINISHED = 6

    dictcount = { count_BAD_REMOVAL:0, count_NOFS:0, count_SHARED:0, count_UNMOUNTABLE:0,  count_SCAN_STARTED:0, count_SCAN_FINISHED:0 }
    dictstate = { 1:"BAD_REMOVAL", 2:"NOFS", 3:"SHARED", 4:"UNMOUNTABLE", 5:"SCAN_STARTED" , 6:"SCAN_FINISHED"}

    prestate = listtupleExternal[0][1]
    retstate = dictstate[prestate]

    dictcount[prestate] += 1



    for tupleExternal in listtupleExternal :
        if tupleExternal[1] != prestate:
            dictcount[tupleExternal[1]] += 1
            prestate = tupleExternal[1]

    ''' gather the 10min's scenario '''
    if bGatheringSeqEvent10min == True :
        for tupleExternal in listtupleExternal :
            timestamp, statevalue = tupleExternal

            TenMinExternalMedia = "ExternalM:" + dictstate[statevalue]
            listlistSeqEvent10min.append( [timestamp, TenMinExternalMedia] )




    return retstate, dictcount[count_BAD_REMOVAL], dictcount[count_NOFS] ,  dictcount[count_SHARED],  dictcount[count_UNMOUNTABLE], dictcount[count_SCAN_STARTED], dictcount[count_SCAN_FINISHED]


def get_data_activity_info(cur,querywhere ):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min
    querydataact = "select %s  from %s " % (f00n_data_act_info, table_data_act_info )
    querydataact += querywhere
    cur.execute(querydataact)

    listtupledataact = cur.fetchall()

    if len( listtupledataact ) == 0 :
        return "", 0,0,0,0,0

    listtupledataact.sort(reverse=True)



    DATA_ACTIVITY_NONE = 0
    DATA_ACTIVITY_IN = 1
    DATA_ACTIVITY_OUT = 2
    DATA_ACTIVITY_INOUT = 3
    DATA_ACTIVITY_DORMANT = 4

    dictcount = {DATA_ACTIVITY_NONE:0, DATA_ACTIVITY_IN:0, DATA_ACTIVITY_OUT:0, DATA_ACTIVITY_INOUT:0, DATA_ACTIVITY_DORMANT:0 }
    dictstate = {DATA_ACTIVITY_NONE:"ACTIVITY_NONE", DATA_ACTIVITY_IN:"ACTIVITY_IN", DATA_ACTIVITY_OUT:"ACTIVITY_OUT", DATA_ACTIVITY_INOUT:"ACTIVITY_INOUT", DATA_ACTIVITY_DORMANT:"ACTIVITY_DORMANT" }

    prestate = listtupledataact[0][2]
    retstate = dictstate[prestate]

    dictcount[prestate] += 1

    for tupledataact in listtupledataact :
        if tupledataact[2] != prestate:
            dictcount[tupledataact[2]] += 1
            prestate = tupledataact[2]

    ''' gather the 10min's scenario '''
    if bGatheringSeqEvent10min == True :
        for tupledataact in listtupledataact :
            timestamp, statetype, statevalue = tupledataact

            TenMinExternalMedia = "DataACT:" + dictstate[statevalue]
            listlistSeqEvent10min.append( [timestamp, TenMinExternalMedia] )

    return retstate, dictcount[DATA_ACTIVITY_NONE], dictcount[DATA_ACTIVITY_IN] ,  dictcount[DATA_ACTIVITY_OUT],  dictcount[DATA_ACTIVITY_INOUT], dictcount[DATA_ACTIVITY_DORMANT]



'''   bring the below code from MLT Viewer Source Code .

            public static Int64 CalcRSSILevel(ETelephonyType _eTelephonyType, Int64 _nSignalStrength, Int64 _nEcio, Int64 _nSnr)
            {
                Int64 nRSSILevel = -1;

                if (_eTelephonyType == ETelephonyType.eTelephonyType_GSM)
                {
                    if (_nSignalStrength <= 2 || _nSignalStrength == 99) nRSSILevel = 0;
                    else if (_nSignalStrength >= 12) nRSSILevel = 4;
                    else if (_nSignalStrength >= 8) nRSSILevel = 3;
                    else if (_nSignalStrength >= 5) nRSSILevel = 2;
                    else nRSSILevel = 1;
                }
                else if (_eTelephonyType == ETelephonyType.eTelephonyType_CDMA)
                {
                    int nLevelDbm = 0;
                    //int nLevelEcio = 0;

                    if (_nSignalStrength >= -75) nLevelDbm = 4;
                    else if (_nSignalStrength >= -85) nLevelDbm = 3;
                    else if (_nSignalStrength >= -95) nLevelDbm = 2;
                    else if (_nSignalStrength >= -100) nLevelDbm = 1;
                    else nLevelDbm = 0;

                    nRSSILevel = nLevelDbm;
                    //// Ec/Io are in dB*10
                    //_nEcio /= 10;
                    //if (_nEcio >= -90) nLevelEcio = 4;
                    //else if (_nEcio >= -110) nLevelEcio = 3;
                    //else if (_nEcio >= -130) nLevelEcio = 2;
                    //else if (_nEcio >= -150) nLevelEcio = 1;
                    //else _nEcio = 0;

                    //nRSSILevel = (nLevelDbm < nLevelEcio) ? nLevelDbm : nLevelEcio;
                }
                else if (_eTelephonyType == ETelephonyType.eTelephonyType_EVDO)
                {
                    int nLevelEvdoDbm = 0;
                    //int nLevelEvdoSnr = 0;

                    if (_nSignalStrength >= -65) nLevelEvdoDbm = 4;
                    else if (_nSignalStrength >= -75) nLevelEvdoDbm = 3;
                    else if (_nSignalStrength >= -90) nLevelEvdoDbm = 2;
                    else if (_nSignalStrength >= -105) nLevelEvdoDbm = 1;
                    else nLevelEvdoDbm = 0;

                    nRSSILevel = nLevelEvdoDbm;

                    //if (_nSnr >= 7) nLevelEvdoSnr = 4;
                    //else if (_nSnr >= 5) nLevelEvdoSnr = 3;
                    //else if (_nSnr >= 3) nLevelEvdoSnr = 2;
                    //else if (_nSnr >= 1) nLevelEvdoSnr = 1;
                    //else nLevelEvdoSnr = 0;

                    //nRSSILevel = (nLevelEvdoDbm < nLevelEvdoSnr) ? nLevelEvdoDbm : nLevelEvdoSnr;
                    ////nRSSILevel = (nLevelEvdoDbm > nLevelEvdoSnr) ? nLevelEvdoDbm : nLevelEvdoSnr;
                }
                else if (_eTelephonyType == ETelephonyType.eTelephonyType_LTE)
                {
                    int nLevelLTEDbm = 0;
                    //int nLevelEvdoSnr = 0;

                    if (_nSignalStrength >= -65) nLevelLTEDbm = 4;
                    else if (_nSignalStrength >= -75) nLevelLTEDbm = 3;
                    else if (_nSignalStrength >= -90) nLevelLTEDbm = 2;
                    else if (_nSignalStrength >= -105) nLevelLTEDbm = 1;
                    else nLevelLTEDbm = 0;

                    //if (_nSnr >= 7) nLevelEvdoSnr = 4;
                    //else if (_nSnr >= 5) nLevelEvdoSnr = 3;
                    //else if (_nSnr >= 3) nLevelEvdoSnr = 2;
                    //else if (_nSnr >= 1) nLevelEvdoSnr = 1;
                    //else nLevelEvdoSnr = 0;

                    nRSSILevel = nLevelLTEDbm;
                }

                return nRSSILevel;
            }

'''


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


def get_sum_signal_level(cur,querywhere ):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min
    querysignalstrength = "select %s  from %s " % (f00n_signal_level_info, table_signal_level_info )
    querysignalstrength += querywhere
    cur.execute(querysignalstrength)
    listtuplesignalstrength = cur.fetchall()

    if len(listtuplesignalstrength) == 0 :
        return 0,0,0,0

    SIGNAL_CDMA = 21
    SIGNAL_EVDO = 22
    SIGNAL_GSM = 23
    SIGNAL_LTE = 24

    avg_cdma_signal = 0
    avg_evdo_signal = 0
    avg_gsm_signal = 0
    avg_lte_signal = 0
    sum_cdma_signal = 0
    sum_evdo_signal = 0
    sum_gsm_signal = 0
    sum_lte_signal = 0
    count_cdma = 0
    count_evdo = 0
    count_gsm = 0
    count_lte = 0

    for tuplesignalstrength in listtuplesignalstrength :
        timestamp, signaltype, signalstrength = tuplesignalstrength
        if not signaltype in [ SIGNAL_CDMA, SIGNAL_EVDO, SIGNAL_GSM, SIGNAL_LTE ] :
            continue
        signallevel = CalcRSSILevel(signaltype, signalstrength )

        if signallevel == 0:
            continue

        if signaltype == SIGNAL_CDMA:
            sum_cdma_signal += signallevel
            count_cdma += 1

        if signaltype == SIGNAL_EVDO:
            sum_evdo_signal += signallevel
            count_evdo += 1

        if signaltype == SIGNAL_GSM:
            sum_gsm_signal += signallevel
            count_gsm += 1

        if signaltype == SIGNAL_LTE:
            sum_lte_signal += signallevel
            count_lte += 1

    if count_cdma != 0:
        avg_cdma_signal = sum_cdma_signal / count_cdma
    if count_evdo != 0:
        avg_evdo_signal = sum_evdo_signal / count_evdo
    if count_gsm != 0:
        avg_gsm_signal = sum_gsm_signal / count_gsm
    if count_lte != 0:
        avg_lte_signal = sum_lte_signal / count_lte

    return  avg_cdma_signal, avg_evdo_signal, avg_gsm_signal, avg_lte_signal


def get_signal_level_info(cur,querywhere ):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min
    querysignalstrength = "select %s  from %s " % (f00n_signal_level_info, table_signal_level_info )
    querysignalstrength += querywhere
    cur.execute(querysignalstrength)
    listtuplesignalstrength = cur.fetchall()

    if len(listtuplesignalstrength) == 0 :
        return "", 0, 0,0,0,0

    listtuplesignalstrength.sort(reverse=True)

    SIGNAL_CDMA = 21
    SIGNAL_EVDO = 22
    SIGNAL_GSM = 23
    SIGNAL_LTE = 24

    dictsignalcount = {SIGNAL_CDMA:0, SIGNAL_EVDO:0, SIGNAL_GSM:0, SIGNAL_LTE:0  }
    dictsignallevel = {SIGNAL_CDMA:0, SIGNAL_EVDO:0, SIGNAL_GSM:0, SIGNAL_LTE:0  }
    dictsignalstate = {SIGNAL_CDMA:"CDMA", SIGNAL_EVDO:"EVDO", SIGNAL_GSM:"GSM", SIGNAL_LTE:"LTE"  }

    firstpass = False


    for tuplesignalstrength in listtuplesignalstrength :
        timestamp, signaltype, signalstrength = tuplesignalstrength
        if not signaltype in [ SIGNAL_CDMA, SIGNAL_EVDO, SIGNAL_GSM, SIGNAL_LTE ] :
            continue
        signallevel = CalcRSSILevel(signaltype, signalstrength )
        if dictsignallevel[signaltype] !=  signallevel :
            dictsignalcount[signaltype]  += 1
            dictsignallevel[signaltype] =  signallevel

        if firstpass == False :
            retsignalstate = dictsignalstate[signaltype]
            retsignallevel = signallevel
            firstpass = True

    ''' gather the 10min's scenario '''
    if bGatheringSeqEvent10min == True :
        for tuplesignalstrength in listtuplesignalstrength :
            timestamp, signaltype, signalstrength = tuplesignalstrength

            if not signaltype in [ SIGNAL_CDMA, SIGNAL_EVDO, SIGNAL_GSM, SIGNAL_LTE ] :
                continue
            signallevel = CalcRSSILevel(signaltype, signalstrength )
            if signaltype == SIGNAL_CDMA :
                TenMinSignal = "Singal:CDMA:" + str(signallevel)
            elif signaltype == SIGNAL_EVDO :
                TenMinSignal = "Singal:EVDO:" + str(signallevel)
            elif signaltype == SIGNAL_GSM :
                TenMinSignal = "Singal:GSM:" + str(signallevel)
            elif signaltype == SIGNAL_LTE :
                TenMinSignal = "Singal:LTE:" + str(signallevel)

            listlistSeqEvent10min.append( [timestamp, TenMinSignal] )


    return retsignalstate, retsignallevel, dictsignalcount[SIGNAL_CDMA], dictsignalcount[SIGNAL_EVDO], dictsignalcount[SIGNAL_GSM], dictsignalcount[SIGNAL_LTE]


''' ======================================================================'''
#dict_exception_type = {
    # 1:"exception_cp",                         --> None
    # 2:"exception_kernel",                     --> None
    # 3:"exception_framework",                  --> to Process
    # 4:"exception_app_fatal",                  --> to Process
    # 5:"exception_app_reset",                  --> None
    # 6:"exception_lockup",                     --> None
    # 7:"exception_anr",                        --> to Process
    # 8:"exception_calldrop",                   --> to Process
    # 13:"exception_Kernel_LastK" }             --> None

    # //===================== CallDrop Info =====================================
    # //	calldrop_reason;call_kind;location_provider;latitude;longitude;accuracy
    # //		calldrop_reason		string
    # //		call_kind			0 (outgoing call)
    # //							1 (incoming call)
    # //		location_provider	0 (GPS)
    # //							1 (Network)
    # //							2 (Passive)
    # //							others (Null)
    # //		latitude			(예 37:15:4.84628)
    # //		longitude			(예 127:20:0.69896)
    # //		accuracy			km 단위 (예 0.01)
    # //========================================================================
''' ======================================================================'''


import string
def get_exception_cause( exceptiontype, strExceptionInfo, strException_lastk_log ) :
    if exceptiontype != 13 and (strExceptionInfo == None or len( strExceptionInfo ) == 0 ):
        return ""
    elif exceptiontype == 13 and ( len(strException_lastk_log) == 0 ) :
        return ""

    # exception_framework
    if exceptiontype == 3 :
        liststrret = strExceptionInfo.split(">>>")
        liststrret = liststrret[1].split("<<<")
        return liststrret[0]

    # exception_app_fatal
    elif exceptiontype == 4 :
        index = strExceptionInfo.find("FATAL EXCEPTION")
        if index == 0 :
            liststrret = strExceptionInfo.splitlines()
            if len(liststrret) >= 2 :
                return liststrret[1]
            else:
                return ""

    # exception_anr
    elif exceptiontype == 7 :
        index = strExceptionInfo.find("ANR in ")
        if index == 0  and (index + 7 ) < len(strExceptionInfo ) :
            strret = strExceptionInfo[7:].strip().split()
            return strret[0]

    # exception_calldrop
    elif exceptiontype == 8 :
        strret = ""
        if strExceptionInfo.find("Calldrop Reason") == -1  :
            liststrCalldrop = DecryptIMSICode( strExceptionInfo ).strip().split(";")

            strret += "Calldrop Reason : " + liststrCalldrop[0]

            if liststrCalldrop[1] == "1" :
                strret += ",Incoming Call"
            else :
                strret += ",Outgoing Call"

            if liststrCalldrop[2] == "2" :
                strret += ",Location Info=Passive"
            elif liststrCalldrop[2] == "1" :
                strret += ",Location Info=Network"
            elif liststrCalldrop[2] == "0" :
                strret += ",Location Info=GPS"
            else:
                strret += ",Location Info=None"

            return strret
        else :
            liststrCalldrop = strExceptionInfo.strip().splitlines()
            strret = liststrCalldrop[0] + "," + liststrCalldrop[1]

            return strret

    # exception_lastk_log
    elif exceptiontype == 13 :
        liststr_lastk_log = strException_lastk_log.splitlines()
        retstr =  liststr_lastk_log[-1].strip()
        if  all ( kk in string.printable for kk in retstr ):
            return retstr
        else:
            return "Data is Corrupted!!!"


def get_app_install_info(cur,timestampstart, timestampend ):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min

    # get the installed  app list between timestampstart and timestampend
    queryappinstall = "select %s  from %s " % ("f004, f003", "t304" )
    queryappinstall += "where f004 > %s and f004 <= %s" % ( timestampstart, timestampend )
    cur.execute(queryappinstall)
    listtupleappinstall = cur.fetchall()

    strappinstall = ""
    for tupleappinstall in listtupleappinstall :
        strappinstall += tupleappinstall[1] + ", "


    # get the deleted  app list between timestampstart and timestampend
    queryappdeleted = "select %s  from %s " % ("f005, f003", "t304" )
    queryappdeleted += "where f005 > %s and f005 <= %s" % ( timestampstart, timestampend )
    cur.execute(queryappdeleted)
    listtupleappdeleted = cur.fetchall()

    strappdeleted = ""
    for tupleappdeleted in listtupleappdeleted :
        strappdeleted += tupleappdeleted[1] + ", "

    ''' gather the 10min's scenario '''
    if bGatheringSeqEvent10min == True :
        for tupleappinstall in listtupleappinstall :
            timestamp, installedAppName = tupleappinstall
            listlistSeqAction10min.append(  [timestamp, "Install:" + installedAppName] )
            listlistSeqEvent10min.append(  [timestamp, "Install:" + installedAppName] )

        for tupleappdeleted in listtupleappdeleted :
            timestamp, deletedAppName = tupleappdeleted
            listlistSeqAction10min.append(  [timestamp, "Install:" + deletedAppName] )
            listlistSeqEvent10min.append(  [timestamp, "Install:" + deletedAppName] )

    return strappinstall, strappdeleted


def get_rooting_info(cur,querywhere ):
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min

    if bGatheringSeqEvent10min == False :
        return

    queryrooting = "select %s  from %s " % ("f002, f003", "t303" )
    queryrooting += querywhere
    cur.execute(queryrooting)
    listtuplerooting = cur.fetchall()

    if len(listtuplerooting) == 0 :
        return

    for tuplerooting in listtuplerooting :
        timestamp, rootingApp = tuplerooting
        listlistSeqAction10min.append(  [timestamp, "rooting:" + rootingApp] )
        listlistSeqEvent10min.append(  [timestamp, "rooting:" + rootingApp] )


## determine if the lock-up is happpened .
## condition : power-on/off is not paired .  that is , power-on is marked as log,  power-off is not marked as log.
##           : the battery level is  less than  20% , this is to determine if battery is enforecd to be taken-off .

def AddExceptionLockup(  listtupleExceptionBlobsTemp, cur, TimeStampPrevious )     :
    global bGatheringSeqEvent10min, listlistSeqEvent10min

    querywhere = " where  f002 > %s " % (TimeStampPrevious )

    bGatheringSeqEvent10min = True

    get_battery_info(cur,querywhere )
    get_telephony_info(cur,querywhere )
    get_connectivity_info(cur,querywhere )
    get_bluetooth_info(cur,querywhere )
    get_wifi_info(cur,querywhere )
    get_power_info(cur,querywhere )
    get_lcd_info(cur,querywhere )
    get_resource_info(cur,querywhere )
    get_recentAct_info(cur,querywhere )
    get_External_Media_info(cur,querywhere )
    get_data_activity_info(cur,querywhere )
    get_signal_level_info(cur,querywhere )

    bGatheringSeqEvent10min = False

    if len( listlistSeqEvent10min ) == 0 :
        return

    listlistSeqEvent10min.sort(reverse=True)

    PowerOnState = 0
    powerOnBatteryLevel = 0
    powerOffBatteryLevel = 0
    powerOfftimestamp = 0
    for listSeqEvent10min in listlistSeqEvent10min :
        timestamp = listSeqEvent10min[0]
        eventname = listSeqEvent10min[1]

        # if eventname == "Power:On" or eventname == "Power:Off" :
            # print "eventname = " + eventname +  ConvertTimeStampToString(timestamp)

        if eventname == "Power:On" :
            # print "Power:On time is "  +  ConvertTimeStampToString(timestamp)
            if PowerOnState ==1 and powerOffBatteryLevel != 0 :
                # two  power-on without power-off
                # print " powerOnBatteryLevel: " +  str(powerOnBatteryLevel)
                # print " powerOffBatteryLevel: " +  str(powerOffBatteryLevel)
                if (powerOnBatteryLevel - powerOffBatteryLevel) < 20 :
                    listtupleExceptionBlobsTemp.append (( powerOfftimestamp, 6, "", "") )

            PowerOnState = 1
            powerOffBatteryLevel = 0
            powerOfftimestamp = 0
            querywhere = " where f002 >= %s and f002 <= %s "  % ( timestamp, timestamp + ( 5 * 60  * 1000L ) )
            listlistBatteryLevel = get_BatteryLevel_info( cur, querywhere   )
            listlistBatteryLevel.sort()
            if len(listlistBatteryLevel) == 0  :
                continue
            powerOnBatteryLevel = listlistBatteryLevel[0][1]
            listlistBatteryLevel = []

            continue

        if PowerOnState == 1 :
            if  eventname == "Power:Off" :      # normal power off
                # print "Power:Off time is "  +  ConvertTimeStampToString(timestamp)
                PowerOnState = 0
                powerOnBatteryLevel = 0
                powerOffBatteryLevel = 0
                powerOfftimestamp = 0
                continue
            elif powerOffBatteryLevel == 0  :                              # abnormal power off
                querywhere = " where f002 >= %s and f002 <= %s "  % ( timestamp - ( 5 * 60  * 1000L ), timestamp  )
                listlistBatteryLevel = get_BatteryLevel_info( cur, querywhere   )
                # print "len(listlistBatteryLevel) " , str(len(listlistBatteryLevel))
                listlistBatteryLevel.sort(reverse=True)
                if len(listlistBatteryLevel) == 0 :
                    continue
                powerOffBatteryLevel = listlistBatteryLevel[0][1]
                powerOfftimestamp = timestamp
                listlistBatteryLevel = []


    listlistSeqEvent10min =[]
    return listtupleExceptionBlobsTemp




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



''' ============================================================  '''

''' declare the global variable  here '''
rindex = 0
cindex = 0

rindex_Basic = 0
cindex_Basic = 0

listtupleBasicInfoExceptInfo = []
# variables.
diroutput = None
excelfilename = ""
dblist = []
sumfieldnames = []
wb = None
ws = None
wsbasic = None
boolCheckBatteryLevelTemperature = True
listdictKeyBatterylevelTemperature = ["OverBatteryLevelCount", "OverBatteryLevelAppList", "OverTemperatureCount" , "OverTemperatureAppList" ]

boolCheckBatteryLevelDuringLCDOff = True
listdictkeyBatteryLevelDropCountDuringLCDOff = [ "BatteryDropDuringLCDOff_Avg", "BatteryDropDuringLCDOff_4diffcount",
                                                "BatteryDropDuringLCDOff_6diffcount", "BatteryDropDuringLCDOff_8diffcount",
                                                "BatteryDropDuringLCDOff_10diffcount","BatteryDropDuringLCDOff_12diffcount"  ]

boolBuildupCallDump = False
listdictKeyCallDump = ["timestamp", "timediff",  "call_os_ver", "call_sw_ver", "Call_InOut", "CellMovementCount", "SignalLowestLevel", "Continued Call", "signal gab over 2" ]
listtupleBasicInfoCallDump = []
wb_calldump = None
ws_calldump = None
rindex_calldump = 0
cindex_calldump = 0

listdictKeyCallDrop = ["timestamp", "daytimezone",  "cdma_bslat", "cdma_bslong", "gsm_cid", "gsm_lac" ]
listtupleBasicInfoCallDrop = []
ws_calldrop = None
rindex_calldrop = 0
cindex_calldrop = 0




listlistSeqApp10min = []
listlistSeqAction10min = []
listlistSeqEvent10min = []
bGatheringSeqEvent10min = False

listrecentActivity = []

#class AnalyzerMLT ():

def setWorkingDir(workdir):
    global diroutput, dblist, listtupleBasicInfoExceptInfo
    diroutput = os.path.abspath(workdir)
    if not os.path.exists(diroutput):
        os.makedirs(diroutput)

    ''' goto the diroutput dir to work '''
    os.chdir(diroutput)
    dblist = glob.glob('*.db')

    listtupleBasicInfoExceptInfo = []

import copy
def writeResultToExcel(dictAdditinalBasicInfo, period ):
    global diroutput
    global listtupleBasicInfoExceptInfo
    global rindex, cindex
    global rindex_Basic, cindex_Basic
    global wb, ws, wsbasic
    global boolCheckBatteryLevelTemperature
    global boolCheckBatteryLevelDuringLCDOff
    global boolBuildupCallDump, rindex_calldump, cindex_calldump, rindex_calldrop, cindex_calldrop
    global wb_calldump, ws_calldump, ws_calldrop, listtupleBasicInfoCallDump, listtupleBasicInfoCallDrop

    if diroutput == None  :
        raise ValueError
    print "Writing to Excel : "

    if boolBuildupCallDump == True :
        fieldnames_calldump = copy.deepcopy(fields_basic_info)
        fieldnames_calldrop = copy.deepcopy(fields_basic_info)
        if dictAdditinalBasicInfo != None :
            fieldnames_calldump +=  dictAdditinalBasicInfo.keys()
            fieldnames_calldrop +=  dictAdditinalBasicInfo.keys()

        fieldnames_calldump += listdictKeyCallDump
        fieldnames_calldrop += listdictKeyCallDrop


        if wb_calldump == None :
            wb_calldump = Workbook()
            ws_calldump = wb_calldump.new_sheet("CallDump_"  + period )

            for fieldname in fieldnames_calldump :
                ws_calldump.cell(coords=(rindex_calldump, cindex_calldump,  ),  value = fieldname )
                ws_calldump.col(index=cindex_calldump, width=15)
                cindex_calldump += 1

            rindex_calldump = 1
            cindex_calldump = 0
            
            ws_calldrop = wb_calldump.new_sheet("CallDrop_"  + period )
            for fieldname in fieldnames_calldrop :
                ws_calldrop.cell(coords=(rindex_calldrop, cindex_calldrop,  ),  value = fieldname )
                ws_calldrop.col(index=cindex_calldrop, width=15)
                cindex_calldrop += 1

            rindex_calldrop = 1
            cindex_calldrop = 0
            
            

        for tupleBasicInfoCallDump in listtupleBasicInfoCallDump :
            dictBasicInfo, listdictCallDump = tupleBasicInfoCallDump

            if dictAdditinalBasicInfo != None :
                dictBasicInfo.update( dictAdditinalBasicInfo )

            for dictCallDump in listdictCallDump :
                print ".",
                dictsum = {}
                dictsum.update(dictBasicInfo)
                dictsum.update(dictCallDump)

                for fieldname in fieldnames_calldump :
                    if fieldname.find("timestamp") >= 0 :
                        ws_calldump.cell(coords=(rindex_calldump, cindex_calldump,  ), value = ConvertTimeStampToString(dictsum.get(fieldname,None ) ) )
                    elif fieldname.find("timediff") >= 0 :
                        ntimediffseconds = dictsum.get(fieldname, None) / 1000
                        strtimedelta = "%s" % (timedelta(seconds=ntimediffseconds))
                        ws_calldump.cell(coords=(rindex_calldump, cindex_calldump,  ), value = strtimedelta )
                    else :
                        ws_calldump.cell(coords=(rindex_calldump, cindex_calldump,  ), value = dictsum.get(fieldname, None) )

                    cindex_calldump += 1
                rindex_calldump += 1
                cindex_calldump = 0

        listtupleBasicInfoCallDump = []
        
        
        for tupleBasicInfoCallDrop in listtupleBasicInfoCallDrop :
            dictBasicInfo, listdictCallDrop = tupleBasicInfoCallDrop

            if dictAdditinalBasicInfo != None :
                dictBasicInfo.update( dictAdditinalBasicInfo )

            for dictCallDrop in listdictCallDrop :
                print ".",
                dictsum = {}
                dictsum.update(dictBasicInfo)
                dictsum.update(dictCallDrop)

                for fieldname in fieldnames_calldrop :
                    if fieldname.find("timestamp") >= 0 :
                        ws_calldrop.cell(coords=(rindex_calldrop, cindex_calldrop,  ), value = ConvertTimeStampToString(dictsum.get(fieldname,None ) ) )
                    elif fieldname.find("daytimezone") >= 0 :
                        daytimezone = ConvertTimeStampToString(dictsum.get("timestamp",None ) )
                        daytimezone = daytimezone.split(" ")[1]
                        daytimezone = daytimezone.split(":")[0]
                        ws_calldrop.cell(coords=(rindex_calldrop, cindex_calldrop,  ), value = daytimezone )
                    else :
                        ws_calldrop.cell(coords=(rindex_calldrop, cindex_calldrop,  ), value = dictsum.get(fieldname, None) )

                    cindex_calldrop += 1
                rindex_calldrop += 1
                cindex_calldrop = 0

        listtupleBasicInfoCallDrop = []
        
        



    sumfield_basic_info = copy.deepcopy(fields_basic_info)
    sumfield_basic_info += ["dbfilename"]
    

    if boolCheckBatteryLevelTemperature == True :
        sumfield_basic_info += listdictKeyBatterylevelTemperature

    if boolCheckBatteryLevelDuringLCDOff == True :
        sumfield_basic_info += listdictkeyBatteryLevelDropCountDuringLCDOff

    if dictAdditinalBasicInfo != None :
        sumfield_basic_info +=  dictAdditinalBasicInfo.keys()

    sumfield_basic_info += fields_sum_signal_level

    sumfieldnames = sumfield_basic_info + fields_exception_blobs + fields_AppInstallException
    sumfieldnames += ["PowerDownAfterExcpt", "ResetAfterExcpt", "WIFI_TA_ON_BeforeExcpt"]
    sumfieldnames +=  fields_SeqAction10min + fields_AppInstall10min +  fields_SeqApp10min + fields_SeqEvent10min + ["app_sum", "activity_sum"]
    sumfieldnames +=  fields_App1_10min_Overlap
    sumfieldnames +=  ["AppName1", "AppName2", "AppName3" ] + fields_App_timediff1 + fields_App_timediff2 + fields_App_timediff3 + ["app_timestamp1", "app_timestamp2" , "app_timestamp3"]

    sumfieldnames +=  fields_app_usage10min + fields_battery_info10min + fields_telephony_info10min + fields_connectivity_info10min + fields_bluetooth_info10min + fields_wifi_info10min + \
        fields_power_info10min + fields_lcd_info10min + fields_resource_info10min + fields_recentAct_info10min + fields_external_media_info10min + fields_data_act_info10min + fields_signal_level_info10min

    sumfieldnames += fields_app_usage1 + fields_battery_info1 + fields_telephony_info1 + fields_connectivity_info1 + fields_bluetooth_info1 + fields_wifi_info1 + \
        fields_power_info1 + fields_lcd_info1 + fields_resource_info1 + fields_recentAct_info1 + fields_external_media_info1 + fields_data_act_info1 + fields_signal_level_info1

    sumfieldnames += fields_app_usage2 + fields_battery_info2 + fields_telephony_info2 + fields_connectivity_info2 + fields_bluetooth_info2 + fields_wifi_info2 + \
        fields_power_info2 + fields_lcd_info2 + fields_resource_info2 + fields_recentAct_info2 + fields_external_media_info2 + fields_data_act_info2 + fields_signal_level_info2


    '''
    sumfieldnames += fields_app_usage3 + fields_battery_info3 + fields_telephony_info3 + fields_connectivity_info3 + fields_bluetooth_info3 + fields_wifi_info3 + \
        fields_power_info3 + fields_lcd_info3 + fields_resource_info3 + fields_recentAct_info3 + fields_external_media_info3 + fields_data_act_info3 + fields_signal_level_info3
    '''


    ''' ============================================================  '''
    ''' first, insert field name to row0 '''

    if wb == None :
        wb = Workbook()
        ws = wb.new_sheet("Excpt_"  + period )
        wsbasic = wb.new_sheet("LOGSUM_" + period)


        for fieldname in sumfieldnames :
            ws.cell(coords=(rindex, cindex,  ),  value = fieldname )
            ws.col(index=cindex, width=30)
            cindex += 1

        for fieldname in sumfield_basic_info :
            wsbasic.cell(coords=(rindex_Basic, cindex_Basic,  ),  value = fieldname )
            wsbasic.col(index=cindex_Basic, width=30)
            cindex_Basic += 1



        ''' print MLT Log info to excel file '''
        rindex = 1
        cindex = 0

        rindex_Basic = 1
        cindex_Basic = 0


    ''' merge some dict to one  for print '''
    for tupleBasicInfoExceptInfo in listtupleBasicInfoExceptInfo :
        dictBasicInfo, listdictExceptionInfo = tupleBasicInfoExceptInfo

        if dictAdditinalBasicInfo != None :
            dictBasicInfo.update( dictAdditinalBasicInfo )


        for fieldname in sumfield_basic_info :
            if fieldname.find("timestamp") >= 0 :
                wsbasic.cell(coords=(rindex_Basic, cindex_Basic,  ), value = ConvertTimeStampToString(dictBasicInfo.get(fieldname,None ) ) )
            else:
                wsbasic.cell(coords=(rindex_Basic, cindex_Basic,  ), value = dictBasicInfo.get(fieldname, None) )
            cindex_Basic += 1

        rindex_Basic += 1
        cindex_Basic = 0

        for dictExceptionInfo in listdictExceptionInfo :
            print ".",
            dictsum = {}
            dictsum.update(dictBasicInfo)
            dictsum.update(dictExceptionInfo)

            for fieldname in sumfieldnames :
                if fieldname.find("app_eventid") >= 0 :
                    ws.cell(coords=(rindex, cindex,  ), value = dict_app_event_type.get(dictsum.get(fieldname, None), None ) )
                elif fieldname.find("timestamp") >= 0 :
                    ws.cell(coords=(rindex, cindex,  ), value = ConvertTimeStampToString(dictsum.get(fieldname,None ) ) )
                elif fieldname.find("app_sum") >= 0 :
                    ws.cell(coords=(rindex, cindex,  ), value = dictsum.get("AppName1","" ) + " < " + dictsum.get("AppName2","" ) + " < " + dictsum.get("AppName3","" ) )
                elif fieldname.find("activity_sum") >= 0 :
                    ws.cell(coords=(rindex, cindex,  ), value = dictsum.get("recentAct_ActivityList1","" ) + " < " + dictsum.get("recentAct_ActivityList2","" ) + " < " + dictsum.get("recentAct_ActivityList3","" ) )
                else:
                    ws.cell(coords=(rindex, cindex,  ), value = dictsum.get(fieldname, None) )

                cindex += 1

            rindex += 1
            cindex = 0
        print "."
    listtupleBasicInfoExceptInfo = []

def closeExcel(excelfilename, excelCallDrop ):
    global wb
    global wb_calldump

       
    curdir = os.path.abspath(os.curdir)
    from xlsxcessive.xlsx import save
    
    if wb != None :
        save(wb,  excelfilename )
        print "Excel Saved : " + curdir + "\\" + excelfilename
        wb = None ;

    if wb_calldump != None :
        save(wb_calldump, excelCallDrop)
        print "Excel Saved : " + curdir + "\\" + excelCallDrop
        wb_calldump = None 


def doProcessing( boolusetimestamp2011 = False, boolProcessingException = False, boolProcessingCallDump = False ):
    global dblist, listtupleBasicInfoExceptInfo
    global listlistSeqAction10min, listlistSeqEvent10min, bGatheringSeqEvent10min
    global listlistSeqApp10min
    global listrecentActivity
    global boolCheckBatteryLevelTemperature
    global boolCheckBatteryLevelDuringLCDOff
    global boolBuildupCallDump
    
    boolBuildupCallDump = boolProcessingCallDump

    for dbfilename in dblist:
        print "Extracting DB : " + dbfilename
        listdictExceptionInfo = []
        ### rename the DB file name to 'temp.db' because theat sqlite3.connect can't handle the hangul file name . ###
        tempdbname = '___processing.db'
        shutil.copy(dbfilename, tempdbname )
        conn = sqlite3.connect(tempdbname)
        ### check if t320 table is exist, if then, keep processing.  ###
        if check_table_exception_blobs(conn) == False:
            conn.close()
            print "No Exception Blobs, DB skip"
            os.remove( tempdbname )
            continue
        cur = conn.cursor()

        ### 1. get the basic info  ###
        query_basic_info = "SELECT %s from %s " % (f00n_basic_info, table_basic_info )
        cur.execute(query_basic_info)
        listtupleBasicInfo = cur.fetchall()

        ### just get the last effective basic info from list by comparing the f003 "registration" ###
        TimeStampLastestRegistration = ConvertDateTimeToMiliSeconds(2011, 7, 1)

        previousRegistration = TimeStampLastestRegistration
        listdictBasicSWVer = []

        for tupleBasicInfo in listtupleBasicInfo :
            dicttempBasicInfo = dict(zip (fields_basic_info, tupleBasicInfo ))
            if dicttempBasicInfo["registration_timestamp"] == None :
                continue
            elif dicttempBasicInfo["registration_timestamp"] > previousRegistration :
                dicttempBasicSWVer = {}
                dicttempBasicSWVer["basic_timestamp"]  = dicttempBasicInfo["basic_timestamp"]
                dicttempBasicSWVer["last_sw_ver"]  = dicttempBasicInfo["last_sw_ver"]
                listdictBasicSWVer.append( dicttempBasicSWVer )
                # print "last_sw_ver: " + dicttempBasicInfo["last_sw_ver"]
                # print "basic_timestamp: " + ConvertTimeStampToString(dicttempBasicInfo["basic_timestamp"]) + " registration_timestamp: " +  ConvertTimeStampToString(dicttempBasicInfo["registration_timestamp"])


        if len(listdictBasicSWVer) == 0 :
            dicttempBasicInfo = dict(zip (fields_basic_info, listtupleBasicInfo[-1] ))
            dicttempBasicSWVer = {}
            dicttempBasicSWVer["basic_timestamp"]  = ConvertDateTimeToMiliSeconds(2011, 7, 1)
            dicttempBasicSWVer["last_sw_ver"]  = dicttempBasicInfo["last_sw_ver"]
            listdictBasicSWVer.append( dicttempBasicSWVer )

        ## build-up the dictBasicInfo
        ## sometimes, dictBasicInfo["phone_type"] has wrong information
        ## To gather the correct,  check the dictBasicInfo["IMEI"] is not zero.
        for tupleBasicInfo in listtupleBasicInfo[::-1] :
            dictBasicInfo = dict(zip (fields_basic_info, tupleBasicInfo ))
            if dictBasicInfo["IMEI"] != None : 
                dictBasicInfo["phone_type"] = dict_phone_type.get(dictBasicInfo["phone_type"], None)
                dictBasicInfo["network_type"] = dict_network_type.get(dictBasicInfo["network_type"], None)
                if (len(dictBasicInfo["IMEI"]) > 20 ) and ( len(dictBasicInfo["IMEI"]) % 4  == 0 ) :
                    dictBasicInfo["IMEI"] = DecryptIMSICode(dictBasicInfo["IMEI"]).strip()
                break



        ### delete listtupleBasicInfo ###
        del listtupleBasicInfo

        ### define and declare the starting time stamp ###
        #TimeStampRegistration = ConvertDateTimeToMiliSeconds(2011, 7, 1)

        if boolusetimestamp2011 == True :
            TimeStampRegistration = listdictBasicSWVer[0]["basic_timestamp"]
        else :
            TimeStampRegistration = getlatesttimestampamongtable(cur)

            

        
        dbfilenamecopy = dbfilename[:]
        dictdbfilename = {}
        dictdbfilename["dbfilename"] = dbfilenamecopy
        
        dictBasicInfo.update( dictdbfilename )
        
        
        
        ## ------------------------------------------------------------------------------------------
        queryWhereWholeTime = " where f002 >= %s " % ( TimeStampRegistration )
        dictsumsignal = dict(zip (fields_sum_signal_level , get_sum_signal_level(cur,queryWhereWholeTime )))
        dictBasicInfo.update( dictsumsignal )


        if boolCheckBatteryLevelTemperature == True :
            #dictBasicInfo.update( dict(zip(listdictKeyBatterylevelTemperature,  getCurrentThermalApp ( cur, queryWhereWholeTime  ))))
            dicttemp = dict(zip(listdictKeyBatterylevelTemperature,  getCurrentThermalApp ( cur, queryWhereWholeTime  )))
            dictBasicInfo.update( dicttemp )

        if boolCheckBatteryLevelDuringLCDOff == True or boolBuildupCallDump == True :
            
            MltDBDump.listdictDBDump = []
            MltDBDump.listdictBasicSWVer = []

            MltDBDump.buildupDBDumpSWver( MltDBDump.listdictDBDump, MltDBDump.listdictBasicSWVer, cur, queryWhereWholeTime )

            if boolCheckBatteryLevelDuringLCDOff == True :
                dicttemp = dict(zip(listdictkeyBatteryLevelDropCountDuringLCDOff,  getBatteryLevelDropCountDuringLCDOff ( MltDBDump.listdictDBDump  )))
                dictBasicInfo.update( dicttemp)

            if boolBuildupCallDump == True :
                listdictCallDump = []
                BuildupCallDump(listdictCallDump, dictBasicInfo["phone_type"] , MltDBDump.listdictDBDump)
                listtupleBasicInfoCallDump.append((dictBasicInfo, listdictCallDump))
                
                listdictCallDrop = []
                BuildupCallDrop(listdictCallDrop, dictBasicInfo["phone_type"] , MltDBDump.listdictDBDump)
                listtupleBasicInfoCallDrop.append((dictBasicInfo, listdictCallDrop))


            MltDBDump.listdictDBDump = []
            MltDBDump.listdictBasicSWVer = []





        ## ------------------------------------------------------------------------------------------

        if boolProcessingException == True :

            TimeStampPrevious = TimeStampRegistration
            ### 2. get the exception info  ###

            query_exception_blobs = "SELECT %s from %s " % (f00n_exception_blobs, table_exception_blobs )
            cur.execute(query_exception_blobs)
            listtupleExceptionBlobs = cur.fetchall()
            #listtupleExceptionBlobs.sort()
            print "len(listtupleExceptionBlobs) : ", len(listtupleExceptionBlobs)

            ## remove the exception_type "lock-up"
            listtupleExceptionBlobsTemp = []
            for tupleExceptionBlob in listtupleExceptionBlobs:
                if tupleExceptionBlob[1] == 6 :
                    # print "delete lock-up"
                    continue
                listtupleExceptionBlobsTemp.append(tupleExceptionBlob)



            ## determine if the lock-up is happpened .
            ## condition : power-on/off is not paired .  that is , power-on is marked as log,  power-off is not marked as log.
            ##           : the battery level is  less than  20% , this is to determine if battery is enforecd to be taken-off .

            AddExceptionLockup(  listtupleExceptionBlobsTemp, cur, TimeStampPrevious )

            listtupleExceptionBlobs = listtupleExceptionBlobsTemp
            listtupleExceptionBlobsTemp = []
            listtupleExceptionBlobs.sort()


            for tupleExceptionBlob in listtupleExceptionBlobs:
                # timestamp, exceptiontype, exception_cause, exception_lastk_log = tupleExceptionBlob
                if tupleExceptionBlob[0] > TimeStampPrevious:
                    timestamp, exceptiontype = tupleExceptionBlob[0], dict_exception_type[ tupleExceptionBlob[1]]
                    exception_cause = get_exception_cause( tupleExceptionBlob[1], tupleExceptionBlob[2], tupleExceptionBlob[3] )

                    ntimediffseconds = (tupleExceptionBlob[0] - TimeStampPrevious)/1000
                    strtimedelta = "%s" % (timedelta(seconds=ntimediffseconds))

                    ## find the exception SW ver
                    strSWver = ""
                    for dictBasicSWVer in listdictBasicSWVer :
                        if dictBasicSWVer["basic_timestamp"]  <= timestamp :
                            strSWver = dictBasicSWVer["last_sw_ver"]

                    dicttemp = dict(zip (fields_exception_blobs, (timestamp, exceptiontype, exception_cause, strtimedelta, strSWver) ))

                    dictAppInstallInfoException = dict(zip(fields_AppInstallException, get_app_install_info(cur, TimeStampPrevious, tupleExceptionBlob[0] )))

                    dicttemp.update( dictAppInstallInfoException )
                    listdictExceptionInfo.append(dicttemp)

                    TimeStampPrevious = tupleExceptionBlob[0]



            print "len(listdictExceptionInfo) : ", len(listdictExceptionInfo)

            ### 3. define the inspect period from listdictExceptionInfo, and  get pattern data.###
            TimeStampPrevious = TimeStampRegistration
            for dictExceptionInfo in listdictExceptionInfo:
                TimeStampExcept = dictExceptionInfo["except_timestamp"]
                ### print  dictExceptionInfo["exception_type"] ###

                ### if dictExceptionInfo["exception_type"] == "exception_lockup" : ###
                ###     print "exception_lockup timestamp "  +  ConvertTimeStampToString(TimeStampExcept) ###

                queryWhere = " Where f002 > %s and f002 <= %s" % (TimeStampPrevious,  TimeStampExcept)

                ### for the next operation ###
                TimeStampPrevious = TimeStampExcept

                ###======================================================================###
                ### calculate the 10 minute period between TimeStampPrevious and TimeStampExcept ###
                TimeStamp10minbefore = TimeStampExcept - (10 * 60 * 1000 )



                ### get the list of apps during 10 minutes before a Exception###
                query_app_usage = "select %s from %s" % (f00n_app_usage,table_app_usage  )
                queryWhere10min = " Where f002 > %s and f002 <= %s" % (TimeStamp10minbefore,  TimeStampExcept)
                query_app_usage += queryWhere10min
                cur.execute(query_app_usage)
                listtupleAppUsage = cur.fetchall()
                listtupleAppUsage.sort(reverse=True)
                dictAppEventInfo = { 11:"start foreground", 12:"start background", 13:"start broadcast", 14:"start service", 15:"start provider", 20:"end",  31:"resumed", 32:"paused" }
                for tupleAppUsage in listtupleAppUsage :
                    ### treat the only type  "start foreground" "start background"  "resumed"  "paused" ###
                    ### timestamp, package, eventid = tupleAppUsage ###
                    if not  tupleAppUsage[2] in [11, 12, 13, 14, 15, 20, 31, 32] :
                        continue

                    AppEventInfo = dictAppEventInfo[tupleAppUsage[2]]
                    AppEventInfo = AppEventInfo + ":" + tupleAppUsage[1]
                    if tupleAppUsage[2] in [11, 31] :
                        listlistSeqApp10min.append ( [tupleAppUsage[0],tupleAppUsage[1]] )
                    listlistSeqEvent10min.append ( [tupleAppUsage[0], AppEventInfo ])


                ### get the list of Exception during 10 minutes before a Exception###
                query_exception_blobs = "SELECT %s from %s " % (f00n_exception_blobs, table_exception_blobs )
                query_exception_blobs += queryWhere10min
                cur.execute(query_exception_blobs)
                listtupleException10min = cur.fetchall()
                listtupleException10min.sort(reverse=True)
                for tupleException10min in listtupleException10min :
                    timestamp, exceptiontype = tupleException10min[0], dict_exception_type[ tupleException10min[1]]
                    exceptiontype = "(" +  ConvertTimeStampToString(timestamp) + ") " + exceptiontype
                    listlistSeqEvent10min.append( [timestamp, exceptiontype] )

                ### ======================================================================###



                ### 3.0 get the 3-step app usage  from t307 during Exception ###
                query_app_usage = "select %s from %s" % (f00n_app_usage,table_app_usage  )
                query_app_usage += queryWhere
                cur.execute(query_app_usage)
                listtupleAppUsage = cur.fetchall()
                if len (listtupleAppUsage ) >= 2 :
                    listtupleAppUsage.sort(reverse=True)


                ### default dict App Usage ###
                dictAppUsage10min = {"app_timestamp10min":None, "AppName10min":None, "app_eventid10min":None}
                dictAppUsage1 = {"app_timestamp1":None, "AppName1":None, "app_eventid1":None }
                dictAppUsage2 = {"app_timestamp2":None, "AppName2":None, "app_eventid2":None }
                dictAppUsage3 = {"app_timestamp3":None, "AppName3":None, "app_eventid3":None }

                listdictAppUsage = [ dictAppUsage1, dictAppUsage2, dictAppUsage3 ]
                listlistAppFields = [ fields_app_usage1, fields_app_usage2, fields_app_usage3 ]


                ### fields_app_usage1 = ["app_timestamp1", "AppName1", "app_eventid1"] ###

                listindex = 0
                for tupleAppUsage in listtupleAppUsage :
                    ### treat the only type  "start foreground"   "resumed"  "paused" ###
                    ### timestamp, package, eventid = tupleAppUsage ###
                    if not  tupleAppUsage[2] in [11, 31, 32] :
                        continue

                    listdictAppUsage[listindex] = dict( zip (listlistAppFields[listindex] ,tupleAppUsage  ))
                    listindex += 1
                    if listindex > 2 :
                        break

                dictAppUsage1 = listdictAppUsage[0]
                dictAppUsage2 = listdictAppUsage[1]
                dictAppUsage3 = listdictAppUsage[2]

                ### 3.1  get pattern information during 10 minute before previous exception  ###
                ### update the TimeStampEnding for the next operation ###
                TimeStampEnding = TimeStampExcept


                if dictAppUsage1["app_timestamp1"] < TimeStamp10minbefore :
                    boolOverlap = 0
                else :
                    boolOverlap = 1

                dictApp1_10min_Overlap = dict(zip(fields_App1_10min_Overlap, (boolOverlap,) ))
                dictExceptionInfo.update ( dictApp1_10min_Overlap )

                dictAppUsage10min["app_timestamp10min"] = TimeStamp10minbefore

                bGatheringSeqEvent10min = True
                if ( True ):
                    ### I will add the 60 seconds to TimeStampEnding to detect the "대기중 꺼짐 for F180" ###
                    querywhereapp10min = "where  f002 > %s and f002 <= %s" % (TimeStamp10minbefore, TimeStampEnding + (60* 1000) )
                    dictBatteryInfo10min = dict(zip (fields_battery_info10min , get_battery_info(cur,querywhereapp10min )))
                    dictTelephonyInfo10min = dict(zip (fields_telephony_info10min , get_telephony_info(cur,querywhereapp10min )))
                    dictConnectivityInfo10min = dict(zip (fields_connectivity_info10min , get_connectivity_info(cur,querywhereapp10min )))
                    dictBluetoothInfo10min = dict(zip (fields_bluetooth_info10min , get_bluetooth_info(cur,querywhereapp10min )))
                    dictWIFIInfo10min = dict(zip (fields_wifi_info10min , get_wifi_info(cur,querywhereapp10min )))
                    dictPowerInfo10min = dict(zip (fields_power_info10min , get_power_info(cur,querywhereapp10min )))
                    dictLcdInfo10min = dict(zip (fields_lcd_info10min , get_lcd_info(cur,querywhereapp10min )))
                    dictResourceInfo10min = dict(zip (fields_resource_info10min , get_resource_info(cur,querywhereapp10min )))
                    dictRecentActInfo10min = dict(zip (fields_recentAct_info10min , (get_recentAct_info(cur,querywhereapp10min ))))
                    dictExternalMediaInfo10min = dict(zip (fields_external_media_info10min , (get_External_Media_info(cur,querywhereapp10min ))))
                    dictDataActivityInfo10min = dict(zip (fields_data_act_info10min , (get_data_activity_info(cur,querywhereapp10min ))))
                    dictSignalLevelInfo10min = dict(zip (fields_signal_level_info10min , (get_signal_level_info(cur,querywhereapp10min ))))

                    ### do get_app_install_info only while 10minutes ###
                    dictAppInstallInfo10min = dict(zip(fields_AppInstall10min, get_app_install_info(cur, TimeStamp10minbefore, TimeStampEnding )))
                    get_rooting_info(cur, querywhereapp10min )

                    dictExceptionInfo.update(dictAppUsage10min)
                    dictExceptionInfo.update(dictBatteryInfo10min)
                    dictExceptionInfo.update(dictTelephonyInfo10min)
                    dictExceptionInfo.update(dictConnectivityInfo10min)
                    dictExceptionInfo.update(dictBluetoothInfo10min)
                    dictExceptionInfo.update(dictWIFIInfo10min)
                    dictExceptionInfo.update(dictPowerInfo10min)
                    dictExceptionInfo.update(dictLcdInfo10min)
                    dictExceptionInfo.update(dictResourceInfo10min)
                    dictExceptionInfo.update(dictRecentActInfo10min)
                    dictExceptionInfo.update(dictExternalMediaInfo10min)
                    dictExceptionInfo.update(dictDataActivityInfo10min)
                    dictExceptionInfo.update(dictSignalLevelInfo10min)
                    dictExceptionInfo.update(dictAppInstallInfo10min)

                bGatheringSeqEvent10min = False
                ### ----------------------------------------------------------------------------- ###
                ### gather the 10min's Sequence Event for an Exception###
                listlistSeqEvent10min.sort(cmp=TimeStampCmp, reverse=True)

                ###  remove the item between  TimeStampEnding and additional 1minute ###
                while(True):
                    if listlistSeqEvent10min[0][0] > TimeStampEnding :
                        listlistSeqEvent10min.pop(0)
                    else:
                        break

                dicttempSeqEvent10min = {}
                countfieldsscenario = len(fields_SeqEvent10min)
                countSeqEvent10min = len (listlistSeqEvent10min)

                for index in range(countfieldsscenario) :
                    dicttempSeqEvent10min[fields_SeqEvent10min[index]] = None

                countfill = countSeqEvent10min
                if countSeqEvent10min > countfieldsscenario :
                    countfill = countfieldsscenario

                for index in range(countfill) :
                    dicttempSeqEvent10min[fields_SeqEvent10min[index]] = listlistSeqEvent10min[index][1]

                dictExceptionInfo.update(dicttempSeqEvent10min)

                listlistSeqEvent10min = []

                ### ----------------------------------------------------------------------------- ###
                ### gather the 10min's Sequencial Action for an Exception###
                listlistSeqAction10min += listlistSeqApp10min  # append the app list
                listlistSeqAction10min.sort(cmp=TimeStampCmp, reverse=True)
                dicttempSeqAction10min = {}
                countfieldsAction = len(fields_SeqAction10min)


                ### check and remove the item between  TimeStampEnding and additional 1minute ###
                boolLogExistAfterExcptIn1min = False
                boolPowerOnAfterExcptIn30sec = False
                while(len(listlistSeqAction10min) > 0 ):
                    if listlistSeqAction10min[0][0] > TimeStampEnding :
                        if ((listlistSeqAction10min[0][0] - TimeStampEnding) <= (30 * 1000 )) and (listlistSeqAction10min[0][1] == "Power:On" ) :
                            boolPowerOnAfterExcptIn30sec = True
                        listlistSeqAction10min.pop(0)
                        boolLogExistAfterExcptIn1min = True
                    else:
                        break

                countSeqAction10min = len (listlistSeqAction10min)

                boolUSBTA_ON_BeforeExcpt = False
                boolTA_ON_BeforeExcpt = False

                querywhere = "where  f002 > %s and f002 <= %s" % (TimeStampRegistration, TimeStampEnding )
                strUSBTAInfo = get_LastUSBTAconnectivity_info(cur,  querywhere )
                if strUSBTAInfo != "PlugType_None":
                    boolUSBTA_ON_BeforeExcpt = True

                if strUSBTAInfo == "PlugType_AC" :
                    boolTA_ON_BeforeExcpt = True

                boolWIFIONBeforeExcpt = False
                strWIFIINFO = get_LastWIFIState(cur,  querywhere )
                if strWIFIINFO == "WIFI_STATE_ENABLING" or strWIFIINFO == "WIFI_STATE_ENABLED" :
                    boolWIFIONBeforeExcpt = True

                boolcheckLCDOFFBeforeLockup = False
                ### check the LCD off at the last state. but if LCD:On is very short close ( 1sec) to Exeception, that will be ignored. ###
                for listSeqAction10min in listlistSeqAction10min :
                    timestamp, SeqAction = listSeqAction10min
                    if SeqAction == "LCD:On" and ((TimeStampEnding - timestamp) < 1000) :
                        ### skip this due to very close to exception_lockup ###
                        continue
                    elif SeqAction == "Power:On" :
                        break
                    ### elif SeqAction == "LCD:On" and ((TimeStampEnding - timestamp) >= 1000) : ###
                    ###     break ###
                    elif SeqAction == "LCD:Off" and ((TimeStampEnding - timestamp) > (60*1000) ) :
                        boolcheckLCDOFFBeforeLockup = True
                        break
                    else :
                        break

                dictPatternCheckAroundExcpt = {"PowerDownAfterExcpt":"", "ResetAfterExcpt":"", "WIFI_TA_ON_BeforeExcpt":"" }
                if (boolcheckLCDOFFBeforeLockup == True and boolUSBTA_ON_BeforeExcpt == False and boolLogExistAfterExcptIn1min == False) and (boolPowerOnAfterExcptIn30sec == False ):
                    dictPatternCheckAroundExcpt["PowerDownAfterExcpt"] = "True"

                if boolPowerOnAfterExcptIn30sec == True :
                    dictPatternCheckAroundExcpt["ResetAfterExcpt"] = "True"

                if boolWIFIONBeforeExcpt == True and boolTA_ON_BeforeExcpt == True :
                    dictPatternCheckAroundExcpt["WIFI_TA_ON_BeforeExcpt"] = "True"

                dictExceptionInfo.update(dictPatternCheckAroundExcpt)


                for index in range(countfieldsAction) :
                    dicttempSeqAction10min[fields_SeqAction10min[index]] = None

                countfill = countSeqAction10min
                if countSeqAction10min > countfieldsAction :
                    countfill = countfieldsAction

                timepoweron = 0
                timelcdon = 0
                columnindex = 0

                for actionindex in range(countfill) :
                    ### if action == "Power:On",  print the time diff between Power:On and previous action ###

                    if listlistSeqAction10min[actionindex][1] == "Power:On" :
                       timepoweron = listlistSeqAction10min[actionindex][0]
                    elif timepoweron > 0 :
                        timepowerdiff =  (timepoweron - listlistSeqAction10min[actionindex][0]) / 1000
                        strtimepowerdiff = "%s" % (timedelta(seconds=timepowerdiff))
                        dicttempSeqAction10min[fields_SeqAction10min[columnindex]] = "PowerInterval=" + strtimepowerdiff
                        columnindex += 1
                        timepoweron = 0
                        if columnindex >= countfieldsAction :
                            break

                    ### if action == "LCD:On",  print the time diff between LCD:On and LCD:Off ###
                    if listlistSeqAction10min[actionindex][1] == "LCD:On" :
                       timelcdon = listlistSeqAction10min[actionindex][0]
                    elif timelcdon > 0  and listlistSeqAction10min[actionindex][1] == "LCD:Off":
                        timelcddiff =  (timelcdon - listlistSeqAction10min[actionindex][0]) / 1000
                        strtimelcddiff = "%s" % (timedelta(seconds=timelcddiff))
                        dicttempSeqAction10min[fields_SeqAction10min[columnindex]] = "LCDInterval=" + strtimelcddiff
                        columnindex += 1
                        timelcdon = 0
                        if columnindex >= countfieldsAction :
                            break

                    dicttempSeqAction10min[fields_SeqAction10min[columnindex]] = listlistSeqAction10min[actionindex][1]
                    columnindex += 1
                    if columnindex >= countfieldsAction :
                        break

                dictExceptionInfo.update(dicttempSeqAction10min)

                listlistSeqAction10min = []


                ### ----------------------------------------------------------------------------- ###
                ### gather the 10min's App list###
                listlistSeqApp10min.sort(cmp=TimeStampCmp, reverse=True)
                countfieldsApps = len(fields_SeqApp10min)
                countSeqApp10min = len(listlistSeqApp10min)

                dicttempSeqApp10min = {}

                for index in range(countfieldsApps) :
                    dicttempSeqApp10min[fields_SeqApp10min[index]] = None

                countfill = countSeqApp10min
                if countSeqApp10min > countfieldsApps :
                    countfill = countfieldsApps

                for index in range(countfill) :
                    strAppName = listlistSeqApp10min[index][1]

                    for recentActivity in listrecentActivity:
                        if strAppName in recentActivity :
                            strAppName = recentActivity


                    dicttempSeqApp10min[fields_SeqApp10min[index]] = strAppName

                dictExceptionInfo.update(dicttempSeqApp10min)

                listlistSeqApp10min = []

                ### ----------------------------------------------------------------------------- ###


                ### 3.2  get pattern information  from except timestamp1 to App event1 and   ###
                ### update the TimeStampEnding for the next operation ###
                TimeStampEnding = TimeStampExcept

                if (dictAppUsage1["app_timestamp1"] != None ):
                    querywhereapp1 = "where  f002 > %s and f002 <= %s" % (dictAppUsage1["app_timestamp1"], TimeStampEnding )
                    dictBatteryInfo1 = dict(zip (fields_battery_info1 , get_battery_info(cur,querywhereapp1 )))
                    dictTelephonyInfo1 = dict(zip (fields_telephony_info1 , get_telephony_info(cur,querywhereapp1 )))
                    dictConnectivityInfo1 = dict(zip (fields_connectivity_info1 , get_connectivity_info(cur,querywhereapp1 )))
                    dictBluetoothInfo1 = dict(zip (fields_bluetooth_info1 , get_bluetooth_info(cur,querywhereapp1 )))
                    dictWIFIInfo1 = dict(zip (fields_wifi_info1 , get_wifi_info(cur,querywhereapp1 )))
                    dictPowerInfo1 = dict(zip (fields_power_info1 , get_power_info(cur,querywhereapp1 )))
                    dictLcdInfo1 = dict(zip (fields_lcd_info1 , get_lcd_info(cur,querywhereapp1 )))
                    dictResourceInfo1 = dict(zip (fields_resource_info1 , get_resource_info(cur,querywhereapp1 )))
                    dictRecentActInfo1 = dict(zip (fields_recentAct_info1 , (get_recentAct_info(cur,querywhereapp1 ))))
                    dictExternalMediaInfo1 = dict(zip (fields_external_media_info1 , (get_External_Media_info(cur,querywhereapp1 ))))
                    dictDataActivityInfo1 = dict(zip (fields_data_act_info1 , (get_data_activity_info(cur,querywhereapp1 ))))
                    dictSignalLevelInfo1 = dict(zip (fields_signal_level_info1 , (get_signal_level_info(cur,querywhereapp1 ))))
                    ntimediffseconds = (TimeStampEnding - dictAppUsage1["app_timestamp1"])/1000
                    strtimedelta = "%s" % (timedelta(seconds=ntimediffseconds))
                    dictAppTimeDiff1 = dict(zip(fields_App_timediff1, (strtimedelta, )))

                    dictExceptionInfo.update(dictAppUsage1)
                    dictExceptionInfo.update(dictBatteryInfo1)
                    dictExceptionInfo.update(dictTelephonyInfo1)
                    dictExceptionInfo.update(dictConnectivityInfo1)
                    dictExceptionInfo.update(dictBluetoothInfo1)
                    dictExceptionInfo.update(dictWIFIInfo1)
                    dictExceptionInfo.update(dictPowerInfo1)
                    dictExceptionInfo.update(dictLcdInfo1)
                    dictExceptionInfo.update(dictResourceInfo1)
                    dictExceptionInfo.update(dictRecentActInfo1)
                    dictExceptionInfo.update(dictExternalMediaInfo1)
                    dictExceptionInfo.update(dictDataActivityInfo1)
                    dictExceptionInfo.update(dictSignalLevelInfo1)
                    dictExceptionInfo.update(dictAppTimeDiff1)


                ### 3.3  get pattern information  from App event1 to App event2 and    ###
                ### update the TimeStampEnding for the next operation ###

                TimeStampEnding = dictAppUsage1["app_timestamp1"]
                dictAppTimeDiff2 = dict(zip(fields_App_timediff2, ("1Days", )))

                if (dictAppUsage2["app_timestamp2"] != None ):
                    querywhereapp2 = "where  f002 > %s and f002 <= %s" % (dictAppUsage2["app_timestamp2"], TimeStampEnding )
                    dictBatteryInfo2 = dict(zip (fields_battery_info2 , get_battery_info(cur,querywhereapp2 )))
                    dictTelephonyInfo2 = dict(zip (fields_telephony_info2 , get_telephony_info(cur,querywhereapp2 )))
                    dictConnectivityInfo2 = dict(zip (fields_connectivity_info2 , get_connectivity_info(cur,querywhereapp2 )))
                    dictBluetoothInfo2 = dict(zip (fields_bluetooth_info2 , get_bluetooth_info(cur,querywhereapp2 )))
                    dictWIFIInfo2 = dict(zip (fields_wifi_info2 , get_wifi_info(cur,querywhereapp2 )))
                    dictPowerInfo2 = dict(zip (fields_power_info2 , get_power_info(cur,querywhereapp2 )))
                    dictLcdInfo2 = dict(zip (fields_lcd_info2 , get_lcd_info(cur,querywhereapp2 )))
                    dictResourceInfo2 = dict(zip (fields_resource_info2 , get_resource_info(cur,querywhereapp2 )))
                    dictRecentActInfo2 = dict(zip (fields_recentAct_info2 , (get_recentAct_info(cur,querywhereapp2 ))))
                    dictExternalMediaInfo2 = dict(zip (fields_external_media_info2 , (get_External_Media_info(cur,querywhereapp2 ))))
                    dictDataActivityInfo2 = dict(zip (fields_data_act_info2 , (get_data_activity_info(cur,querywhereapp2 ))))
                    dictSignalLevelInfo2 = dict(zip (fields_signal_level_info2 , (get_signal_level_info(cur,querywhereapp2 ))))
                    ntimediffseconds = (TimeStampEnding - dictAppUsage2["app_timestamp2"])/1000
                    strtimedelta = "%s" % (timedelta(seconds=ntimediffseconds))
                    dictAppTimeDiff2 = dict(zip(fields_App_timediff2, (strtimedelta, )))

                    dictExceptionInfo.update(dictAppUsage2)
                    dictExceptionInfo.update(dictBatteryInfo2)
                    dictExceptionInfo.update(dictTelephonyInfo2)
                    dictExceptionInfo.update(dictConnectivityInfo2)
                    dictExceptionInfo.update(dictBluetoothInfo2)
                    dictExceptionInfo.update(dictWIFIInfo2)
                    dictExceptionInfo.update(dictPowerInfo2)
                    dictExceptionInfo.update(dictLcdInfo2)
                    dictExceptionInfo.update(dictResourceInfo2)
                    dictExceptionInfo.update(dictRecentActInfo2)
                    dictExceptionInfo.update(dictExternalMediaInfo2)
                    dictExceptionInfo.update(dictDataActivityInfo2)
                    dictExceptionInfo.update(dictSignalLevelInfo2)
                    dictExceptionInfo.update(dictAppTimeDiff2)



                ### 3.4  get pattern information  from App event2 to App event3 and    ###
                ### update the TimeStampEnding for the next operation ###

                ###
                # TimeStampEnding = dictAppUsage2["app_timestamp2"]
                # dictAppTimeDiff3 = dict(zip(fields_App_timediff3, ("1Days", )))

                # if (dictAppUsage3["app_timestamp3"] != None ):
                    # querywhereapp3 = "where  f003 > %s and f003 <= %s" % (dictAppUsage3["app_timestamp3"], TimeStampEnding )
                    # dictBatteryInfo3 = dict(zip (fields_battery_info3 , get_battery_info(cur,querywhereapp3 )))
                    # dictTelephonyInfo3 = dict(zip (fields_telephony_info3 , get_telephony_info(cur,querywhereapp3 )))
                    # dictConnectivityInfo3 = dict(zip (fields_connectivity_info3 , get_connectivity_info(cur,querywhereapp3 )))
                    # dictBluetoothInfo3 = dict(zip (fields_bluetooth_info3 , get_bluetooth_info(cur,querywhereapp3 )))
                    # dictWIFIInfo3 = dict(zip (fields_wifi_info3 , get_wifi_info(cur,querywhereapp3 )))
                    # dictPowerInfo3 = dict(zip (fields_power_info3 , get_power_info(cur,querywhereapp3 )))
                    # dictLcdInfo3 = dict(zip (fields_lcd_info3 , get_lcd_info(cur,querywhereapp3 )))
                    # dictResourceInfo3 = dict(zip (fields_resource_info3 , get_resource_info(cur,querywhereapp3 )))
                    # dictRecentActInfo3 = dict(zip (fields_recentAct_info3 , (get_recentAct_info(cur,querywhereapp3 ))))
                    # dictExternalMediaInfo3 = dict(zip (fields_external_media_info3 , (get_External_Media_info(cur,querywhereapp3 ))))
                    # dictDataActivityInfo3 = dict(zip (fields_data_act_info3 , (get_data_activity_info(cur,querywhereapp3 ))))
                    # dictSignalLevelInfo3 = dict(zip (fields_signal_level_info3 , (get_signal_level_info(cur,querywhereapp3 ))))
                    # ntimediffseconds = (TimeStampEnding - dictAppUsage3["app_timestamp3"])/1000
                    # strtimedelta = "%s" % (timedelta(seconds=ntimediffseconds))
                    # dictAppTimeDiff3 = dict(zip(fields_App_timediff3, (strtimedelta, )))

                    # dictExceptionInfo.update(dictAppUsage3)
                    # dictExceptionInfo.update(dictBatteryInfo3)
                    # dictExceptionInfo.update(dictTelephonyInfo3)
                    # dictExceptionInfo.update(dictConnectivityInfo3)
                    # dictExceptionInfo.update(dictBluetoothInfo3)
                    # dictExceptionInfo.update(dictWIFIInfo3)
                    # dictExceptionInfo.update(dictPowerInfo3)
                    # dictExceptionInfo.update(dictLcdInfo3)
                    # dictExceptionInfo.update(dictResourceInfo3)
                    # dictExceptionInfo.update(dictRecentActInfo3)
                    # dictExceptionInfo.update(dictExternalMediaInfo3)
                    # dictExceptionInfo.update(dictDataActivityInfo3)
                    # dictExceptionInfo.update(dictSignalLevelInfo3)
                    # dictExceptionInfo.update(dictAppTimeDiff3)
                ###

        listtupleBasicInfoExceptInfo.append((dictBasicInfo, listdictExceptionInfo))
        conn.close()

        os.remove( tempdbname )

    dblist = []












