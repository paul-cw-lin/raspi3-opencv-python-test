import cv2

o = cv2.imread('img8.jpg')
img = o
cv2.imshow('original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

ellipse = cv2.fitEllipse(contours[0])
print('ellipse = ', ellipse)

cv2.ellipse(img, ellipse, (0, 255, 0), 2)
cv2.imshow('result', img)

cv2.waitKey()
cv2.destroyAllWindows()