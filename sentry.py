#import code to send email alerts
from emailer import sendAlert, init, printEmailSetup, resetEmail

#import code to say things
from speaker import say

#import code to detect motion
import tracker

#import code for password input
from input_timed import readInput
import getpass
import time

USER_PASSWORD = "robats"

def man_init():
    user_email = raw_input('What is your email addess? ')
    user_input = raw_input('Would you like to configure outgoing email as well? If you \nuse the default, email will be sent from RobotSentry@gmail.com.\n(y/n)')
    if(user_input == 'y'):
        system_hostname = raw_input('What is your hostname? ')
        system_login = raw_input('What is your host login? (same as email) ')
        system_password = raw_input('What is your host password? ')
        init(user_email, system_hostname, system_login, system_password)
    else:
        init(user_email)
    global USER_PASSWORD
    getpassword = True
    while getpassword:
        password = getpass.getpass("Enter a password")
        if(getpass.getpass("please re-enter it:") == password):
            USER_PASSWORD = password
            getpassword = False
        else:
            print "Sorry, those two didn't match"
        
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

e = raw_input("Press enter to calibrate motion tracker...\n(make sure nothing is moving onscreen)")
tracker.calibrate()

print "\nInitiation Complete:\n\ntracker running..."

tickcount = 0
movecount = 0

while tracker.running():
    #Robot Sentry Main Loop
    tickcount += 1    
    tracker.tick()

    if tracker.movement():
        #Movement Detected
        print 'detected movement... ', movecount
        movecount += 1

        if movecount > 3:
            file1, file2, file3 = tracker.save(tickcount)
            movecount = 0
            seconds = 5
            say("Intruder Alert! Intruder Alert! You have " + str(seconds) + " seconds to enter your passcode")
            pw = readInput("Password: ", "not the password", seconds)
            if not pw == USER_PASSWORD:
                print "Intruder Detected! Sending alert!"
                sendAlert("Intruder. Systime: " + str(time.time()), "Intruder", file2)
    else:
        if movecount > 0:
            movecount -= 1
        

#exit
print 'Exiting... '
say('goodbye')
sendAlert('Robot Sentry has stopped', 'Exit Notice')
