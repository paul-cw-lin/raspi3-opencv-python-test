import cv2
import numpy as np

o = cv2.imread('img10.jpg')
img = o

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)
k = np.ones((10,10), dtype=np.uint8)
binaryo = cv2.morphologyEx(binary, cv2.MORPH_OPEN, k)

contours, hierarchy = cv2.findContours(binaryo, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

image1 = img.copy()
hull = cv2.convexHull(contours[0])
cv2.polylines(image1, [hull], True, (0,255,0), 2)
print('is cv2.convexHull() Convexity? : ', cv2.isContourConvex(hull))
cv2.imshow('result1', image1)

image2 = img.copy()
epsilon = 0.01*cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
image2 = cv2.drawContours(image2, [approx], 0, (0,0,255), 2)
print('Is cv2.approxPolyDP() Convexity? : ', cv2.isContourConvex(approx))
cv2.imshow('result2', image2)

cv2.waitKey()
cv2.destroyAllWindows()