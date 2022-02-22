import cv2

capture = cv2.VideoCapture('images/video.mp4')

while cv2.waitKey(33) < 0:
    ret, frame =capture.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video',frame)
    cv2.imshow('gray',frame_gray)
capture.release()
cv2.destroyAllWindows()