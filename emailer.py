# Import smtplib to actually send
import smtplib

# Import email module
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#setup info
USER_EMAIL = 'decamun@gmail.com'
SYSTEM_EMAIL = 'robotsentry@gmail.com'
SYSTEM_PASSWORD = 'youshallnotpass!'
SYSTEM_HOSTNAME = 'smtp.gmail.com'
SYSTEM_PORT = 465

#open SMTP connection
s = smtplib.SMTP_SSL(SYSTEM_HOSTNAME, SYSTEM_PORT)
s.login(SYSTEM_EMAIL, SYSTEM_PASSWORD)

#reset connection
def resetEmail():
    s = smtplib.SMTP_SSL(SYSTEM_HOSTNAME, SYSTEM_PORT)
    s.login(SYSTEM_EMAIL, SYSTEM_PASSWORD)

#print all setup info
def printEmailSetup():
    print '\nEmail setup:'
    print "User Email: ", USER_EMAIL
    print "System Email: ", SYSTEM_EMAIL
    print "System Hostname: ", SYSTEM_HOSTNAME
    print "System Password: ", SYSTEM_PASSWORD

#changes setup info
def init(email, host = SYSTEM_HOSTNAME, username = SYSTEM_EMAIL, password = SYSTEM_PASSWORD):
    
    global USER_EMAIL
    USER_EMAIL = email
    global SYSTEM_EMAIL
    SYSTEM_EMAIL = username
    global SYSTEM_PASSWORD
    SYSTEM_PASSWORD = password
    global SYSTEM_HOSTNAME
    SYSTEM_HOSTNAME = host

# Sends an email alert to the user.
# Params: img:(Image) text:(Text)
def sendAlert(msgtext, msgsubject, msgattch = 0):


    #make an email msg from the file
    msg = MIMEMultipart()
    
    #make text component
    txt = MIMEText(msgtext)
    msg.attach(txt)
    

    #make image component
    if not (msgattch == 0):
        img_data = open(msgattch, 'rb').read()
        img = MIMEImage(img_data, name=os.path.basename(msgattch))
        msg.attach(img)
    
    #create message header
    msg['Subject'] = msgsubject
    msg['From'] = 'robotsentry@gmail.com'
    msg['To'] = USER_EMAIL

    #send alert
    print('Sending Alert to: {}:\n{}'.format(USER_EMAIL, msgtext))
    s.sendmail(SYSTEM_EMAIL, [USER_EMAIL], msg.as_string())



    
    

    
