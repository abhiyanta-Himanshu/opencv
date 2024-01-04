import cv2 as cv;

def rescaleFrame(frame,scale=0.75):        # frame --> is a array we can say image
    # this method is for image , video ,live video.
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)


def changeRes(width , height):
    #only works for live video
    cap.set(3,width)
    cap.set(4,height)
    

#-----image resizing-------
img = cv.imread('photo/4.jpeg');
cv.imshow("2",img);

img_resize = rescaleFrame(img,1.7);
cv.imshow('resize2',img_resize);

cv.waitKey(0);

#----video resizing-------

cap = cv.VideoCapture("video/carVideoForAnnotation.mp4")
print(cap.isOpened)

while cap.isOpened :
    isTrue, frame = cap.read();

    frame_resized = rescaleFrame(frame,0.75);

    cv.imshow("video",frame)
    cv.imshow("resized_video",frame_resized)

    if cv.waitKey(150) == ord('d') :
        break

cap.release();
cv.destroyAllWindows();