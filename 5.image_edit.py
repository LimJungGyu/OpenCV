#사진 처리 >>
import cv2

###  소스 영상
img_src = cv2.imread('images/lol_ryze.jpg',cv2.IMREAD_COLOR)
###  이미지 처리 (좌 우 대칭)
#cv2.flip(source,option) option 0:상하 대칭 1:좌우 대칭 -1:상하좌우 대칭
img_dst_ud = cv2.flip(img_src,0)  #상 하  대칭   
img_dst_lr = cv2.flip(img_src,1)  #좌 우  대칭
img_dst_lrud = cv2.flip(img_src,-1)  #상 하 좌 우  대칭

### 이미지 붙이기
img_tmp_up=cv2.hconcat([img_src, img_dst_lr])  ##([왼쪽, 오른쪽])으로 가로로 합친다
img_tmp_dn=cv2.hconcat([img_dst_ud, img_dst_lrud])
img_result =cv2.vconcat([img_tmp_up,img_tmp_dn]) ##([위, 아래])로 세로로 합친다

##3  이미지 크기 줄이기
#img_result = cv2.pyrup(img_result)    ##이미지 가로 세로를 배로 늘인다
#img_result = cv2.pyrDown(img_result)    ##이미지 가로 세로를 절반으로 줄인다
img_result = cv2.resize(img_result,dsize=(0,0),fx=0.7,fy=0.7,interpolation=cv2.INTER_LINEAR) #비율변경

###  이미지 처리 종료


###  결과 영상 출력
cv2.imshow("src",img_src)
cv2.imshow("dst_ud",img_dst_ud)
cv2.imshow("dst_lr",img_dst_lr)
cv2.imshow("dst_lrud",img_dst_lrud)
cv2.imshow("dst(up)",img_tmp_up)
cv2.imshow("dst(dn)",img_tmp_dn)
cv2.imshow("dst(result)",img_result)
cv2.waitKey()
cv2.destroyAllWindows()


