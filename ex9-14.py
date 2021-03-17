import cv2

o = cv2.imread('yuko.jpg', cv2.IMREAD_GRAYSCALE)

Laplacian = cv2.Laplacian(o, cv2.CV_64F, ksize=3)
Laplacian = cv2.convertScaleAbs(Laplacian)

cv2.imshow('o', o)
cv2.imshow('L', Laplacian)

cv2.waitKey()
cv2.destroyAllWindows()