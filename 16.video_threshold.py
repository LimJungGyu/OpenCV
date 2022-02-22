import cv2

myVideo = 'images/video.mp4'
capture = cv2.VideoCapture(myVideo)

while cv2.waitKey(33) <0:                                     
    ret, frame = capture.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,frame_dst = cv2.threshold(frame_gray,100,255,cv2.THRESH_OTSU)
    cv2.imshow("Video",frame)
    cv2.imshow("Video1",frame_dst)

     
capture.release()
cv2.waitKey()
cv2.destroyAllWindows()


