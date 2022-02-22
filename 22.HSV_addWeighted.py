#HSV
import cv2
from cv2 import COLOR_HSV2BGR

img_src =cv2.imread('images/tomato.jpg',cv2.IMREAD_COLOR)
img_hsv =cv2.cvtColor(img_src,cv2.COLOR_BGR2HSV)
img_h , img_s, img_v = cv2.split(img_hsv)
#파란색
img_h1 =  cv2.inRange(img_h,90,135)
img_blue = cv2.bitwise_and(img_hsv,img_hsv,mask=img_h1)
img_blue = cv2.cvtColor(img_blue,COLOR_HSV2BGR)
#노란색
img_h2 =  cv2.inRange(img_h,20,40)
img_yello = cv2.bitwise_and(img_hsv,img_hsv,mask=img_h2)
img_yello = cv2.cvtColor(img_yello,COLOR_HSV2BGR)
#빨간색 ---- h에서가 아니라 hsv에서 뽑아내야한다
lower_red = cv2.inRange(img_hsv, (0, 60, 80), (7, 255, 255)) #<---rgb값 아님 색상 채도 명도랑 비슷
upper_red = cv2.inRange(img_hsv, (170, 0, 0), (180, 255, 255))
added_red = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0)
img_red = cv2.bitwise_and(img_hsv,img_hsv,mask=added_red)
img_red = cv2.cvtColor(img_red,COLOR_HSV2BGR)

cv2.imshow('src',img_src)
cv2.imshow('h1',img_h1)
cv2.imshow('blue',img_blue)
cv2.imshow('yello',img_yello)
cv2.imshow('red',img_red)
cv2.waitKey()
cv2.destroyAllWindows()