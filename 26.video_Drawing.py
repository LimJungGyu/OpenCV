import cv2
import numpy as np
capture = cv2.VideoCapture("images/video.mp4")

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
center_point=(int(width/2),int(height/2))
print('w:',width,'h:',height)

while cv2.waitKey(33)<0:
    ret, frame = capture.read()
    cv2.circle(frame,(center_point),60,(255,0,0),3)
    cv2.rectangle(frame,(int(width/4),int(height/4)),(int(width/4*3),int(height/4*3)),(255,255,0),3)
    cv2.imshow('Video',frame)
cv2.waitKey()
cv2.destroyAllWindows
