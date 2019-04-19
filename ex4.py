import numpy as np
import cv2 as cv

def drawing():
    img = np.zeros((512, 512, 3), np.uint8)
    #numpy배열을 만들고 모든 값을 0으로 채우는 함수
    #즉 512 x 512 크기의 검정색 이미지를 생성

    cv.line(img, (0,0), (511, 511), (255, 0, 0), 5)
    # (0,0)에서 (511,511)까지 두께 5인 파란색직선을 생성
    cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    # 좌측 상단인 (384, 0) 부터 우측 하단인 (510, 128)까지 두께 3인 녹색의 사각형을 생성
    cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
    cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)

    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)

    cv.imshow('drawing', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

drawing()


