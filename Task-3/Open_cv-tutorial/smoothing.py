import cv2 as cv
import numpy as np

img=cv.imread('Task-3/sources/cat.jpeg')
cv.imshow('cat',img)

bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('blur',bilateral)


cv.waitKey(0)