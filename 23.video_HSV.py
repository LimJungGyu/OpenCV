import cv2
import numpy as np
capture = cv2.VideoCapture("images/blue.mp4")

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('w:',width,'h:',height)

while cv2.waitKey(33) < 0: #아무키나 누르면 동영상 종료
    ret, frame = capture.read()
    frame = cv2.pyrDown(frame)
    ###
    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_mask1 = (80,100,100); lower_mask2 = (120,255,255)
    mask_blue = cv2.inRange(frame_hsv, lower_mask1, lower_mask2)
    frame_blue = cv2.bitwise_and(frame_hsv, frame_hsv, mask=mask_blue)# 
    frame_blue = cv2.cvtColor(frame_blue,cv2.COLOR_HSV2BGR)
        
    cv2.imshow('Video',frame_blue)
    
capture.release()
cv2.destroyAllWindows()