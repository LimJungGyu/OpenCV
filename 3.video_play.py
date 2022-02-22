#<동영상 재생1>
import cv2

myVideo = 'images/video.mp4'
capture = cv2.VideoCapture(myVideo)

# 동영상 파일 읽기 예외 처리
if capture.isOpened() == False:
    print("동영상을 열수 없습니다")
    exit(1)

while True:
    ret, frame = capture.read()  #비디오파일 자체를 튜플 형태로 읽어냄 Frame을 하나씩 읽을어냄 ret는 seq비슷
    if ret == False:  #동영상 파일이 끝났을때 반복문 종료
        print("동영상 파일 읽기 완료")
        break
    cv2.imshow("Video",frame)
    key = cv2.waitKey(25)          
    if key == 27:    #esc key 누르면 종료
        print("동영상 읽기 강제 종료")
        break

capture.release()
cv2.destroyAllWindows()      #윈도우로 반환