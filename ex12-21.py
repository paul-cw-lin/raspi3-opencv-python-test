import cv2
import numpy as np

o = cv2.imread('img10.jpg')
img = o
cv2.imshow('original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)

# Morphology OPEN
k = np.ones((5,5), dtype=np.uint8)
r1 = cv2.morphologyEx(binary, cv2.MORPH_OPEN, k)

contours, hierarchy = cv2.findContours(r1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#print(len(contours))

hull = cv2.convexHull(contours[0])

cv2.polylines(img, [hull], True, (0,0,255), 3)

cv2.imshow('result', img)
cv2.waitKey()
cv2.destroyAllWindows()