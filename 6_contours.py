# contour are the edges of the image

import cv2 as cv 
import numpy as np

img = cv.imread('photo/7.jpeg')
cv.imshow('img',img)

# Creating a blank image
blank = np.zeros((img.shape[0],img.shape[1],3),dtype='uint8')
cv.imshow('blank',blank)

# converting bgr inage to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# Converting Gray image to blur image
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# Finding the edge of blur image
canny = cv.Canny(blur,125,175)
cv.imshow("canny",canny)

# ---------- Threshold function to find edge of img -------------
ret , thres = cv.threshold(gray , 125 , 255 , cv.THRESH_BINARY)
cv.imshow('thres' , thres)
# Will learn threshold funtion later but it is used to binaries the image.

# -------- Contour Detection -----------
# In open CV the contour are detected using the findcontour function
# This function returns two value contours and hierarchies
# contours , hierarchies = cv.findContours("edges" ,"mode" , "apporimation method")
# contours -> python list which includes coordinates of all contour
# hierarchies -> used by opencv to find the contours.
# Let's see these arguments 
# edges -> the frame(img) is passes in which edges is find.
# mode -> there are several modes of finding contours i.e, cv.RETR_TREE (for all hierarchical tree) , cv.RETR_EXTERNAL (return s only external contour) , cv.RETR_LIST (for all contour in image)
# contour approximation method -> cv.CHAIN_APPROX_NONE , cv.CHAIN_APPROX_SIMPLE . 

contours , hierarchies = cv.findContours(thres,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found in the image')


# ------- draw contour on a blank image ----------
cv.drawContours(blank , contours , -1, (0,0,255),1)
# blank -> frame on which contours are to be drawn
# contours -> list of coordinates of contour
# (no. f contours to be drawn)-1 -> shows all contour
# (0,0,255) -> color of line
# thickness -> 1 
cv.imshow('Contour drawn',blank)

cv.waitKey(0)