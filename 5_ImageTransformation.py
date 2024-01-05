import cv2 as cv
import numpy as np

img = cv.imread('photo/6.jpeg')
cv.imshow("img",img)

# Translation --> shifting image about x-axis and y-axis.
def translate(img, x, y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    cv.imshow('transmat',transmat)
    dimension = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img,transmat,dimension)
    # -x ---> left
    # -y ---> up
    #  x ---> right
    #  y ---> down

translated = translate(img , -100 , 100)
cv.imshow('translated',translated)

# Rotation
def rotate(img, angle , rotPoint=None):
    (height,width) = img.shape[:2] # [:2] -> [0:2] i.e, [0],[1]
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint , angle ,1.0)
    dimension = (width,height)
    
    return cv.warpAffine(img,rotMat,dimension)

rotated = rotate(img,45)
cv.imshow("rotated",rotated)

rotated_rotated = rotate(img,-45)
cv.imshow("rotated_rotated",rotated_rotated)


# Flip Image
flip = cv.flip(img , 1)
# 1 --> horizontally or y-axis
# 0 --> vertically or x-axis
# -1 -> both horizontally and vertically
cv.imshow("flip",flip)

# cropping
crop = img[0:50,50:100]
cv.imshow("crop",crop)

cv.waitKey(0)