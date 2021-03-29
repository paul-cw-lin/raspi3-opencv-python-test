import cv2
import numpy as np

o = cv2.imread('img13.jpg')
img = o


#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#t, binary = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
#k = np.ones((10,10), dtype=np.uint8)
#imgopen = cv2.morphologyEx(binary, cv2.MORPH_OPEN, k)
#t, binaryr = cv2.threshold(imgopen, 127, 255, cv2.THRESH_BINARY_INV)
#hand = binaryr[10:470, 0:460]
cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()