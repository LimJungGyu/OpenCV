from string import hexdigits
import cv2

img_src = cv2.imread('images/balloon2.jpg',cv2.IMREAD_COLOR)
height , width = img_src.shape[:2]

print('w :',width,' h : ',height)

img_gray =cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)

cv2.imshow('src',img_src)
cv2.imshow('src_gray',img_gray)
cv2.waitKey()
cv2.destroyAllWindows()