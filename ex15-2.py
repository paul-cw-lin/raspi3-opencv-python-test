import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('yuko.jpg', 0)
img = o
o1 = cv2.imread('yuko-eye.jpg', 0)
template = o1

tw, th = template.shape[::-1]
rv = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)
topLeft = maxLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img, topLeft, bottomRight, 255, 2)

plt.subplot(121), plt.imshow(rv, cmap='gray')
plt.title('matching result'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('detected point'), plt.xticks([]), plt.yticks([])
plt.show()