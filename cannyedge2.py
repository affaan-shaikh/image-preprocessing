import cv2 as cv

img= cv.imread('img/mild.jpg')
img=cv.resize(img, (300,300))

cv.imshow('MILD', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 100, 200)
cv.imshow('Canny', canny)


cv.waitKey(0)




# img= cv.imread('img/mild.jpg')
# img=cv.resize(img, (300,300))
# gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# def nothing(x):
#     pass

# cv.namedWindow('canny')
# cv.createTrackbar('Threshold','canny',0,255,nothing)

# while True:
#     a= cv.getTrackbar('Threshhold','canny')
#     print(a)
#     res=cv.Canny(img_gray,a,255)
#     cv.imshow("Canny",res)
#     k=cv.waitKey(1) & 0xFF
#     if k == 27:
#         break
         

# cv.destroyAllWindows()