import cv2

img_src=cv2.imread('images/shape2.png',cv2.IMREAD_COLOR)
height , width = img_src.shape[:2]
print('h:',height,'w:',width)
img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)
_,img_bin = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY_INV)
contours,hierarchy=cv2.findContours(img_bin,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

for i,contour in enumerate(contours):
    area =cv2.contourArea(contour)
    if area > 1000:
        mu = cv2.moments(contour)
        cx = int(mu['m10'] / (mu['m00']+1e-5))
        cy = int(mu['m01'] / (mu['m00']+1e-5))
        cv2.drawContours(img_src,contour,i,(255,255,0),2)
        cv2.circle(img_src,(cx,cy),3,(255,255,0),-1)
        cv2.putText(img_src,str(int(area)),(cx-30,cy+50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),1)
    cv2.imshow('src',img_src)

cv2.imshow('src',img_src)
cv2.waitKey()
cv2.destroyAllWindows()