import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),(255),thickness=-1)
circle=cv.circle(blank.copy(),(200,200),200,(255),thickness=-1)
cv.imshow('circle',circle)
cv.imshow('rectangle',rectangle)



bitwise_or=cv.bitwise_or(circle,rectangle)
cv.imshow("or",bitwise_or)
bitwise_and=cv.bitwise_and(circle,rectangle)
cv.imshow("and",bitwise_and)
cv.waitKey(0)