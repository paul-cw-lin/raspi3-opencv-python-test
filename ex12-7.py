import cv2
import numpy as np

o = cv2.imread('img5.jpg')
img = o
cv2.imshow('original', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)
cntLen = []

for i in range(n):
    cntLen.append(cv2.arcLength(contours[i], True))
    print('The ['+str(i)+']  contours length : %d' %cntLen[i])
    
cntLenSum = np.sum(cntLen)
cntLenAvr = cntLenSum/n
print('The total contours length is : %d' %cntLenSum)
print('The average contours length is : %d' %cntLenAvr)

contoursImg = []

for i in range(n):
    temp = np.zeros(img.shape, dtype=np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, (0,0,255), 3)
    if cv2.arcLength(contours[i], True) > cntLenAvr:
        cv2.imshow('Contours['+str(i)+']', contoursImg[i])
        
cv2.waitKey()
cv2.destroyAllWindows()