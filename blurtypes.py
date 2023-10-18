import cv2 as cv

img= cv.imread('img/mild.jpg')

cv.imshow('mild', img)


#Avg blur
average= cv. blur(img, (3,3))
cv.imshow('AVG', average)

#Gaussin
gauss= cv.GaussianBlur(img, (3,3), 0)
cv.imshow('GAUSSIAN', gauss)

#MEDIAN
median= cv.medianBlur(img, (3), 0)
cv.imshow('MEDIAN', median)


#BILATERAL
bilateral= cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('BILATERAL', bilateral)


cv.waitKey(0)