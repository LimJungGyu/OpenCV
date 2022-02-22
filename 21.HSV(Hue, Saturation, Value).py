#HSV
import cv2

### img_src : BGR 색 좌표계
img_src=cv2.imread('images/tomato.jpg',cv2.IMREAD_COLOR)
### RGB(BGR) --> HSV 색 좌표계로 변환
img_hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)
### HSV 색 좌표계 영상을 h,s,v로 분리(split)
img_h , img_s , img_v = cv2.split(img_hsv)
### 어떤 특정한 칼라를 뽑아내기
img_h1 = cv2.inRange(img_h,7,22)  ##주황색 부분만 출력

### HSV에서 주황색영역을 추출한 영상
img_orange = cv2.bitwise_and(img_hsv,img_hsv,mask=img_h1)

### HSV ---> BGR 로 색변환
img_orange = cv2.cvtColor(img_orange,cv2.COLOR_HSV2BGR)

cv2.imshow('src',img_src)
cv2.imshow('h',img_h)
cv2.imshow('h1',img_h1)
cv2.imshow('result',img_orange)
# cv2.imshow('s',img_s)
# cv2.imshow('v',img_v)
cv2.waitKey()
cv2.destroyAllWindows()