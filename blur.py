# blur

import cv2 as cv


img= cv.imread('img/b.jpg')

cv.imshow('b', img)
blur= cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

cv.waitKey(0)