#사진 불러오기 >>
from turtle import width
import cv2

#상대경로
img_src = cv2.imread('images/balloon2.jpg',cv2.IMREAD_COLOR) #경로의 그림을 칼러로 읽어드려서 변수로
#절대경로
#img_src = cv2.imread('D:\coding\openCV\opencv_space\images\balloon2.jpg',cv2.IMREAD_COLOR)

print(img_src.shape)

# height, width  = img_src.shape[:2] #크기 정보만
# print(height,width)
height, width , channel  = img_src.shape[:2] #칼라 영상일때 에러 없음
print(height,width,channel)
cv2.imshow("src",img_src)
cv2.waitKey()
cv2.destroyAllWindows()
