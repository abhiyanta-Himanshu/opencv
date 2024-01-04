import cv2 as cv
import numpy as np

# reading an image
img = cv.imread("photo/pic.png")

# resizing the image
resized_img = cv.resize(img , (900,600) , interpolation=cv.INTER_AREA);

# display the image
# cv.imshow("4",resized_img)


# ------------ 1st way ---------
# by creating a blank image

# blank image
blank = np.zeros((500,500,3) , dtype='uint8') 
# (500,500,3) ----> (height,width,color_channels)
# dtype= uint8 ---> image i.e, 2d array of pixels
# cv.imshow("blank" , blank)
cv.waitKey(0)

# 1. Paint the whole image a certain color
blank[:] = 0,255,0

# cv.imshow("green" , blank)


# 2. Paint a section of image
# blank[200:300 , 300:400]= 225,0,0
# cv.imshow("blue" , blank)
# cv.waitKey(0)

# ----fun

# blank[0:100,0:100]=0,0,255
# blank[100:200,100:200]=0,0,225
# blank[200:300,200:300]=0,0,195
# blank[300:400,300:400]=0,0,165
# blank[400:500,400:500]=0,0,135

# blank[0:100,400:500]=255,0,0
# blank[100:200,300:400]=225,0,0
# blank[200:300,200:300]=195,0,0
# blank[300:400,100:200]=165,0,0
# blank[400:500,0:100]=135,0,0
# cv.imshow("blue" , blank)
# cv.waitKey(0)

# 3. Draw a rectangle
# cv.rectangle(blank,(0,0),(100,100),(0,0,0),thickness=2) # try thickness=cv.filled and -1
# cv.imshow("red",blank)
# cv.waitKey(0)

# 4. Draw a circle
# cv.circle(blank , (53,53),50,(250,0,0),thickness=3)
# cv.imshow("circle",blank)
# cv.waitKey(0)

# 5.Draw a line
# cv.line(blank,(200,200),(300,300),(0,0,255),thickness=2)
# cv.imshow("line",blank)
# cv.waitKey(0)

# 6. Write a text
cv.putText(blank,'TeXt',(100,100),fontFace=cv.FONT_HERSHEY_TRIPLEX,fontScale=2.0,color=(0,160,0),thickness=3)
cv.imshow("text",blank)
cv.waitKey(0)
