# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:07:07 2013

@author: jaehyek.choi
"""
import m_email


f = open("bodymsg.txt", "r")
listmsg = f.readlines()
f.close()

m_email.send_mail("jaehyek.choi@lge.com", ["jaehyek.choi@lge.com"], listmsg[0],
                  "\n".join(listmsg[1:]), [])