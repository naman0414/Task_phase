import cv2 as cv
img=cv.imread('Task-3/sources/boston.jpeg')
cv.imshow('boston',img)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur=cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#edge cascade
canny=cv.Canny(blur,125,75)
cv.imshow('canny',canny)

dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilated',dilated)

eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('erode',eroded)

resize=cv.resize(img,(500,500),cv.INTER_AREA)
cv.imshow('rsx',resize)

crop=img[50:200,200:400]
cv.imshow('cropped',crop)
cv.waitKey(0)
cv.destroyAllWindows()