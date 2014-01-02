#import code to send email alerts
from emailer import sendAlert, init
from speaker import say



text = open('test.txt', 'rb')
img = open('trollface.jpg', 'rb')
txt = str(text.read())
sendAlert(txt, img)
say(txt)
text.close()
