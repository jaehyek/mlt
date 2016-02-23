# -*- coding: utf-8 -*-
"""
Created on Wed Sep 04 18:01:37 2013

@author: jaehyek.choi
"""

strlog = '''
07-12 11:19:19.035 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:19.035 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:19.035 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:19.035 D/RILJ    ( 1227): responseGetModemInfo[I@42c95fc8
07-12 11:19:19.035 D/RILJ    ( 1227): [11305]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:19.045 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:19.085 D/GSM     ( 1227): [GSMphone] mIccRecords.iccid = 8982051006425136633
07-12 11:19:19.145 D/RILJ    ( 1227): [UNSL]< UNSOL_WCDMA_ACCEPT_RECEIVED {0, 1}
07-12 11:19:19.145 E/GSM     ( 1227): LGT Network Accept: mm_accept = 0 ,gmm_accept = 1
07-12 11:19:19.145 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:19.145 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:19.145 D/RILJ    ( 1227): [11306]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:19.145 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:19.145 D/RILJ    ( 1227): [11307]> OPERATOR
07-12 11:19:19.145 D/RILJ    ( 1227): [11308]> DATA_REGISTRATION_STATE
07-12 11:19:19.155 D/RILJ    ( 1227): [11309]> VOICE_REGISTRATION_STATE
07-12 11:19:19.155 D/RILJ    ( 1227): [11310]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:19.155 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:19.155 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:19.155 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:19.155 D/RILJ    ( 1227): [11311]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:19.165 D/RILJ    ( 1227): responseGetModemInfo[I@42cfaa58
07-12 11:19:19.165 D/RILJ    ( 1227): [11306]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:19.165 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:19.165 D/RILJ    ( 1227): responseGetModemInfo[I@42fb5f88
07-12 11:19:19.165 D/RILJ    ( 1227): [11311]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:19.165 D/RILJ    ( 1227): [11307]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:19.165 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:19.175 D/RILJ    ( 1227): [11309]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:19:19.175 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 0, CStype = 3
07-12 11:19:19.175 D/RILJ    ( 1227): [11310]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:19.175 D/RILJ    ( 1227): [11308]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, 20}
07-12 11:19:19.175 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:19:19.175 D/GSM     ( 1227): [EONS] Received CID = 65803784
07-12 11:19:19.175 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:19:19.175 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:19.175 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:19:19.175 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:19.175 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:19.175 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:20.976 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:19:20.976 D/RILJ    ( 1227): [11312]> GET_CURRENT_CALLS
07-12 11:19:20.976 E/RILC    (  341): numberplus = ""
07-12 11:19:20.976 E/RILC    (  341): signalIE = 0
07-12 11:19:20.976 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:19:20.976 D/RILJ    ( 1227): No calling name expression is received
07-12 11:19:20.976 D/RILJ    ( 1227): signal = 0
07-12 11:19:20.976 D/RILJ    ( 1227): DriverCall dc = id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:19:20.976 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:19:20.976 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:19:20.976 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:19:20.976 D/RILJ    ( 1227): [DriverCall] dc : id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:19:20.976 D/RILJ    ( 1227): [11312]< GET_CURRENT_CALLS  [id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:19:20.986 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:19:20.986 D/GSM     ( 1227): [GSMConn] update: parent=ALERTING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=true
07-12 11:19:20.986 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:19:23.409 D/RILJ    ( 1227): [11313]> SCREEN_STATE: true
07-12 11:19:23.429 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:23.429 D/RILJ    ( 1227): [11313]< SCREEN_STATE 
07-12 11:19:23.559 D/RILJ    ( 1227): [11314]> OPERATOR
07-12 11:19:23.559 D/RILJ    ( 1227): [11315]> DATA_REGISTRATION_STATE
07-12 11:19:23.559 D/RILJ    ( 1227): [11316]> VOICE_REGISTRATION_STATE
07-12 11:19:23.569 D/RILJ    ( 1227): [11315]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, 20}
07-12 11:19:23.569 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:23.569 D/RILJ    ( 1227): [11317]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:23.569 D/RILJ    ( 1227): [11316]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:19:23.569 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:23.569 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:23.569 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:23.569 D/RILJ    ( 1227): [11318]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:23.569 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 3
07-12 11:19:23.569 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:19:23.569 D/RILJ    ( 1227): responseGetModemInfo[I@436ee6a8
07-12 11:19:23.569 D/RILJ    ( 1227): [11318]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:23.569 D/RILJ    ( 1227): [11314]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:23.569 D/RILJ    ( 1227): [11317]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:23.679 D/GSM     ( 1227): [GsmDCT] onReceive: action=android.intent.action.SCREEN_ON
07-12 11:19:23.679 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:19:23.679 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:19:23.679 D/GSM     ( 1227): [GsmDCT] startNetStatPoll
07-12 11:19:23.689 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:19:23.689 D/GSM     ( 1227): [EONS] Received CID = 65803784
07-12 11:19:23.689 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:19:23.689 D/RILJ    ( 1227): [11319]> OPERATOR
07-12 11:19:23.689 D/RILJ    ( 1227): [11320]> DATA_REGISTRATION_STATE
07-12 11:19:23.699 D/RILJ    ( 1227): [11319]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:23.699 D/RILJ    ( 1227): [11321]> VOICE_REGISTRATION_STATE
07-12 11:19:23.699 D/RILJ    ( 1227): [11322]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:23.699 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:23.699 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:23.699 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:23.699 D/RILJ    ( 1227): [11323]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:23.699 D/RILJ    ( 1227): [11320]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, 20}
07-12 11:19:23.699 D/RILJ    ( 1227): [11321]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:19:23.699 D/RILJ    ( 1227): responseGetModemInfo[I@43b4a038
07-12 11:19:23.699 D/RILJ    ( 1227): [11323]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:23.709 D/RILJ    ( 1227): [11322]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:23.719 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:23.769 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:19:23.769 D/GSM     ( 1227): [EONS] Received CID = 65803784
07-12 11:19:23.769 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:19:23.769 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:19:23.769 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:23.769 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:23.769 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:19:23.769 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:23.769 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:23.769 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:24.360 D/GSM     ( 1227): [GsmCallTracker] (foregnd) hangup dialing or alerting...
07-12 11:19:24.360 D/RILJ    ( 1227): hangupConnection: gsmIndex=1
07-12 11:19:24.360 D/RILJ    ( 1227): [11324]> HANGUP 1
07-12 11:19:24.640 D/RILJ    ( 1227): [11324]< HANGUP 
07-12 11:19:24.640 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:19:24.670 D/RILJ    ( 1227): [11325]> GET_CURRENT_CALLS
07-12 11:19:24.670 D/RILJ    ( 1227): [11325]< GET_CURRENT_CALLS  
07-12 11:19:24.670 D/RILJ    ( 1227): [11326]> GET_CURRENT_CALLS
07-12 11:19:24.670 D/RILJ    ( 1227): [11326]< GET_CURRENT_CALLS  
07-12 11:19:24.670 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 3
07-12 11:19:24.670 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:19:24.780 D/GSM     ( 1227): [GSMConn] releaseWakeLock
07-12 11:19:24.780 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270344 when=-3ms obj=android.os.AsyncResult@437cba98 }
07-12 11:19:24.780 D/GSM     ( 1227): [GsmDCT] onVoiceCallEnded
07-12 11:19:24.780 D/GSM     ( 1227): [LGE_DATA] functionForPacketDrop for ACTION_VOICE_CALL_ENDED
07-12 11:19:24.790 E/RILC    (  341): responseLGERPInd(): param(425992(0x00068008)), data_valid(1), data_len(4)
07-12 11:19:24.790 I/RILJ    ( 1227): LGE_UNSOL_RRC_RELEASE_CAUSE: releaseCause = 1
07-12 11:19:24.800 D/GSM     ( 1227): [GsmDCT] setupDataOnReadyApns: 2GVoiceCallEnded
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] configureRetry: forDefault=true retryCount=0 dc={GsmDC-1: State=DcActiveState apnSetting=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 apnList= [{mApnType=ims mState=CONNECTED mWaitingApns=[[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 mDataConnectionAc=GsmDC-1 mReason=dataEnabled mRetryCount=0 mDataEnabled=true mDependencyMet=true}] RefCount=1 cid=0 create=1373486750617 lastFail=-1 lastFailCause=NONE}
07-12 11:19:24.810 E/GSM     ( 1227): [GsmDCT] [LG_DATA] configureRetry : by DOMESTIC_DATA_RETRY_CONFIG
07-12 11:19:24.810 D/RILJ    ( 1227): returned data  = [B@437e5ab0
07-12 11:19:24.810 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDC-1] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] configureRetry: forDefault=false retryCount=0 dc={GsmDC-2: State=DcInactiveState apnSetting=null apnList= [] RefCount=0 cid=-1 create=-1 lastFail=-1 lastFailCause=NONE}
07-12 11:19:24.810 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDC-2] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:admin] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:fota] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:ktmultirab1] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:entitlement] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:dun] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:ktmultirab2] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:supl] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:hipri] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:tethering] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:ims] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDC-1] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:usccapp] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:default] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:vzw800] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:mms] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:cbs] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:bip] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:vzwapp] setRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:19:24.810 D/GSM     ( 1227): [ApnContext:default] set reason as 2GVoiceCallEnded,current state IDLE
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] trySetupData for type:default due to 2GVoiceCallEnded
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] trySetupData with mIsPsRestricted=false
07-12 11:19:24.810 E/GSM     ( 1227): [GSMPhone] getEsn() is a CDMA method
07-12 11:19:24.810 E/GSM     ( 1227): [GSMPhone] getEsn() is a CDMA method
07-12 11:19:24.810 D/GSM     ( 1227): [LGE_DATA] <mbooting_phone> = false
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] MMS is available even if data enabled sets off : false
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:admin
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] isDataPossible(admin): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] get active apn string for type:admin
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:fota
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] isDataPossible(fota): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] get active apn string for type:fota
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:ktmultirab1
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] isDataPossible(ktmultirab1): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ktmultirab1
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:entitlement
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] isDataPossible(entitlement): possible=false isDataAllowed=true apnTypePossible=false apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.810 D/GSM     ( 1227): [GsmDCT] get active apn string for type:entitlement
07-12 11:19:24.820 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:dun
07-12 11:19:24.820 D/GSM     ( 1227): [GsmDCT] isDataPossible(dun): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.820 D/GSM     ( 1227): [GsmDCT] get active apn string for type:dun
07-12 11:19:24.820 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:ktmultirab2
07-12 11:19:24.820 D/GSM     ( 1227): [GsmDCT] isDataPossible(ktmultirab2): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.820 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ktmultirab2
07-12 11:19:24.820 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:supl
07-12 11:19:24.820 D/GSM     ( 1227): [GsmDCT] isDataPossible(supl): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.820 D/GSM     ( 1227): [GsmDCT] get active apn string for type:supl
07-12 11:19:24.830 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:hipri
07-12 11:19:24.830 D/GSM     ( 1227): [GsmDCT] isDataPossible(hipri): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.830 D/GSM     ( 1227): [GsmDCT] get active apn string for type:hipri
07-12 11:19:24.830 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:tethering
07-12 11:19:24.830 D/GSM     ( 1227): [GsmDCT] isDataPossible(tethering): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.830 D/GSM     ( 1227): [GsmDCT] get active apn string for type:tethering
07-12 11:19:24.830 D/GSM     ( 1227): [GsmDCT] notifyOffApnsOfAvailability skipped apn due to isReady==false: {mApnType=ims mState=CONNECTED mWaitingApns=[[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 mDataConnectionAc=GsmDC-1 mReason=dataEnabled mRetryCount=0 mDataEnabled=true mDependencyMet=true}
07-12 11:19:24.830 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:usccapp
07-12 11:19:24.830 D/GSM     ( 1227): [GsmDCT] isDataPossible(usccapp): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.830 D/GSM     ( 1227): [GsmDCT] get active apn string for type:usccapp
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] notifyOffApnsOfAvailability skipped apn due to isReady==false: {mApnType=default mState=IDLE mWaitingApns=[[ApnSettingV2] SKT, 476, 45005, lte.sktelecom.com, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, default | mms | dun | hipri | supl | fota | cbs, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT, 476, 45005, lte.sktelecom.com, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, default | mms | dun | hipri | supl | fota | cbs, IP, IP, true, 0 mDataConnectionAc=null mReason=2GVoiceCallEnded mRetryCount=0 mDataEnabled=true mDependencyMet=true}
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:vzw800
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] isDataPossible(vzw800): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] get active apn string for type:vzw800
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:mms
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] isDataPossible(mms): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] get active apn string for type:mms
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:cbs
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] isDataPossible(cbs): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] get active apn string for type:cbs
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:bip
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] isDataPossible(bip): possible=false isDataAllowed=true apnTypePossible=false apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.840 D/GSM     ( 1227): [GsmDCT] get active apn string for type:bip
07-12 11:19:24.850 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:vzwapp
07-12 11:19:24.850 D/GSM     ( 1227): [GsmDCT] isDataPossible(vzwapp): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:24.850 D/GSM     ( 1227): [GsmDCT] get active apn string for type:vzwapp
07-12 11:19:24.890 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:19:24.890 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:19:24.890 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:19:24.890 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:19:24.890 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:19:24.890 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:19:24.910 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:19:24.910 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:19:24.910 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:19:25.721 D/RILJ    ( 1227): [UNSL]< UNSOL_NITZ_TIME_RECEIVED 13/07/12,02:19:26+36,00
07-12 11:19:25.721 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4d4c0408000b00000002000d0001040000000000
07-12 11:19:25.721 D/GSM     ( 1227): [GsmSST] NITZ: 13/07/12,02:19:26+36,00,108838751 start=108838755 delay=4
07-12 11:19:25.721 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:19:25.721 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:19:25.721 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525388
07-12 11:19:25.721 D/RILJ    ( 1227): Response ID 525388is not served in this process.
07-12 11:19:25.721 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:19:25.721 D/RILJ    ( 1227): [UNSL]< UNSOL_WCDMA_ACCEPT_RECEIVED {1, 1}
07-12 11:19:25.721 I/GSM     ( 1227): NITZ: current iso = kr, mGotCountryCode = true
07-12 11:19:25.721 I/GSM     ( 1227):  NITZ: after iso = kr, mGotCountryCode = true
07-12 11:19:25.721 D/RILJ    ( 1227): [UNSL]< UNSOL_VOICE_RADIO_TECH_CHANGED {0}
07-12 11:19:25.721 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:25.721 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:25.721 D/GSM     ( 1227): [GsmSST] NITZ:2 getAutoTimeZone() is OK : Asia/Seoul
07-12 11:19:25.721 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: setTimeZone=Asia/Seoul
07-12 11:19:25.721 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: call alarm.setTimeZone and broadcast zoneId=Asia/Seoul
07-12 11:19:25.721 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595559005,108832047,Asia/Seoul,450
07-12 11:19:25.731 D/GSM     ( 1227): [GsmSST] NITZ: Setting time of day to Fri Jul 12 11:19:26 GMT+09:00 2013 NITZ receive delay(ms): 11 gained(ms): 273 from 13/07/12,02:19:26+36,00
07-12 11:19:25.731 W/GSM     ( 1227): BroadcastNITZTime
07-12 11:19:25.731 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTime: time=1373595566011ms
07-12 11:19:26.011 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:26.011 I/GSM     ( 1227): NITZ: after Setting time of day
07-12 11:19:26.011 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595566011,108838777,Asia/Seoul,450
07-12 11:19:26.021 E/GSM     ( 1227): LGT Network Accept: mm_accept = 1 ,gmm_accept = 1
07-12 11:19:26.021 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:26.021 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:26.021 D/RILJ    ( 1227): [11327]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:26.021 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 3
07-12 11:19:26.021 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:19:26.031 D/RILJ    ( 1227): responseGetModemInfo[I@438c5050
07-12 11:19:26.031 D/RILJ    ( 1227): [11327]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:26.041 D/PHONE   ( 1227): [PhoneProxy] Ignoring voice radio technology changed message. newVoiceRadioTech = Unknown. Active Phone = GSM
07-12 11:19:26.041 D/RILJ    ( 1227): [11328]> OPERATOR
07-12 11:19:26.041 D/RILJ    ( 1227): [11329]> DATA_REGISTRATION_STATE
07-12 11:19:26.041 D/RILJ    ( 1227): [11330]> VOICE_REGISTRATION_STATE
07-12 11:19:26.041 D/RILJ    ( 1227): [11331]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:26.041 D/RILJ    ( 1227): [11328]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:26.051 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:26.051 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:26.051 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:26.051 D/RILJ    ( 1227): [11332]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:26.051 D/RILJ    ( 1227): [11333]> OPERATOR
07-12 11:19:26.051 D/RILJ    ( 1227): [11334]> DATA_REGISTRATION_STATE
07-12 11:19:26.051 D/RILJ    ( 1227): [11335]> VOICE_REGISTRATION_STATE
07-12 11:19:26.051 D/RILJ    ( 1227): [11336]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:26.051 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:26.051 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:26.051 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:26.051 D/RILJ    ( 1227): [11337]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:26.051 D/RILJ    ( 1227): [11338]> OPERATOR
07-12 11:19:26.051 D/RILJ    ( 1227): [11339]> DATA_REGISTRATION_STATE
07-12 11:19:26.051 D/RILJ    ( 1227): [11340]> VOICE_REGISTRATION_STATE
07-12 11:19:26.051 D/RILJ    ( 1227): [11341]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:26.051 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:26.051 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:26.051 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:26.051 D/RILJ    ( 1227): [11342]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:26.051 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:26.061 D/RILJ    ( 1227): responseGetModemInfo[I@43947590
07-12 11:19:26.061 D/RILJ    ( 1227): [11332]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:26.061 D/RILJ    ( 1227): [11331]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:26.061 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:26.061 D/RILJ    ( 1227): responseGetModemInfo[I@435f5650
07-12 11:19:26.061 D/RILJ    ( 1227): [11337]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:26.061 D/RILJ    ( 1227): [11329]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:26.061 D/RILJ    ( 1227): [11334]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:26.061 D/RILJ    ( 1227): [11339]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:26.061 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:26.061 D/RILJ    ( 1227): responseGetModemInfo[I@43b480f0
07-12 11:19:26.061 D/RILJ    ( 1227): [11342]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:26.061 D/RILJ    ( 1227): [11336]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:26.061 D/GSM     ( 1227): [EONS] Received TAC = 12818
07-12 11:19:26.061 D/GSM     ( 1227): [EONS] Received CID = 10825479
07-12 11:19:26.061 D/RILJ    ( 1227): [11341]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:26.061 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =14 , mTAC =12818
07-12 11:19:26.061 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:26.061 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:26.071 D/RILJ    ( 1227): [11333]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:26.071 D/RILJ    ( 1227): [11338]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:26.071 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:26.071 D/RILJ    ( 1227): [11330]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:26.071 D/RILJ    ( 1227): [11335]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:26.071 D/RILJ    ( 1227): [11343]> OPERATOR
07-12 11:19:26.071 D/RILJ    ( 1227): [11344]> DATA_REGISTRATION_STATE
07-12 11:19:26.071 D/RILJ    ( 1227): [11340]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:26.071 D/RILJ    ( 1227): [11345]> VOICE_REGISTRATION_STATE
07-12 11:19:26.071 D/RILJ    ( 1227): [11346]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:26.071 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:26.071 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:26.071 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:26.071 D/RILJ    ( 1227): [11347]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:26.071 D/RILJ    ( 1227): [11348]> OPERATOR
07-12 11:19:26.071 D/RILJ    ( 1227): [11349]> DATA_REGISTRATION_STATE
07-12 11:19:26.071 D/RILJ    ( 1227): [11343]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:26.071 D/RILJ    ( 1227): [11344]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:26.071 D/RILJ    ( 1227): [11345]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:26.071 D/RILJ    ( 1227): [11346]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:26.071 D/RILJ    ( 1227): responseGetModemInfo[I@42fa3bf8
07-12 11:19:26.071 D/RILJ    ( 1227): [11347]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:26.071 D/RILJ    ( 1227): [11350]> VOICE_REGISTRATION_STATE
07-12 11:19:26.081 D/RILJ    ( 1227): [11351]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:26.081 D/RILJ    ( 1227): [11348]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:26.081 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:26.081 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:26.081 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:26.081 D/RILJ    ( 1227): [11350]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:26.081 D/RILJ    ( 1227): [11352]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:26.081 D/RILJ    ( 1227): [11349]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:26.081 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:26.081 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 14, CStype = 14
07-12 11:19:26.081 D/GSM     ( 1227): [EONS] Received TAC = 12818
07-12 11:19:26.081 D/GSM     ( 1227): [EONS] Received CID = 10825479
07-12 11:19:26.081 D/GSM     ( 1227): use mTAC  with LTE: 12818
07-12 11:19:26.081 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =14 , mTAC =12818
07-12 11:19:26.091 D/RILJ    ( 1227): responseGetModemInfo[I@438f9c60
07-12 11:19:26.091 D/RILJ    ( 1227): [11352]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:26.091 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:26.091 D/RILJ    ( 1227): [11351]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:26.091 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:26.091 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=LTE
07-12 11:19:26.091 D/GSM     ( 1227): [IMS_AFW] Radio Tech is LTE, Get LTE Info from modem
07-12 11:19:26.091 D/RILJ    ( 1227): [11353]> RIL_REQUEST_LTE_INFO_FOR_IMS
07-12 11:19:26.091 D/GSM     ( 1227): [GsmSST] RAT switched UMTS -> LTE at cell 10825479
07-12 11:19:26.091 D/RILJ    ( 1227): [11353]< RIL_REQUEST_LTE_INFO_FOR_IMS 450,05,0a52f07,3212
07-12 11:19:26.091 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:26.091 D/GSM     ( 1227): [EONS] updateEons() lactac = 12818 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:26.091 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:26.091 D/GSM     ( 1227): [GsmSST] shouldFixTimeZoneNow: retVal=false iccCard=null iccCard.state=null iccCardExist=false operatorNumeric=45005 mcc=450 prevOperatorNumeric=45005 prevMcc=450 needToFixTimeZone=false ltod=07-12 11:19:26.101
07-12 11:19:26.101 D/GSM     ( 1227): [GsmDCT] get all active apn types
07-12 11:19:26.101 D/GSM     ( 1227): [GsmDCT] return link properites for ims
07-12 11:19:26.111 D/GSM     ( 1227): [GsmDCT] get active pdp is not null, return link Capabilities for ims
07-12 11:19:26.111 D/GSM     ( 1227): [GsmDCT] isDataPossible(ims): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=CONNECTED
07-12 11:19:26.111 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ims
07-12 11:19:26.111 D/GSM     ( 1227): [GsmDCT] isDataPossible(default): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=IDLE
07-12 11:19:26.111 D/GSM     ( 1227): [GsmDCT] get active apn string for type:default
07-12 11:19:26.121 D/GSM     ( 1227): [GsmSST] [IMS_AFW] EVENT_GET_LTE_INFO_DONE
07-12 11:19:26.121 D/GSM     ( 1227): [GsmSST] [IMS_AFW] GET LTE Info: 450,05,0a52f07,3212
07-12 11:19:26.121 D/GSM     ( 1227): [GSMphone] mIccRecords.iccid = 8982051006425136633
07-12 11:19:26.121 D/GSM     ( 1227): [GsmSST] [IMS_AFW] MCC : 450, MNC : 05, Cell ID : 0a52f07, TAC : 3212
07-12 11:19:26.881 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:19:26.881 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:19:26.881 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:19:29.183 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4d4c0408000b00000002000d0001040000000000
07-12 11:19:29.183 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:19:29.183 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:19:29.183 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525388
07-12 11:19:29.183 D/RILJ    ( 1227): Response ID 525388is not served in this process.
07-12 11:19:29.183 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:19:29.183 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:29.183 D/RILJ    ( 1227): [11354]> OPERATOR
07-12 11:19:29.183 D/RILJ    ( 1227): [11355]> DATA_REGISTRATION_STATE
07-12 11:19:29.183 D/RILJ    ( 1227): [11355]< DATA_REGISTRATION_STATE {1, 3212, 00a52f03, 14, null, 20}
07-12 11:19:29.193 D/RILJ    ( 1227): [11356]> VOICE_REGISTRATION_STATE
07-12 11:19:29.193 D/RILJ    ( 1227): [11357]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:29.193 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:29.193 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:29.193 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:29.193 D/RILJ    ( 1227): [11358]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:29.203 D/RILJ    ( 1227): [11354]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:29.203 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:19:29.203 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:19:29.203 D/RILJ    ( 1227): [11356]< VOICE_REGISTRATION_STATE {1, null, 00a52f03, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:29.203 D/RILJ    ( 1227): [11357]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:29.203 D/RILJ    ( 1227): responseGetModemInfo[I@43cc8f80
07-12 11:19:29.203 D/RILJ    ( 1227): [11358]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:29.213 D/GSM     ( 1227): [EONS] Received TAC = 12818
07-12 11:19:29.213 D/GSM     ( 1227): [EONS] Received CID = 10825475
07-12 11:19:29.213 D/GSM     ( 1227): use mTAC  with LTE: 12818
07-12 11:19:29.213 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =14 , mTAC =12818
07-12 11:19:29.213 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 14, CStype = 14
07-12 11:19:29.213 D/GSM     ( 1227): use mTAC instead of lac because NULL with LTE: 12818
07-12 11:19:29.213 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:29.223 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=LTE newType=LTE
07-12 11:19:29.223 D/GSM     ( 1227): [IMS_AFW] Radio Tech is LTE, Get LTE Info from modem
07-12 11:19:29.223 D/RILJ    ( 1227): [11359]> RIL_REQUEST_LTE_INFO_FOR_IMS
07-12 11:19:29.223 D/RILJ    ( 1227): [11359]< RIL_REQUEST_LTE_INFO_FOR_IMS 450,05,0a52f03,3212
07-12 11:19:29.223 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:29.223 D/GSM     ( 1227): [EONS] updateEons() lactac = 12818 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:29.223 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:29.223 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:29.233 D/GSM     ( 1227): [GsmSST] [IMS_AFW] EVENT_GET_LTE_INFO_DONE
07-12 11:19:29.233 D/GSM     ( 1227): [GsmSST] [IMS_AFW] GET LTE Info: 450,05,0a52f03,3212
07-12 11:19:29.233 D/GSM     ( 1227): [GsmSST] [IMS_AFW] MCC : 450, MNC : 05, Cell ID : 0a52f03, TAC : 3212
07-12 11:19:31.185 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:19:31.185 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:19:31.185 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:19:36.761 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:19:36.761 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:19:37.142 E/PHONE   ( 1227): Settings Exception Reading Dual Sim Voice Prompt Values
07-12 11:19:37.142 D/PHONE   ( 1227): Prompt option:false
07-12 11:19:37.242 D/GSM     ( 1227): isTwoDigitShortCode
07-12 11:19:37.242 D/GSM     ( 1227): dialing w/ mmi 'null'...
07-12 11:19:37.242 D/GSM     ( 1227): [GSMConn] acquireWakeLock
07-12 11:19:37.242 D/RILJ    ( 1227): [11360]> SET_MUTE false
07-12 11:19:37.242 D/RILJ    ( 1227): [11360]< SET_MUTE 
07-12 11:19:37.242 D/RILJ    ( 1227): [11361]> DIAL
07-12 11:19:37.482 E/RILC    (  341): responseLGERPInd(): param(426000(0x00068010)), data_valid(1), data_len(1)
07-12 11:19:37.482 I/RILJ    ( 1227): LGE_UNSOL_IS_LTE_AVAILABLE:1
07-12 11:19:37.492 D/RILJ    ( 1227): returned data  = [B@42882828
07-12 11:19:37.492 D/RILJ    ( 1227): [11361]< DIAL 
07-12 11:19:37.492 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:19:37.602 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:19:37.602 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:19:37.672 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270343 when=-426ms obj=android.os.AsyncResult@428429d0 }
07-12 11:19:37.672 D/GSM     ( 1227): [GsmDCT] onVoiceCallStarted
07-12 11:19:37.672 D/RILJ    ( 1227): [11362]> GET_CURRENT_CALLS
07-12 11:19:37.682 E/RILC    (  341): numberplus = ""
07-12 11:19:37.682 E/RILC    (  341): signalIE = 0
07-12 11:19:37.682 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:19:37.682 D/RILJ    ( 1227): No calling name expression is received
07-12 11:19:37.682 D/RILJ    ( 1227): signal = 0
07-12 11:19:37.682 D/RILJ    ( 1227): DriverCall dc = id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:19:37.682 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:19:37.682 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:19:37.682 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:19:37.682 D/RILJ    ( 1227): [DriverCall] dc : id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:19:37.682 D/RILJ    ( 1227): [11362]< GET_CURRENT_CALLS  [id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:19:37.682 D/RILJ    ( 1227): [11363]> GET_CURRENT_CALLS
07-12 11:19:37.682 E/RILC    (  341): numberplus = ""
07-12 11:19:37.682 E/RILC    (  341): signalIE = 0
07-12 11:19:37.682 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:19:37.682 D/RILJ    ( 1227): No calling name expression is received
07-12 11:19:37.682 D/RILJ    ( 1227): signal = 0
07-12 11:19:37.682 D/RILJ    ( 1227): DriverCall dc = id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:19:37.682 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:19:37.682 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:19:37.682 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:19:37.682 D/RILJ    ( 1227): [DriverCall] dc : id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:19:37.682 D/RILJ    ( 1227): [11363]< GET_CURRENT_CALLS  [id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:19:37.702 D/RILJ    ( 1227): responseDataCallList ver=7 num=1
07-12 11:19:37.702 D/RILJ    ( 1227): [UNSL]< UNSOL_DATA_CALL_LIST_CHANGED [DataCallState: {version=7 status=0 retry=-1 cid=0 active=2 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}]
07-12 11:19:37.742 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:19:37.742 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:19:37.742 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:19:37.752 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:19:37.752 D/GSM     ( 1227): [GSMConn] update: parent=DIALING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=false
07-12 11:19:37.752 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:19:37.752 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270340 when=-55ms obj=android.os.AsyncResult@43225650 }
07-12 11:19:37.752 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): E
07-12 11:19:37.752 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): DataCallState size=1
07-12 11:19:37.762 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): E dcacs=[GsmDC-1]
07-12 11:19:37.762 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): X list=[]
07-12 11:19:37.762 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): Found ConnId=0 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=2 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:19:37.762 D/GSM     ( 1227): addr/pl=42.19.184.78/30
07-12 11:19:37.762 D/GSM     ( 1227): [GsmDC-1] REQ_UPDATE_LINK_PROPERTIES_DATA_CALL_STATE result=com.android.internal.telephony.DataConnection$UpdateLinkPropertyResult@42a21468 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=2 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:19:37.762 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): no change
07-12 11:19:37.762 D/GSM     ( 1227): [GsmDCT] onDataStateChanged: Data Activity updated to NONE. isAnyDataCallActive = true isAnyDataCallDormant = false
07-12 11:19:37.762 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:19:37.762 D/GSM     ( 1227): [GsmDCT] onDataStateChange(ar): apnsToCleanup=[]
07-12 11:19:37.762 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): X
07-12 11:19:37.782 D/RILJ    ( 1227): responseDataCallList ver=7 num=1
07-12 11:19:37.782 D/RILJ    ( 1227): [UNSL]< UNSOL_DATA_CALL_LIST_CHANGED [DataCallState: {version=7 status=0 retry=-1 cid=0 active=1 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}]
07-12 11:19:37.903 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270340 when=-113ms obj=android.os.AsyncResult@43c9ddb0 }
07-12 11:19:37.903 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): E
07-12 11:19:37.903 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): DataCallState size=1
07-12 11:19:37.903 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): E dcacs=[GsmDC-1]
07-12 11:19:37.903 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): X list=[]
07-12 11:19:37.903 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): Found ConnId=0 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=1 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:19:37.903 D/GSM     ( 1227): addr/pl=42.19.184.78/30
07-12 11:19:37.903 D/GSM     ( 1227): [GsmDC-1] REQ_UPDATE_LINK_PROPERTIES_DATA_CALL_STATE result=com.android.internal.telephony.DataConnection$UpdateLinkPropertyResult@42a2f0f0 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=1 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:19:37.903 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): no change
07-12 11:19:37.903 D/GSM     ( 1227): topActivity.getPackageName(); = com.android.phone
07-12 11:19:37.903 D/GSM     ( 1227): topActivity.getClassName(); = com.android.phone.InCallScreen
07-12 11:19:37.903 D/GSM     ( 1227): VOICE CALL  ::true
07-12 11:19:37.903 D/GSM     ( 1227): (InCallScreen) topActivity.getClassName(); = com.android.phone.InCallScreen
07-12 11:19:37.913 D/GSM     ( 1227): functionForPacketDrop is called
07-12 11:19:37.913 D/GSM     ( 1227): [GsmDCT] onDataStateChanged: Data Activity updated to DORMANT. stopNetStatePoll
07-12 11:19:37.913 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:19:37.923 D/GSM     ( 1227): [GsmDCT] onDataStateChange(ar): apnsToCleanup=[]
07-12 11:19:37.923 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): X
07-12 11:19:38.523 D/RILJ    ( 1227): [11364]> SCREEN_STATE: false
07-12 11:19:38.533 D/RILJ    ( 1227): [11364]< SCREEN_STATE 
07-12 11:19:38.543 D/GSM     ( 1227): [GsmDCT] onReceive: action=android.intent.action.SCREEN_OFF
07-12 11:19:38.543 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:19:38.543 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:19:38.543 D/GSM     ( 1227): [GsmDCT] startNetStatPoll
07-12 11:19:39.494 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4def0308000100000003
07-12 11:19:39.494 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:19:39.494 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:19:39.494 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525295
07-12 11:19:39.494 D/RILJ    ( 1227): Response ID 525295is not served in this process.
07-12 11:19:39.494 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:19:39.494 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4d4c0408000b00000002000d0001040000000000
07-12 11:19:39.494 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:19:39.494 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:19:39.494 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525388
07-12 11:19:39.494 D/RILJ    ( 1227): Response ID 525388is not served in this process.
07-12 11:19:39.494 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:19:39.494 D/RILJ    ( 1227): [UNSL]< UNSOL_VOICE_RADIO_TECH_CHANGED {3}
07-12 11:19:39.494 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:39.494 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:39.494 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:39.494 D/PHONE   ( 1227): [PhoneProxy] Ignoring voice radio technology changed message. newVoiceRadioTech = 3 Active Phone = GSM
07-12 11:19:39.494 D/RILJ    ( 1227): [11365]> OPERATOR
07-12 11:19:39.494 D/RILJ    ( 1227): [11366]> DATA_REGISTRATION_STATE
07-12 11:19:39.504 D/RILJ    ( 1227): [11367]> VOICE_REGISTRATION_STATE
07-12 11:19:39.504 D/RILJ    ( 1227): [11368]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:39.504 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:39.504 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:39.504 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:39.504 D/RILJ    ( 1227): [11369]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:39.504 D/RILJ    ( 1227): [11370]> OPERATOR
07-12 11:19:39.504 D/RILJ    ( 1227): [11371]> DATA_REGISTRATION_STATE
07-12 11:19:39.504 D/RILJ    ( 1227): [11372]> VOICE_REGISTRATION_STATE
07-12 11:19:39.504 D/RILJ    ( 1227): [11373]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:39.504 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:39.504 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:39.504 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:39.504 D/RILJ    ( 1227): [11374]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:39.504 D/RILJ    ( 1227): [11375]> OPERATOR
07-12 11:19:39.504 D/RILJ    ( 1227): [11376]> DATA_REGISTRATION_STATE
07-12 11:19:39.504 D/RILJ    ( 1227): [11377]> VOICE_REGISTRATION_STATE
07-12 11:19:39.514 D/RILJ    ( 1227): [11368]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:39.514 D/RILJ    ( 1227): [11367]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, null, null, null, 0, 31}
07-12 11:19:39.514 D/RILJ    ( 1227): [11366]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:19:39.514 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:39.514 D/RILJ    ( 1227): [11378]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:39.514 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:39.514 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:39.514 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:39.514 D/RILJ    ( 1227): [11379]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:39.514 D/RILJ    ( 1227): [11380]> OPERATOR
07-12 11:19:39.514 D/RILJ    ( 1227): [11381]> DATA_REGISTRATION_STATE
07-12 11:19:39.514 D/RILJ    ( 1227): [11365]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:39.514 D/RILJ    ( 1227): responseGetModemInfo[I@43689b18
07-12 11:19:39.514 D/RILJ    ( 1227): [11369]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:39.514 D/RILJ    ( 1227): responseGetModemInfo[I@4368d500
07-12 11:19:39.514 D/RILJ    ( 1227): [11374]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:39.514 D/RILJ    ( 1227): [11382]> VOICE_REGISTRATION_STATE
07-12 11:19:39.514 D/RILJ    ( 1227): responseGetModemInfo[I@436a9f90
07-12 11:19:39.514 D/RILJ    ( 1227): [11379]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:39.514 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:39.514 D/RILJ    ( 1227): [11373]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:39.524 D/RILJ    ( 1227): [11378]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:39.524 D/RILJ    ( 1227): [11383]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:39.524 D/RILJ    ( 1227): [11372]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:19:39.524 D/RILJ    ( 1227): [11377]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:19:39.524 D/RILJ    ( 1227): [11382]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:19:39.524 D/RILJ    ( 1227): [11371]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:19:39.524 D/RILJ    ( 1227): [11376]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:19:39.524 D/RILJ    ( 1227): [11381]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:19:39.524 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:39.524 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:39.524 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:39.524 D/RILJ    ( 1227): [11384]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:39.524 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:39.524 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:39.524 D/RILJ    ( 1227): [11370]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:39.524 D/RILJ    ( 1227): [11375]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:39.524 D/RILJ    ( 1227): [11380]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:39.524 D/RILJ    ( 1227): responseGetModemInfo[I@436f1698
07-12 11:19:39.524 D/RILJ    ( 1227): [11384]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:39.524 D/RILJ    ( 1227): [11383]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:39.534 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:39.534 D/RILJ    ( 1227): [11385]> OPERATOR
07-12 11:19:39.534 D/RILJ    ( 1227): [11386]> DATA_REGISTRATION_STATE
07-12 11:19:39.534 D/RILJ    ( 1227): [11387]> VOICE_REGISTRATION_STATE
07-12 11:19:39.534 D/RILJ    ( 1227): [11388]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:39.534 D/RILJ    ( 1227): [11386]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:19:39.534 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:39.534 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:39.534 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:39.534 D/RILJ    ( 1227): [11389]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:39.534 D/RILJ    ( 1227): [11385]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:39.534 D/RILJ    ( 1227): [11388]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:39.534 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:39.534 D/RILJ    ( 1227): [11387]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:19:39.534 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:19:39.534 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:19:39.534 D/GSM     ( 1227): use mTAC  with LTE: 8689
07-12 11:19:39.534 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:19:39.534 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:19:39.534 D/GSM     ( 1227): use lac because Not NULL: 8689
07-12 11:19:39.534 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:39.534 D/RILJ    ( 1227): responseGetModemInfo[I@4374c1b0
07-12 11:19:39.544 D/RILJ    ( 1227): [11389]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:39.544 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=LTE newType=UMTS
07-12 11:19:39.544 D/GSM     ( 1227): [GsmSST] RAT switched LTE -> UMTS at cell 65803780
07-12 11:19:39.544 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:39.544 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:39.544 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:39.544 D/GSM     ( 1227): [GsmSST] shouldFixTimeZoneNow: retVal=false iccCard=null iccCard.state=null iccCardExist=false operatorNumeric=45005 mcc=450 prevOperatorNumeric=45005 prevMcc=450 needToFixTimeZone=false ltod=07-12 11:19:39.549
07-12 11:19:39.544 D/GSM     ( 1227): [GsmDCT] get all active apn types
07-12 11:19:39.544 D/GSM     ( 1227): [GsmDCT] return link properites for ims
07-12 11:19:39.554 D/GSM     ( 1227): [GsmDCT] get active pdp is not null, return link Capabilities for ims
07-12 11:19:39.554 D/GSM     ( 1227): [GsmDCT] isDataPossible(ims): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=CONNECTED
07-12 11:19:39.554 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ims
07-12 11:19:39.554 D/GSM     ( 1227): [GsmDCT] isDataPossible(default): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=IDLE
07-12 11:19:39.554 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:19:39.554 D/GSM     ( 1227): [GsmDCT] get active apn string for type:default
07-12 11:19:39.554 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:19:39.564 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:39.644 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:19:39.644 D/RILJ    ( 1227): [11390]> GET_CURRENT_CALLS
07-12 11:19:39.644 E/RILC    (  341): numberplus = ""
07-12 11:19:39.644 E/RILC    (  341): signalIE = 0
07-12 11:19:39.644 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:19:39.644 D/RILJ    ( 1227): No calling name expression is received
07-12 11:19:39.644 D/RILJ    ( 1227): signal = 0
07-12 11:19:39.644 D/RILJ    ( 1227): DriverCall dc = id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:19:39.644 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:19:39.644 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:19:39.644 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:19:39.644 D/RILJ    ( 1227): [DriverCall] dc : id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:19:39.644 D/RILJ    ( 1227): [11390]< GET_CURRENT_CALLS  [id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:19:39.644 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:19:39.644 D/GSM     ( 1227): [GSMConn] update: parent=DIALING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=false
07-12 11:19:39.644 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:19:39.714 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:39.714 D/RILJ    ( 1227): [11391]> OPERATOR
07-12 11:19:39.714 D/RILJ    ( 1227): [11392]> DATA_REGISTRATION_STATE
07-12 11:19:39.714 D/RILJ    ( 1227): [11393]> VOICE_REGISTRATION_STATE
07-12 11:19:39.714 D/RILJ    ( 1227): [11394]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:39.714 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:39.714 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:39.714 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:39.724 D/RILJ    ( 1227): [11395]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:39.724 D/RILJ    ( 1227): [11392]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:19:39.724 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:19:39.724 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:19:39.724 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:19:39.724 D/RILJ    ( 1227): [11391]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:39.724 D/RILJ    ( 1227): [11394]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:39.724 D/RILJ    ( 1227): [11393]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:19:39.724 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:19:39.724 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:39.724 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:19:39.724 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:39.724 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:39.724 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:39.724 D/RILJ    ( 1227): responseGetModemInfo[I@438475a8
07-12 11:19:39.724 D/RILJ    ( 1227): [11395]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:39.724 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:41.857 D/RILJ    ( 1227): [UNSL]< UNSOL_NITZ_TIME_RECEIVED 13/07/12,02:19:42+36,00
07-12 11:19:41.857 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:41.857 D/GSM     ( 1227): [GsmSST] NITZ: 13/07/12,02:19:42+36,00,108854614 start=108854617 delay=3
07-12 11:19:41.857 I/GSM     ( 1227): NITZ: current iso = kr, mGotCountryCode = true
07-12 11:19:41.857 I/GSM     ( 1227):  NITZ: after iso = kr, mGotCountryCode = true
07-12 11:19:41.857 D/GSM     ( 1227): [GsmSST] NITZ:2 getAutoTimeZone() is OK : Asia/Seoul
07-12 11:19:41.857 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: setTimeZone=Asia/Seoul
07-12 11:19:41.867 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: call alarm.setTimeZone and broadcast zoneId=Asia/Seoul
07-12 11:19:41.867 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595566011,108838777,Asia/Seoul,450
07-12 11:19:41.867 D/GSM     ( 1227): [GsmSST] NITZ: Setting time of day to Fri Jul 12 11:19:42 GMT+09:00 2013 NITZ receive delay(ms): 14 gained(ms): 138 from 13/07/12,02:19:42+36,00
07-12 11:19:41.867 W/GSM     ( 1227): BroadcastNITZTime
07-12 11:19:41.877 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTime: time=1373595582014ms
07-12 11:19:42.084 I/GSM     ( 1227): NITZ: after Setting time of day
07-12 11:19:42.084 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595582014,108854714,Asia/Seoul,450
07-12 11:19:42.084 D/RILJ    ( 1227): [11396]> OPERATOR
07-12 11:19:42.094 D/RILJ    ( 1227): [11397]> DATA_REGISTRATION_STATE
07-12 11:19:42.094 D/RILJ    ( 1227): [11398]> VOICE_REGISTRATION_STATE
07-12 11:19:42.104 D/RILJ    ( 1227): [11396]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:42.104 D/RILJ    ( 1227): [11399]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:42.104 D/RILJ    ( 1227): [11397]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:19:42.104 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:42.104 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:42.104 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:42.114 D/RILJ    ( 1227): [11398]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:19:42.114 D/RILJ    ( 1227): [11399]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:42.134 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:42.134 D/RILJ    ( 1227): [UNSL]< UNSOL_WCDMA_ACCEPT_RECEIVED {0, 1}
07-12 11:19:42.134 D/RILJ    ( 1227): responseGetModemInfo[I@438d32e8
07-12 11:19:42.134 D/RILJ    ( 1227): [11400]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:42.144 D/RILJ    ( 1227): [11400]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:42.144 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:19:42.144 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:19:42.144 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:19:42.154 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:19:42.154 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:42.154 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:19:42.154 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:42.154 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:42.154 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:42.154 D/RILJ    ( 1227): [11401]> OPERATOR
07-12 11:19:42.164 D/RILJ    ( 1227): [11402]> DATA_REGISTRATION_STATE
07-12 11:19:42.164 D/RILJ    ( 1227): [11401]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:42.164 D/RILJ    ( 1227): [11403]> VOICE_REGISTRATION_STATE
07-12 11:19:42.164 D/RILJ    ( 1227): [11402]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:19:42.164 D/RILJ    ( 1227): [11404]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:42.164 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:42.164 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:42.164 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:42.164 D/RILJ    ( 1227): [11405]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:42.164 E/GSM     ( 1227): LGT Network Accept: mm_accept = 0 ,gmm_accept = 1
07-12 11:19:42.174 D/RILJ    ( 1227): [11403]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:19:42.174 D/RILJ    ( 1227): [11404]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:42.174 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:42.174 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:42.174 D/RILJ    ( 1227): [11406]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:42.174 D/RILJ    ( 1227): responseGetModemInfo[I@43913140
07-12 11:19:42.174 D/RILJ    ( 1227): [11405]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:42.184 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:42.184 D/RILJ    ( 1227): responseGetModemInfo[I@439199a0
07-12 11:19:42.184 D/RILJ    ( 1227): [11406]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:42.184 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:19:42.184 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:19:42.184 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:19:42.184 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:19:42.184 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:42.184 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:19:42.184 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:42.184 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:42.184 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:42.184 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:42.184 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:42.194 D/GSM     ( 1227): [GSMphone] mIccRecords.iccid = 8982051006425136633
07-12 11:19:44.125 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:19:44.125 D/RILJ    ( 1227): [11407]> GET_CURRENT_CALLS
07-12 11:19:44.125 E/RILC    (  341): numberplus = ""
07-12 11:19:44.125 E/RILC    (  341): signalIE = 0
07-12 11:19:44.125 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:19:44.125 D/RILJ    ( 1227): No calling name expression is received
07-12 11:19:44.125 D/RILJ    ( 1227): signal = 0
07-12 11:19:44.125 D/RILJ    ( 1227): DriverCall dc = id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:19:44.125 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:19:44.135 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:19:44.135 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:19:44.135 D/RILJ    ( 1227): [DriverCall] dc : id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:19:44.135 D/RILJ    ( 1227): [11407]< GET_CURRENT_CALLS  [id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:19:44.135 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:19:44.135 D/GSM     ( 1227): [GSMConn] update: parent=ALERTING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=true
07-12 11:19:44.135 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:19:46.187 D/RILJ    ( 1227): [11408]> SCREEN_STATE: true
07-12 11:19:46.207 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:46.217 D/RILJ    ( 1227): [11408]< SCREEN_STATE 
07-12 11:19:46.387 D/RILJ    ( 1227): [11409]> OPERATOR
07-12 11:19:46.387 D/RILJ    ( 1227): [11410]> DATA_REGISTRATION_STATE
07-12 11:19:46.387 D/RILJ    ( 1227): [11411]> VOICE_REGISTRATION_STATE
07-12 11:19:46.387 D/RILJ    ( 1227): [11412]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:46.387 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:46.387 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:46.387 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:46.387 D/RILJ    ( 1227): [11413]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:46.387 D/RILJ    ( 1227): [11410]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:19:46.387 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 3
07-12 11:19:46.387 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:19:46.387 D/RILJ    ( 1227): [11412]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:46.398 D/RILJ    ( 1227): responseGetModemInfo[I@43d1efd8
07-12 11:19:46.398 D/RILJ    ( 1227): [11413]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:46.398 D/RILJ    ( 1227): [11409]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:46.398 D/RILJ    ( 1227): [11411]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:19:46.398 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:46.408 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:19:46.408 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:19:46.408 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:19:46.418 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:46.418 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:19:46.418 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:46.418 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:19:46.418 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:46.418 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:46.418 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:46.418 D/RILJ    ( 1227): [11414]> OPERATOR
07-12 11:19:46.418 D/RILJ    ( 1227): [11415]> DATA_REGISTRATION_STATE
07-12 11:19:46.418 D/RILJ    ( 1227): [11416]> VOICE_REGISTRATION_STATE
07-12 11:19:46.418 D/RILJ    ( 1227): [11415]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:19:46.418 D/RILJ    ( 1227): [11417]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:46.418 D/RILJ    ( 1227): [11414]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:46.418 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:46.418 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:46.418 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:46.418 D/RILJ    ( 1227): [11418]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:46.418 D/RILJ    ( 1227): [11417]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:46.428 D/RILJ    ( 1227): responseGetModemInfo[I@43d7bdd0
07-12 11:19:46.428 D/RILJ    ( 1227): [11418]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:19:46.438 D/RILJ    ( 1227): [11416]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:19:46.518 D/GSM     ( 1227): [GsmDCT] onReceive: action=android.intent.action.SCREEN_ON
07-12 11:19:46.518 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:19:46.518 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:19:46.518 D/GSM     ( 1227): [GsmDCT] startNetStatPoll
07-12 11:19:46.528 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:19:46.528 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:19:46.528 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:19:46.528 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:46.528 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:19:46.528 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:46.528 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:19:46.528 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:46.528 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:46.528 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:47.208 D/GSM     ( 1227): [GsmCallTracker] (foregnd) hangup dialing or alerting...
07-12 11:19:47.208 D/RILJ    ( 1227): hangupConnection: gsmIndex=1
07-12 11:19:47.208 D/RILJ    ( 1227): [11419]> HANGUP 1
07-12 11:19:47.499 D/RILJ    ( 1227): [11419]< HANGUP 
07-12 11:19:47.499 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:19:47.509 D/RILJ    ( 1227): [11420]> GET_CURRENT_CALLS
07-12 11:19:47.509 D/RILJ    ( 1227): [11421]> GET_CURRENT_CALLS
07-12 11:19:47.509 D/RILJ    ( 1227): [11420]< GET_CURRENT_CALLS  
07-12 11:19:47.509 D/RILJ    ( 1227): [11421]< GET_CURRENT_CALLS  
07-12 11:19:47.509 D/GSM     ( 1227): [GSMConn] releaseWakeLock
07-12 11:19:47.519 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270344 when=-5ms obj=android.os.AsyncResult@42948de0 }
07-12 11:19:47.519 D/GSM     ( 1227): [GsmDCT] onVoiceCallEnded
07-12 11:19:47.519 D/GSM     ( 1227): [LGE_DATA] functionForPacketDrop for ACTION_VOICE_CALL_ENDED
07-12 11:19:47.539 D/GSM     ( 1227): [GsmDCT] setupDataOnReadyApns: 2GVoiceCallEnded
07-12 11:19:47.539 D/GSM     ( 1227): [GsmDCT] configureRetry: forDefault=true retryCount=0 dc={GsmDC-1: State=DcActiveState apnSetting=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 apnList= [{mApnType=ims mState=CONNECTED mWaitingApns=[[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 mDataConnectionAc=GsmDC-1 mReason=dataEnabled mRetryCount=0 mDataEnabled=true mDependencyMet=true}] RefCount=1 cid=0 create=1373486750617 lastFail=-1 lastFailCause=NONE}
07-12 11:19:47.539 E/GSM     ( 1227): [GsmDCT] [LG_DATA] configureRetry : by DOMESTIC_DATA_RETRY_CONFIG
07-12 11:19:47.539 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [GsmDC-1] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [GsmDCT] configureRetry: forDefault=false retryCount=0 dc={GsmDC-2: State=DcInactiveState apnSetting=null apnList= [] RefCount=0 cid=-1 create=-1 lastFail=-1 lastFailCause=NONE}
07-12 11:19:47.539 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [GsmDC-2] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:admin] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:fota] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:ktmultirab1] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:entitlement] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:dun] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:ktmultirab2] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:supl] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:hipri] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:tethering] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:ims] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [GsmDC-1] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:usccapp] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:default] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:vzw800] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:mms] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:cbs] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:bip] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:vzwapp] setRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:19:47.539 D/GSM     ( 1227): [ApnContext:default] set reason as 2GVoiceCallEnded,current state IDLE
07-12 11:19:47.539 D/GSM     ( 1227): [GsmDCT] trySetupData for type:default due to 2GVoiceCallEnded
07-12 11:19:47.539 D/GSM     ( 1227): [GsmDCT] trySetupData with mIsPsRestricted=false
07-12 11:19:47.539 E/GSM     ( 1227): [GSMPhone] getEsn() is a CDMA method
07-12 11:19:47.539 E/GSM     ( 1227): [GSMPhone] getEsn() is a CDMA method
07-12 11:19:47.549 D/GSM     ( 1227): [LGE_DATA] <mbooting_phone> = false
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] MMS is available even if data enabled sets off : false
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:admin
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] isDataPossible(admin): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] get active apn string for type:admin
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:fota
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] isDataPossible(fota): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] get active apn string for type:fota
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:ktmultirab1
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] isDataPossible(ktmultirab1): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ktmultirab1
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:entitlement
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] isDataPossible(entitlement): possible=false isDataAllowed=true apnTypePossible=false apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] get active apn string for type:entitlement
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:dun
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] isDataPossible(dun): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.549 D/GSM     ( 1227): [GsmDCT] get active apn string for type:dun
07-12 11:19:47.559 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:ktmultirab2
07-12 11:19:47.559 D/GSM     ( 1227): [GsmDCT] isDataPossible(ktmultirab2): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.559 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ktmultirab2
07-12 11:19:47.559 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:supl
07-12 11:19:47.559 D/GSM     ( 1227): [GsmDCT] isDataPossible(supl): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.559 D/GSM     ( 1227): [GsmDCT] get active apn string for type:supl
07-12 11:19:47.559 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:hipri
07-12 11:19:47.559 D/GSM     ( 1227): [GsmDCT] isDataPossible(hipri): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.559 D/GSM     ( 1227): [GsmDCT] get active apn string for type:hipri
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:tethering
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] isDataPossible(tethering): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] get active apn string for type:tethering
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] notifyOffApnsOfAvailability skipped apn due to isReady==false: {mApnType=ims mState=CONNECTED mWaitingApns=[[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 mDataConnectionAc=GsmDC-1 mReason=dataEnabled mRetryCount=0 mDataEnabled=true mDependencyMet=true}
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:usccapp
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] isDataPossible(usccapp): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] get active apn string for type:usccapp
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] notifyOffApnsOfAvailability skipped apn due to isReady==false: {mApnType=default mState=IDLE mWaitingApns=[[ApnSettingV2] SKT, 476, 45005, lte.sktelecom.com, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, default | mms | dun | hipri | supl | fota | cbs, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT, 476, 45005, lte.sktelecom.com, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, default | mms | dun | hipri | supl | fota | cbs, IP, IP, true, 0 mDataConnectionAc=null mReason=2GVoiceCallEnded mRetryCount=0 mDataEnabled=true mDependencyMet=true}
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:vzw800
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] isDataPossible(vzw800): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] get active apn string for type:vzw800
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:mms
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] isDataPossible(mms): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.569 D/GSM     ( 1227): [GsmDCT] get active apn string for type:mms
07-12 11:19:47.579 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:cbs
07-12 11:19:47.579 D/GSM     ( 1227): [GsmDCT] isDataPossible(cbs): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.579 D/GSM     ( 1227): [GsmDCT] get active apn string for type:cbs
07-12 11:19:47.579 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:bip
07-12 11:19:47.579 D/GSM     ( 1227): [GsmDCT] isDataPossible(bip): possible=false isDataAllowed=true apnTypePossible=false apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.579 D/GSM     ( 1227): [GsmDCT] get active apn string for type:bip
07-12 11:19:47.579 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:vzwapp
07-12 11:19:47.579 D/GSM     ( 1227): [GsmDCT] isDataPossible(vzwapp): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:19:47.579 D/GSM     ( 1227): [GsmDCT] get active apn string for type:vzwapp
07-12 11:19:47.629 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:19:47.629 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:19:47.629 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:19:47.629 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:19:47.629 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:19:47.629 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:19:47.639 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:19:47.639 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:19:47.639 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:19:47.659 E/RILC    (  341): responseLGERPInd(): param(425992(0x00068008)), data_valid(1), data_len(4)
07-12 11:19:47.659 I/RILJ    ( 1227): LGE_UNSOL_RRC_RELEASE_CAUSE: releaseCause = 1
07-12 11:19:47.659 D/RILJ    ( 1227): returned data  = [B@429125e8
07-12 11:19:48.350 D/RILJ    ( 1227): [11422]> SCREEN_STATE: false
07-12 11:19:48.360 D/RILJ    ( 1227): [11422]< SCREEN_STATE 
07-12 11:19:48.440 D/GSM     ( 1227): [GsmDCT] onReceive: action=android.intent.action.SCREEN_OFF
07-12 11:19:48.440 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:19:48.440 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:19:48.440 D/GSM     ( 1227): [GsmDCT] startNetStatPoll
07-12 11:19:48.730 D/RILJ    ( 1227): [UNSL]< UNSOL_NITZ_TIME_RECEIVED 13/07/12,02:19:48+36,00
07-12 11:19:48.730 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:48.740 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4d4c0408000b00000002000d0001040000000000
07-12 11:19:48.740 D/GSM     ( 1227): [GsmSST] NITZ: 13/07/12,02:19:48+36,00,108861369 start=108861373 delay=4
07-12 11:19:48.740 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:19:48.740 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:19:48.740 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525388
07-12 11:19:48.740 D/RILJ    ( 1227): Response ID 525388is not served in this process.
07-12 11:19:48.740 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:19:48.740 D/RILJ    ( 1227): [UNSL]< UNSOL_VOICE_RADIO_TECH_CHANGED {0}
07-12 11:19:48.740 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:48.740 I/GSM     ( 1227): NITZ: current iso = kr, mGotCountryCode = true
07-12 11:19:48.740 I/GSM     ( 1227):  NITZ: after iso = kr, mGotCountryCode = true
07-12 11:19:48.740 D/GSM     ( 1227): [GsmSST] NITZ:2 getAutoTimeZone() is OK : Asia/Seoul
07-12 11:19:48.740 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: setTimeZone=Asia/Seoul
07-12 11:19:48.740 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: call alarm.setTimeZone and broadcast zoneId=Asia/Seoul
07-12 11:19:48.740 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595582014,108854714,Asia/Seoul,450
07-12 11:19:48.740 D/GSM     ( 1227): [GsmSST] NITZ: Setting time of day to Fri Jul 12 11:19:48 GMT+09:00 2013 NITZ receive delay(ms): 10 gained(ms): -746 from 13/07/12,02:19:48+36,00
07-12 11:19:48.740 W/GSM     ( 1227): BroadcastNITZTime
07-12 11:19:48.010 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:48.010 D/RILJ    ( 1227): [UNSL]< UNSOL_WCDMA_ACCEPT_RECEIVED {1, 1}
07-12 11:19:48.010 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:48.010 I/GSM     ( 1227): NITZ: after Setting time of day
07-12 11:19:48.010 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595588010,108861396,Asia/Seoul,450
07-12 11:19:48.010 D/RILJ    ( 1227): [11423]> OPERATOR
07-12 11:19:48.010 D/RILJ    ( 1227): [11424]> DATA_REGISTRATION_STATE
07-12 11:19:48.010 D/RILJ    ( 1227): [11425]> VOICE_REGISTRATION_STATE
07-12 11:19:48.010 D/RILJ    ( 1227): [11426]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:48.010 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:48.020 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:48.020 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:48.020 D/RILJ    ( 1227): [11423]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:48.020 D/RILJ    ( 1227): [11427]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:48.020 D/RILJ    ( 1227): [11426]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:48.020 D/RILJ    ( 1227): responseGetModemInfo[I@43b963a0
07-12 11:19:48.020 D/RILJ    ( 1227): [11427]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:48.020 D/RILJ    ( 1227): [11424]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:48.020 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:48.020 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:48.020 D/RILJ    ( 1227): [11425]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:48.030 D/PHONE   ( 1227): [PhoneProxy] Ignoring voice radio technology changed message. newVoiceRadioTech = Unknown. Active Phone = GSM
07-12 11:19:48.030 D/RILJ    ( 1227): [11428]> OPERATOR
07-12 11:19:48.030 D/RILJ    ( 1227): [11429]> DATA_REGISTRATION_STATE
07-12 11:19:48.030 D/RILJ    ( 1227): [11430]> VOICE_REGISTRATION_STATE
07-12 11:19:48.030 D/RILJ    ( 1227): [11431]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:48.030 D/RILJ    ( 1227): [11428]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:48.030 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:48.030 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:48.030 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:48.030 D/GSM     ( 1227): [GSMphone] mIccRecords.iccid = 8982051006425136633
07-12 11:19:48.040 D/RILJ    ( 1227): [11432]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:48.040 D/RILJ    ( 1227): [11433]> OPERATOR
07-12 11:19:48.040 D/RILJ    ( 1227): [11434]> DATA_REGISTRATION_STATE
07-12 11:19:48.040 D/RILJ    ( 1227): [11435]> VOICE_REGISTRATION_STATE
07-12 11:19:48.040 D/RILJ    ( 1227): [11436]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:48.040 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:48.040 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:48.040 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:48.040 D/RILJ    ( 1227): [11430]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:48.040 D/RILJ    ( 1227): [11437]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:48.040 E/GSM     ( 1227): LGT Network Accept: mm_accept = 1 ,gmm_accept = 1
07-12 11:19:48.040 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:48.040 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:48.040 D/RILJ    ( 1227): [11438]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:48.040 D/RILJ    ( 1227): [11439]> OPERATOR
07-12 11:19:48.040 D/RILJ    ( 1227): [11429]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:48.040 D/RILJ    ( 1227): [11440]> DATA_REGISTRATION_STATE
07-12 11:19:48.040 D/RILJ    ( 1227): [11441]> VOICE_REGISTRATION_STATE
07-12 11:19:48.040 D/RILJ    ( 1227): [11442]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:48.040 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:48.040 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:48.040 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:48.050 D/RILJ    ( 1227): [11443]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:48.050 D/RILJ    ( 1227): responseGetModemInfo[I@4318e600
07-12 11:19:48.050 D/RILJ    ( 1227): [11432]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:48.050 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:48.050 D/RILJ    ( 1227): [11444]> OPERATOR
07-12 11:19:48.050 D/RILJ    ( 1227): [11445]> DATA_REGISTRATION_STATE
07-12 11:19:48.050 D/RILJ    ( 1227): [11446]> VOICE_REGISTRATION_STATE
07-12 11:19:48.050 D/RILJ    ( 1227): [11431]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:48.050 D/RILJ    ( 1227): [11436]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:48.050 D/RILJ    ( 1227): responseGetModemInfo[I@431055a8
07-12 11:19:48.050 D/RILJ    ( 1227): [11437]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:48.050 D/RILJ    ( 1227): [11433]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:48.050 D/RILJ    ( 1227): [11447]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:48.050 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:48.050 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:48.050 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:48.050 D/RILJ    ( 1227): [11435]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:48.050 D/RILJ    ( 1227): [11434]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:48.050 D/RILJ    ( 1227): responseGetModemInfo[I@431c34c8
07-12 11:19:48.060 D/RILJ    ( 1227): [11438]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:48.060 D/RILJ    ( 1227): [11448]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:48.060 D/RILJ    ( 1227): [11449]> OPERATOR
07-12 11:19:48.060 D/RILJ    ( 1227): [11442]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:48.060 D/RILJ    ( 1227): responseGetModemInfo[I@431c9c38
07-12 11:19:48.060 D/RILJ    ( 1227): [11443]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:48.060 D/RILJ    ( 1227): [11450]> DATA_REGISTRATION_STATE
07-12 11:19:48.060 D/RILJ    ( 1227): [11440]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:48.060 D/RILJ    ( 1227): [11451]> VOICE_REGISTRATION_STATE
07-12 11:19:48.060 D/RILJ    ( 1227): [11452]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:48.060 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:48.060 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:48.060 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:48.060 D/RILJ    ( 1227): [11453]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:48.070 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:48.070 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:48.070 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:48.070 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:48.070 D/RILJ    ( 1227): [11445]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:48.070 D/RILJ    ( 1227): [11441]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:48.070 D/RILJ    ( 1227): [11446]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:48.070 D/RILJ    ( 1227): [11439]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:48.070 D/RILJ    ( 1227): [11444]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:48.070 D/RILJ    ( 1227): [11447]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:48.070 D/RILJ    ( 1227): responseGetModemInfo[I@43163c60
07-12 11:19:48.070 D/RILJ    ( 1227): [11448]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:48.070 D/RILJ    ( 1227): [11450]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:48.070 D/RILJ    ( 1227): [11449]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:48.070 D/RILJ    ( 1227): responseGetModemInfo[I@43003b30
07-12 11:19:48.070 D/RILJ    ( 1227): [11453]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:48.070 D/RILJ    ( 1227): [11451]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:48.070 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:48.070 D/GSM     ( 1227): [EONS] Received TAC = 12818
07-12 11:19:48.070 D/GSM     ( 1227): [EONS] Received CID = 10825479
07-12 11:19:48.070 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =14 , mTAC =12818
07-12 11:19:48.070 D/RILJ    ( 1227): [11452]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:48.080 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:48.080 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 14, CStype = 14
07-12 11:19:48.080 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:48.080 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=LTE
07-12 11:19:48.080 D/GSM     ( 1227): [IMS_AFW] Radio Tech is LTE, Get LTE Info from modem
07-12 11:19:48.080 D/RILJ    ( 1227): [11454]> RIL_REQUEST_LTE_INFO_FOR_IMS
07-12 11:19:48.080 D/RILJ    ( 1227): [11454]< RIL_REQUEST_LTE_INFO_FOR_IMS 450,05,0a52f07,3212
07-12 11:19:48.080 D/GSM     ( 1227): [GsmSST] RAT switched UMTS -> LTE at cell 10825479
07-12 11:19:48.080 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:48.080 D/GSM     ( 1227): [EONS] updateEons() lactac = 12818 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:48.080 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:48.080 D/GSM     ( 1227): [GsmSST] shouldFixTimeZoneNow: retVal=false iccCard=null iccCard.state=null iccCardExist=false operatorNumeric=45005 mcc=450 prevOperatorNumeric=45005 prevMcc=450 needToFixTimeZone=false ltod=07-12 11:19:48.092
07-12 11:19:48.100 D/GSM     ( 1227): [GsmDCT] get all active apn types
07-12 11:19:48.100 D/GSM     ( 1227): [GsmDCT] return link properites for ims
07-12 11:19:48.100 D/GSM     ( 1227): [GsmDCT] get active pdp is not null, return link Capabilities for ims
07-12 11:19:48.100 D/GSM     ( 1227): [GsmDCT] isDataPossible(ims): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=CONNECTED
07-12 11:19:48.100 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ims
07-12 11:19:48.100 D/GSM     ( 1227): [GsmDCT] isDataPossible(default): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=IDLE
07-12 11:19:48.100 D/GSM     ( 1227): [GsmDCT] get active apn string for type:default
07-12 11:19:48.110 D/GSM     ( 1227): [GsmSST] [IMS_AFW] EVENT_GET_LTE_INFO_DONE
07-12 11:19:48.110 D/GSM     ( 1227): [GsmSST] [IMS_AFW] GET LTE Info: 450,05,0a52f07,3212
07-12 11:19:48.110 D/GSM     ( 1227): [GsmSST] [IMS_AFW] MCC : 450, MNC : 05, Cell ID : 0a52f07, TAC : 3212
07-12 11:19:48.490 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:19:48.490 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:19:48.490 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:19:48.750 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTime: time=1373595588010ms
07-12 11:19:50.241 D/RILJ    ( 1227): [11455]> SCREEN_STATE: true
07-12 11:19:50.261 D/GSM     ( 1227): [GsmDCT] onReceive: action=android.intent.action.SCREEN_ON
07-12 11:19:50.261 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:19:50.261 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:19:50.261 D/GSM     ( 1227): [GsmDCT] startNetStatPoll
07-12 11:19:50.271 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:50.271 D/RILJ    ( 1227): [11455]< SCREEN_STATE 
07-12 11:19:50.271 D/RILJ    ( 1227): [11456]> OPERATOR
07-12 11:19:50.271 D/RILJ    ( 1227): [11457]> DATA_REGISTRATION_STATE
07-12 11:19:50.271 D/RILJ    ( 1227): [11458]> VOICE_REGISTRATION_STATE
07-12 11:19:50.271 D/RILJ    ( 1227): [11459]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:50.271 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:50.271 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:50.271 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:50.281 D/RILJ    ( 1227): [11460]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:50.281 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:19:50.281 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:19:50.281 D/RILJ    ( 1227): [11457]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:50.281 D/RILJ    ( 1227): responseGetModemInfo[I@4368a608
07-12 11:19:50.281 D/RILJ    ( 1227): [11460]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:50.281 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:50.281 D/RILJ    ( 1227): [11459]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:50.281 D/RILJ    ( 1227): [11458]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:50.281 D/RILJ    ( 1227): [11456]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:50.281 D/GSM     ( 1227): [EONS] Received TAC = 12818
07-12 11:19:50.281 D/GSM     ( 1227): [EONS] Received CID = 10825479
07-12 11:19:50.281 D/GSM     ( 1227): use mTAC  with LTE: 12818
07-12 11:19:50.281 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =14 , mTAC =12818
07-12 11:19:50.281 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:50.281 D/RILJ    ( 1227): [11461]> OPERATOR
07-12 11:19:50.291 D/RILJ    ( 1227): [11462]> DATA_REGISTRATION_STATE
07-12 11:19:50.291 D/RILJ    ( 1227): [11463]> VOICE_REGISTRATION_STATE
07-12 11:19:50.291 D/RILJ    ( 1227): [11461]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:50.291 D/RILJ    ( 1227): [11464]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:50.291 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:50.291 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:50.291 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:50.291 D/RILJ    ( 1227): [11465]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:50.291 D/RILJ    ( 1227): [11462]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:19:50.291 D/GSM     ( 1227): [EONS] Received TAC = 12818
07-12 11:19:50.291 D/GSM     ( 1227): [EONS] Received CID = 10825479
07-12 11:19:50.291 D/GSM     ( 1227): use mTAC  with LTE: 12818
07-12 11:19:50.291 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =14 , mTAC =12818
07-12 11:19:50.291 D/RILJ    ( 1227): [11463]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:50.291 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 14, CStype = 14
07-12 11:19:50.291 D/GSM     ( 1227): use mTAC instead of lac because NULL with LTE: 12818
07-12 11:19:50.301 D/RILJ    ( 1227): responseGetModemInfo[I@430bcd30
07-12 11:19:50.301 D/RILJ    ( 1227): [11465]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:50.301 D/RILJ    ( 1227): [11464]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:50.301 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:50.301 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:50.301 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=LTE newType=LTE
07-12 11:19:50.301 D/GSM     ( 1227): [IMS_AFW] Radio Tech is LTE, Get LTE Info from modem
07-12 11:19:50.301 D/RILJ    ( 1227): [11466]> RIL_REQUEST_LTE_INFO_FOR_IMS
07-12 11:19:50.301 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:50.301 D/GSM     ( 1227): [EONS] updateEons() lactac = 12818 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:50.301 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:50.301 D/RILJ    ( 1227): [11466]< RIL_REQUEST_LTE_INFO_FOR_IMS 450,05,0a52f07,3212
07-12 11:19:50.301 D/GSM     ( 1227): [GsmSST] [IMS_AFW] EVENT_GET_LTE_INFO_DONE
07-12 11:19:50.301 D/GSM     ( 1227): [GsmSST] [IMS_AFW] GET LTE Info: 450,05,0a52f07,3212
07-12 11:19:50.301 D/GSM     ( 1227): [GsmSST] [IMS_AFW] MCC : 450, MNC : 05, Cell ID : 0a52f07, TAC : 3212
07-12 11:19:50.311 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4d4c0408000b00000002000d0001040000000000
07-12 11:19:50.311 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:19:50.311 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:19:50.311 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525388
07-12 11:19:50.311 D/RILJ    ( 1227): Response ID 525388is not served in this process.
07-12 11:19:50.311 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:19:50.311 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:19:50.321 D/RILJ    ( 1227): [11467]> OPERATOR
07-12 11:19:50.321 D/RILJ    ( 1227): [11468]> DATA_REGISTRATION_STATE
07-12 11:19:50.321 D/RILJ    ( 1227): [11469]> VOICE_REGISTRATION_STATE
07-12 11:19:50.321 D/RILJ    ( 1227): [11470]> QUERY_NETWORK_SELECTION_MODE
07-12 11:19:50.321 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:19:50.321 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:19:50.321 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:19:50.321 D/RILJ    ( 1227): [11471]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:19:50.321 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:19:50.321 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:19:50.321 D/RILJ    ( 1227): [11470]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:19:50.321 D/RILJ    ( 1227): [11469]< VOICE_REGISTRATION_STATE {1, null, 00a52f03, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:19:50.331 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:19:50.331 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:19:50.331 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:19:50.331 D/RILJ    ( 1227): responseGetModemInfo[I@43b476a0
07-12 11:19:50.331 D/RILJ    ( 1227): [11471]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:19:50.331 D/RILJ    ( 1227): [11467]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:19:50.331 D/RILJ    ( 1227): [11468]< DATA_REGISTRATION_STATE {1, 3212, 00a52f03, 14, null, 20}
07-12 11:19:50.331 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 0, CStype = 14
07-12 11:19:50.331 D/GSM     ( 1227): use mTAC instead of lac because NULL with LTE: 12818
07-12 11:19:50.331 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:19:50.341 D/GSM     ( 1227): [EONS] Received TAC = 12818
07-12 11:19:50.341 D/GSM     ( 1227): [EONS] Received CID = 10825475
07-12 11:19:50.341 D/GSM     ( 1227): use mTAC  with LTE: 12818
07-12 11:19:50.341 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =14 , mTAC =12818
07-12 11:19:50.341 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:19:50.341 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=LTE newType=LTE
07-12 11:19:50.341 D/GSM     ( 1227): [IMS_AFW] Radio Tech is LTE, Get LTE Info from modem
07-12 11:19:50.341 D/RILJ    ( 1227): [11472]> RIL_REQUEST_LTE_INFO_FOR_IMS
07-12 11:19:50.361 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:19:50.361 D/GSM     ( 1227): [EONS] updateEons() lactac = 12818 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:19:50.361 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:19:50.361 D/RILJ    ( 1227): [11472]< RIL_REQUEST_LTE_INFO_FOR_IMS 450,05,0a52f03,3212
07-12 11:19:50.361 D/GSM     ( 1227): [GsmSST] [IMS_AFW] EVENT_GET_LTE_INFO_DONE
07-12 11:19:50.361 D/GSM     ( 1227): [GsmSST] [IMS_AFW] GET LTE Info: 450,05,0a52f03,3212
07-12 11:19:50.361 D/GSM     ( 1227): [GsmSST] [IMS_AFW] MCC : 450, MNC : 05, Cell ID : 0a52f03, TAC : 3212
07-12 11:19:55.347 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:19:55.347 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:19:59.181 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:19:59.181 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:03.025 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:20:03.025 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:05.327 D/GSM     ( 1227): [GsmDCT] [LGE_DATA] updateDataActivity: tx_onlycount = 61
07-12 11:20:06.869 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:20:06.869 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:09.422 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:20:09.422 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:14.057 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:14.067 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:14.067 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:20:17.090 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:20:17.090 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:18.892 E/PHONE   ( 1227): Settings Exception Reading Dual Sim Voice Prompt Values
07-12 11:20:18.892 D/PHONE   ( 1227): Prompt option:false
07-12 11:20:19.042 D/GSM     ( 1227): isTwoDigitShortCode
07-12 11:20:19.042 D/GSM     ( 1227): dialing w/ mmi 'null'...
07-12 11:20:19.042 D/GSM     ( 1227): [GSMConn] acquireWakeLock
07-12 11:20:19.042 D/RILJ    ( 1227): [11473]> SET_MUTE false
07-12 11:20:19.042 D/RILJ    ( 1227): [11474]> DIAL
07-12 11:20:19.042 D/RILJ    ( 1227): [11473]< SET_MUTE 
07-12 11:20:19.282 E/RILC    (  341): responseLGERPInd(): param(426000(0x00068010)), data_valid(1), data_len(1)
07-12 11:20:19.282 I/RILJ    ( 1227): LGE_UNSOL_IS_LTE_AVAILABLE:1
07-12 11:20:19.282 D/RILJ    ( 1227): returned data  = [B@4309f2a8
07-12 11:20:19.282 D/RILJ    ( 1227): [11474]< DIAL 
07-12 11:20:19.292 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:20:19.422 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:19.422 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:19.482 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270343 when=-431ms obj=android.os.AsyncResult@436e16a0 }
07-12 11:20:19.482 D/GSM     ( 1227): [GsmDCT] onVoiceCallStarted
07-12 11:20:19.482 D/RILJ    ( 1227): [11475]> GET_CURRENT_CALLS
07-12 11:20:19.482 E/RILC    (  341): numberplus = ""
07-12 11:20:19.482 E/RILC    (  341): signalIE = 0
07-12 11:20:19.482 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:20:19.482 D/RILJ    ( 1227): No calling name expression is received
07-12 11:20:19.482 D/RILJ    ( 1227): signal = 0
07-12 11:20:19.482 D/RILJ    ( 1227): DriverCall dc = id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:19.482 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:20:19.482 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:20:19.482 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:20:19.482 D/RILJ    ( 1227): [11476]> GET_CURRENT_CALLS
07-12 11:20:19.492 D/RILJ    ( 1227): [DriverCall] dc : id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:19.492 D/RILJ    ( 1227): [11475]< GET_CURRENT_CALLS  [id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:20:19.492 E/RILC    (  341): numberplus = ""
07-12 11:20:19.492 E/RILC    (  341): signalIE = 0
07-12 11:20:19.492 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:20:19.492 D/RILJ    ( 1227): No calling name expression is received
07-12 11:20:19.492 D/RILJ    ( 1227): signal = 0
07-12 11:20:19.492 D/RILJ    ( 1227): DriverCall dc = id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:19.492 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:20:19.492 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:20:19.492 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:20:19.492 D/RILJ    ( 1227): [DriverCall] dc : id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:19.492 D/RILJ    ( 1227): [11476]< GET_CURRENT_CALLS  [id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:20:19.492 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:20:19.492 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:19.512 D/RILJ    ( 1227): responseDataCallList ver=7 num=1
07-12 11:20:19.512 D/RILJ    ( 1227): [UNSL]< UNSOL_DATA_CALL_LIST_CHANGED [DataCallState: {version=7 status=0 retry=-1 cid=0 active=2 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}]
07-12 11:20:19.593 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:19.593 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:19.593 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:20:19.603 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:20:19.603 D/GSM     ( 1227): [GSMConn] update: parent=DIALING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=false
07-12 11:20:19.603 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:20:19.603 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270340 when=-85ms obj=android.os.AsyncResult@43981608 }
07-12 11:20:19.603 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): E
07-12 11:20:19.603 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): DataCallState size=1
07-12 11:20:19.603 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): E dcacs=[GsmDC-1]
07-12 11:20:19.603 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): X list=[]
07-12 11:20:19.603 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): Found ConnId=0 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=2 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:20:19.603 D/GSM     ( 1227): addr/pl=42.19.184.78/30
07-12 11:20:19.603 D/GSM     ( 1227): [GsmDC-1] REQ_UPDATE_LINK_PROPERTIES_DATA_CALL_STATE result=com.android.internal.telephony.DataConnection$UpdateLinkPropertyResult@433d8f80 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=2 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:20:19.603 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): no change
07-12 11:20:19.603 D/GSM     ( 1227): [GsmDCT] onDataStateChanged: Data Activity updated to NONE. isAnyDataCallActive = true isAnyDataCallDormant = false
07-12 11:20:19.603 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:20:19.603 D/GSM     ( 1227): [GsmDCT] onDataStateChange(ar): apnsToCleanup=[]
07-12 11:20:19.603 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): X
07-12 11:20:19.613 D/RILJ    ( 1227): responseDataCallList ver=7 num=1
07-12 11:20:19.613 D/RILJ    ( 1227): [UNSL]< UNSOL_DATA_CALL_LIST_CHANGED [DataCallState: {version=7 status=0 retry=-1 cid=0 active=1 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}]
07-12 11:20:19.723 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270340 when=-115ms obj=android.os.AsyncResult@439ebb48 }
07-12 11:20:19.723 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): E
07-12 11:20:19.723 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): DataCallState size=1
07-12 11:20:19.733 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): E dcacs=[GsmDC-1]
07-12 11:20:19.733 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): X list=[]
07-12 11:20:19.733 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): Found ConnId=0 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=1 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:20:19.733 D/GSM     ( 1227): addr/pl=42.19.184.78/30
07-12 11:20:19.733 D/GSM     ( 1227): [GsmDC-1] REQ_UPDATE_LINK_PROPERTIES_DATA_CALL_STATE result=com.android.internal.telephony.DataConnection$UpdateLinkPropertyResult@43b5c898 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=1 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:20:19.733 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): no change
07-12 11:20:19.733 D/GSM     ( 1227): topActivity.getPackageName(); = com.android.phone
07-12 11:20:19.733 D/GSM     ( 1227): topActivity.getClassName(); = com.android.phone.InCallScreen
07-12 11:20:19.733 D/GSM     ( 1227): VOICE CALL  ::true
07-12 11:20:19.733 D/GSM     ( 1227): (InCallScreen) topActivity.getClassName(); = com.android.phone.InCallScreen
07-12 11:20:19.743 D/GSM     ( 1227): functionForPacketDrop is called
07-12 11:20:19.743 D/GSM     ( 1227): [GsmDCT] onDataStateChanged: Data Activity updated to DORMANT. stopNetStatePoll
07-12 11:20:19.743 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:20:19.743 D/GSM     ( 1227): [GsmDCT] onDataStateChange(ar): apnsToCleanup=[]
07-12 11:20:19.743 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): X
07-12 11:20:20.173 D/RILJ    ( 1227): [11477]> SCREEN_STATE: false
07-12 11:20:20.193 D/RILJ    ( 1227): [11477]< SCREEN_STATE 
07-12 11:20:20.333 D/GSM     ( 1227): [GsmDCT] onReceive: action=android.intent.action.SCREEN_OFF
07-12 11:20:20.333 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:20:20.333 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:20:20.333 D/GSM     ( 1227): [GsmDCT] startNetStatPoll
07-12 11:20:20.894 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4def0308000100000003
07-12 11:20:20.894 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:20:20.894 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:20:20.894 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525295
07-12 11:20:20.894 D/RILJ    ( 1227): Response ID 525295is not served in this process.
07-12 11:20:20.894 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:20:20.894 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4d4c0408000b00000002000d0001040000000000
07-12 11:20:20.894 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:20:20.894 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:20:20.894 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525388
07-12 11:20:20.894 D/RILJ    ( 1227): Response ID 525388is not served in this process.
07-12 11:20:20.894 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:20:20.894 D/RILJ    ( 1227): [UNSL]< UNSOL_VOICE_RADIO_TECH_CHANGED {3}
07-12 11:20:20.894 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:20.894 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:20.894 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:20.894 D/PHONE   ( 1227): [PhoneProxy] Ignoring voice radio technology changed message. newVoiceRadioTech = 3 Active Phone = GSM
07-12 11:20:20.894 D/RILJ    ( 1227): [11478]> OPERATOR
07-12 11:20:20.894 D/RILJ    ( 1227): [11479]> DATA_REGISTRATION_STATE
07-12 11:20:20.894 D/RILJ    ( 1227): [11480]> VOICE_REGISTRATION_STATE
07-12 11:20:20.894 D/RILJ    ( 1227): [11481]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:20.894 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:20.894 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:20.894 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:20.894 D/RILJ    ( 1227): [11482]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:20.894 D/RILJ    ( 1227): [11483]> OPERATOR
07-12 11:20:20.904 D/RILJ    ( 1227): [11484]> DATA_REGISTRATION_STATE
07-12 11:20:20.904 D/RILJ    ( 1227): [11485]> VOICE_REGISTRATION_STATE
07-12 11:20:20.904 D/RILJ    ( 1227): [11486]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:20.904 D/RILJ    ( 1227): [11479]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:20.904 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:20.904 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:20.904 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:20.904 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:20.904 D/RILJ    ( 1227): [11481]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:20.904 D/RILJ    ( 1227): [11480]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:20.904 D/RILJ    ( 1227): [11487]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:20.904 D/RILJ    ( 1227): [11488]> OPERATOR
07-12 11:20:20.904 D/RILJ    ( 1227): [11489]> DATA_REGISTRATION_STATE
07-12 11:20:20.904 D/RILJ    ( 1227): [11490]> VOICE_REGISTRATION_STATE
07-12 11:20:20.904 D/RILJ    ( 1227): [11491]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:20.904 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:20.904 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:20.904 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:20.904 D/RILJ    ( 1227): [11492]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:20.904 D/RILJ    ( 1227): [11493]> OPERATOR
07-12 11:20:20.914 D/RILJ    ( 1227): [11494]> DATA_REGISTRATION_STATE
07-12 11:20:20.914 D/RILJ    ( 1227): [11495]> VOICE_REGISTRATION_STATE
07-12 11:20:20.914 D/RILJ    ( 1227): [11496]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:20.914 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:20.914 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:20.914 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:20.914 D/RILJ    ( 1227): [11497]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:20.914 D/RILJ    ( 1227): responseGetModemInfo[I@438c6e70
07-12 11:20:20.914 D/RILJ    ( 1227): [11482]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:20.914 D/RILJ    ( 1227): [11478]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:20.914 D/RILJ    ( 1227): [11486]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:20.914 D/RILJ    ( 1227): responseGetModemInfo[I@438c8110
07-12 11:20:20.914 D/RILJ    ( 1227): [11487]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:20.924 D/RILJ    ( 1227): [11484]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:20.924 D/RILJ    ( 1227): [11489]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:20.924 D/RILJ    ( 1227): responseGetModemInfo[I@43a8ab10
07-12 11:20:20.934 D/RILJ    ( 1227): [11492]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:20.934 D/RILJ    ( 1227): [11483]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:20.934 D/RILJ    ( 1227): [11488]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:20.934 D/RILJ    ( 1227): [11493]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:20.934 D/RILJ    ( 1227): responseGetModemInfo[I@43a8c270
07-12 11:20:20.934 D/RILJ    ( 1227): [11497]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:20.934 D/RILJ    ( 1227): [11485]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:20.934 D/RILJ    ( 1227): [11490]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:20.934 D/RILJ    ( 1227): [11495]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:20.934 D/RILJ    ( 1227): [11491]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:20.934 D/RILJ    ( 1227): [11496]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:20.934 D/RILJ    ( 1227): [11494]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:20.934 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:20.944 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:20.944 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:20.944 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:20.944 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:20.944 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 0, CStype = 3
07-12 11:20:20.944 D/GSM     ( 1227): use lac because Not NULL: 8689
07-12 11:20:20.954 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:20.954 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:20.954 D/GSM     ( 1227): use mTAC  with LTE: 8689
07-12 11:20:20.954 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:20.954 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:20.954 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=LTE newType=UMTS
07-12 11:20:20.954 D/GSM     ( 1227): [GsmSST] RAT switched LTE -> UMTS at cell 65803780
07-12 11:20:20.954 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:20.954 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:20.954 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:20.954 D/GSM     ( 1227): [GsmSST] shouldFixTimeZoneNow: retVal=false iccCard=null iccCard.state=null iccCardExist=false operatorNumeric=45005 mcc=450 prevOperatorNumeric=45005 prevMcc=450 needToFixTimeZone=false ltod=07-12 11:20:20.964
07-12 11:20:20.964 D/GSM     ( 1227): [GsmDCT] get all active apn types
07-12 11:20:20.964 D/GSM     ( 1227): [GsmDCT] return link properites for ims
07-12 11:20:20.964 D/GSM     ( 1227): [GsmDCT] get active pdp is not null, return link Capabilities for ims
07-12 11:20:20.964 D/GSM     ( 1227): [GsmDCT] isDataPossible(ims): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=CONNECTED
07-12 11:20:20.964 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ims
07-12 11:20:20.974 D/GSM     ( 1227): [GsmDCT] isDataPossible(default): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=IDLE
07-12 11:20:20.974 D/GSM     ( 1227): [GsmDCT] get active apn string for type:default
07-12 11:20:20.974 D/RILJ    ( 1227): [11498]> OPERATOR
07-12 11:20:20.984 D/RILJ    ( 1227): [11499]> DATA_REGISTRATION_STATE
07-12 11:20:20.984 D/RILJ    ( 1227): [11500]> VOICE_REGISTRATION_STATE
07-12 11:20:20.984 D/RILJ    ( 1227): [11501]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:20.984 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:20.984 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:20.984 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:20.984 D/RILJ    ( 1227): [11502]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:20.994 D/RILJ    ( 1227): [11499]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:20.994 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:20.994 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:20.994 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:20.994 D/RILJ    ( 1227): [11501]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:20.994 D/RILJ    ( 1227): [11498]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:20.994 D/RILJ    ( 1227): responseGetModemInfo[I@430decd8
07-12 11:20:20.994 D/RILJ    ( 1227): [11502]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:20.994 D/RILJ    ( 1227): [11500]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:20.994 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:20.994 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:20:20.994 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:20.994 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:20:20.994 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:20.994 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:20.994 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:20.994 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:20:20.994 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:20:21.044 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:20:21.044 D/RILJ    ( 1227): [11503]> GET_CURRENT_CALLS
07-12 11:20:21.044 E/RILC    (  341): numberplus = ""
07-12 11:20:21.044 E/RILC    (  341): signalIE = 0
07-12 11:20:21.044 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:20:21.044 D/RILJ    ( 1227): No calling name expression is received
07-12 11:20:21.044 D/RILJ    ( 1227): signal = 0
07-12 11:20:21.044 D/RILJ    ( 1227): DriverCall dc = id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:21.044 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:20:21.044 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:20:21.044 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:20:21.044 D/RILJ    ( 1227): [DriverCall] dc : id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:21.044 D/RILJ    ( 1227): [11503]< GET_CURRENT_CALLS  [id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:20:21.044 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:20:21.044 D/GSM     ( 1227): [GSMConn] update: parent=DIALING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=false
07-12 11:20:21.044 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:20:21.104 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:21.104 D/RILJ    ( 1227): [11504]> OPERATOR
07-12 11:20:21.104 D/RILJ    ( 1227): [11505]> DATA_REGISTRATION_STATE
07-12 11:20:21.104 D/RILJ    ( 1227): [11506]> VOICE_REGISTRATION_STATE
07-12 11:20:21.104 D/RILJ    ( 1227): [11507]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:21.104 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:21.104 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:21.104 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:21.104 D/RILJ    ( 1227): [11508]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:21.114 D/RILJ    ( 1227): [11504]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:21.114 D/RILJ    ( 1227): responseGetModemInfo[I@43984800
07-12 11:20:21.114 D/RILJ    ( 1227): [11508]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:21.114 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:21.114 D/RILJ    ( 1227): [11506]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:21.114 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 0, CStype = 3
07-12 11:20:21.114 D/RILJ    ( 1227): [11507]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:21.114 D/RILJ    ( 1227): [11505]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:21.114 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:21.114 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:21.114 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:21.114 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:21.114 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:20:21.114 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:21.114 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:21.114 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:23.567 D/RILJ    ( 1227): [UNSL]< UNSOL_NITZ_TIME_RECEIVED 13/07/12,02:20:24+36,00
07-12 11:20:23.567 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:23.567 D/GSM     ( 1227): [GsmSST] NITZ: 13/07/12,02:20:24+36,00,108896940 start=108896943 delay=3
07-12 11:20:23.567 I/GSM     ( 1227): NITZ: current iso = kr, mGotCountryCode = true
07-12 11:20:23.567 I/GSM     ( 1227):  NITZ: after iso = kr, mGotCountryCode = true
07-12 11:20:23.567 D/GSM     ( 1227): [GsmSST] NITZ:2 getAutoTimeZone() is OK : Asia/Seoul
07-12 11:20:23.567 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: setTimeZone=Asia/Seoul
07-12 11:20:23.577 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: call alarm.setTimeZone and broadcast zoneId=Asia/Seoul
07-12 11:20:23.577 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595588010,108861396,Asia/Seoul,450
07-12 11:20:23.577 D/GSM     ( 1227): [GsmSST] NITZ: Setting time of day to Fri Jul 12 11:20:24 GMT+09:00 2013 NITZ receive delay(ms): 16 gained(ms): 432 from 13/07/12,02:20:24+36,00
07-12 11:20:23.577 W/GSM     ( 1227): BroadcastNITZTime
07-12 11:20:23.587 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTime: time=1373595624016ms
07-12 11:20:24.086 I/GSM     ( 1227): NITZ: after Setting time of day
07-12 11:20:24.086 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595624016,108897042,Asia/Seoul,450
07-12 11:20:24.086 D/RILJ    ( 1227): [11509]> OPERATOR
07-12 11:20:24.086 D/RILJ    ( 1227): [11510]> DATA_REGISTRATION_STATE
07-12 11:20:24.096 D/RILJ    ( 1227): [11511]> VOICE_REGISTRATION_STATE
07-12 11:20:24.096 D/RILJ    ( 1227): [11512]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:24.096 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:24.096 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:24.096 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:24.106 D/RILJ    ( 1227): [11513]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:24.116 D/RILJ    ( 1227): [11509]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:24.116 D/RILJ    ( 1227): [11510]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:24.116 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:24.116 D/RILJ    ( 1227): [11511]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:24.116 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:24.116 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:24.116 D/RILJ    ( 1227): [11512]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:24.116 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:20:24.116 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:24.116 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:20:24.116 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:24.116 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:24.116 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:24.126 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:24.126 D/RILJ    ( 1227): [UNSL]< UNSOL_WCDMA_ACCEPT_RECEIVED {0, 1}
07-12 11:20:24.126 D/RILJ    ( 1227): responseGetModemInfo[I@42845a98
07-12 11:20:24.126 D/RILJ    ( 1227): [11514]> OPERATOR
07-12 11:20:24.126 D/RILJ    ( 1227): [11513]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:24.126 D/RILJ    ( 1227): [11515]> DATA_REGISTRATION_STATE
07-12 11:20:24.136 D/RILJ    ( 1227): [11516]> VOICE_REGISTRATION_STATE
07-12 11:20:24.136 D/RILJ    ( 1227): [11517]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:24.146 D/RILJ    ( 1227): [11514]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:24.146 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:24.146 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:24.146 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:24.146 D/RILJ    ( 1227): [11518]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:24.146 E/GSM     ( 1227): LGT Network Accept: mm_accept = 0 ,gmm_accept = 1
07-12 11:20:24.146 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:24.146 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:24.146 D/RILJ    ( 1227): [11519]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:24.146 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:24.156 D/RILJ    ( 1227): [11515]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:24.156 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:24.156 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:24.156 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:24.156 D/RILJ    ( 1227): responseGetModemInfo[I@42b77b10
07-12 11:20:24.156 D/RILJ    ( 1227): [11518]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:24.166 D/RILJ    ( 1227): [11517]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:24.166 D/RILJ    ( 1227): [11516]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:24.166 D/RILJ    ( 1227): responseGetModemInfo[I@43b81a08
07-12 11:20:24.166 D/RILJ    ( 1227): [11519]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:24.166 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:24.166 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:20:24.166 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:24.166 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:20:24.166 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:24.166 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:24.166 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:24.166 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:24.186 D/GSM     ( 1227): [GSMphone] mIccRecords.iccid = 8982051006425136633
07-12 11:20:26.087 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:20:26.087 D/RILJ    ( 1227): [11520]> GET_CURRENT_CALLS
07-12 11:20:26.087 E/RILC    (  341): numberplus = ""
07-12 11:20:26.087 E/RILC    (  341): signalIE = 0
07-12 11:20:26.087 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:20:26.087 D/RILJ    ( 1227): No calling name expression is received
07-12 11:20:26.087 D/RILJ    ( 1227): signal = 0
07-12 11:20:26.087 D/RILJ    ( 1227): DriverCall dc = id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:26.087 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:20:26.087 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:20:26.097 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:20:26.097 D/RILJ    ( 1227): [DriverCall] dc : id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:26.097 D/RILJ    ( 1227): [11520]< GET_CURRENT_CALLS  [id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:20:26.097 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:20:26.097 D/GSM     ( 1227): [GSMConn] update: parent=ALERTING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=true
07-12 11:20:26.097 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:20:27.398 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270368 when=0 arg1=1 }
07-12 11:20:28.770 D/RILJ    ( 1227): [11521]> SCREEN_STATE: true
07-12 11:20:28.790 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:28.790 D/RILJ    ( 1227): [11521]< SCREEN_STATE 
07-12 11:20:28.970 D/RILJ    ( 1227): [11522]> OPERATOR
07-12 11:20:28.970 D/RILJ    ( 1227): [11523]> DATA_REGISTRATION_STATE
07-12 11:20:28.970 D/RILJ    ( 1227): [11524]> VOICE_REGISTRATION_STATE
07-12 11:20:28.970 D/RILJ    ( 1227): [11525]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:28.970 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:28.970 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:28.970 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:28.970 D/RILJ    ( 1227): [11526]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:28.970 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 3
07-12 11:20:28.970 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:28.970 D/RILJ    ( 1227): [11523]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:28.970 D/RILJ    ( 1227): responseGetModemInfo[I@4326d2c0
07-12 11:20:28.970 D/RILJ    ( 1227): [11526]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:28.980 D/RILJ    ( 1227): [11522]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:28.980 D/RILJ    ( 1227): [11525]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:28.980 D/RILJ    ( 1227): [11524]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:28.980 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:28.990 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:28.990 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:28.990 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:28.990 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:28.990 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:20:28.990 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:28.990 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:20:28.990 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:28.990 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:28.990 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:29.250 D/RILJ    ( 1227): [11527]> OPERATOR
07-12 11:20:29.260 D/RILJ    ( 1227): [11528]> DATA_REGISTRATION_STATE
07-12 11:20:29.260 D/RILJ    ( 1227): [11529]> VOICE_REGISTRATION_STATE
07-12 11:20:29.260 D/RILJ    ( 1227): [11530]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:29.260 D/RILJ    ( 1227): [11527]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:29.260 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:29.260 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:29.260 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:29.260 D/RILJ    ( 1227): [11529]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:29.260 D/RILJ    ( 1227): [11531]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:29.260 D/GSM     ( 1227): [GsmDCT] onReceive: action=android.intent.action.SCREEN_ON
07-12 11:20:29.260 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:20:29.260 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:20:29.260 D/GSM     ( 1227): [GsmDCT] startNetStatPoll
07-12 11:20:29.260 D/RILJ    ( 1227): [11530]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:29.260 D/RILJ    ( 1227): [11528]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:29.270 D/RILJ    ( 1227): responseGetModemInfo[I@43dd7cc8
07-12 11:20:29.270 D/RILJ    ( 1227): [11531]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:29.300 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 0, CStype = 3
07-12 11:20:29.300 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:29.300 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:29.300 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:29.320 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:29.320 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:20:29.320 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:29.320 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:29.320 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:29.341 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:29.621 D/GSM     ( 1227): [GsmCallTracker] (foregnd) hangup dialing or alerting...
07-12 11:20:29.621 D/RILJ    ( 1227): hangupConnection: gsmIndex=1
07-12 11:20:29.621 D/RILJ    ( 1227): [11532]> HANGUP 1
07-12 11:20:29.901 D/RILJ    ( 1227): [11532]< HANGUP 
07-12 11:20:29.901 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:20:29.921 D/RILJ    ( 1227): [11533]> GET_CURRENT_CALLS
07-12 11:20:29.931 D/RILJ    ( 1227): [11534]> GET_CURRENT_CALLS
07-12 11:20:29.931 D/RILJ    ( 1227): [11533]< GET_CURRENT_CALLS  
07-12 11:20:29.931 D/RILJ    ( 1227): [11534]< GET_CURRENT_CALLS  
07-12 11:20:29.931 D/GSM     ( 1227): [GSMConn] releaseWakeLock
07-12 11:20:29.931 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270344 when=-2ms obj=android.os.AsyncResult@43299ff8 }
07-12 11:20:29.931 D/GSM     ( 1227): [GsmDCT] onVoiceCallEnded
07-12 11:20:29.931 D/GSM     ( 1227): [LGE_DATA] functionForPacketDrop for ACTION_VOICE_CALL_ENDED
07-12 11:20:29.951 D/GSM     ( 1227): [GsmDCT] setupDataOnReadyApns: 2GVoiceCallEnded
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDCT] configureRetry: forDefault=true retryCount=0 dc={GsmDC-1: State=DcActiveState apnSetting=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 apnList= [{mApnType=ims mState=CONNECTED mWaitingApns=[[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 mDataConnectionAc=GsmDC-1 mReason=dataEnabled mRetryCount=0 mDataEnabled=true mDependencyMet=true}] RefCount=1 cid=0 create=1373486750617 lastFail=-1 lastFailCause=NONE}
07-12 11:20:29.961 E/GSM     ( 1227): [GsmDCT] [LG_DATA] configureRetry : by DOMESTIC_DATA_RETRY_CONFIG
07-12 11:20:29.961 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDC-1] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDCT] configureRetry: forDefault=false retryCount=0 dc={GsmDC-2: State=DcInactiveState apnSetting=null apnList= [] RefCount=0 cid=-1 create=-1 lastFail=-1 lastFailCause=NONE}
07-12 11:20:29.961 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDC-2] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:admin] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:fota] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:ktmultirab1] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:entitlement] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:dun] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:ktmultirab2] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:supl] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:hipri] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:tethering] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:ims] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDC-1] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:usccapp] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:default] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:vzw800] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:mms] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:cbs] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:bip] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:vzwapp] setRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:20:29.961 D/GSM     ( 1227): [ApnContext:default] set reason as 2GVoiceCallEnded,current state IDLE
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDCT] trySetupData for type:default due to 2GVoiceCallEnded
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDCT] trySetupData with mIsPsRestricted=false
07-12 11:20:29.961 E/GSM     ( 1227): [GSMPhone] getEsn() is a CDMA method
07-12 11:20:29.961 E/GSM     ( 1227): [GSMPhone] getEsn() is a CDMA method
07-12 11:20:29.961 D/GSM     ( 1227): [LGE_DATA] <mbooting_phone> = false
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDCT] MMS is available even if data enabled sets off : false
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:admin
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDCT] isDataPossible(admin): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDCT] get active apn string for type:admin
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:fota
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDCT] isDataPossible(fota): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDCT] get active apn string for type:fota
07-12 11:20:29.961 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:ktmultirab1
07-12 11:20:29.971 D/GSM     ( 1227): [GsmDCT] isDataPossible(ktmultirab1): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.971 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ktmultirab1
07-12 11:20:29.971 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:entitlement
07-12 11:20:29.971 D/GSM     ( 1227): [GsmDCT] isDataPossible(entitlement): possible=false isDataAllowed=true apnTypePossible=false apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.971 D/GSM     ( 1227): [GsmDCT] get active apn string for type:entitlement
07-12 11:20:29.971 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:dun
07-12 11:20:29.971 D/GSM     ( 1227): [GsmDCT] isDataPossible(dun): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.971 D/GSM     ( 1227): [GsmDCT] get active apn string for type:dun
07-12 11:20:29.971 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:ktmultirab2
07-12 11:20:29.971 D/GSM     ( 1227): [GsmDCT] isDataPossible(ktmultirab2): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.971 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ktmultirab2
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:supl
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] isDataPossible(supl): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] get active apn string for type:supl
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:hipri
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] isDataPossible(hipri): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] get active apn string for type:hipri
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:tethering
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] isDataPossible(tethering): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] get active apn string for type:tethering
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] notifyOffApnsOfAvailability skipped apn due to isReady==false: {mApnType=ims mState=CONNECTED mWaitingApns=[[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 mDataConnectionAc=GsmDC-1 mReason=dataEnabled mRetryCount=0 mDataEnabled=true mDependencyMet=true}
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:usccapp
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] isDataPossible(usccapp): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] get active apn string for type:usccapp
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] notifyOffApnsOfAvailability skipped apn due to isReady==false: {mApnType=default mState=IDLE mWaitingApns=[[ApnSettingV2] SKT, 476, 45005, lte.sktelecom.com, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, default | mms | dun | hipri | supl | fota | cbs, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT, 476, 45005, lte.sktelecom.com, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, default | mms | dun | hipri | supl | fota | cbs, IP, IP, true, 0 mDataConnectionAc=null mReason=2GVoiceCallEnded mRetryCount=0 mDataEnabled=true mDependencyMet=true}
07-12 11:20:29.981 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:vzw800
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] isDataPossible(vzw800): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] get active apn string for type:vzw800
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:mms
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] isDataPossible(mms): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] get active apn string for type:mms
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:cbs
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] isDataPossible(cbs): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] get active apn string for type:cbs
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:bip
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] isDataPossible(bip): possible=false isDataAllowed=true apnTypePossible=false apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] get active apn string for type:bip
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:vzwapp
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] isDataPossible(vzwapp): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:29.991 D/GSM     ( 1227): [GsmDCT] get active apn string for type:vzwapp
07-12 11:20:30.021 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:30.021 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:30.021 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:20:30.021 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:30.021 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:30.021 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:20:30.041 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:30.041 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:30.041 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:20:30.061 E/RILC    (  341): responseLGERPInd(): param(425992(0x00068008)), data_valid(1), data_len(4)
07-12 11:20:30.061 I/RILJ    ( 1227): LGE_UNSOL_RRC_RELEASE_CAUSE: releaseCause = 1
07-12 11:20:30.061 D/RILJ    ( 1227): returned data  = [B@43239880
07-12 11:20:30.842 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 3
07-12 11:20:30.842 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:31.012 D/RILJ    ( 1227): [UNSL]< UNSOL_NITZ_TIME_RECEIVED 13/07/12,02:20:31+36,00
07-12 11:20:31.012 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4d4c0408000b00000002000d0001040000000000
07-12 11:20:31.012 D/GSM     ( 1227): [GsmSST] NITZ: 13/07/12,02:20:31+36,00,108903971 start=108903975 delay=4
07-12 11:20:31.012 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:20:31.012 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:20:31.012 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525388
07-12 11:20:31.012 D/RILJ    ( 1227): Response ID 525388is not served in this process.
07-12 11:20:31.012 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:20:31.012 D/RILJ    ( 1227): [UNSL]< UNSOL_WCDMA_ACCEPT_RECEIVED {1, 1}
07-12 11:20:31.012 I/GSM     ( 1227): NITZ: current iso = kr, mGotCountryCode = true
07-12 11:20:31.012 I/GSM     ( 1227):  NITZ: after iso = kr, mGotCountryCode = true
07-12 11:20:31.012 D/GSM     ( 1227): [GsmSST] NITZ:2 getAutoTimeZone() is OK : Asia/Seoul
07-12 11:20:31.012 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: setTimeZone=Asia/Seoul
07-12 11:20:31.012 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: call alarm.setTimeZone and broadcast zoneId=Asia/Seoul
07-12 11:20:31.012 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595624016,108897042,Asia/Seoul,450
07-12 11:20:31.012 D/RILJ    ( 1227): [UNSL]< UNSOL_VOICE_RADIO_TECH_CHANGED {0}
07-12 11:20:31.012 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:31.012 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:31.012 D/GSM     ( 1227): [GsmSST] NITZ: Setting time of day to Fri Jul 12 11:20:31 GMT+09:00 2013 NITZ receive delay(ms): 8 gained(ms): -23 from 13/07/12,02:20:31+36,00
07-12 11:20:31.012 W/GSM     ( 1227): BroadcastNITZTime
07-12 11:20:31.008 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:31.008 I/GSM     ( 1227): NITZ: after Setting time of day
07-12 11:20:31.008 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595631008,108903994,Asia/Seoul,450
07-12 11:20:31.008 E/GSM     ( 1227): LGT Network Accept: mm_accept = 1 ,gmm_accept = 1
07-12 11:20:31.008 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:31.008 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:31.008 D/RILJ    ( 1227): [11535]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:31.008 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 3
07-12 11:20:31.008 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:31.008 D/RILJ    ( 1227): responseGetModemInfo[I@42ac8980
07-12 11:20:31.008 D/RILJ    ( 1227): [11535]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:31.018 D/PHONE   ( 1227): [PhoneProxy] Ignoring voice radio technology changed message. newVoiceRadioTech = Unknown. Active Phone = GSM
07-12 11:20:31.018 D/RILJ    ( 1227): [11536]> OPERATOR
07-12 11:20:31.018 D/RILJ    ( 1227): [11537]> DATA_REGISTRATION_STATE
07-12 11:20:31.018 D/RILJ    ( 1227): [11538]> VOICE_REGISTRATION_STATE
07-12 11:20:31.018 D/RILJ    ( 1227): [11539]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:31.018 D/RILJ    ( 1227): [11536]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:31.018 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:31.018 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:31.018 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:31.018 D/RILJ    ( 1227): [11540]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:31.018 D/RILJ    ( 1227): [11541]> OPERATOR
07-12 11:20:31.018 D/RILJ    ( 1227): [11542]> DATA_REGISTRATION_STATE
07-12 11:20:31.018 D/RILJ    ( 1227): [11543]> VOICE_REGISTRATION_STATE
07-12 11:20:31.018 D/RILJ    ( 1227): [11544]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:31.018 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:31.018 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:31.018 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:31.022 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTime: time=1373595631008ms
07-12 11:20:31.028 D/RILJ    ( 1227): [11545]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:31.028 D/RILJ    ( 1227): [11546]> OPERATOR
07-12 11:20:31.028 D/RILJ    ( 1227): [11547]> DATA_REGISTRATION_STATE
07-12 11:20:31.028 D/RILJ    ( 1227): [11548]> VOICE_REGISTRATION_STATE
07-12 11:20:31.028 D/RILJ    ( 1227): [11549]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:31.028 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:31.028 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:31.028 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:31.028 D/RILJ    ( 1227): [11550]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:31.028 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:31.028 D/RILJ    ( 1227): responseGetModemInfo[I@43cd4b98
07-12 11:20:31.028 D/RILJ    ( 1227): [11540]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:31.028 D/RILJ    ( 1227): [11539]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:31.028 D/RILJ    ( 1227): [11544]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:31.028 D/RILJ    ( 1227): responseGetModemInfo[I@43ce6528
07-12 11:20:31.028 D/RILJ    ( 1227): [11545]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:31.038 D/RILJ    ( 1227): [11537]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:20:31.038 D/RILJ    ( 1227): [11542]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:20:31.038 D/RILJ    ( 1227): [11547]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:20:31.038 D/RILJ    ( 1227): responseGetModemInfo[I@42c4c6c0
07-12 11:20:31.038 D/RILJ    ( 1227): [11550]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:31.038 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:31.038 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:31.038 D/RILJ    ( 1227): [11538]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:20:31.038 D/RILJ    ( 1227): [11543]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:20:31.038 D/RILJ    ( 1227): [11548]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:20:31.038 D/RILJ    ( 1227): [11541]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:31.038 D/RILJ    ( 1227): [11546]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:31.038 D/RILJ    ( 1227): [11549]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:31.058 D/GSM     ( 1227): [GSMphone] mIccRecords.iccid = 8982051006425136633
07-12 11:20:31.178 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:31.178 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:31.178 D/GSM     ( 1227): [EONS] Received TAC = 12818
07-12 11:20:31.178 D/GSM     ( 1227): [EONS] Received CID = 10825479
07-12 11:20:31.178 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =14 , mTAC =12818
07-12 11:20:31.178 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:31.178 D/RILJ    ( 1227): [11551]> OPERATOR
07-12 11:20:31.218 D/RILJ    ( 1227): [11552]> DATA_REGISTRATION_STATE
07-12 11:20:31.228 D/RILJ    ( 1227): [11553]> VOICE_REGISTRATION_STATE
07-12 11:20:31.228 D/RILJ    ( 1227): [11554]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:31.228 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:31.228 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:31.228 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:31.228 D/RILJ    ( 1227): [11551]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:31.228 D/RILJ    ( 1227): [11555]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:31.228 D/RILJ    ( 1227): [11556]> OPERATOR
07-12 11:20:31.228 D/RILJ    ( 1227): [11557]> DATA_REGISTRATION_STATE
07-12 11:20:31.228 D/RILJ    ( 1227): [11558]> VOICE_REGISTRATION_STATE
07-12 11:20:31.228 D/RILJ    ( 1227): [11559]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:31.238 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:31.238 D/RILJ    ( 1227): [11552]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:20:31.238 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:31.238 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:31.238 D/RILJ    ( 1227): responseGetModemInfo[I@43ce3aa0
07-12 11:20:31.238 D/RILJ    ( 1227): [11555]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:31.238 D/RILJ    ( 1227): [11560]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:31.238 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:31.238 D/RILJ    ( 1227): [11553]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:20:31.238 D/RILJ    ( 1227): [11554]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:31.238 D/RILJ    ( 1227): [11559]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:31.238 D/RILJ    ( 1227): [11556]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:31.238 D/RILJ    ( 1227): [11557]< DATA_REGISTRATION_STATE {1, 3212, 00a52f07, 14, null, 20}
07-12 11:20:31.248 D/RILJ    ( 1227): responseGetModemInfo[I@42b32170
07-12 11:20:31.248 D/RILJ    ( 1227): [11560]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:31.248 D/RILJ    ( 1227): [11558]< VOICE_REGISTRATION_STATE {1, null, 00a52f07, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:20:31.248 D/GSM     ( 1227): [EONS] Received TAC = 12818
07-12 11:20:31.248 D/GSM     ( 1227): [EONS] Received CID = 10825479
07-12 11:20:31.248 D/GSM     ( 1227): use mTAC  with LTE: 12818
07-12 11:20:31.248 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =14 , mTAC =12818
07-12 11:20:31.248 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:31.248 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 14, CStype = 14
07-12 11:20:31.248 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:31.248 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=LTE
07-12 11:20:31.248 D/GSM     ( 1227): [IMS_AFW] Radio Tech is LTE, Get LTE Info from modem
07-12 11:20:31.248 D/RILJ    ( 1227): [11561]> RIL_REQUEST_LTE_INFO_FOR_IMS
07-12 11:20:31.248 D/GSM     ( 1227): [GsmSST] RAT switched UMTS -> LTE at cell 10825479
07-12 11:20:31.248 D/RILJ    ( 1227): [11561]< RIL_REQUEST_LTE_INFO_FOR_IMS 450,05,0a52f07,3212
07-12 11:20:31.248 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:31.248 D/GSM     ( 1227): [EONS] updateEons() lactac = 12818 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:31.248 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:31.248 D/GSM     ( 1227): [GsmSST] shouldFixTimeZoneNow: retVal=false iccCard=null iccCard.state=null iccCardExist=false operatorNumeric=45005 mcc=450 prevOperatorNumeric=45005 prevMcc=450 needToFixTimeZone=false ltod=07-12 11:20:31.264
07-12 11:20:31.268 D/GSM     ( 1227): [GsmDCT] get all active apn types
07-12 11:20:31.268 D/GSM     ( 1227): [GsmDCT] return link properites for ims
07-12 11:20:31.278 D/GSM     ( 1227): [GsmDCT] get active pdp is not null, return link Capabilities for ims
07-12 11:20:31.278 D/GSM     ( 1227): [GsmDCT] isDataPossible(ims): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=CONNECTED
07-12 11:20:31.278 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ims
07-12 11:20:31.288 D/GSM     ( 1227): [GsmDCT] isDataPossible(default): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=IDLE
07-12 11:20:31.288 D/GSM     ( 1227): [GsmDCT] get active apn string for type:default
07-12 11:20:31.288 D/GSM     ( 1227): [GsmSST] [IMS_AFW] EVENT_GET_LTE_INFO_DONE
07-12 11:20:31.288 D/GSM     ( 1227): [GsmSST] [IMS_AFW] GET LTE Info: 450,05,0a52f07,3212
07-12 11:20:31.288 D/GSM     ( 1227): [GsmSST] [IMS_AFW] MCC : 450, MNC : 05, Cell ID : 0a52f07, TAC : 3212
07-12 11:20:31.678 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:31.678 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:31.678 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:20:34.240 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4d4c0408000b00000002000d0001040000000000
07-12 11:20:34.240 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:20:34.240 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:20:34.240 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525388
07-12 11:20:34.240 D/RILJ    ( 1227): Response ID 525388is not served in this process.
07-12 11:20:34.240 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:20:34.250 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:34.250 D/RILJ    ( 1227): [11562]> OPERATOR
07-12 11:20:34.260 D/RILJ    ( 1227): [11563]> DATA_REGISTRATION_STATE
07-12 11:20:34.260 D/RILJ    ( 1227): [11564]> VOICE_REGISTRATION_STATE
07-12 11:20:34.270 D/RILJ    ( 1227): [11565]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:34.280 D/RILJ    ( 1227): [11562]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:34.280 D/RILJ    ( 1227): [11563]< DATA_REGISTRATION_STATE {1, 3212, 00a52f03, 14, null, 20}
07-12 11:20:34.280 D/RILJ    ( 1227): [11564]< VOICE_REGISTRATION_STATE {1, null, 00a52f03, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:20:34.280 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:34.280 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:34.280 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:34.280 D/RILJ    ( 1227): [11565]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:34.280 D/RILJ    ( 1227): [11566]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:34.290 D/RILJ    ( 1227): responseGetModemInfo[I@43ab4b20
07-12 11:20:34.290 D/RILJ    ( 1227): [11566]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:34.290 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:20:34.290 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:34.300 D/GSM     ( 1227): [EONS] Received TAC = 12818
07-12 11:20:34.300 D/GSM     ( 1227): [EONS] Received CID = 10825475
07-12 11:20:34.300 D/GSM     ( 1227): use mTAC  with LTE: 12818
07-12 11:20:34.300 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =14 , mTAC =12818
07-12 11:20:34.300 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 14, CStype = 14
07-12 11:20:34.300 D/GSM     ( 1227): use mTAC instead of lac because NULL with LTE: 12818
07-12 11:20:34.300 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:34.300 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=LTE newType=LTE
07-12 11:20:34.300 D/GSM     ( 1227): [IMS_AFW] Radio Tech is LTE, Get LTE Info from modem
07-12 11:20:34.300 D/RILJ    ( 1227): [11567]> RIL_REQUEST_LTE_INFO_FOR_IMS
07-12 11:20:34.300 D/RILJ    ( 1227): [11567]< RIL_REQUEST_LTE_INFO_FOR_IMS 450,05,0a52f03,3212
07-12 11:20:34.300 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:34.300 D/GSM     ( 1227): [EONS] updateEons() lactac = 12818 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:34.300 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:34.310 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:34.310 D/GSM     ( 1227): [GsmSST] [IMS_AFW] EVENT_GET_LTE_INFO_DONE
07-12 11:20:34.310 D/GSM     ( 1227): [GsmSST] [IMS_AFW] GET LTE Info: 450,05,0a52f03,3212
07-12 11:20:34.310 D/GSM     ( 1227): [GsmSST] [IMS_AFW] MCC : 450, MNC : 05, Cell ID : 0a52f03, TAC : 3212
07-12 11:20:35.121 E/PHONE   ( 1227): Settings Exception Reading Dual Sim Voice Prompt Values
07-12 11:20:35.121 D/PHONE   ( 1227): Prompt option:false
07-12 11:20:35.301 D/GSM     ( 1227): isTwoDigitShortCode
07-12 11:20:35.311 D/GSM     ( 1227): dialing w/ mmi 'null'...
07-12 11:20:35.311 D/GSM     ( 1227): [GSMConn] acquireWakeLock
07-12 11:20:35.311 D/RILJ    ( 1227): [11568]> SET_MUTE false
07-12 11:20:35.311 D/RILJ    ( 1227): [11568]< SET_MUTE 
07-12 11:20:35.311 D/RILJ    ( 1227): [11569]> DIAL
07-12 11:20:35.552 E/RILC    (  341): responseLGERPInd(): param(426000(0x00068010)), data_valid(1), data_len(1)
07-12 11:20:35.552 D/RILJ    ( 1227): [11569]< DIAL 
07-12 11:20:35.552 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:20:35.552 I/RILJ    ( 1227): LGE_UNSOL_IS_LTE_AVAILABLE:1
07-12 11:20:35.552 D/RILJ    ( 1227): returned data  = [B@42a3aaf0
07-12 11:20:35.632 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:35.642 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:35.732 D/RILJ    ( 1227): responseDataCallList ver=7 num=1
07-12 11:20:35.742 D/RILJ    ( 1227): [UNSL]< UNSOL_DATA_CALL_LIST_CHANGED [DataCallState: {version=7 status=0 retry=-1 cid=0 active=2 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}]
07-12 11:20:35.752 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270343 when=-436ms obj=android.os.AsyncResult@42aae110 }
07-12 11:20:35.752 D/GSM     ( 1227): [GsmDCT] onVoiceCallStarted
07-12 11:20:35.752 D/RILJ    ( 1227): [11570]> GET_CURRENT_CALLS
07-12 11:20:35.752 D/RILJ    ( 1227): [11571]> GET_CURRENT_CALLS
07-12 11:20:35.752 E/RILC    (  341): numberplus = ""
07-12 11:20:35.752 E/RILC    (  341): signalIE = 0
07-12 11:20:35.752 E/RILC    (  341): numberplus = ""
07-12 11:20:35.752 E/RILC    (  341): signalIE = 0
07-12 11:20:35.752 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:20:35.752 D/RILJ    ( 1227): No calling name expression is received
07-12 11:20:35.752 D/RILJ    ( 1227): signal = 0
07-12 11:20:35.752 D/RILJ    ( 1227): DriverCall dc = id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:35.752 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:20:35.752 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:20:35.752 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:20:35.752 D/RILJ    ( 1227): [DriverCall] dc : id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:35.752 D/RILJ    ( 1227): [11570]< GET_CURRENT_CALLS  [id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:20:35.752 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:20:35.752 D/RILJ    ( 1227): No calling name expression is received
07-12 11:20:35.752 D/RILJ    ( 1227): signal = 0
07-12 11:20:35.762 D/RILJ    ( 1227): DriverCall dc = id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:35.762 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:20:35.762 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:20:35.762 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:20:35.762 D/RILJ    ( 1227): [DriverCall] dc : id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:35.762 D/RILJ    ( 1227): [11571]< GET_CURRENT_CALLS  [id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:20:35.762 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270340 when=-28ms obj=android.os.AsyncResult@429f5970 }
07-12 11:20:35.762 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): E
07-12 11:20:35.762 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): DataCallState size=1
07-12 11:20:35.762 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): E dcacs=[GsmDC-1]
07-12 11:20:35.772 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): X list=[]
07-12 11:20:35.772 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): Found ConnId=0 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=2 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:20:35.772 D/GSM     ( 1227): addr/pl=42.19.184.78/30
07-12 11:20:35.772 D/GSM     ( 1227): [GsmDC-1] REQ_UPDATE_LINK_PROPERTIES_DATA_CALL_STATE result=com.android.internal.telephony.DataConnection$UpdateLinkPropertyResult@4295e800 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=2 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:20:35.772 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): no change
07-12 11:20:35.772 D/GSM     ( 1227): [GsmDCT] onDataStateChanged: Data Activity updated to NONE. isAnyDataCallActive = true isAnyDataCallDormant = false
07-12 11:20:35.772 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:20:35.772 D/GSM     ( 1227): [GsmDCT] onDataStateChange(ar): apnsToCleanup=[]
07-12 11:20:35.772 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): X
07-12 11:20:35.802 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:35.802 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:35.802 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:20:35.822 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:20:35.822 D/GSM     ( 1227): [GSMConn] update: parent=DIALING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=false
07-12 11:20:35.822 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:20:35.822 D/RILJ    ( 1227): responseDataCallList ver=7 num=1
07-12 11:20:35.822 D/RILJ    ( 1227): [UNSL]< UNSOL_DATA_CALL_LIST_CHANGED [DataCallState: {version=7 status=0 retry=-1 cid=0 active=1 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}]
07-12 11:20:35.942 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270340 when=-113ms obj=android.os.AsyncResult@428861b0 }
07-12 11:20:35.942 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): E
07-12 11:20:35.942 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): DataCallState size=1
07-12 11:20:35.942 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): E dcacs=[GsmDC-1]
07-12 11:20:35.942 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): X list=[]
07-12 11:20:35.942 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): Found ConnId=0 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=1 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:20:35.942 D/GSM     ( 1227): addr/pl=42.19.184.78/30
07-12 11:20:35.942 D/GSM     ( 1227): [GsmDC-1] REQ_UPDATE_LINK_PROPERTIES_DATA_CALL_STATE result=com.android.internal.telephony.DataConnection$UpdateLinkPropertyResult@429eef58 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=1 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:20:35.942 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): no change
07-12 11:20:35.942 D/GSM     ( 1227): topActivity.getPackageName(); = com.android.phone
07-12 11:20:35.942 D/GSM     ( 1227): topActivity.getClassName(); = com.android.phone.InCallScreen
07-12 11:20:35.942 D/GSM     ( 1227): VOICE CALL  ::true
07-12 11:20:35.942 D/GSM     ( 1227): (InCallScreen) topActivity.getClassName(); = com.android.phone.InCallScreen
07-12 11:20:35.952 D/GSM     ( 1227): functionForPacketDrop is called
07-12 11:20:35.952 D/GSM     ( 1227): [GsmDCT] onDataStateChanged: Data Activity updated to DORMANT. stopNetStatePoll
07-12 11:20:35.952 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:20:35.952 D/GSM     ( 1227): [GsmDCT] onDataStateChange(ar): apnsToCleanup=[]
07-12 11:20:35.952 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): X
07-12 11:20:37.304 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4def0308000100000003
07-12 11:20:37.304 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:20:37.304 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:20:37.304 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525295
07-12 11:20:37.304 D/RILJ    ( 1227): Response ID 525295is not served in this process.
07-12 11:20:37.304 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:20:37.314 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4d4c0408000b00000002000d0001040000000000
07-12 11:20:37.314 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:20:37.314 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:20:37.314 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525388
07-12 11:20:37.314 D/RILJ    ( 1227): Response ID 525388is not served in this process.
07-12 11:20:37.314 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:20:37.334 D/RILJ    ( 1227): [UNSL]< UNSOL_VOICE_RADIO_TECH_CHANGED {3}
07-12 11:20:37.334 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:37.334 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:20:37.334 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:37.364 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:20:37.364 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:37.364 D/PHONE   ( 1227): [PhoneProxy] Ignoring voice radio technology changed message. newVoiceRadioTech = 3 Active Phone = GSM
07-12 11:20:37.364 D/RILJ    ( 1227): [11572]> OPERATOR
07-12 11:20:37.364 D/RILJ    ( 1227): [11573]> DATA_REGISTRATION_STATE
07-12 11:20:37.374 D/RILJ    ( 1227): [11574]> VOICE_REGISTRATION_STATE
07-12 11:20:37.374 D/RILJ    ( 1227): [11575]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:37.374 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:37.374 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:37.374 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:37.384 D/RILJ    ( 1227): [11576]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:37.384 D/RILJ    ( 1227): [11573]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:37.384 D/RILJ    ( 1227): responseGetModemInfo[I@43b01ae0
07-12 11:20:37.384 D/RILJ    ( 1227): [11576]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:37.384 D/RILJ    ( 1227): [11572]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:37.384 D/RILJ    ( 1227): [11574]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:37.384 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:37.384 D/RILJ    ( 1227): [11575]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:37.384 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:37.384 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:37.384 D/GSM     ( 1227): use mTAC  with LTE: 8689
07-12 11:20:37.384 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:37.384 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:37.384 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:20:37.384 D/GSM     ( 1227): use lac because Not NULL: 8689
07-12 11:20:37.384 D/RILJ    ( 1227): [11577]> OPERATOR
07-12 11:20:37.384 D/RILJ    ( 1227): [11578]> DATA_REGISTRATION_STATE
07-12 11:20:37.384 D/RILJ    ( 1227): [11579]> VOICE_REGISTRATION_STATE
07-12 11:20:37.384 D/RILJ    ( 1227): [11580]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:37.394 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:37.394 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:37.394 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:37.394 D/RILJ    ( 1227): [11581]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:37.394 D/RILJ    ( 1227): responseGetModemInfo[I@43d2dea8
07-12 11:20:37.394 D/RILJ    ( 1227): [11581]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:37.394 D/RILJ    ( 1227): [11579]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:37.394 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:37.394 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:20:37.394 D/GSM     ( 1227): use lac because Not NULL: 8689
07-12 11:20:37.394 D/RILJ    ( 1227): [11578]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:37.394 D/RILJ    ( 1227): [11580]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:37.394 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:37.394 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:37.394 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:37.404 D/RILJ    ( 1227): [11577]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:37.404 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:37.404 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=LTE newType=UMTS
07-12 11:20:37.404 D/GSM     ( 1227): [GsmSST] RAT switched LTE -> UMTS at cell 65803780
07-12 11:20:37.404 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:37.404 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:37.404 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:37.404 D/GSM     ( 1227): [GsmSST] shouldFixTimeZoneNow: retVal=false iccCard=null iccCard.state=null iccCardExist=false operatorNumeric=45005 mcc=450 prevOperatorNumeric=45005 prevMcc=450 needToFixTimeZone=false ltod=07-12 11:20:37.410
07-12 11:20:37.424 D/GSM     ( 1227): [GsmDCT] get all active apn types
07-12 11:20:37.424 D/GSM     ( 1227): [GsmDCT] return link properites for ims
07-12 11:20:37.424 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:20:37.424 D/GSM     ( 1227): [GsmDCT] get active pdp is not null, return link Capabilities for ims
07-12 11:20:37.424 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:20:37.424 D/GSM     ( 1227): [GsmDCT] isDataPossible(ims): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=CONNECTED
07-12 11:20:37.424 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ims
07-12 11:20:37.434 D/GSM     ( 1227): [GsmDCT] isDataPossible(default): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=IDLE
07-12 11:20:37.434 D/GSM     ( 1227): [GsmDCT] get active apn string for type:default
07-12 11:20:37.474 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:20:37.474 D/RILJ    ( 1227): [11582]> GET_CURRENT_CALLS
07-12 11:20:37.484 E/RILC    (  341): numberplus = ""
07-12 11:20:37.484 E/RILC    (  341): signalIE = 0
07-12 11:20:37.484 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:20:37.484 D/RILJ    ( 1227): No calling name expression is received
07-12 11:20:37.484 D/RILJ    ( 1227): signal = 0
07-12 11:20:37.484 D/RILJ    ( 1227): DriverCall dc = id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:37.484 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:20:37.484 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:20:37.484 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:20:37.484 D/RILJ    ( 1227): [DriverCall] dc : id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:37.484 D/RILJ    ( 1227): [11582]< GET_CURRENT_CALLS  [id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:20:37.484 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:20:37.484 D/GSM     ( 1227): [GSMConn] update: parent=DIALING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=false
07-12 11:20:37.484 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:20:37.514 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:37.514 D/RILJ    ( 1227): [11583]> OPERATOR
07-12 11:20:37.514 D/RILJ    ( 1227): [11584]> DATA_REGISTRATION_STATE
07-12 11:20:37.514 D/RILJ    ( 1227): [11585]> VOICE_REGISTRATION_STATE
07-12 11:20:37.514 D/RILJ    ( 1227): [11586]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:37.514 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:37.514 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:37.514 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:37.514 D/RILJ    ( 1227): [11587]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:37.514 D/RILJ    ( 1227): [11583]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:37.514 D/RILJ    ( 1227): [11584]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:37.514 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:37.514 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:37.514 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:37.514 D/RILJ    ( 1227): [11585]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:37.514 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:20:37.514 D/RILJ    ( 1227): [11586]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:37.514 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:37.514 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:20:37.514 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:37.514 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:37.514 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:37.514 D/RILJ    ( 1227): responseGetModemInfo[I@43ca5b50
07-12 11:20:37.514 D/RILJ    ( 1227): [11587]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:37.524 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:39.055 D/RILJ    ( 1227): [11588]> SCREEN_STATE: false
07-12 11:20:39.085 D/RILJ    ( 1227): [11588]< SCREEN_STATE 
07-12 11:20:39.166 D/GSM     ( 1227): [GsmDCT] onReceive: action=android.intent.action.SCREEN_OFF
07-12 11:20:39.166 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:20:39.166 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:20:39.166 D/GSM     ( 1227): [GsmDCT] startNetStatPoll
07-12 11:20:39.896 D/RILJ    ( 1227): [UNSL]< UNSOL_NITZ_TIME_RECEIVED 13/07/12,02:20:40+36,00
07-12 11:20:39.896 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:39.896 D/GSM     ( 1227): [GsmSST] NITZ: 13/07/12,02:20:40+36,00,108912883 start=108912884 delay=1
07-12 11:20:39.896 I/GSM     ( 1227): NITZ: current iso = kr, mGotCountryCode = true
07-12 11:20:39.896 I/GSM     ( 1227):  NITZ: after iso = kr, mGotCountryCode = true
07-12 11:20:39.896 D/GSM     ( 1227): [GsmSST] NITZ:2 getAutoTimeZone() is OK : Asia/Seoul
07-12 11:20:39.896 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: setTimeZone=Asia/Seoul
07-12 11:20:39.896 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: call alarm.setTimeZone and broadcast zoneId=Asia/Seoul
07-12 11:20:39.896 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595631008,108903994,Asia/Seoul,450
07-12 11:20:39.896 D/GSM     ( 1227): [GsmSST] NITZ: Setting time of day to Fri Jul 12 11:20:40 GMT+09:00 2013 NITZ receive delay(ms): 5 gained(ms): 92 from 13/07/12,02:20:40+36,00
07-12 11:20:39.896 W/GSM     ( 1227): BroadcastNITZTime
07-12 11:20:39.896 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTime: time=1373595640005ms
07-12 11:20:40.015 I/GSM     ( 1227): NITZ: after Setting time of day
07-12 11:20:40.015 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595640005,108912902,Asia/Seoul,450
07-12 11:20:40.015 D/RILJ    ( 1227): [11589]> OPERATOR
07-12 11:20:40.015 D/RILJ    ( 1227): [11590]> DATA_REGISTRATION_STATE
07-12 11:20:40.015 D/RILJ    ( 1227): [11591]> VOICE_REGISTRATION_STATE
07-12 11:20:40.015 D/RILJ    ( 1227): [11592]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:40.015 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:40.015 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:40.015 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:40.025 D/RILJ    ( 1227): [11591]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:40.035 D/RILJ    ( 1227): [11593]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:40.035 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 0, CStype = 3
07-12 11:20:40.035 D/RILJ    ( 1227): [11590]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:40.035 D/RILJ    ( 1227): [11589]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:40.035 D/RILJ    ( 1227): [11592]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:40.035 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:40.035 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:40.035 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:40.035 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:40.035 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:20:40.035 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:40.035 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:40.035 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:40.035 D/RILJ    ( 1227): responseGetModemInfo[I@42cef528
07-12 11:20:40.035 D/RILJ    ( 1227): [11593]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:40.035 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:40.095 D/GSM     ( 1227): [GSMphone] mIccRecords.iccid = 8982051006425136633
07-12 11:20:40.135 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:40.135 D/RILJ    ( 1227): [11594]> OPERATOR
07-12 11:20:40.135 D/RILJ    ( 1227): [11595]> DATA_REGISTRATION_STATE
07-12 11:20:40.135 D/RILJ    ( 1227): [11596]> VOICE_REGISTRATION_STATE
07-12 11:20:40.135 D/RILJ    ( 1227): [11597]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:40.135 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:40.135 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:40.135 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:40.135 D/RILJ    ( 1227): [11598]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:40.145 D/RILJ    ( 1227): [UNSL]< UNSOL_WCDMA_ACCEPT_RECEIVED {0, 1}
07-12 11:20:40.145 E/GSM     ( 1227): LGT Network Accept: mm_accept = 0 ,gmm_accept = 1
07-12 11:20:40.145 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:40.145 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:40.145 D/RILJ    ( 1227): [11599]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:40.145 D/RILJ    ( 1227): [11595]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:40.145 D/RILJ    ( 1227): [11596]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:40.155 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:40.155 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:40.155 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:40.155 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:20:40.155 D/RILJ    ( 1227): responseGetModemInfo[I@4326aa40
07-12 11:20:40.155 D/RILJ    ( 1227): [11598]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:40.155 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:40.155 D/RILJ    ( 1227): [11594]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:40.155 D/RILJ    ( 1227): [11597]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:40.155 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:40.155 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:20:40.155 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:40.155 D/RILJ    ( 1227): responseGetModemInfo[I@43728ae8
07-12 11:20:40.155 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:40.155 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:40.155 D/RILJ    ( 1227): [11599]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:40.155 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:41.866 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:20:41.866 D/RILJ    ( 1227): [11600]> GET_CURRENT_CALLS
07-12 11:20:41.866 E/RILC    (  341): numberplus = ""
07-12 11:20:41.866 E/RILC    (  341): signalIE = 0
07-12 11:20:41.866 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:20:41.866 D/RILJ    ( 1227): No calling name expression is received
07-12 11:20:41.866 D/RILJ    ( 1227): signal = 0
07-12 11:20:41.866 D/RILJ    ( 1227): DriverCall dc = id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:41.866 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:20:41.866 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:20:41.866 D/RILJ    ( 1227): [DriverCall] dc : id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:20:41.866 D/RILJ    ( 1227): [11600]< GET_CURRENT_CALLS  [id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:20:41.866 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:20:41.866 D/GSM     ( 1227): [GSMConn] update: parent=ALERTING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=true
07-12 11:20:41.866 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:20:41.866 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:20:43.708 D/RILJ    ( 1227): [11601]> SCREEN_STATE: true
07-12 11:20:43.728 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:43.728 D/RILJ    ( 1227): [11601]< SCREEN_STATE 
07-12 11:20:43.868 D/RILJ    ( 1227): [11602]> OPERATOR
07-12 11:20:43.868 D/RILJ    ( 1227): [11603]> DATA_REGISTRATION_STATE
07-12 11:20:43.868 D/RILJ    ( 1227): [11604]> VOICE_REGISTRATION_STATE
07-12 11:20:43.868 D/RILJ    ( 1227): [11603]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:43.868 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:43.868 D/RILJ    ( 1227): [11605]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:43.868 D/RILJ    ( 1227): [11604]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:43.868 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:43.868 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:43.868 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:43.878 D/RILJ    ( 1227): [11602]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:43.878 D/RILJ    ( 1227): [11605]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:43.878 D/RILJ    ( 1227): [11606]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:43.878 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 3
07-12 11:20:43.878 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:43.878 D/RILJ    ( 1227): responseGetModemInfo[I@43e0b778
07-12 11:20:43.878 D/RILJ    ( 1227): [11606]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:43.988 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:43.988 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:43.988 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:43.988 D/RILJ    ( 1227): [11607]> OPERATOR
07-12 11:20:43.988 D/RILJ    ( 1227): [11608]> DATA_REGISTRATION_STATE
07-12 11:20:43.988 D/RILJ    ( 1227): [11607]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:43.998 D/RILJ    ( 1227): [11609]> VOICE_REGISTRATION_STATE
07-12 11:20:43.998 D/RILJ    ( 1227): [11610]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:43.998 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:43.998 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:43.998 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:43.998 D/RILJ    ( 1227): [11608]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, 20}
07-12 11:20:43.998 D/RILJ    ( 1227): [11611]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:43.998 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:43.998 D/GSM     ( 1227): [GsmDCT] onReceive: action=android.intent.action.SCREEN_ON
07-12 11:20:43.998 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:20:43.998 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:20:43.998 D/GSM     ( 1227): [GsmDCT] startNetStatPoll
07-12 11:20:43.998 D/RILJ    ( 1227): [11609]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1604, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:20:43.998 D/RILJ    ( 1227): [11610]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:44.008 D/RILJ    ( 1227): responseGetModemInfo[I@42adfc70
07-12 11:20:44.008 D/RILJ    ( 1227): [11611]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:20:44.018 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:20:44.018 D/GSM     ( 1227): [EONS] Received CID = 65803780
07-12 11:20:44.018 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:20:44.018 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:20:44.018 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:44.018 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:20:44.018 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:44.018 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:44.018 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:44.018 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:44.499 D/GSM     ( 1227): [GsmCallTracker] (foregnd) hangup dialing or alerting...
07-12 11:20:44.499 D/RILJ    ( 1227): hangupConnection: gsmIndex=1
07-12 11:20:44.499 D/RILJ    ( 1227): [11612]> HANGUP 1
07-12 11:20:44.789 D/RILJ    ( 1227): [11612]< HANGUP 
07-12 11:20:44.789 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:20:44.799 D/RILJ    ( 1227): [11613]> GET_CURRENT_CALLS
07-12 11:20:44.799 D/RILJ    ( 1227): [11614]> GET_CURRENT_CALLS
07-12 11:20:44.799 D/RILJ    ( 1227): [11613]< GET_CURRENT_CALLS  
07-12 11:20:44.799 D/RILJ    ( 1227): [11614]< GET_CURRENT_CALLS  
07-12 11:20:44.799 D/GSM     ( 1227): [GSMConn] releaseWakeLock
07-12 11:20:44.799 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270344 when=-5ms obj=android.os.AsyncResult@42cbbba8 }
07-12 11:20:44.799 D/GSM     ( 1227): [GsmDCT] onVoiceCallEnded
07-12 11:20:44.799 D/GSM     ( 1227): [LGE_DATA] functionForPacketDrop for ACTION_VOICE_CALL_ENDED
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] setupDataOnReadyApns: 2GVoiceCallEnded
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] configureRetry: forDefault=true retryCount=0 dc={GsmDC-1: State=DcActiveState apnSetting=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 apnList= [{mApnType=ims mState=CONNECTED mWaitingApns=[[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 mDataConnectionAc=GsmDC-1 mReason=dataEnabled mRetryCount=0 mDataEnabled=true mDependencyMet=true}] RefCount=1 cid=0 create=1373486750617 lastFail=-1 lastFailCause=NONE}
07-12 11:20:44.829 E/GSM     ( 1227): [GsmDCT] [LG_DATA] configureRetry : by DOMESTIC_DATA_RETRY_CONFIG
07-12 11:20:44.829 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDC-1] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] configureRetry: forDefault=false retryCount=0 dc={GsmDC-2: State=DcInactiveState apnSetting=null apnList= [] RefCount=0 cid=-1 create=-1 lastFail=-1 lastFailCause=NONE}
07-12 11:20:44.829 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDC-2] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:admin] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:fota] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:ktmultirab1] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:entitlement] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:dun] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:ktmultirab2] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:supl] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:hipri] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:tethering] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:ims] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDC-1] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:usccapp] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:default] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:vzw800] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:mms] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:cbs] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:bip] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:vzwapp] setRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:20:44.829 D/GSM     ( 1227): [ApnContext:default] set reason as 2GVoiceCallEnded,current state IDLE
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] trySetupData for type:default due to 2GVoiceCallEnded
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] trySetupData with mIsPsRestricted=false
07-12 11:20:44.829 E/GSM     ( 1227): [GSMPhone] getEsn() is a CDMA method
07-12 11:20:44.829 E/GSM     ( 1227): [GSMPhone] getEsn() is a CDMA method
07-12 11:20:44.829 D/GSM     ( 1227): [LGE_DATA] <mbooting_phone> = false
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] MMS is available even if data enabled sets off : false
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:admin
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] isDataPossible(admin): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] get active apn string for type:admin
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:fota
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] isDataPossible(fota): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] get active apn string for type:fota
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:ktmultirab1
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] isDataPossible(ktmultirab1): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.829 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ktmultirab1
07-12 11:20:44.839 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:entitlement
07-12 11:20:44.839 D/GSM     ( 1227): [GsmDCT] isDataPossible(entitlement): possible=false isDataAllowed=true apnTypePossible=false apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.839 D/GSM     ( 1227): [GsmDCT] get active apn string for type:entitlement
07-12 11:20:44.839 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:dun
07-12 11:20:44.839 D/GSM     ( 1227): [GsmDCT] isDataPossible(dun): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.839 D/GSM     ( 1227): [GsmDCT] get active apn string for type:dun
07-12 11:20:44.839 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:ktmultirab2
07-12 11:20:44.839 D/GSM     ( 1227): [GsmDCT] isDataPossible(ktmultirab2): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.839 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ktmultirab2
07-12 11:20:44.839 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:supl
07-12 11:20:44.839 D/GSM     ( 1227): [GsmDCT] isDataPossible(supl): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.839 D/GSM     ( 1227): [GsmDCT] get active apn string for type:supl
07-12 11:20:44.849 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:hipri
07-12 11:20:44.849 D/GSM     ( 1227): [GsmDCT] isDataPossible(hipri): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.849 D/GSM     ( 1227): [GsmDCT] get active apn string for type:hipri
07-12 11:20:44.849 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:tethering
07-12 11:20:44.849 D/GSM     ( 1227): [GsmDCT] isDataPossible(tethering): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.849 D/GSM     ( 1227): [GsmDCT] get active apn string for type:tethering
07-12 11:20:44.849 D/GSM     ( 1227): [GsmDCT] notifyOffApnsOfAvailability skipped apn due to isReady==false: {mApnType=ims mState=CONNECTED mWaitingApns=[[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 mDataConnectionAc=GsmDC-1 mReason=dataEnabled mRetryCount=0 mDataEnabled=true mDependencyMet=true}
07-12 11:20:44.849 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:usccapp
07-12 11:20:44.849 D/GSM     ( 1227): [GsmDCT] isDataPossible(usccapp): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.849 D/GSM     ( 1227): [GsmDCT] get active apn string for type:usccapp
07-12 11:20:44.859 D/GSM     ( 1227): [GsmDCT] notifyOffApnsOfAvailability skipped apn due to isReady==false: {mApnType=default mState=IDLE mWaitingApns=[[ApnSettingV2] SKT, 476, 45005, lte.sktelecom.com, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, default | mms | dun | hipri | supl | fota | cbs, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT, 476, 45005, lte.sktelecom.com, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, default | mms | dun | hipri | supl | fota | cbs, IP, IP, true, 0 mDataConnectionAc=null mReason=2GVoiceCallEnded mRetryCount=0 mDataEnabled=true mDependencyMet=true}
07-12 11:20:44.859 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:vzw800
07-12 11:20:44.859 D/GSM     ( 1227): [GsmDCT] isDataPossible(vzw800): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.859 D/GSM     ( 1227): [GsmDCT] get active apn string for type:vzw800
07-12 11:20:44.859 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:mms
07-12 11:20:44.859 D/GSM     ( 1227): [GsmDCT] isDataPossible(mms): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.859 D/GSM     ( 1227): [GsmDCT] get active apn string for type:mms
07-12 11:20:44.859 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:cbs
07-12 11:20:44.859 D/GSM     ( 1227): [GsmDCT] isDataPossible(cbs): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.859 D/GSM     ( 1227): [GsmDCT] get active apn string for type:cbs
07-12 11:20:44.869 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:bip
07-12 11:20:44.869 D/GSM     ( 1227): [GsmDCT] isDataPossible(bip): possible=false isDataAllowed=true apnTypePossible=false apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.869 D/GSM     ( 1227): [GsmDCT] get active apn string for type:bip
07-12 11:20:44.869 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:vzwapp
07-12 11:20:44.869 D/GSM     ( 1227): [GsmDCT] isDataPossible(vzwapp): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:20:44.869 D/GSM     ( 1227): [GsmDCT] get active apn string for type:vzwapp
07-12 11:20:44.899 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:44.899 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:44.899 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:20:44.899 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:44.899 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:44.899 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:20:44.919 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:44.919 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:44.919 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:20:44.959 E/RILC    (  341): responseLGERPInd(): param(425992(0x00068008)), data_valid(1), data_len(4)
07-12 11:20:44.959 I/RILJ    ( 1227): LGE_UNSOL_RRC_RELEASE_CAUSE: releaseCause = 1
07-12 11:20:44.959 D/RILJ    ( 1227): returned data  = [B@43a5ca58
07-12 11:20:45.430 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 3
07-12 11:20:45.430 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:45.930 D/RILJ    ( 1227): [UNSL]< UNSOL_NITZ_TIME_RECEIVED 13/07/12,02:20:46+36,00
07-12 11:20:45.930 D/GSM     ( 1227): [GsmSST] NITZ: 13/07/12,02:20:46+36,00,108918820 start=108918821 delay=1
07-12 11:20:45.930 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:45.930 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4d4c0408000b00000002000d0001040000000000
07-12 11:20:45.930 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:20:45.930 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:20:45.930 I/GSM     ( 1227): NITZ: current iso = kr, mGotCountryCode = true
07-12 11:20:45.930 I/GSM     ( 1227):  NITZ: after iso = kr, mGotCountryCode = true
07-12 11:20:45.930 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525388
07-12 11:20:45.930 D/GSM     ( 1227): [GsmSST] NITZ:2 getAutoTimeZone() is OK : Asia/Seoul
07-12 11:20:45.930 D/RILJ    ( 1227): Response ID 525388is not served in this process.
07-12 11:20:45.930 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:20:45.930 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: setTimeZone=Asia/Seoul
07-12 11:20:45.930 D/RILJ    ( 1227): [UNSL]< UNSOL_WCDMA_ACCEPT_RECEIVED {1, 1}
07-12 11:20:45.930 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: call alarm.setTimeZone and broadcast zoneId=Asia/Seoul
07-12 11:20:45.930 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595640005,108912902,Asia/Seoul,450
07-12 11:20:45.930 D/RILJ    ( 1227): [UNSL]< UNSOL_VOICE_RADIO_TECH_CHANGED {0}
07-12 11:20:45.930 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:45.930 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:45.940 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:46.050 D/GSM     ( 1227): [GsmSST] NITZ: Setting time of day to Fri Jul 12 11:20:46 GMT+09:00 2013 NITZ receive delay(ms): 126 gained(ms): 65 from 13/07/12,02:20:46+36,00
07-12 11:20:46.050 W/GSM     ( 1227): BroadcastNITZTime
07-12 11:20:46.050 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTime: time=1373595646126ms
07-12 11:20:46.136 I/GSM     ( 1227): NITZ: after Setting time of day
07-12 11:20:46.136 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595646126,108918963,Asia/Seoul,450
07-12 11:20:46.136 D/RILJ    ( 1227): [11615]> OPERATOR
07-12 11:20:46.146 D/RILJ    ( 1227): [11616]> DATA_REGISTRATION_STATE
07-12 11:20:46.146 D/RILJ    ( 1227): [11617]> VOICE_REGISTRATION_STATE
07-12 11:20:46.146 D/RILJ    ( 1227): [11618]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:46.146 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:46.146 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:46.146 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:46.146 D/RILJ    ( 1227): [11615]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:46.146 D/RILJ    ( 1227): [11619]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:46.146 D/RILJ    ( 1227): [11617]< VOICE_REGISTRATION_STATE {1, null, 00a52f03, 14, null, null, null, 0, null, null, null, null, null, 0, 0}
07-12 11:20:46.146 D/RILJ    ( 1227): responseGetModemInfo[I@43d0e4f8
07-12 11:20:46.156 D/RILJ    ( 1227): [11619]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:46.156 D/RILJ    ( 1227): [11616]< DATA_REGISTRATION_STATE {1, 3212, 00a52f03, 14, null, 20}
07-12 11:20:46.156 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:46.156 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:46.156 D/RILJ    ( 1227): [11618]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:46.166 E/GSM     ( 1227): LGT Network Accept: mm_accept = 1 ,gmm_accept = 1
07-12 11:20:46.166 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:46.166 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:46.166 D/RILJ    ( 1227): [11620]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:46.166 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 3
07-12 11:20:46.166 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:46.166 D/RILJ    ( 1227): responseGetModemInfo[I@431f07d8
07-12 11:20:46.166 D/RILJ    ( 1227): [11620]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:46.176 D/GSM     ( 1227): [GSMphone] mIccRecords.iccid = 8982051006425136633
07-12 11:20:46.176 D/PHONE   ( 1227): [PhoneProxy] Ignoring voice radio technology changed message. newVoiceRadioTech = Unknown. Active Phone = GSM
07-12 11:20:46.176 D/RILJ    ( 1227): [11621]> OPERATOR
07-12 11:20:46.176 D/RILJ    ( 1227): [11622]> DATA_REGISTRATION_STATE
07-12 11:20:46.176 D/RILJ    ( 1227): [11623]> VOICE_REGISTRATION_STATE
07-12 11:20:46.176 D/RILJ    ( 1227): [11621]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:46.176 D/RILJ    ( 1227): [11624]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:46.176 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:46.176 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:46.176 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:46.176 D/RILJ    ( 1227): [11625]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:46.176 D/RILJ    ( 1227): [11626]> OPERATOR
07-12 11:20:46.176 D/RILJ    ( 1227): [11627]> DATA_REGISTRATION_STATE
07-12 11:20:46.186 D/RILJ    ( 1227): [11628]> VOICE_REGISTRATION_STATE
07-12 11:20:46.186 D/RILJ    ( 1227): [11629]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:46.186 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:46.186 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:46.186 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:46.186 D/RILJ    ( 1227): [11630]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:46.186 D/RILJ    ( 1227): [11631]> OPERATOR
07-12 11:20:46.186 D/RILJ    ( 1227): [11632]> DATA_REGISTRATION_STATE
07-12 11:20:46.186 D/RILJ    ( 1227): [11633]> VOICE_REGISTRATION_STATE
07-12 11:20:46.186 D/RILJ    ( 1227): [11634]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:46.186 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:46.186 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:46.186 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:46.186 D/RILJ    ( 1227): [11635]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:46.186 D/RILJ    ( 1227): [11622]< DATA_REGISTRATION_STATE {1, 3212, 00a52f03, 14, null, 20}
07-12 11:20:46.186 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:20:46.186 D/RILJ    ( 1227): [11623]< VOICE_REGISTRATION_STATE {1, null, 00a52f03, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:20:46.186 D/RILJ    ( 1227): [11624]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:46.186 D/RILJ    ( 1227): responseGetModemInfo[I@43b7b580
07-12 11:20:46.186 D/RILJ    ( 1227): [11625]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:46.196 D/RILJ    ( 1227): responseGetModemInfo[I@431bd988
07-12 11:20:46.196 D/RILJ    ( 1227): [11630]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:46.196 D/RILJ    ( 1227): [11626]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:46.196 D/RILJ    ( 1227): [11631]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:46.196 D/RILJ    ( 1227): [11628]< VOICE_REGISTRATION_STATE {1, null, 00a52f03, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:20:46.196 D/RILJ    ( 1227): [11633]< VOICE_REGISTRATION_STATE {1, null, 00a52f03, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:20:46.196 D/RILJ    ( 1227): [11629]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:46.196 D/RILJ    ( 1227): [11634]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:46.196 D/RILJ    ( 1227): responseGetModemInfo[I@431be910
07-12 11:20:46.196 D/RILJ    ( 1227): [11635]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:46.196 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:46.196 D/RILJ    ( 1227): [11636]> OPERATOR
07-12 11:20:46.196 D/RILJ    ( 1227): [11627]< DATA_REGISTRATION_STATE {1, 3212, 00a52f03, 14, null, 20}
07-12 11:20:46.196 D/RILJ    ( 1227): [11632]< DATA_REGISTRATION_STATE {1, 3212, 00a52f03, 14, null, 20}
07-12 11:20:46.196 D/RILJ    ( 1227): [11637]> DATA_REGISTRATION_STATE
07-12 11:20:46.206 D/RILJ    ( 1227): [11636]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:46.206 D/RILJ    ( 1227): [11638]> VOICE_REGISTRATION_STATE
07-12 11:20:46.206 D/RILJ    ( 1227): [11639]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:46.206 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:46.206 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:46.206 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:46.206 D/RILJ    ( 1227): [11640]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:46.206 D/RILJ    ( 1227): [11638]< VOICE_REGISTRATION_STATE {1, null, 00a52f03, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:20:46.206 D/RILJ    ( 1227): [11641]> OPERATOR
07-12 11:20:46.206 D/RILJ    ( 1227): [11637]< DATA_REGISTRATION_STATE {1, 3212, 00a52f03, 14, null, 20}
07-12 11:20:46.206 D/RILJ    ( 1227): [11642]> DATA_REGISTRATION_STATE
07-12 11:20:46.216 D/RILJ    ( 1227): [11643]> VOICE_REGISTRATION_STATE
07-12 11:20:46.216 D/RILJ    ( 1227): [11644]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:46.216 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:46.216 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:46.216 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:46.216 D/RILJ    ( 1227): [11645]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:46.216 D/RILJ    ( 1227): responseGetModemInfo[I@432b2318
07-12 11:20:46.216 D/RILJ    ( 1227): [11640]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:46.216 D/RILJ    ( 1227): [11639]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:46.216 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:46.216 D/RILJ    ( 1227): [11646]> OPERATOR
07-12 11:20:46.216 D/RILJ    ( 1227): [11647]> DATA_REGISTRATION_STATE
07-12 11:20:46.216 D/RILJ    ( 1227): [11641]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:46.226 D/RILJ    ( 1227): [11648]> VOICE_REGISTRATION_STATE
07-12 11:20:46.226 D/RILJ    ( 1227): [11649]> QUERY_NETWORK_SELECTION_MODE
07-12 11:20:46.226 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:20:46.226 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:20:46.226 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:20:46.226 D/RILJ    ( 1227): [11650]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:20:46.226 D/RILJ    ( 1227): responseGetModemInfo[I@42b52478
07-12 11:20:46.226 D/RILJ    ( 1227): [11645]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:46.226 D/RILJ    ( 1227): [11643]< VOICE_REGISTRATION_STATE {1, null, 00a52f03, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:20:46.226 D/RILJ    ( 1227): [11642]< DATA_REGISTRATION_STATE {1, 3212, 00a52f03, 14, null, 20}
07-12 11:20:46.226 D/RILJ    ( 1227): [11644]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:46.226 D/RILJ    ( 1227): [11646]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:20:46.226 D/RILJ    ( 1227): [11647]< DATA_REGISTRATION_STATE {1, 3212, 00a52f03, 14, null, 20}
07-12 11:20:46.226 D/RILJ    ( 1227): responseGetModemInfo[I@438a71e0
07-12 11:20:46.226 D/RILJ    ( 1227): [11650]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 9}
07-12 11:20:46.226 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:46.226 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:46.226 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:46.226 D/RILJ    ( 1227): [11649]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:20:46.236 D/RILJ    ( 1227): [11648]< VOICE_REGISTRATION_STATE {1, null, 00a52f03, 14, null, null, null, 0, null, null, 1, null, null, 0, 0}
07-12 11:20:46.236 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:46.236 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:46.236 D/GSM     ( 1227): [EONS] Received TAC = 12818
07-12 11:20:46.236 D/GSM     ( 1227): [EONS] Received CID = 10825475
07-12 11:20:46.236 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =14 , mTAC =12818
07-12 11:20:46.236 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:20:46.236 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 14, CStype = 14
07-12 11:20:46.236 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:20:46.236 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=LTE
07-12 11:20:46.236 D/GSM     ( 1227): [IMS_AFW] Radio Tech is LTE, Get LTE Info from modem
07-12 11:20:46.236 D/RILJ    ( 1227): [11651]> RIL_REQUEST_LTE_INFO_FOR_IMS
07-12 11:20:46.236 D/GSM     ( 1227): [GsmSST] RAT switched UMTS -> LTE at cell 10825475
07-12 11:20:46.236 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:20:46.236 D/GSM     ( 1227): [EONS] updateEons() lactac = 12818 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:20:46.236 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:20:46.236 D/RILJ    ( 1227): [11651]< RIL_REQUEST_LTE_INFO_FOR_IMS 450,05,0a52f03,3212
07-12 11:20:46.236 D/GSM     ( 1227): [GsmSST] shouldFixTimeZoneNow: retVal=false iccCard=null iccCard.state=null iccCardExist=false operatorNumeric=45005 mcc=450 prevOperatorNumeric=45005 prevMcc=450 needToFixTimeZone=false ltod=07-12 11:20:46.244
07-12 11:20:46.246 D/GSM     ( 1227): [GsmDCT] get all active apn types
07-12 11:20:46.246 D/GSM     ( 1227): [GsmDCT] return link properites for ims
07-12 11:20:46.246 D/GSM     ( 1227): [GsmDCT] get active pdp is not null, return link Capabilities for ims
07-12 11:20:46.246 D/GSM     ( 1227): [GsmDCT] isDataPossible(ims): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=CONNECTED
07-12 11:20:46.246 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ims
07-12 11:20:46.256 D/GSM     ( 1227): [GsmDCT] isDataPossible(default): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=IDLE
07-12 11:20:46.256 D/GSM     ( 1227): [GsmDCT] get active apn string for type:default
07-12 11:20:46.256 D/GSM     ( 1227): [GsmSST] [IMS_AFW] EVENT_GET_LTE_INFO_DONE
07-12 11:20:46.256 D/GSM     ( 1227): [GsmSST] [IMS_AFW] GET LTE Info: 450,05,0a52f03,3212
07-12 11:20:46.256 D/GSM     ( 1227): [GsmSST] [IMS_AFW] MCC : 450, MNC : 05, Cell ID : 0a52f03, TAC : 3212
07-12 11:20:50.930 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:20:50.930 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:53.483 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:20:53.483 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:20:54.103 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:20:54.103 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:20:54.103 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:21:02.893 E/PHONE   ( 1227): Settings Exception Reading Dual Sim Voice Prompt Values
07-12 11:21:02.893 D/PHONE   ( 1227): Prompt option:false
07-12 11:21:02.963 D/GSM     ( 1227): isTwoDigitShortCode
07-12 11:21:02.963 D/GSM     ( 1227): dialing w/ mmi 'null'...
07-12 11:21:02.963 D/GSM     ( 1227): [GSMConn] acquireWakeLock
07-12 11:21:02.963 D/RILJ    ( 1227): [11652]> SET_MUTE false
07-12 11:21:02.963 D/RILJ    ( 1227): [11653]> DIAL
07-12 11:21:02.973 D/RILJ    ( 1227): [11652]< SET_MUTE 
07-12 11:21:03.203 E/RILC    (  341): responseLGERPInd(): param(426000(0x00068010)), data_valid(1), data_len(1)
07-12 11:21:03.203 D/RILJ    ( 1227): [11653]< DIAL 
07-12 11:21:03.213 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:21:03.213 I/RILJ    ( 1227): LGE_UNSOL_IS_LTE_AVAILABLE:1
07-12 11:21:03.213 D/RILJ    ( 1227): returned data  = [B@439cea58
07-12 11:21:03.283 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:21:03.283 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:21:03.373 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270343 when=-407ms obj=android.os.AsyncResult@42b99358 }
07-12 11:21:03.373 D/GSM     ( 1227): [GsmDCT] onVoiceCallStarted
07-12 11:21:03.383 D/RILJ    ( 1227): [11654]> GET_CURRENT_CALLS
07-12 11:21:03.383 E/RILC    (  341): numberplus = ""
07-12 11:21:03.383 E/RILC    (  341): signalIE = 0
07-12 11:21:03.383 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:21:03.383 D/RILJ    ( 1227): No calling name expression is received
07-12 11:21:03.383 D/RILJ    ( 1227): signal = 0
07-12 11:21:03.383 D/RILJ    ( 1227): DriverCall dc = id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:21:03.383 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:21:03.383 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:21:03.383 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:21:03.383 D/RILJ    ( 1227): [DriverCall] dc : id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:21:03.393 D/RILJ    ( 1227): [11654]< GET_CURRENT_CALLS  [id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:21:03.393 D/RILJ    ( 1227): [11655]> GET_CURRENT_CALLS
07-12 11:21:03.393 E/RILC    (  341): numberplus = ""
07-12 11:21:03.393 E/RILC    (  341): signalIE = 0
07-12 11:21:03.393 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:21:03.393 D/RILJ    ( 1227): No calling name expression is received
07-12 11:21:03.393 D/RILJ    ( 1227): signal = 0
07-12 11:21:03.393 D/RILJ    ( 1227): DriverCall dc = id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:21:03.393 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:21:03.393 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:21:03.393 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:21:03.393 D/RILJ    ( 1227): [DriverCall] dc : id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:21:03.393 D/RILJ    ( 1227): [11655]< GET_CURRENT_CALLS  [id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:21:03.433 D/RILJ    ( 1227): responseDataCallList ver=7 num=1
07-12 11:21:03.433 D/RILJ    ( 1227): [UNSL]< UNSOL_DATA_CALL_LIST_CHANGED [DataCallState: {version=7 status=0 retry=-1 cid=0 active=2 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}]
07-12 11:21:03.433 D/GSM     ( 1227): [getVoiceMailNumber] isNetworkRoaming: false
07-12 11:21:03.433 D/GSM     ( 1227): **HEE** GsmPhone - getVoiceMailNumber() number = null
07-12 11:21:03.433 D/PHONE   ( 1227): VM: PhoneSubInfo.getVoiceMailNUmber: 
07-12 11:21:03.443 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:21:03.443 D/GSM     ( 1227): [GSMConn] update: parent=DIALING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=false
07-12 11:21:03.443 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:21:03.443 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:21:03.443 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:21:03.523 D/RILJ    ( 1227): responseDataCallList ver=7 num=1
07-12 11:21:03.523 D/RILJ    ( 1227): [UNSL]< UNSOL_DATA_CALL_LIST_CHANGED [DataCallState: {version=7 status=0 retry=-1 cid=0 active=1 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}]
07-12 11:21:03.593 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270340 when=-159ms obj=android.os.AsyncResult@42a9ca48 }
07-12 11:21:03.593 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): E
07-12 11:21:03.593 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): DataCallState size=1
07-12 11:21:03.593 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): E dcacs=[GsmDC-1]
07-12 11:21:03.593 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): X list=[]
07-12 11:21:03.593 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): Found ConnId=0 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=2 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:21:03.593 D/GSM     ( 1227): addr/pl=42.19.184.78/30
07-12 11:21:03.593 D/GSM     ( 1227): [GsmDC-1] REQ_UPDATE_LINK_PROPERTIES_DATA_CALL_STATE result=com.android.internal.telephony.DataConnection$UpdateLinkPropertyResult@43e253f0 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=2 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:21:03.593 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): no change
07-12 11:21:03.593 D/GSM     ( 1227): [GsmDCT] onDataStateChanged: Data Activity updated to NONE. isAnyDataCallActive = true isAnyDataCallDormant = false
07-12 11:21:03.593 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:21:03.593 D/GSM     ( 1227): [GsmDCT] onDataStateChange(ar): apnsToCleanup=[]
07-12 11:21:03.593 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): X
07-12 11:21:03.794 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270340 when=-268ms obj=android.os.AsyncResult@43983e18 }
07-12 11:21:03.794 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): E
07-12 11:21:03.794 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): DataCallState size=1
07-12 11:21:03.794 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): E dcacs=[GsmDC-1]
07-12 11:21:03.794 D/GSM     ( 1227): [GsmDCT] findApnContextToClean(ar): X list=[]
07-12 11:21:03.794 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): Found ConnId=0 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=1 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:21:03.794 D/GSM     ( 1227): addr/pl=42.19.184.78/30
07-12 11:21:03.794 D/GSM     ( 1227): [GsmDC-1] REQ_UPDATE_LINK_PROPERTIES_DATA_CALL_STATE result=com.android.internal.telephony.DataConnection$UpdateLinkPropertyResult@43271f98 newState=DataCallState: {version=7 status=0 retry=-1 cid=0 active=1 type=IP' ifname='rmnet0' addresses=[42.19.184.78/30] dnses=[211.234.229.23,113.217.240.31] gateways=[42.19.184.77]}
07-12 11:21:03.794 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): no change
07-12 11:21:03.794 D/GSM     ( 1227): topActivity.getPackageName(); = com.android.phone
07-12 11:21:03.794 D/GSM     ( 1227): topActivity.getClassName(); = com.android.phone.InCallScreen
07-12 11:21:03.794 D/GSM     ( 1227): VOICE CALL  ::true
07-12 11:21:03.794 D/GSM     ( 1227): (InCallScreen) topActivity.getClassName(); = com.android.phone.InCallScreen
07-12 11:21:03.804 D/GSM     ( 1227): functionForPacketDrop is called
07-12 11:21:03.804 D/GSM     ( 1227): [GsmDCT] onDataStateChanged: Data Activity updated to DORMANT. stopNetStatePoll
07-12 11:21:03.804 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:21:03.804 D/GSM     ( 1227): [GsmDCT] onDataStateChange(ar): apnsToCleanup=[]
07-12 11:21:03.804 D/GSM     ( 1227): [GsmDCT] onDataStateChanged(ar): X
07-12 11:21:04.655 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4def0308000100000003
07-12 11:21:04.655 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:21:04.655 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:21:04.655 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525295
07-12 11:21:04.655 D/RILJ    ( 1227): Response ID 525295is not served in this process.
07-12 11:21:04.655 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:21:04.665 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4d4c0408000b00000002000d0001040000000000
07-12 11:21:04.665 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:21:04.665 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:21:04.665 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525388
07-12 11:21:04.665 D/RILJ    ( 1227): Response ID 525388is not served in this process.
07-12 11:21:04.665 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:21:04.685 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:21:04.685 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:21:04.695 D/RILJ    ( 1227): [UNSL]< UNSOL_VOICE_RADIO_TECH_CHANGED {3}
07-12 11:21:04.695 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:21:04.705 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 14
07-12 11:21:04.705 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:21:04.705 D/PHONE   ( 1227): [PhoneProxy] Ignoring voice radio technology changed message. newVoiceRadioTech = 3 Active Phone = GSM
07-12 11:21:04.705 D/RILJ    ( 1227): [11656]> OPERATOR
07-12 11:21:04.715 D/RILJ    ( 1227): [11657]> DATA_REGISTRATION_STATE
07-12 11:21:04.715 D/RILJ    ( 1227): [11658]> VOICE_REGISTRATION_STATE
07-12 11:21:04.715 D/RILJ    ( 1227): [11659]> QUERY_NETWORK_SELECTION_MODE
07-12 11:21:04.715 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:21:04.715 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:21:04.715 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:21:04.715 D/RILJ    ( 1227): [11660]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:21:04.715 D/RILJ    ( 1227): responseGetModemInfo[I@43b95d08
07-12 11:21:04.715 D/RILJ    ( 1227): [11660]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:21:04.725 D/RILJ    ( 1227): [11657]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, 20}
07-12 11:21:04.725 D/RILJ    ( 1227): [11659]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:21:04.725 D/RILJ    ( 1227): [11658]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:21:04.725 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:21:04.725 D/RILJ    ( 1227): [11656]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:21:04.725 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:21:04.725 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:21:04.725 D/GSM     ( 1227): [EONS] Received CID = 65803784
07-12 11:21:04.725 D/GSM     ( 1227): use mTAC  with LTE: 8689
07-12 11:21:04.725 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:21:04.725 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:21:04.725 D/GSM     ( 1227): use lac because Not NULL: 8689
07-12 11:21:04.725 D/RILJ    ( 1227): [11661]> OPERATOR
07-12 11:21:04.725 D/RILJ    ( 1227): [11662]> DATA_REGISTRATION_STATE
07-12 11:21:04.725 D/RILJ    ( 1227): [11663]> VOICE_REGISTRATION_STATE
07-12 11:21:04.725 D/RILJ    ( 1227): [11664]> QUERY_NETWORK_SELECTION_MODE
07-12 11:21:04.725 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:21:04.725 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:21:04.725 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:21:04.725 D/RILJ    ( 1227): [11665]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:21:04.735 D/RILJ    ( 1227): responseGetModemInfo[I@43268470
07-12 11:21:04.735 D/RILJ    ( 1227): [11665]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:21:04.735 D/RILJ    ( 1227): [11663]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:21:04.735 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:21:04.735 D/RILJ    ( 1227): [11662]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, 20}
07-12 11:21:04.735 D/RILJ    ( 1227): [11664]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:21:04.735 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:21:04.735 D/GSM     ( 1227): use lac because Not NULL: 8689
07-12 11:21:04.735 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:21:04.735 D/GSM     ( 1227): [EONS] Received CID = 65803784
07-12 11:21:04.735 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:21:04.735 D/RILJ    ( 1227): [11661]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:21:04.735 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:21:04.735 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  LTE CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=LTE newType=UMTS
07-12 11:21:04.735 D/GSM     ( 1227): [GsmSST] RAT switched LTE -> UMTS at cell 65803784
07-12 11:21:04.735 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:21:04.735 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:21:04.735 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:21:04.745 D/GSM     ( 1227): [GsmSST] shouldFixTimeZoneNow: retVal=false iccCard=null iccCard.state=null iccCardExist=false operatorNumeric=45005 mcc=450 prevOperatorNumeric=45005 prevMcc=450 needToFixTimeZone=false ltod=07-12 11:21:04.748
07-12 11:21:04.755 D/GSM     ( 1227): [GsmDCT] get all active apn types
07-12 11:21:04.755 D/GSM     ( 1227): [GsmDCT] return link properites for ims
07-12 11:21:04.755 D/GSM     ( 1227): [GsmDCT] get active pdp is not null, return link Capabilities for ims
07-12 11:21:04.765 D/GSM     ( 1227): [GsmDCT] isDataPossible(ims): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=CONNECTED
07-12 11:21:04.765 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ims
07-12 11:21:04.765 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:21:04.765 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:21:04.765 D/GSM     ( 1227): [GsmDCT] isDataPossible(default): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=true apnContextState()=IDLE
07-12 11:21:04.765 D/GSM     ( 1227): [GsmDCT] get active apn string for type:default
07-12 11:21:04.825 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:21:04.825 D/RILJ    ( 1227): [11666]> GET_CURRENT_CALLS
07-12 11:21:04.825 E/RILC    (  341): numberplus = ""
07-12 11:21:04.825 E/RILC    (  341): signalIE = 0
07-12 11:21:04.835 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:21:04.835 D/RILJ    ( 1227): No calling name expression is received
07-12 11:21:04.835 D/RILJ    ( 1227): signal = 0
07-12 11:21:04.835 D/RILJ    ( 1227): DriverCall dc = id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:21:04.835 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:21:04.835 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:21:04.835 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:21:04.835 D/RILJ    ( 1227): [DriverCall] dc : id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:21:04.835 D/RILJ    ( 1227): [11666]< GET_CURRENT_CALLS  [id=1,DIALING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:21:04.835 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:21:04.835 D/GSM     ( 1227): [GSMConn] update: parent=DIALING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=false
07-12 11:21:04.835 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:21:04.855 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:21:04.855 D/RILJ    ( 1227): [11667]> OPERATOR
07-12 11:21:04.855 D/RILJ    ( 1227): [11668]> DATA_REGISTRATION_STATE
07-12 11:21:04.855 D/RILJ    ( 1227): [11669]> VOICE_REGISTRATION_STATE
07-12 11:21:04.855 D/RILJ    ( 1227): [11670]> QUERY_NETWORK_SELECTION_MODE
07-12 11:21:04.855 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:21:04.855 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:21:04.855 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:21:04.855 D/RILJ    ( 1227): [11671]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:21:04.865 D/RILJ    ( 1227): [11668]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, 20}
07-12 11:21:04.865 D/RILJ    ( 1227): [11667]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:21:04.865 D/RILJ    ( 1227): [11669]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:21:04.865 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:21:04.865 D/GSM     ( 1227): [EONS] Received CID = 65803784
07-12 11:21:04.865 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:21:04.865 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:21:04.865 D/RILJ    ( 1227): [11670]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:21:04.865 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:21:04.865 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:21:04.865 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:21:04.865 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:21:04.865 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:21:04.865 D/RILJ    ( 1227): responseGetModemInfo[I@4382cb48
07-12 11:21:04.865 D/RILJ    ( 1227): [11671]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:21:04.865 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:21:05.155 D/RILJ    ( 1227): [11672]> SCREEN_STATE: false
07-12 11:21:05.175 D/RILJ    ( 1227): [11672]< SCREEN_STATE 
07-12 11:21:05.245 D/GSM     ( 1227): [GsmDCT] onReceive: action=android.intent.action.SCREEN_OFF
07-12 11:21:05.245 D/GSM     ( 1227): [GsmDCT] stopNetStatPoll
07-12 11:21:05.245 D/GSM     ( 1227): [GsmDCT] overall state is CONNECTED
07-12 11:21:05.245 D/GSM     ( 1227): [GsmDCT] startNetStatPoll
07-12 11:21:07.297 D/RILJ    ( 1227): [UNSL]< UNSOL_NITZ_TIME_RECEIVED 13/07/12,02:21:08+36,00
07-12 11:21:07.297 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:21:07.297 D/GSM     ( 1227): [GsmSST] NITZ: 13/07/12,02:21:08+36,00,108940134 start=108940137 delay=3
07-12 11:21:07.297 I/GSM     ( 1227): NITZ: current iso = kr, mGotCountryCode = true
07-12 11:21:07.297 I/GSM     ( 1227):  NITZ: after iso = kr, mGotCountryCode = true
07-12 11:21:07.297 D/GSM     ( 1227): [GsmSST] NITZ:2 getAutoTimeZone() is OK : Asia/Seoul
07-12 11:21:07.297 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: setTimeZone=Asia/Seoul
07-12 11:21:07.307 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTimeZone: call alarm.setTimeZone and broadcast zoneId=Asia/Seoul
07-12 11:21:07.307 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595646126,108918963,Asia/Seoul,450
07-12 11:21:07.307 D/GSM     ( 1227): [GsmSST] NITZ: Setting time of day to Fri Jul 12 11:21:08 GMT+09:00 2013 NITZ receive delay(ms): 14 gained(ms): 688 from 13/07/12,02:21:08+36,00
07-12 11:21:07.307 W/GSM     ( 1227): BroadcastNITZTime
07-12 11:21:07.317 D/GSM     ( 1227): [GsmSST] setAndBroadcastNetworkSetTime: time=1373595668014ms
07-12 11:21:08.064 I/GSM     ( 1227): NITZ: after Setting time of day
07-12 11:21:08.064 D/GSM     ( 1227): [GsmSST] setRoamingNITZInfo :1373595668014,108940218,Asia/Seoul,450
07-12 11:21:08.084 D/RILJ    ( 1227): [11673]> OPERATOR
07-12 11:21:08.104 D/RILJ    ( 1227): [11674]> DATA_REGISTRATION_STATE
07-12 11:21:08.104 D/RILJ    ( 1227): [11675]> VOICE_REGISTRATION_STATE
07-12 11:21:08.104 D/RILJ    ( 1227): [11676]> QUERY_NETWORK_SELECTION_MODE
07-12 11:21:08.114 D/RILJ    ( 1227): [11673]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:21:08.114 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:21:08.114 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:21:08.114 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:21:08.134 D/RILJ    ( 1227): [11674]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, 20}
07-12 11:21:08.134 D/RILJ    ( 1227): [11676]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:21:08.134 D/RILJ    ( 1227): [UNSL]< UNSOL_WCDMA_ACCEPT_RECEIVED {0, 1}
07-12 11:21:08.134 D/RILJ    ( 1227): [11675]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:21:08.134 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:21:08.134 D/RILJ    ( 1227): [11677]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:21:08.134 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:21:08.134 D/GSM     ( 1227): [EONS] Received CID = 65803784
07-12 11:21:08.134 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:21:08.134 E/GSM     ( 1227): LGT Network Accept: mm_accept = 0 ,gmm_accept = 1
07-12 11:21:08.134 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:21:08.134 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:21:08.134 D/RILJ    ( 1227): responseGetModemInfo[I@438cb1c8
07-12 11:21:08.134 D/RILJ    ( 1227): [11677]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:21:08.134 D/RILJ    ( 1227): [11678]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:21:08.134 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:21:08.134 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:21:08.134 D/RILJ    ( 1227): responseGetModemInfo[I@438cc268
07-12 11:21:08.134 D/RILJ    ( 1227): [11678]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:21:08.134 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:21:08.144 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:21:08.144 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:21:08.144 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:21:08.144 D/RILJ    ( 1227): [11679]> OPERATOR
07-12 11:21:08.144 D/RILJ    ( 1227): [11680]> DATA_REGISTRATION_STATE
07-12 11:21:08.144 D/RILJ    ( 1227): [11681]> VOICE_REGISTRATION_STATE
07-12 11:21:08.144 D/RILJ    ( 1227): [11682]> QUERY_NETWORK_SELECTION_MODE
07-12 11:21:08.154 D/RILJ    ( 1227): [11679]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:21:08.154 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:21:08.154 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:21:08.154 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:21:08.154 D/RILJ    ( 1227): [11683]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:21:08.154 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:21:08.164 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:21:08.164 D/RILJ    ( 1227): [11680]< DATA_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, 20}
07-12 11:21:08.164 D/RILJ    ( 1227): [11681]< VOICE_REGISTRATION_STATE {1, 21f1, 03ec1608, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:21:08.164 D/RILJ    ( 1227): responseGetModemInfo[I@439e92c8
07-12 11:21:08.164 D/RILJ    ( 1227): [11683]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:21:08.164 D/RILJ    ( 1227): [11682]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:21:08.164 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:21:08.164 D/GSM     ( 1227): [EONS] Received CID = 65803784
07-12 11:21:08.164 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:21:08.164 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:21:08.164 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:21:08.164 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:21:08.164 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:21:08.164 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:21:08.164 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:21:08.164 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:21:08.174 D/GSM     ( 1227): [GSMphone] mIccRecords.iccid = 8982051006425136633
07-12 11:21:09.885 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:21:09.885 D/RILJ    ( 1227): [11684]> GET_CURRENT_CALLS
07-12 11:21:09.895 E/RILC    (  341): numberplus = ""
07-12 11:21:09.895 E/RILC    (  341): signalIE = 0
07-12 11:21:09.895 V/RILJ    ( 1227): Incoming UUS : NOT present!
07-12 11:21:09.895 D/RILJ    ( 1227): No calling name expression is received
07-12 11:21:09.895 D/RILJ    ( 1227): signal = 0
07-12 11:21:09.895 D/RILJ    ( 1227): DriverCall dc = id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:21:09.895 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST = 0
07-12 11:21:09.895 D/RILJ    ( 1227): Settings.Secure.OEM_RAD_TEST_RCV_PRFIX = 82
07-12 11:21:09.895 D/RILJ    ( 1227): InCall VoicePrivacy is disabled
07-12 11:21:09.895 D/RILJ    ( 1227): [DriverCall] dc : id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0
07-12 11:21:09.895 D/RILJ    ( 1227): [11684]< GET_CURRENT_CALLS  [id=1,ALERTING,toa=129,norm,mo,0,callmode=0,noevp,,cli=1,,0] 
07-12 11:21:09.895 D/GSM     ( 1227): [GSMConn] --dssds----null
07-12 11:21:09.895 D/GSM     ( 1227): [GSMConn] update: parent=ALERTING, hasNewParent=false, wasConnectingInOrOut=true, wasHolding=false, isConnectingInOrOut=true, changed=true
07-12 11:21:09.895 D/GSM     ( 1227): [GSMConn] cdnipNumber 1 = 
07-12 11:21:14.239 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_CALL_STATE_CHANGED
07-12 11:21:14.239 D/RILJ    ( 1227): [11685]> GET_CURRENT_CALLS
07-12 11:21:14.239 D/RILJ    ( 1227): [11685]< GET_CURRENT_CALLS  
07-12 11:21:14.239 D/RILJ    ( 1227): [11686]> LAST_CALL_FAIL_CAUSE
07-12 11:21:14.249 D/RILJ    ( 1227): [11686]< LAST_CALL_FAIL_CAUSE {17}
07-12 11:21:14.249 D/GSM     ( 1227): [GSMConn] releaseWakeLock
07-12 11:21:14.280 D/GSM     ( 1227): [GsmDCT] handleMessage msg={ what=270344 when=-28ms obj=android.os.AsyncResult@431e8a68 }
07-12 11:21:14.280 D/GSM     ( 1227): [GsmDCT] onVoiceCallEnded
07-12 11:21:14.280 D/GSM     ( 1227): [LGE_DATA] functionForPacketDrop for ACTION_VOICE_CALL_ENDED
07-12 11:21:14.400 D/GSM     ( 1227): [GsmDCT] setupDataOnReadyApns: 2GVoiceCallEnded
07-12 11:21:14.400 D/GSM     ( 1227): [GsmDCT] configureRetry: forDefault=true retryCount=0 dc={GsmDC-1: State=DcActiveState apnSetting=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 apnList= [{mApnType=ims mState=CONNECTED mWaitingApns=[[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 mDataConnectionAc=GsmDC-1 mReason=dataEnabled mRetryCount=0 mDataEnabled=true mDependencyMet=true}] RefCount=1 cid=0 create=1373486750617 lastFail=-1 lastFailCause=NONE}
07-12 11:21:14.400 E/GSM     ( 1227): [GsmDCT] [LG_DATA] configureRetry : by DOMESTIC_DATA_RETRY_CONFIG
07-12 11:21:14.400 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:21:14.400 D/GSM     ( 1227): [GsmDC-1] setRetryCount: 0
07-12 11:21:14.400 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [GsmDCT] configureRetry: forDefault=false retryCount=0 dc={GsmDC-2: State=DcInactiveState apnSetting=null apnList= [] RefCount=0 cid=-1 create=-1 lastFail=-1 lastFailCause=NONE}
07-12 11:21:14.410 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [GsmDC-2] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:admin] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:fota] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:ktmultirab1] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:entitlement] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:dun] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:ktmultirab2] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:supl] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:hipri] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:tethering] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:ims] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [GsmDC-1] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [RM] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:usccapp] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:default] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:vzw800] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:mms] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:cbs] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:bip] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [ApnContext:vzwapp] setRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:21:14.410 D/GSM     ( 1227): [RM] resetRetryCount: 0
07-12 11:21:14.420 D/GSM     ( 1227): [ApnContext:default] set reason as 2GVoiceCallEnded,current state IDLE
07-12 11:21:14.420 D/GSM     ( 1227): [GsmDCT] trySetupData for type:default due to 2GVoiceCallEnded
07-12 11:21:14.420 D/GSM     ( 1227): [GsmDCT] trySetupData with mIsPsRestricted=false
07-12 11:21:14.420 E/GSM     ( 1227): [GSMPhone] getEsn() is a CDMA method
07-12 11:21:14.420 E/GSM     ( 1227): [GSMPhone] getEsn() is a CDMA method
07-12 11:21:14.420 D/GSM     ( 1227): [LGE_DATA] <mbooting_phone> = false
07-12 11:21:14.420 D/GSM     ( 1227): [GsmDCT] MMS is available even if data enabled sets off : false
07-12 11:21:14.420 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:admin
07-12 11:21:14.420 D/GSM     ( 1227): [GsmDCT] isDataPossible(admin): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.420 D/GSM     ( 1227): [GsmDCT] get active apn string for type:admin
07-12 11:21:14.420 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:fota
07-12 11:21:14.430 D/GSM     ( 1227): [GsmDCT] isDataPossible(fota): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.430 D/GSM     ( 1227): [GsmDCT] get active apn string for type:fota
07-12 11:21:14.430 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:ktmultirab1
07-12 11:21:14.430 D/GSM     ( 1227): [GsmDCT] isDataPossible(ktmultirab1): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.430 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ktmultirab1
07-12 11:21:14.440 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:entitlement
07-12 11:21:14.440 D/GSM     ( 1227): [GsmDCT] isDataPossible(entitlement): possible=false isDataAllowed=true apnTypePossible=false apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.440 D/GSM     ( 1227): [GsmDCT] get active apn string for type:entitlement
07-12 11:21:14.440 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:dun
07-12 11:21:14.440 D/GSM     ( 1227): [GsmDCT] isDataPossible(dun): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.440 D/GSM     ( 1227): [GsmDCT] get active apn string for type:dun
07-12 11:21:14.440 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:ktmultirab2
07-12 11:21:14.440 D/GSM     ( 1227): [GsmDCT] isDataPossible(ktmultirab2): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.440 D/GSM     ( 1227): [GsmDCT] get active apn string for type:ktmultirab2
07-12 11:21:14.450 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:supl
07-12 11:21:14.450 D/GSM     ( 1227): [GsmDCT] isDataPossible(supl): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.450 D/GSM     ( 1227): [GsmDCT] get active apn string for type:supl
07-12 11:21:14.450 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:hipri
07-12 11:21:14.450 D/GSM     ( 1227): [GsmDCT] isDataPossible(hipri): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.460 D/GSM     ( 1227): [GsmDCT] get active apn string for type:hipri
07-12 11:21:14.460 E/RILC    (  341): responseLGERPInd(): param(425992(0x00068008)), data_valid(1), data_len(4)
07-12 11:21:14.460 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:tethering
07-12 11:21:14.460 D/GSM     ( 1227): [GsmDCT] isDataPossible(tethering): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.460 D/GSM     ( 1227): [GsmDCT] get active apn string for type:tethering
07-12 11:21:14.460 I/RILJ    ( 1227): LGE_UNSOL_RRC_RELEASE_CAUSE: releaseCause = 1
07-12 11:21:14.460 D/RILJ    ( 1227): returned data  = [B@43cedfa8
07-12 11:21:14.470 D/GSM     ( 1227): [GsmDCT] notifyOffApnsOfAvailability skipped apn due to isReady==false: {mApnType=ims mState=CONNECTED mWaitingApns=[[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT IMS, 477, 45005, ims, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, ims, IP, IP, true, 0 mDataConnectionAc=GsmDC-1 mReason=dataEnabled mRetryCount=0 mDataEnabled=true mDependencyMet=true}
07-12 11:21:14.470 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:usccapp
07-12 11:21:14.470 D/GSM     ( 1227): [GsmDCT] isDataPossible(usccapp): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.470 D/GSM     ( 1227): [GsmDCT] get active apn string for type:usccapp
07-12 11:21:14.470 D/GSM     ( 1227): [GsmDCT] notifyOffApnsOfAvailability skipped apn due to isReady==false: {mApnType=default mState=IDLE mWaitingApns=[[ApnSettingV2] SKT, 476, 45005, lte.sktelecom.com, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, default | mms | dun | hipri | supl | fota | cbs, IP, IP, true, 0] mWaitingApnsPermanentFailureCountDown=1 mDataProfile=[ApnSettingV2] SKT, 476, 45005, lte.sktelecom.com, , http://omms.nate.com:9082/oma_mms, smart.nate.com, 9093, 80, 0, default | mms | dun | hipri | supl | fota | cbs, IP, IP, true, 0 mDataConnectionAc=null mReason=2GVoiceCallEnded mRetryCount=0 mDataEnabled=true mDependencyMet=true}
07-12 11:21:14.470 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:vzw800
07-12 11:21:14.470 D/GSM     ( 1227): [GsmDCT] isDataPossible(vzw800): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.470 D/GSM     ( 1227): [GsmDCT] get active apn string for type:vzw800
07-12 11:21:14.480 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:mms
07-12 11:21:14.480 D/GSM     ( 1227): [GsmDCT] isDataPossible(mms): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.480 D/GSM     ( 1227): [GsmDCT] get active apn string for type:mms
07-12 11:21:14.480 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:cbs
07-12 11:21:14.480 D/GSM     ( 1227): [GsmDCT] isDataPossible(cbs): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.480 D/GSM     ( 1227): [GsmDCT] get active apn string for type:cbs
07-12 11:21:14.490 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:bip
07-12 11:21:14.490 D/GSM     ( 1227): [GsmDCT] isDataPossible(bip): possible=false isDataAllowed=true apnTypePossible=false apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.490 D/GSM     ( 1227): [GsmDCT] get active apn string for type:bip
07-12 11:21:14.490 D/GSM     ( 1227): [GsmDCT] notifyOffApnOfAvailability type:vzwapp
07-12 11:21:14.490 D/GSM     ( 1227): [GsmDCT] isDataPossible(vzwapp): possible=true isDataAllowed=true apnTypePossible=true apnContextisEnabled=false apnContextState()=IDLE
07-12 11:21:14.490 D/GSM     ( 1227): [GsmDCT] get active apn string for type:vzwapp
07-12 11:21:14.550 D/GSM     ( 1227): [GsmDCT] onReceive: action=com.skt.CALL_PROTECTION_MENU_ON
07-12 11:21:14.550 D/GSM     ( 1227): [GsmDCT] [LGE_DATA] com.skt.CALL_PROTECTION_MENU_ON
07-12 11:21:14.550 D/GSM     ( 1227): [GsmDCT] onReceive: action=com.skt.CALL_PROTECTION_MENU_ON
07-12 11:21:14.550 D/GSM     ( 1227): [GsmDCT] [LGE_DATA] com.skt.CALL_PROTECTION_MENU_ON
07-12 11:21:14.720 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4def0308000100000003
07-12 11:21:14.720 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:21:14.720 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:21:14.720 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525295
07-12 11:21:14.720 D/RILJ    ( 1227): Response ID 525295is not served in this process.
07-12 11:21:14.720 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:21:14.720 V/RILJ    ( 1227): [UNSL]< UNSOL_OEM_HOOK_RAW 5155414c434f4d4d4c0408000b00000002000d0001040000000000
07-12 11:21:14.720 D/RILJ    ( 1227): Oem ID in RIL_UNSOL_OEM_HOOK_RAW is QUALCOMM
07-12 11:21:14.720 D/RILJ    ( 1227): OEM ID check Passed
07-12 11:21:14.720 D/RILJ    ( 1227): Response ID in RIL_UNSOL_OEM_HOOK_RAW is 525388
07-12 11:21:14.720 D/RILJ    ( 1227): Response ID 525388is not served in this process.
07-12 11:21:14.720 D/RILJ    ( 1227): To broadcast an Intent via the notifier to external apps
07-12 11:21:14.720 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:21:14.730 D/RILJ    ( 1227): [11687]> OPERATOR
07-12 11:21:14.730 D/RILJ    ( 1227): [11688]> DATA_REGISTRATION_STATE
07-12 11:21:14.730 D/RILJ    ( 1227): [11689]> VOICE_REGISTRATION_STATE
07-12 11:21:14.730 D/RILJ    ( 1227): [11690]> QUERY_NETWORK_SELECTION_MODE
07-12 11:21:14.730 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:21:14.730 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:21:14.730 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:21:14.730 D/RILJ    ( 1227): [11691]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:21:14.760 D/RILJ    ( 1227): [11688]< DATA_REGISTRATION_STATE {1, 21f1, null, 3, null, 20}
07-12 11:21:14.760 D/RILJ    ( 1227): [11687]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:21:14.760 D/RILJ    ( 1227): [11689]< VOICE_REGISTRATION_STATE {1, 21f1, null, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
07-12 11:21:14.760 D/RILJ    ( 1227): responseGetModemInfo[I@43d27680
07-12 11:21:14.760 D/RILJ    ( 1227): [11691]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:21:14.760 D/RILJ    ( 1227): [11690]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:21:14.760 D/GSM     ( 1227): [EONS] Received TAC = 8689
07-12 11:21:14.760 D/GSM     ( 1227): [EONS] EVENT_POLL_STATE_GPRS newGPRSState =0 , mDataRadioTechnology =3 , mTAC =8689
07-12 11:21:14.760 D/GSM     ( 1227): [GsmSST] EVENT_POLL_STATE_REGISTRATION. mNewRadioTechnology = 3, CStype = 3
07-12 11:21:14.760 D/GSM     ( 1227): [SIMRecords] getUsimIsEmpty() 1
07-12 11:21:14.760 D/GSM     ( 1227): isOemRadTestSettingTrue : Settings.Secure.OEM_RAD_TEST = 0, phone.getPhoneType() =1
07-12 11:21:14.760 D/GSM     ( 1227): [GsmSST] Poll ServiceState done:  oldSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] newSS=[0 home SKTelecom SKTelecom 45005  UMTS CSS not supported -1 -1 mDataState=0 RoamInd=-1 DefRoamInd=-1 EmergOnly=falseDual carrier0] oldGprs=0 newData=0 oldMaxDataCalls=20 mNewMaxDataCalls=20 oldReasonDataDenied=-1 mNewReasonDataDenied=-1 oldType=UMTS newType=UMTS
07-12 11:21:14.760 I/GSM     ( 1227): Network State Changed, get EONS and update operator name display
07-12 11:21:14.760 D/GSM     ( 1227): [EONS] updateEons() lactac = 8689 , needsUpdate = true , OperatorNumeric = 45005 , Emergency Only = false
07-12 11:21:14.760 D/GSM     ( 1227): [EONS] updateEons() eonsLong = null
07-12 11:21:14.900 D/RILJ    ( 1227): [11692]> SCREEN_STATE: true
07-12 11:21:14.920 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:21:14.920 D/RILJ    ( 1227): [11692]< SCREEN_STATE 
07-12 11:21:15.090 D/RILJ    ( 1227): [11693]> OPERATOR
07-12 11:21:15.090 D/RILJ    ( 1227): [11694]> DATA_REGISTRATION_STATE
07-12 11:21:15.090 D/RILJ    ( 1227): [11695]> VOICE_REGISTRATION_STATE
07-12 11:21:15.090 D/RILJ    ( 1227): [11696]> QUERY_NETWORK_SELECTION_MODE
07-12 11:21:15.100 D/RILJ    ( 1227): [11693]< OPERATOR {SKTelecom, SKTelecom, 45005}
07-12 11:21:15.100 D/GSM     ( 1227): [LGE] getBal ModemItem.W_BASE.LGE_MODEM_INFO_SERVICE_STATUS
07-12 11:21:15.100 D/PHONE   ( 1227): PhoneBase getModemStringItem item_index = 393244
07-12 11:21:15.100 D/RILJ    ( 1227): getModemStringItem item = 393244
07-12 11:21:15.100 D/RILJ    ( 1227): [11697]> RIL_REQUEST_GET_MODEM_INFO
07-12 11:21:15.100 D/GSM     ( 1227): [GsmSST] onSignalStrengthResult() = 3
07-12 11:21:15.100 D/GSM     ( 1227): [GsmSST] set ss feature feature = 6
07-12 11:21:15.100 D/RILJ    ( 1227): responseGetModemInfo[I@43b64208
07-12 11:21:15.100 D/RILJ    ( 1227): [11697]< RIL_REQUEST_GET_MODEM_INFO {3, 0, 0, 0, 450, 0, 5, 2, 3, 5}
07-12 11:21:15.100 D/RILJ    ( 1227): [11696]< QUERY_NETWORK_SELECTION_MODE {0}
07-12 11:21:15.100 D/RILJ    ( 1227): [11694]< DATA_REGISTRATION_STATE {1, 21f1, null, 3, null, 20}
07-12 11:21:15.100 D/RILJ    ( 1227): [UNSL]< UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED
07-12 11:21:15.100 D/RILJ    ( 1227): [11695]< VOICE_REGISTRATION_STATE {1, 21f1, null, 3, null, null, null, 0, null, null, 1, null, null, 0, 31}
'''