import cv2
img_src = cv2.imread('images/rice.png',cv2.IMREAD_COLOR)
height, width = img_src.shape[:2]

img_gray =cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
kernel =(10,10)
#anchor로 중심점 잡는다 -1-1로 하면 그냥 알아서 중심점 잡아줌
img_dst = cv2.blur(img_gray,kernel,anchor=(-1,-1),borderType=cv2.BORDER_DEFAULT)
_,img_dst_thr  = cv2.threshold(img_dst,100,255,cv2.THRESH_OTSU)
_,img_gray_thr  = cv2.threshold(img_gray,100,255,cv2.THRESH_OTSU)
cv2.imshow('source',img_src)
cv2.imshow('gray',img_gray)
cv2.imshow('dst',img_dst)
cv2.imshow('result1',img_dst_thr)
cv2.imshow('result2',img_gray_thr)
cv2.waitKey()
cv2.destroyAllWindows()