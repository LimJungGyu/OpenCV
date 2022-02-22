import cv2


import cv2
# 비디오 하나를 읽어드림
capture = cv2.VideoCapture('images/video.mp4')

while cv2.waitKey(33) < 0:
    # 원본 비디오를 gray로 바꿈
    ret, frame =capture.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # 원본, gray의 크기를 절반으로(pyrdown)
    frame_half =cv2.pyrDown(frame)
    frame_half_gray=cv2.pyrDown(frame_gray)

    #원본+gray를 vconcat하여 붙임(상하로 붙임) 
    # -color는 3채널 gray는 1채널 이 둘은 붙지 않는다 (gray의 채널을 3채널로 변경해야함)
    frame_gray_bgr=cv2.cv2.cvtColor(frame_gray, cv2.COLOR_GRAY2BGR) 
    frame_hconcat=cv2.hconcat([frame, frame_gray_bgr])

    # 원본은 그대로 , gray영상은  좌우 대칭 
    frame_half_gray =  cv2.flip(frame_half_gray,1)
    
    cv2.imshow('Video',frame_half)
    cv2.imshow('gray',frame_half_gray)
    cv2.imshow('hconcat',frame_hconcat)
capture.release()
cv2.destroyAllWindows()



# 원본은 그대로 , gray영상은  좌우 대칭 