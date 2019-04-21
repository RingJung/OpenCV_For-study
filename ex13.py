import numpy as np
import cv2 as cv

def onMouse():
    pass

def bluring():
    img = cv.imread('circle.jpg')

    cv.namedWindow('BlurPane')
    cv.createTrackbar('BLUR_MODE', 'BlurPane', 0, 2, onMouse)
    cv.createTrackbar('BLUR', 'BlurPane', 0, 5, onMouse)

    mode = cv.getTrackbarPos('BLUR_MODE', 'BlurPane')
    val = cv.getTrackbarPos('BLUR', 'BlurPane')

    while True:
        val = val *2 + 1

        try:
            if mode == 0:
                blur = cv.blur(img, (val, val))
            elif mode == 1:
                blur = cv.GaussianBlur(img, (val, val), 0)
            elif mode == 2:
                blur = cv.medianBlur(img, val)
            else:
                 break

            cv.imshow('BlurPane', blur)
        except:
            break

        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

        mode = cv.getTrackbarPos('BLUR_MODE', 'BlurPane')
        val = cv.getTrackbarPos('BLUR', 'BlurPane')

    cv.destroyAllWindows()

bluring()
#Gaussian Filter는 이미지의 가우스 노이즈를 제거하는데에 효과적임
