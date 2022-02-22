import cv2

myVideo = 'images/video.mp4'
capture = cv2.VideoCapture(myVideo)

while cv2.waitKey(33) <0:                                     
    ret, frame = capture.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.cvtColor(frame_gray,cv2.COLOR_GRAY2BGR)
    frame2 =cv2.hconcat([frame,frame_gray])
    frame2 =cv2.vconcat([frame2,frame2])
    frame2 =cv2.resize(frame2,(0,0),fx=1.3,fy=1.3)
    img_canny= cv2.Canny(frame_gray,70,150)

    cv2.imshow("Video",frame)
    cv2.imshow("gray",frame_gray)
    cv2.imshow("frame2",frame2)
    cv2.imshow("canny",img_canny)

capture.release()
cv2.waitKey()
cv2.destroyAllWindows()
