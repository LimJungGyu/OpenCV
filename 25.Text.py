import cv2
import numpy as np

img_src = np.zeros((600,800,3),dtype=np.uint8)
height,width = img_src.shape[:2]

mystr = "Hello"
img_src = cv2.putText(img_src, mystr,(200,200),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),1)

cv2.imshow('src',img_src)
cv2.waitKey()
cv2.destroyAllWindows()