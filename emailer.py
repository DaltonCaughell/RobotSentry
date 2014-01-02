# Import smtplib to actually send
import smtplib

# Import email module
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#setup info
USER_EMAIL = 'decamun@gmail.com'
SYSTEM_EMAIL = 'robotsentry@gmail.com'
SYSTEM_PASSWORD = 'youshallnotpass!'
SYSTEM_HOSTNAME = 'smtp.gmail.com'

#changes setup info
def init(email, host = SYSTEM_HOSTNAME, username = SYSTEM_EMAIL, password = SYSTEM_PASSWORD):
    USER_EMAIL = email
    SYSTEM_EMAIL = username
    SYSTEM_PASSWORD = password
    SYSTEM_HOSTNAME = host

# Sends an email alert to the user.
# Params: img:(Image) text:(Text)
def sendAlert(msgtext, msgimg):

    #make an email msg from the file
    msg = MIMEMultipart()
    
    #make text component
    txt = MIMEText(msgtext)

    #make image component (not working yet!)
    #img = MIMEImage(str(msgimg.read()))
    msgimg.close()

    #build message
    msg.attach(txt)
    #msg.attach(img)

    #create message header
    msg['Subject'] = 'Intruder Alert!'
    msg['From'] = 'robotsentry@gmail.com'
    msg['To'] = USER_EMAIL

    #open SMTP connection
    s = smtplib.SMTP_SSL(SYSTEM_HOSTNAME)
    s.login(SYSTEM_EMAIL, SYSTEM_PASSWORD)

    #send alert
    print('Sending Alert to: {}: \nAlert: \n{}'.format(USER_EMAIL, msgtext))
    s.sendmail(SYSTEM_EMAIL, [USER_EMAIL], msg.as_string())
    s.quit()



    
    

    
