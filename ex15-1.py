import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('yuko.jpg', 0)
img = o
o1 = cv2.imread('yuko-eye.jpg', 0)
template = o1

th, tw = template.shape[::]
rv = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)

topLeft = minLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img, topLeft, bottomRight, 255, 2)

plt.subplot(121), plt.imshow(rv, cmap='gray')
plt.title('matching result'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('detectd point'), plt.xticks([]), plt.yticks([])
plt.show()
