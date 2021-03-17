import cv2
import numpy as np

o1 = cv2.imread('erode.jpg', cv2.IMREAD_UNCHANGED)
o2 = cv2.imread('yuko.jpg', cv2.IMREAD_UNCHANGED)

k = np.ones((5,5), np.uint8)

r1 = cv2.morphologyEx(o1, cv2.MORPH_TOPHAT, k)
r2 = cv2.morphologyEx(o2, cv2.MORPH_TOPHAT, k)

cv2.imshow('o1', o1)
cv2.imshow('r1', r1)
cv2.imshow('o2', o2)
cv2.imshow('r2', r2)

cv2.waitKey()
cv2.destroyAllWindows() 