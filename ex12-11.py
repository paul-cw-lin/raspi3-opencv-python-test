import cv2

o = cv2.imread('img8.jpg')
img = o

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

x,y,w,h = cv2.boundingRect(contours[0])
print('apex length width :')
print('x = ', x)
print('y = ', y)
print('w = ', w)
print('h = ', h)

rect = cv2.boundingRect(contours[0])
print('\none return value :')
print('rect', rect)