import cv2
import cv2
from cv2 import COLOR_GRAY2BGR
#3채널 칼러
img_src=cv2.imread('images/pawn.jpg',cv2.IMREAD_COLOR)
#1채널 그레이
img_gray=cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)
#3채널 그레이로 변환
img_gray_bgr= cv2.cvtColor(img_gray,COLOR_GRAY2BGR)

img_dst = img_src.copy()
h1=185; h2=620
w1=35; w2=230
img_dst[h1:h2,w1:w2,:]=img_gray_bgr[h1:h2,w1:w2,:]
img_dst[255:610,325:482,:]=img_gray_bgr[255:610,325:482,:]
img_dst[325:600,582:730:]=img_gray_bgr[325:600,582:730,:]
cv2.imshow('src',img_src)
cv2.imshow('gray',img_gray)
cv2.imshow('dst',img_dst)

cv2.waitKey()
cv2.destroyAllWindows()