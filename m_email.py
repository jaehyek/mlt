# -*- coding: utf-8 -*-
"""
Created on Tue Oct 08 09:53:39 2013

@author: jaehyek.choi
"""

import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def send_mail(send_from, send_to, subject, text, files=[], server="lgekrhqmh01.lge.com"):
    assert type(send_to)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
    print "Eamil Sending Complete ...."
    
    
import  argparse
if __name__ == "__main__":
    
    ffrom = ""
    to = ""
    subject = ""
    contents = ""
    files = ""
    svr = "lgekrhqmh01.lge.com"
    
    cmdlineopt = argparse.ArgumentParser(description='send email with attachment')
    cmdlineopt.add_argument('-f', action="store", dest="ffrom", default="",  help='from sender , default="" ' )
    cmdlineopt.add_argument('-t', action="store", dest="to",  default="", help='to receiver  default= "" ' )
    cmdlineopt.add_argument('-s', action="store", dest="subject",  default="", help='mail subject  default= "" ' )
    cmdlineopt.add_argument('-c', action="store", dest="contents",  default="", help='mail contents  default= "" ' )
    cmdlineopt.add_argument('-l', action="store", dest="files",  default="", help='mail attachment  default= "" ' )
    cmdlineopt.add_argument('-svr', action="store", dest="svr",  default="", help='mail server to send  default= lgekrhqmh01.lge.com ' )

    cmdlineresults = cmdlineopt.parse_args()
    ffrom = cmdlineresults.ffrom
    to = cmdlineresults.to
    subject = cmdlineresults.subject
    contents = cmdlineresults.contents
    files = cmdlineresults.files
    svr = cmdlineresults.svr
    
    to = to.split()
    files = files.split()
    
    try :
        send_mail( ffrom, to, subject, contents, files, svr )
    except:
        print "Eamil Sending Error .... " 
        import traceback

        strReportFileName = "ErrorEmail_log.txt"
        f = open(strReportFileName, "w")
        f.write( traceback.format_exc() )

        f.close()
        
        
    
    
    
    
