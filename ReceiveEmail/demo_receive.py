#import sys
#sys.path.append('/.../ReceiveEmail')
import imaplib
import email
import base64
import config
import threading
import Mail

class InBox:

    mailAmount=0
    emails=[]
    __conn=None
    
    def getAccountOnline(self):

        

        self.__conn=imaplib.IMAP4_SSL(config.host,993)
        self.__conn.login(config.username,config.password)
        print 'You have log in successfully\n'
        print 'receiving mails'
        #self.emails.append(self.__getMail())

    def getAccountOffline(self):

        try:
            t.cancel()
            self.__conn.close()
        except:
            pass
            t.cancel()
        self.__conn.logout()


    def getMail_15(self):
        global t
        self.emails.append(self.__getMail())
        t=threading.Timer(900.0,self.getMail_15)
        t.start()

    def getMail_30(self):
        self.emails.append(self.__getMail())
        t=threading.Timer(1800.0,self.getMail_30)
        t.start()

    def getMail_1h(self):
        self.emails.append(self.__getMail())
        t=threading.Timer(3600.0,self.getMail_1h)
        t.start()

    

        
    

    def __getMail(self):

        def extract_body(payload):
            if isinstance(payload,str):
                return payload
            else:
                    return '\n'.join([extract_body(part.get_payload()) for part in payload])
    

        
        #__conn=imaplib.IMAP4_SSL(config.host,993)
        #__conn.login(config.username,config.password)
        self.__conn.select()
        typ, data=self.__conn.search(None, 'UNSEEN')
        index = data[0].split()
        print index
        self.mailAmount=self.mailAmount+len(index)
        mails=[]
        i=0
        try:
            for num in index:
                
                
                mails.append(Mail.myMail())
                typ,msg_data=self.__conn.fetch(num, '(RFC822)')
                
                for response_part in msg_data:
                    if isinstance(response_part,tuple):
                        msg=email.message_from_string(response_part[1])
                        mails[i].trackNumber=num
                        mails[i].fro=msg['from']
                        subject=msg['subject']
                        print i 
                        mails[i].header=email.Header.decode_header(subject)[0][0]                        
                        payload=msg.get_payload()
                        body=extract_body(payload)
                        type=msg.get_content_charset()
                        mails[i].content_charset=type
                        print type
                        if type==None:
                            mails[i].content=body
                        else:
                            mails[i].content=body.decode("base64")
                i=i+1

            return mails
            typ,response=__conn.store(num,'+FLAGS',r'(\Seen)')
        finally:
            try:
                print "Done"
            except:
                pass
            
