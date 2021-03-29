import cv2
import numpy as np

o = cv2.imread('img8.jpg')
img = o

cv2.imshow('original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

x,y,w,h = cv2.boundingRect(contours[0])
a = x+w
b = y+h

brcnt = np.array([[[x, y]], [[a, y]], [[a, b]], [[x, b]]])
cv2.drawContours(img, [brcnt], -1, (255, 255, 255), 2)

cv2.imshow('result', img)
cv2.waitKey()
cv2.destroyAllWindows()