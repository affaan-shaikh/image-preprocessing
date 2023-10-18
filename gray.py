import cv2 as cv
# import numpy as np

img= cv.imread('img/b.jpg')

cv.imshow('b', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)



cv.waitKey(0)