# three color channels red,blue,green

import cv2 as cv
import numpy as np

img = cv.imread('photo/7.jpeg')
cv.imshow('img',img)

# spiliting the color channel
b,g,r = cv.split(img) 
# b -> blue image (light where blue pixels present and dark where blue pixel not present)
# g -> green image
# r -> red image
# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)

# merge image
merged = cv.merge([b,g,r])
cv.imshow('merged image',merged)

# constructing image through blank image
blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

# img.shape[:2] -> (width,height)
# img.shape -> (width,height,color_channels)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)

cv.waitKey(0)