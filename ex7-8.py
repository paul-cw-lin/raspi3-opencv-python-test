import cv2

o = cv2.imread('bamboo1.jpg')
r = cv2.bilateralFilter(o, d=5, sigmaColor=100, sigmaSpace=100)

cv2.imshow('Original', o)
cv2.imshow('Result', r)

cv2.waitKey()
cv2.destroyAllWindows()