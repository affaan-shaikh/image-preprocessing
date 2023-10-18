import cv2 as cv
import numpy as np

img= cv.imread('img/mild.jpg')
img = cv.resize(img,(300,300))

img_gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('ORIGINAL', img_gray)

cv.waitKey(0)