import cv2 as cv
import numpy as np
 
# img = cv.imread('photo/9.jpeg')
# cv.imshow('img',img)

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,- 1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

# bitwise And
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise_and',bitwise_and)
# white + white -> white
# black + black -> black
# black + white -> black

# bitwise_or
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise_or',bitwise_or)
# white + white -> white
# black + black -> black
# black + white -> white

# bitwise xor
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise_xor',bitwise_xor)
# white + white -> black
# black + black -> black
# black + white -> white

# bitwise not
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise_not',bitwise_not)
# black -> white 
# white -> black

cv.waitKey(0)