import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import colorsys
#import PIL import Image



# Loads image
image = cv2.imread('pyramid.png')
IMG = image/255

# Get the image width & height of each pixel
[xs, ys] = IMG.file.size
max_intensity=100
hues = {}

# Examine each pixel in the image
for x in xrange(0, xs):
    for y in xrange(0, ys):

# Get RGB value of each pixel
        [R, G, B] = IMG[x, y]



def RGB2HSI(R, G, B):
    eps = 1E-6
    if(0<=R<=255 and 0<=G<=255 and 0<=B<=255):
        d = float(R+G+B)
        r = IMG*float(R)/d # The normalization for the RGB image needed?
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

# Calling the RGB2HSI function to convert the colors
 [H, S, I] =  RGB2HSI(R, G, B)

cv2.imshow('image', IMG)
cv2.waitKey(0)

cv2.destroyAllWindows()

