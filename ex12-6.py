import cv2
import numpy as np
o = cv2.imread('img2.jpg')
img = o
cv2.imshow('original', o)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)
contoursImg = []

for i in range(n):
    temp = np.zeros(img.shape, dtype=np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, (255,255,255), 3)
    if cv2.contourArea(contours[i]) < 12000:
        print('Contours['+str(i)+'] Area = ', cv2.contourArea(contours[i]))
        cv2.imshow('Contours['+str(i)+']', contoursImg[i])
        
cv2.waitKey()
cv2.destroyAllWindows()