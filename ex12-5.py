import cv2
import numpy as np

o = cv2.imread('img2.jpg')
img = o
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('original', img)

n = len(contours)
contoursImg = []

for i in range(n):
    print('Contours['+str(i)+'] Area=', cv2.contourArea(contours[i]))
    temp = np.zeros(img.shape, dtype=np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, (255,255,255), 3)
    cv2.imshow('Contours['+str(i)+']', contoursImg[i])
    
cv2.waitKey()
cv2.destroyAllWindows()