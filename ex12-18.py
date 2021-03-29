import cv2

o = cv2.imread('img8.jpg')
img = o

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

area, trgl = cv2.minEnclosingTriangle(contours[0])
print('Area = ', area)
print('Trgl = ', trgl)

for i in range(0,3):
    cv2.line(img, tuple(trgl[i][0]), tuple(trgl[(i+1) % 3][0]), (0,255,0), 2)
    
cv2.imshow('result', img)
cv2.waitKey()
cv2.destroyAllWindows()