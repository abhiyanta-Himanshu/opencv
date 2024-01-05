import cv2 as cv

img = cv.imread('photo/4.jpeg')
cv.imshow("img",img)

# 1. Converting to greyscale
grey =cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
cv.imshow('gray',grey)


# 2. BLUR 
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
# Note : To increase blurness increase kernel (3,3)-->(7,7)


# 3. Edge Cascade --> Generate Edge on image
canny = cv.Canny(blur,125,175)
cv.imshow('canny',canny)


# 4. Dilating the image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("dilated",dilated)

# 5. Erading --> Getting the same edge back after dilated
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

# Cropping
cropped = img[50:100,50:100]
cv.imshow('cropped',cropped)

  
cv.waitKey(0)