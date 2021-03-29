import cv2

o = cv2.imread('img2.jpg')
o1 = o
cv2.imshow('o1', o1)
gray = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
o1 = cv2.drawContours(o1, contours, -1, (0,0,255), 5)

cv2.imshow('r', o1)

cv2.waitKey()
cv2.destroyAllWindows()