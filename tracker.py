import cv2
import numpy as np

trackerRunning = True

#test video capture
cap = cv2.VideoCapture(0)
#set the width and height
cap.set(3,1280)
cap.set(4,1024)

lastimg = cap.read()
img = cap.read()

print "Tracker initialized correctly using OpenCV version ", cv2.__version__

def tick():
    
    ret, img = cap.read()
    
    cv2.imshow("input", img)

def running():
    return trackerRunning

def movement():
    return False

def setCam(cam):
    global cap
    cap = cv2.VideoCapture(cam)
