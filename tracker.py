import cv2
import numpy as np

trackerRunning = True

#test video capture
cam = cv2.VideoCapture(0)


_, i1 = cam.read()
i2 = i1
i3 = i1
moved = False

avg_diff = 1000 #diff threshold for movement


print "Tracker initialized correctly using OpenCV version ", cv2.__version__



#converts images to a binary threshold
def threshold(img):
    
    img = cv2.medianBlur(img,5)

    _, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    return thr1

def diff(t1, t2, t3):
    #compute diff images
    d1 = cv2.absdiff(t1, t2)
    d2 = cv2.absdiff(t2, t3)
    diffImg = cv2.bitwise_and(d1, d2)
    diffImg = cv2.cvtColor(diffImg, cv2.COLOR_RGB2GRAY)
    return diffImg

def tick():

    #pull globals
    global i1
    global i2
    global i3
    global avg_diff

    #get images
    i1 = i2
    i2 = i3
    _, i3 = cam.read()

    #threshold images
    t1 = threshold(i1)
    t2 = threshold(i2)
    t3 = threshold(i3)

    diffImg = diff(t1, t2, t3)

    #show images
    cv2.imshow("diff", diffImg)
    cv2.imshow("original", i2)

    #compute number of changed pixels and adjust weighted average
    count = cv2.countNonZero(diffImg)
    avg_diff = (avg_diff * 0.95) + (count * 0.05)

    #check for movement
    global moved
    moved = count > avg_diff * 1.3


    #wait 50
    k = cv2.waitKey(50) & 0xFF
    if k == 27:
        #user hit escape
        cv2.destroyAllWindows()
        print "Escape Key"
        global trackerRunning
        trackerRunning = False




def running():
    return trackerRunning

def movement():
    return moved


def calibrate():
    tick()
    tick()
    tick()
    count = cv2.countNonZero(diff(threshold(i1), threshold(i2), threshold(i3)))
    global avg_diff
    avg_diff = count
    print "Tracker Calibrated, diff: ", count

def save(num):
    file1 = "i1:" + str(num) + ".jpg"
    file2 = "i2:" + str(num) + ".jpg"
    file3 = "i3:" + str(num) + ".jpg"
    cv2.imwrite(file1, i1)
    cv2.imwrite(file2, i1)
    cv2.imwrite(file3, i1)
    return file1, file2, file3

def setCam(camNum):
    global cam
    cam = cv2.VideoCapture(camNum)

def wait(t):
    k = cv2.waitKey(t) & 0xFF
    return k
