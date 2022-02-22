#<동영상 재생2 -무한재생>
import cv2

myVideo = 'images/video.mp4'
capture = cv2.VideoCapture(myVideo)

# 동영상 파일 읽기 예외 처리
if capture.isOpened() == False:
    print("동영상을 열수 없습니다")
    exit(1)

#동영상이 끝나면 동영상 시작으로 가라
while cv2.waitKey(33) <0:
    
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT): #프레임이 끝이면
        capture.set(cv2.CAP_PROP_POS_FRAMES,0)                                         #프레임 시작으로 세팅
    ret, frame = capture.read()  
    cv2.imshow("Video",frame)
capture.release()
cv2.destroyAllWindows()      #윈도우로 반환