from SimpleCV import Camera, Display, Image
import time

cam = Camera()
 

while(True):
    img = cam.getImage()
    img.show()
