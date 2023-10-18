import cv2 as cv
import numpy as np


img= cv.imread('img/mild.jpg')
img = cv.resize(img,(300,300))
cv.imshow('mild', img)

kernel = np.ones((5,5),np.float32)/25

h_filter = cv.filter2D(img,-1,kernel) 
cv.imshow("homogeneous==",h_filter)

blur = cv.blur(img,(5,5)) #here we have image and kernel as parameter
cv.imshow("blur==",blur)

gau= cv.GaussianBlur(img,(5,5),0) #here 0 is sigma x value
cv.imshow("gau blur=",gau)

med = cv.medianBlur(img,5)
cv.imshow("median filter",med)

bi_f = cv.bilateralFilter(img,9,75,75)
cv.imshow("bi_f",bi_f)




cv.waitKey(0)