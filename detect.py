import cv2 as cv

img= cv.imread('img/mild.jpg')

cv.imshow('MILD', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haarcascade= cv.CascadeClassifier('img.jpg')

faces_rect = haarcascade.detectMultiScale(gray, 
scalefactor=1.1, minNeighbours=3)
print(f'Ans=  {len(face_rect)}')

cv.waitKey(0)