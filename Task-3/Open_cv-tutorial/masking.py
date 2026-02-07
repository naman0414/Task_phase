import cv2 as cv
import numpy as np

img=cv.imread('Task-3/sources/cat.jpeg')
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('cat',img)
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),(255),thickness=-1)
circle=cv.circle(blank.copy(),(1200,500),200,(255),thickness=-1)
cv.imshow('circle',circle)
cv.imshow('rectangle',rectangle)

masked=cv.bitwise_and(img,img,mask=circle)
cv.imshow('masked',masked)

cv.waitKey(0)