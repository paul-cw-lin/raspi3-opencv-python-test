import cv2

o = cv2.imread('img-H.jpg', cv2.IMREAD_UNCHANGED)

kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (59,59))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (59,59))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (59,59))

dst1 = cv2.dilate(o, kernel1, iterations=2)
dst2 = cv2.dilate(o, kernel2, iterations=2)
dst3 = cv2.dilate(o, kernel3, iterations=2)

cv2.imshow('o', o)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)

cv2.waitKey()
cv2.destroyAllWindows()