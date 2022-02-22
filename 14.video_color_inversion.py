import cv2

myVideo = 'images/video.mp4'
capture = cv2.VideoCapture(myVideo)

while cv2.waitKey(33) <0:                                     
    ret, frame = capture.read()
    frame_dst = cv2.bitwise_not(frame)
    cv2.imshow("Video",frame)
    cv2.imshow("Video1",frame_dst)
capture.release()
cv2.destroyAllWindows()      
capture.release()
cv2.waitKey()
cv2.destroyAllWindows()