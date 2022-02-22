import cv2
import numpy as np
capture = cv2.VideoCapture("images/blue.mp4")

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('w:',width,'h:',height)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    frame = cv2.pyrDown(frame)
    ###
    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_mask1 = (7,60,60); lower_mask2 = (21,255,255)

    mask_blue = cv2.inRange(frame_hsv, lower_mask1, lower_mask2)
    contours,hierarchy=cv2.findContours(mask_blue,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    for i,contour in enumerate(contours):
        area =cv2.contourArea(contour)
        if area >100:
            cv2.drawContours(frame, [contours[i]], 0, (0, 0, 255), 2)
            mu = cv2.moments(contour)
            cx = int(mu['m10'] / (mu['m00']+1e-5))
            cy = int(mu['m01'] / (mu['m00']+1e-5))
            cv2.drawContours(frame,contours,i,(0,0,255),2)
            cv2.circle(frame,(cx,cy),3,(0,0,255),-1)

        cv2.imshow('src',frame)

capture.release()
cv2.destroyAllWindows()