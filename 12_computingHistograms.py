# Histograms repersents the distribution of pixel intensities(color or grayscale) in a image 

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img = cv.imread('photo/9.jpeg')
cv.imshow('img',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

# gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# mask
circle = cv.circle(blank,(img.shape[1]//2+30,img.shape[0]//2-15),55,255,-1)
# cv.imshow('circle',circle)

# mask = cv.bitwise_and(gray,gray,mask=circle)
# cv.imshow('mask',mask)

# # grayscale histogram
# gray_hist = cv.calcHist([gray] , [0] , mask , [256] , [0,256])

# plt.figure()
# plt.title('GrayScale Histogram')
# plt.xlabel('bins')
# plt.ylabel('% of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

 
# color histogram
plt.figure()
plt.title('color Histogram')
plt.xlabel('bins')
plt.ylabel('% of pixels')
colors = ('b', 'g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],circle,[256],[0,256])
    # in color histogram mask is allow of binary color channels.
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)