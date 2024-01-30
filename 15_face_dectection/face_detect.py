# haar_face.xml
import cv2 as cv

img = cv.imread('face2.jpeg')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# taking haar_face file into a variable
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# dectecting faces through haar_cascade file
face_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1 , minNeighbors=3)

# printing how many faces are there in image
print(f'number of faces found = {len(face_rect)}')

# show the faces in image
for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('detected faces',img)

cv.waitKey(0)