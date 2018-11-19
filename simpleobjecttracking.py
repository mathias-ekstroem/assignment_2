import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('pyramid.png')
#plt.hist(image.ravel(),256, [0,256]); plt.show()


    # Convert BGR to HSV
    #hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    #lower_red = np.array([110,40,40])
    #upper_red = np.array([240,255,255])

    # Threshold the HSV image to get only blue colors
    #mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(image,image, mask= mask)

cv2.imshow('image',image)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()