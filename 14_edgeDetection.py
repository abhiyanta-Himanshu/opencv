# gradients
import cv2 as cv
import numpy as np

img = cv.imread('photo/6.jpeg')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap',lap)

# sobel 
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx , sobely)

cv.imshow('Sobel X',sobelx)
cv.imshow('sobel y',sobely)
cv.imshow('sobel',combined_sobel)

# canny edge dectecter
canny = cv.Canny(gray,150,175)
cv.imshow('canny',canny)

cv.waitKey(0)