import cv2
#image load
img_src = cv2.imread('images/balloon2.jpg',cv2.IMREAD_COLOR)
height, width = img_src.shape[:2]  #이미지의 크기정보 얻어오기

#이미지 크기조절(*2, /2)
img_dst1 =cv2.pyrUp(img_src,dstsize=(width*2,height*2),\
    borderType=cv2.BORDER_DEFAULT)
img_dst2 =cv2.pyrDown(img_src)                        
img_dst3 =cv2.resize(img_src, dsize=(320,240),\
    interpolation=cv2.INTER_LINEAR)                   #직접 크기 입력
img_dst4 =cv2.resize(img_src, dsize=(0,0),fx=0.7,fy=1.3,\
    interpolation=cv2.INTER_LINEAR)                    #비율로 지정

cv2.imshow('src',img_src)
cv2.imshow('src_up',img_dst1)
cv2.imshow('src_dn',img_dst2)
cv2.imshow('img_resize',img_dst3)
cv2.imshow('img_resize2',img_dst4)
cv2.waitKey()
cv2.destroyAllWindows()