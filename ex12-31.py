import cv2
import numpy as np

o = cv2.imread('img8.jpg', 0)
img = o

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
t, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours[0], -1, (0,0,255), 2)
cntArea = cv2.contourArea(contours[0])
equiDiameter = np.sqrt(4*cntArea/np.pi)
print(equiDiameter)

cv2.circle(img, (100, 100), int(equiDiameter/2), (0,0,255), 2)

cv2.imshow('result', img)
cv2.waitKey()
cv2.destroyAllWindows()