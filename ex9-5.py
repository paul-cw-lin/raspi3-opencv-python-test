import cv2

o = cv2.imread('well.jpg', cv2.IMREAD_GRAYSCALE)

Sobelxy = cv2.Sobel(o, cv2.CV_64F, 1, 1)
Sobelxy = cv2.convertScaleAbs(Sobelxy)

cv2.imshow('o', o)
cv2.imshow('xy', Sobelxy)

cv2.waitKey()
cv2.destroyAllWindows()