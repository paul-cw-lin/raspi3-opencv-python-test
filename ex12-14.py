import cv2
import numpy as np

o = cv2.imread('img8.jpg')
img = o

cv2.imshow('original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

rect = cv2.minAreaRect(contours[0])
print('return rect :\n', rect)

points = cv2.boxPoints(rect)
print('\nThe points after transformation :\n', points)

points = np.int0(points)
image = cv2.drawContours(img, [points], 0, (255,255,255), 2)

cv2.imshow('result', image)
cv2.waitKey()
cv2.destroyAllWindows()