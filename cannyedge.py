import cv2 as cv
img= cv.imread('img/mild.jpg')
cv.imshow('MILD', img)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)