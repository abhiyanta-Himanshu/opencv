import cv2 as cv
import numpy as np

img = cv.imread('photo/6.jpeg')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# simple thresholding
threshold , thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY)
# thresh --> threshloded image
# threshold --> (100) thresholded value u pass
cv.imshow('simple Threshold', thresh)
# Simple threshold take two value and convert these range to black (100,255)


# Adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive thresh',adaptive_thresh)
# adaptive thrshold take a mean and subtract it from value

cv.waitKey(0)