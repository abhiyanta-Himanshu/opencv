import cv2 as cv
import numpy as np

img = cv.imread('photo/9.jpeg')
cv.imshow('img',img)

# Averaging 
average = cv.blur(img,(3,3))
cv.imshow('average',average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img,(3,3),0)
cv.imshow('gauss',gaussian)

# median blur
median = cv.medianBlur(img,3)
cv.imshow("median",median)

# bilateral blur (most effective)
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow("bilateral",bilateral)


cv.waitKey(0)