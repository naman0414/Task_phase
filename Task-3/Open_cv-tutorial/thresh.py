import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Task-3/sources/cat.jpeg')
cv.imshow('Cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('simple threshold',thresh)

threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('simple threshold_inv',thresh_inv)

adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive threshold',adaptive_thresh)

adaptive_thresh_INV=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow('adaptive threshold_INV',adaptive_thresh_INV)



cv.waitKey(0)