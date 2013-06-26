import email
import smtplib
import time
import base64
import cStringIO

def sendMail(server,fro,to, subject, text):
    

    msg=email.Message.Message()
    msg['From']=fro 
    msg['Subject'] = subject
    msg['To'] =to
    msg['Date']=time.ctime()

    body=email.MIMEText.MIMEText(text)
    server=smtplib.SMTP_SSL(server)
    print "Connected to Server!"
    server.login('*******@gmail.com','*******')
    print "You have log in"
    server.sendmail(fro,to,msg.as_string()[:-1]+body.as_string())
    print "Email have been sent"
    server.quit()
    print "You have disconnected from server"



#sendMail('smtp.gmail.com','sender@gmail.com','receiver@gmail.com','Greet','Nice to meet you')
