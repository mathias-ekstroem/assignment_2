import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import colorsys

# Loads image
image = cv2.imread('pyramid.png')
IMG = image/255

def RGB2HSI(R, G, B):
    eps = 1E-6
    if(0<=R<=255 and 0<=G<=255 and 0<=B<=255):
        d = float(R+G+B)
        r = IMG*float(R)/d # The normalzation for the RGB image needed?
        g = IMG*float(G)/d
        b = IMG*float(B)/d
        numer = float(0.5*((r-g)+(r-b)))
        denom = float(((r-g)*(r-g)+(r-b)*(g-b))*math.pow(0.5)) # when uplifting you can use ** as well!
        if(b<=g):
            h = math.acos(numer/denom+eps) # to not divide with 0  !
        if(b>g):
            h = (2*math.pi) - math.acos(numer/denom)
        s = 1 - (3*min(r,g,b))
        i = float(R+G+B)/float(3*255)
        # The HSI in corrected numbers!
        H = h*(180/math.pi)
        S = s*100
        I = i*255

    while(1):
        cv2.imshow('image', )
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break


#while(1):

    #cv2.imshow('image',image)


    #k = cv2.waitKey(5) & 0xFF
    #if k == 27:
     #   break

#cv2.destroyAllWindows()






#R = I(:,:,1)
