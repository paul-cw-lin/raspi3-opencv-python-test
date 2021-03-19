import cv2
import numpy as np

o = cv2.imread('img4.jpg')
img = o

cv2.imshow('original', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
n = len(contours)
temp = []

for i in range(n):
    matrix = np.zeros(img.shape, dtype=np.uint8)
    temp.append(matrix)
    cv2.drawContours(temp[i], contours, i, 266,3)
    cv2.imshow('temp['+str(i)+']', temp[i])
    
print('(moments) :')
for i in range(n):
    print('Contour'+str(i)+'matrix :\n', cv2.moments(contours[i]))
    print('Controus area : ')
    
for i in range(n):
    print('Contour'+str(i)+'area : %d' %cv2.moments(contours[i])['m00'])
          


cv2.waitKey()
cv2.destroyAllWindows()