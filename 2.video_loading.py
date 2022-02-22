#웹캠으로 실시간 영상 불러오기 >>
import cv2

myIP = 'http://192.168.0.11:4747/video'    #스마트폰 드로이드캠 어플에서 보여주는 ip주소 입력
cap =cv2.VideoCapture(myIP)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,640)

while cv2.waitKey(33) < 0:
    ret, frame = cap.read()
    cv2.imshow("Video" ,frame)
cv2.waitKey()
cv2.destroyAllWindows()