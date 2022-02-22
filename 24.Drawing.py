#drawing
import cv2
import numpy as np

img_src = np.zeros((600,800,3),dtype=np.uint8)
height,width = img_src.shape[:2]

#직선 -대각선
cv2.line(img_src,(0,0),(800,600),(255,0,0),3)
cv2.line(img_src,(0,600),(800,0),(0,0,255),3)

#원그리기
center_point = (int(width/2),int(height/2))
cv2.circle(img_src,(center_point),50,(255,255,0),-1)  #선굵기 -1 은 채우기
cv2.circle(img_src,(center_point),100,(255,0,255),3)
cv2.circle(img_src,(center_point),150,(0,255,255),3)

#사각형그리기
cv2.rectangle(img_src, (200,150),(600,450),(0,255,255),1)
cv2.rectangle(img_src, (267,200),(533,400),(255,0,255),1)
cv2.rectangle(img_src, (332,250),(468,350),(255,255,0),1)

#타원그리기 (x축 반지름:10,y축 반지름: 200 노란색 타원)
cv2.ellipse(img_src,center_point,(10,200),45, 0,360,(0,255,255),2) #45도 시계방향으로 회전

#타원그리기2 (x축 반지름:200,y축 반지름: 100 녹색 타원)
cv2.ellipse(img_src,center_point,(200,10),0, 0,360,(0,255,0),2)
#원
cv2.circle(img_src,center_point,200,(0,0,255),1)
#호 그리기 x축 반지름 200 y축반지름 200 0도
cv2.ellipse(img_src,center_point,(300,300),0, 0,90,(0,0,255),2)

cv2.imshow('src',img_src)
cv2.waitKey()
cv2.destroyAllWindows()