import cv2 as cv

img=cv.imread('Task-3/sources/cat.jpeg')
cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.75):
    #method for img,video and live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeres(width,height):
        #only for live video
        capture.set(3,width)
        capture.set(4,height)


resized_img=rescaleFrame(img,scale=0.2)
cv.imshow('Cat_resized',resized_img)

#reading videos
capture=cv.VideoCapture('Task-3/sources/vidcat.mp4')

while True:
    isTrue,frame=capture.read()

    frame_resized=rescaleFrame(frame,scale=0.2)
    cv.imshow('Video',frame)
    cv.imshow('video,resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()   

cv.waitKey(0)
cv.destroyAllWindows()