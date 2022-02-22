
import cv2

img_src = cv2.imread("images/lol_r.jpg",cv2.IMREAD_COLOR)
height, width = img_src.shape[:2]

##회전###
center = (width/2,height/2) #회전할 이미지의 중심점(가로,세로의 중간)
rotation_angle = 90         #회전할 각도
scale = 1                   #확대/축소 비율
matrix = cv2.getRotationMatrix2D(center,rotation_angle,scale)
###결과영상
img_dst =cv2.warpAffine(img_src,matrix,(width,height))

cv2.imshow("source",img_src)
cv2.imshow("result",img_dst)
cv2.waitKey()
cv2.destroyAllWindows()