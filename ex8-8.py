import cv2
import numpy as np

img1 = cv2.imread('j-dot.jpg')
img2 = cv2.imread('2-wb.jpg')

k = np.ones((10,10), np.uint8)
r1 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, k, iterations=3)
r2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, k, iterations=3)

cv2.imshow('img1', img1)
cv2.imshow('r1', r1)
cv2.imshow('img2', img2)
cv2.imshow('r2', r2)

cv2.waitKey()
cv2.destroyAllWindows()