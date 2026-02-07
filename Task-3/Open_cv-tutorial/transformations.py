import cv2 as cv
img=cv.imread('Task-3/sources/boston.jpeg')
cv.imshow('boston',img)

def rotate(img,angle,rotPoint=None):
    height,width=img.shape[0:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)  

    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,-45)
cv.imshow('Rotated',rotated)


resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resize',resized)

flip=cv.flip(img,-1)
cv.imshow('flip',flip)

cropped=img[200:400,300:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)
cv.destroyAllWindows()