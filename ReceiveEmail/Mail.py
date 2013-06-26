import imaplib
import email
import base64
import config
import re

class myMail:

    fro=''
    header=''
    content=''
    trackNumber=''
    content_charset=''
    emailAddress=[]

    def processFROM(self):
        try:
            pattern=re.compile(r'\w+(\.\w+)*@\w+(\.\w+)+')
            match=pattern.search(self.fro)
            self.fro=match.group()
        except:
            print "Unexcepted regular expression"
            pass

    def processContent(self):
        try:
            pattern=re.compile(r'\w+[-]?\w+\.\w+(?=\.wscdns\.com\.?)|\w+[-]?\w+\.\w+(?=\.lxdns\.com\.?)|\w+[-]?\w+\.\w+(?=\.cdn20\.com\.?)')
            self.emailAddress=list(set(pattern.findall(self.content.decode("base64"))))
        except:
            print "Unexcepted regular expression"
            pass

    
        
    

