import cv2
import numpy as np

o = cv2.imread('yuko.jpg')
img = o

cv2.imshow('Original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

mask = np.zeros(img.shape, dtype=np.uint8)
cv2.drawContours(mask, contours, -1, (255,255,255), -1)
cv2.imshow('mask', mask)
loc = cv2.bitwise_and(img, mask)
cv2.imshow('loc', loc)

cv2.waitKey()
cv2.destroyAllWindows()