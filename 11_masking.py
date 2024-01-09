# masking -> focus on spicific part of image

import cv2 as cv
import numpy as np

img = cv.imread('photo/9.jpeg')
cv.imshow('img',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

circle = cv.circle(blank.copy(),(img.shape[0]//2,img.shape[1]//2-45),50,255,-1)
cv.imshow('circle',circle)

rectangle = cv.rectangle(blank.copy(),(30,30),(120,120),255,-1)
cv.imshow('rectangle',rectangle)

# masking image
masked_circle = cv.bitwise_and(img,img,mask=circle)
cv.imshow('mask',masked_circle)

masked_rectangle = cv.bitwise_and(img,img,mask=rectangle)
cv.imshow('mask_rect',masked_rectangle)

weird_shape = cv.bitwise_and(rectangle,circle)
cv.imshow('weird_shape',weird_shape)

masked_weird = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('weird_shape',masked_weird)

cv.waitKey(0)