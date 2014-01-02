#import code to send email alerts
from emailer import sendAlert, init, printEmailSetup, resetEmail

#import code to say things
from speaker import say

#import code to detect motion
import tracker

def man_init():
    user_email = raw_input('What is your email addess? ')
    tracker.setCam(raw_input('What camera would you like to use? (integrated is usually "0"' ))
    user_input = raw_input('Would you like to configure outgoing email as well? If you \nuse the default, email will be sent from RobotSentry@gmail.com.\n(y/n)')
    if(user_input == 'y'):
        system_hostname = raw_input('What is your hostname? ')
        system_login = raw_input('What is your host login? (same as email) ')
        system_password = raw_input('What is your host password? ')
        init(user_email, system_hostname, system_login, system_password)
    else:
        init(user_email)
        
#initialize
print '\nWelcome to Robot Sentry'
user_input = raw_input('Would you like to use default settings? (y/n) ')
while(user_input == 'n'):
    man_init()
    printEmailSetup()
    user_input = raw_input('Does that look right?')
    if not user_input == 'n':
        resetEmail()
        text = open('init.txt', 'rb')
        subj = 'Initiation Complete'
        txt = str(text.read())
        sendAlert(txt, subj)
        say(txt)
        text.close()


while tracker.running():
    #Robot Sentry Main Loop

    tracker.tick()

    if tracker.movement():
        #Movement Detected
        print 'detected movement... '
        

#exit
print 'Exiting... '
say('goodbye')
sendAlert('Robot Sentry has stopped', 'Exit Notice')
