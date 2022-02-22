import cv2
import numpy as np
myVideo = 'images/video.mp4'
cap = cv2.VideoCapture(myVideo)

#get을 통해 width heiht를 구함 get을 통해 얻으면 실수값으로 나오기때문에 int화
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)
while cv2.waitKey(33) < 0:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_gray_bgr=cv2.cvtColor(frame_gray,cv2.COLOR_GRAY2BGR)

#split으로 색을 나누고 zeros로 빈색 값을 만듬 그리고 merge로 합침
    frame_b, frame_g, frame_r = cv2.split(frame)
    zero =np.zeros((height,width,1),dtype=np.uint8)
    frame_zero_bgr = cv2.merge((zero,zero,frame_r))

#구한 height width 값을 영상 가운데에 맞춰서 좌표 입력
    h1=int(height/4); h2=int(height*3/4)
    w1=int(width/4); w2=int(width*3/4)

    frame1=frame.copy()
    frame1[h1:h2,w1:w2,:]=frame_gray_bgr[h1:h2,w1:w2,:]
    frame[h1:h2,w1:w2,:]=frame_zero_bgr[h1:h2,w1:w2,:]
    cv2.imshow("target_red" ,frame)
    cv2.imshow("target_gray",frame1)
    cv2.imshow("gray",frame_gray)
    cv2.imshow("bgr",frame_zero_bgr)

cap.release()
cv2.waitKey()
cv2.destroyAllWindows()