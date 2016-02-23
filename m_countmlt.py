#!/usr/bin/python
# 출력파일에서  처리한 IMEI의 개수를 count한다.
import glob
import sys

total = 0 

model_list = [ "F180L", "F180K", "F180S", 
        "F200L", "F200K", "F200S", 
        "F240L", "F240K", "F240S", 
        "F220K", "F260S" ]

dictmodel = dict(zip(model_list, [0 for k in  model_list]))

flist = glob.glob("*.txt")
for filename in flist : 
    f = open(filename, "r")
    lines = f.readlines()
    fcount = int(lines[-1].split("=")[1] )
    total += fcount 
    f.close()
    for model_name in model_list : 
        if model_name in filename : 
            dictmodel[model_name] += fcount 

print dictmodel 
print "total count : %s" % total 

