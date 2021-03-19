import cv2
import numpy as np

o = cv2.imread('img2.jpg')
img = o

cv2.imshow('Original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)

for i in range(n):
    temp = np.zeros(img.shape, dtype=np.uint8)
    cv2.drawContours(temp, contours, i, (255,255,255), 3)
    cv2.imshow('t['+str(i)+']', temp)

cv2.waitKey()
cv2.destroyAllWindows()
