import cv2 as cv;

#-----------------------Image Section---------------------------

#taking image in  a variabe 
img = cv.imread("photo/5.jpeg");

# #display image
cv.imshow("cat",img); # cat --> here denotes the name of the frame

# #To hold the display screen
cv.waitKey(0); # 0 -> stands for infinte time 


#-----------video section------------

#reading videos
capture = cv.VideoCapture('video/ChickenDataset.mp4');

while True:
    isTrue,frame = capture.read(); # cap.read --> returns a tuple containing two value (True , array_here)
    # 1. boolean value --> if frame capture correctly
    # 2. array --> frame captured

    cv.imshow('video',frame)  # cv.imshow --> used to display the frame i.e., the frame is array 

    if (cv.waitKey(30) & 0xFF)==ord('d'): # cv.waitkey --> returns the value pressed by keyboard & is the bitwise and operator that 
        # when operated with 0xff(255 or 11111111)returns the value it is operated 
        #note the behaviour of waitkey is chamged you can directly use cv.waitkey(..) == ord('d)
        break

capture.release();
cv.destroyAllWindows();