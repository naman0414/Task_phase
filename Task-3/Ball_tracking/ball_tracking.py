import cv2 as cv
import numpy as np

vid=cv.VideoCapture('Task-3/Ball_tracking/Ball_Tracking.mp4')

while True:
    isTrue,frame=vid.read()

    blur=cv.GaussianBlur(frame,(11,11),0)
    hsv=cv.cvtColor(blur,cv.COLOR_BGR2HSV)

    lower_color = np.array([29, 86, 6])
    upper_color = np.array([64, 255, 255])

    mask=cv.inRange(hsv,lower_color,upper_color)

    contours,hierarchies=cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for i in contours:
        if cv.contourArea(i)>600:
            x,y,w,h=cv.boundingRect(i)
            cv.rectangle(frame,(x,y),(x+w+2,y+h+2),(255,255,0),thickness=3)


    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

vid.release()

