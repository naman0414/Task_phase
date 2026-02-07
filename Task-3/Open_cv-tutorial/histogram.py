import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Task-3/sources/cat.jpeg')
cv.imshow('Cat',img)
blank=np.zeros(img.shape[0:2],dtype='uint8')

circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0//2]-600),200,255,-1)
cv.imshow('circle',circle)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

mask=cv.bitwise_and(img,img,mask=circle)
cv.imshow('masked',mask)

# gray_hist=cv.calcHist([mask],[0],circle,[256],[0,256])

# plt.figure()
# plt.xlabel('Bins')
# plt.ylabel('No. of pixels')
# plt.title('GRayscale_histogram')
# plt.plot(gray_hist)
# plt.xlim(0,256)
# plt.show()

colours=('b','g','r')
plt.figure()
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
plt.title('Colour_histogram')
for i,cols in enumerate(colours):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=cols)
    plt.xlim(0,256)

plt.show()
cv.waitKey(0)