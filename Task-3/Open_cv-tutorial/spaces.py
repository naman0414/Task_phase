import cv2 as cv
img=cv.imread('Task-3/sources/boston.jpeg')

cv.imshow('Boston',img)
bgr_torgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('bgrtorgb',bgr_torgb)
cv.waitKey(0)
cv.destroyAllWindows()