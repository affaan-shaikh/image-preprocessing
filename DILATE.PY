import cv2 as cv
img= cv.imread('img/mild.jpg')
cv.imshow('MILD', img)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

#DILATING THE IMAGE :
dilated= cv.dilate(canny, (7,7), iterations=3)
cv.imshow('DILATED', dilated)
cv.waitKey(0)