import cv2 as cv
# import numpy as np

img= cv.imread('img/mild.jpg')

cv.imshow('MILD', img)
resize= cv.resize(img, (512,512))
cv.imshow('RESIZE', resize)
cv.waitKey(0)