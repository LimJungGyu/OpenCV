import cv2
img_src = cv2.imread('images/lol_ryze.jpg',cv2.IMREAD_COLOR)
#bitwise를 통한 색반전
img_dst = cv2.bitwise_not(img_src)
#노가다를 통한 색반전
# img_b,img_g,img_r =cv2.split(img_src)
# img_b=255-img_b;
# img_g=255-img_g;
# img_r=255-img_r;
# img_dst = cv2.merge((img_b,img_g,img_r))

cv2.imshow('src',img_src)
cv2.imshow('dst',img_dst)
cv2.waitKey()
cv2.destroyAllWindows()