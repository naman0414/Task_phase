import cv2 as cv
img=cv.imread('Task-3/sources/group.jpg')
cv.imshow('person',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade=cv.CascadeClassifier('Task-3/haar_face.xml')

face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

print('no. of faces:',len(face_rect))

for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=3)

cv.imshow('detected_img',img)

cv.waitKey(0)