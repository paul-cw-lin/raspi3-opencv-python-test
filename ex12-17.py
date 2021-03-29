import cv2
import numpy as np

o = cv2.imread('img8.jpg')
img = o

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

rows, cols = img.shape[:2]

[vx, vy, x, y] = cv2.fitLine(contours[0], cv2.DIST_L2, 0, 0.01, 0.01)
print('vx, vy, x, y : ', vx, vy, x, y)
a = np.int0(x)
b = np.int0(y)
print('a, b : ', a, b)

lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx) + y)

cv2.line(img, (cols-1, righty), (0, lefty), (0,255,0), 2)
cv2.imshow('result', img)

cv2.waitKey()
cv2.destroyAllWindows()