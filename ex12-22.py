import cv2
import numpy as np

o = cv2.imread('img10.jpg')
img = o

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)
k = np.ones((10,10), dtype=np.uint8)
binaryo = cv2.morphologyEx(binary, cv2.MORPH_OPEN, k)

contours, hierarchy = cv2.findContours(binaryo, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
print('defects = \n', defects)

for i in range(defects.shape[0]):
    s,e,f,d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0,0,255], 2)
    cv2.circle(img, far, 5, (255,255,0), -1)
    
cv2.imshow('result', img)
cv2.waitKey()
cv2.destroyAllWindows()
