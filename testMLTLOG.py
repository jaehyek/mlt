# _*_ coding: utf-8 _*_

'''
Created on 2012. 8. 2.

@author: jaehyek
'''

import MltDBDump as dump
import sample



def main():
    strlog = sample.strlog
    dicttemp =  dump.getDictRilLogCause(strlog)
    print dicttemp 


if __name__ == "__main__":
    main()