import cv2
import numpy as np

o = cv2.imread('erode.jpg', cv2.IMREAD_UNCHANGED)
k = np.ones((5,5), np.uint8)

r = cv2.morphologyEx(o, cv2.MORPH_GRADIENT, k)

cv2.imshow('o', o)
cv2.imshow('r', r)

cv2.waitKey()
cv2.destroyAllWindows() 