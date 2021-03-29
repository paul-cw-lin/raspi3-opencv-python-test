import cv2

o = cv2.imread('img8.jpg')
img = o
cv2.imshow('original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

(x,y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))
radius = int(radius)

cv2.circle(img, center, radius, (255,255,255), 2)

cv2.imshow('result', img)

cv2.waitKey()
cv2.destroyAllWindows()