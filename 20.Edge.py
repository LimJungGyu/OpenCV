#외곽선 추출
import cv2

img_src=cv2.imread('images/boat.jpg',cv2.IMREAD_COLOR)
###1.칼러이미지 gray로 변환
img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)
###2. 옵션 : 그레이 이미지에 블러적용(이미지에 잡음이 없으면 생략가능)
img_blur = cv2.blur(img_gray,ksize=(5,5),anchor=(-1,-1))
###3. threshold 적용으로 이진화
_,img_binary = cv2.threshold(img_blur,50,255,cv2.THRESH_OTSU)
###4. 외곽선(Edge) 추출 -(Sobel,Laplacian,Canny)

###Sobel 방법
#간단 코드 sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
#복잡 코드 ref : https://docs.opencv.org/4.x/d2/d2c/tutorial_sobel_derivatives.html
scale = 1; delta = 0; ddepth = cv2.CV_16S

grad_x = cv2.Sobel(img_binary, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
grad_y = cv2.Sobel(img_binary, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)
img_sobel = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

###Laplacian 방법
#코드 ref : https://docs.opencv.org/4.x/d5/db5/tutorial_laplace_operator.html
img_laplacian = cv2.Laplacian(img_binary, ddepth, ksize=3)
img_laplacian = cv2.convertScaleAbs(img_laplacian)

###Canny 방법
#코드 ref : https://docs.opencv.org/4.x/da/d5c/tutorial_canny_detector.html
img_canny= cv2.Canny(img_binary,70,150)

cv2.imshow('src',img_src)
cv2.imshow('blur',img_blur)
cv2.imshow('bin',img_binary)
cv2.imshow('sobel',img_sobel)
cv2.imshow('Laplacian',img_laplacian)
cv2.imshow('Canny',img_canny)
cv2.waitKey()
cv2.destroyAllWindows()