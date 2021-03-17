import cv2

o = cv2.imread('well.jpg', cv2.IMREAD_GRAYSCALE)

Scharrx = cv2.Sobel(o, cv2.CV_64F, 1, 0, -1)
Scharry = cv2.Sobel(o, cv2.CV_64F, 0, 1, -1)
Scharrx = cv2.convertScaleAbs(Scharrx)
Scharry = cv2.convertScaleAbs(Scharry)

cv2.imshow('o', o)
cv2.imshow('x', Scharrx)
cv2.imshow('y', Scharry)

cv2.waitKey()
cv2.destroyAllWindows()