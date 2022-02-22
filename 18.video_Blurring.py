import cv2

myVideo = 'images/video.mp4'
capture = cv2.VideoCapture(myVideo)

while cv2.waitKey(33) <0:                                     
    ret, frame = capture.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_gray_blur = cv2.blur(frame_gray,(3,3),anchor=(-1,-1),borderType=cv2.BORDER_DEFAULT)
    frame_blur = cv2.blur(frame,(3,3),anchor=(-1,-1),borderType=cv2.BORDER_DEFAULT)

    ret,frame_gray = cv2.threshold(frame_gray,100,255,cv2.THRESH_OTSU)
    ret,frame_gray_blur = cv2.threshold(frame_gray_blur,100,255,cv2.THRESH_OTSU)
    cv2.imshow("Video",frame)
    cv2.imshow("gray",frame_gray)
    cv2.imshow("frame_blur",frame_blur)
    cv2.imshow("frame_gray_blur",frame_gray_blur)

     
capture.release()
cv2.waitKey()
cv2.destroyAllWindows()
