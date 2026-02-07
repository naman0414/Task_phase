import cv2 as cv


# img=cv.imread('Task-3/sources/cat.jpeg')
# cv.imshow('Cat',img)
capture=cv.VideoCapture('Task-3/sources/vidcat.mp4')

while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()   

cv.waitKey(0)
cv.destroyAllWindows()