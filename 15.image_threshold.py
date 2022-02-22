#이진화 :무언가를 검출할 목적
#검출 하고 싶은 것을 표시하려고
#흰색과 검은색가운데 검축하려고 하는 것을 흰색으로 표시
#또는 표시하고 싶지 않은것을 검은색으로 표현
#임계값보다 높고 낮고 검출
import cv2
img_src = cv2.imread('images/sudoku.jpg',cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)


#threshold 임계값 찾는 함수/thresh_binary 100보다 높은값은 흰색으로 표시하겟다 
ret ,img_bin = cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY)
#노가다로 같은 결과
#ret ,img_dst = cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY)
#img_bin=cv2.bitwise_not(img_bin)
ret ,img_bin_inv = cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY_INV)

#230보다 크면 원래 값으로
ret ,img_trunc = cv2.threshold(img_gray,230,255,cv2.THRESH_TRUNC)
#200보다 작은 것은 제로 로
ret ,img_tozero = cv2.threshold(img_gray,200,255,cv2.THRESH_TOZERO)
#200보다 큰것은 제로로
ret ,img_tozero_inv = cv2.threshold(img_gray,200,255,cv2.THRESH_TOZERO_INV)

#쓰레스홀드값을 지가 알아서 하는 알고리즘
ret ,img_otsu = cv2.threshold(img_gray,100,255,cv2.THRESH_OTSU)
#<적응형 쓰레스 홀드>  지엽적으로(직접입력X 주변공간(지정)에 대해) 쓰레스홀드하는 알고리즘
#mean 평균값
dst_adp_mean = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,5)
#gaussian 중간값
dst_adp_gau = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,5)
cv2.imshow('src',img_src)
cv2.imshow('dst',img_gray)
cv2.imshow('bin',img_bin)
cv2.imshow('bin_inv',img_bin_inv)
cv2.imshow('trunc',img_trunc)
cv2.imshow('toZero',img_tozero)
cv2.imshow('toZeroInv',img_tozero_inv)
cv2.imshow('otsu',img_otsu)
cv2.imshow('adp_mean',dst_adp_mean)
cv2.imshow('adp_gaussian',dst_adp_gau)
cv2.waitKey()
cv2.destroyAllWindows()



