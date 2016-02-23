# _*_ coding: utf-8 _*_

'''
Created on 2012. 7. 6.

@author: jaehyek
'''


symptomtablestatement = "select symptom_cd, symptom_name from dmm_symptom_info"
dictsymptomcodetable = {}

def initializeMLTSymptomInfo( cur ):
    global symptomtablestatement, dictsymptomcodetable
    cur.execute(symptomtablestatement)
    listdictsymptominfos = cur.fetchall()
    print "len(listdictsymptominfos) : ", len(listdictsymptominfos)
    for dictsymptominfos in listdictsymptominfos:
        dictsymptomcodetable[dictsymptominfos["symptom_cd"]] = dictsymptominfos["symptom_name"]


def mapSymptomCodeToName( code ):
    return dictsymptomcodetable.get( code, "None" )













