import cv2

img_src=cv2.imread('images/shape.png',cv2.IMREAD_COLOR)
height , width = img_src.shape[:2]
print('h:',height,'w:',width)
##################################################################

### 1. 영상을 gray로 변환
img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)
### 2. gray영상을 이진화(내가 검출하려고 하는 것을  white(255)로 추출)
_,img_bin = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY_INV)

######################################################################
### 3. 흰색으로 추출된 객체(들) 의 외곽선 추출(findContours)
#ccomp는 계층구조가 존재한다는 것(2단계까지)  /chain_approx_none은 모든 외곽선을 추출하는것
contours,hierarchy=cv2.findContours(img_bin,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
######################################################################
# for i,contour in enumerate(contours):
#     cv2.drawContours(img_src,[contour],0,(0,255,0),2)
#     cv2.putText(img_src,str(i),tuple(contour[0][0]),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),1)
for i,contour in enumerate(contours):
    cv2.drawContours(img_src, contour,i, (0, 0, 255), 2)
    cv2.putText(img_src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    
    cv2.imshow('src',img_src)
    cv2.waitKey()
cv2.imshow('src',img_src)
cv2.imshow('gray',img_gray)
cv2.imshow('bin',img_bin)
cv2.waitKey()
cv2.destroyAllWindows()