# swichting between the color spaces i.e, rgb , grayscale , hsv , l*a*b

import cv2 as cv

img = cv.imread('photo/10.jpeg')
cv.imshow('img',img)

# BGR to Grayscale(Shows the distribution of pixel intensities)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

# BGR to l*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

cv.waitKey(0)