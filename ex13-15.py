import cv2
import matplotlib.pyplot as plt

o = cv2.imread('annie.jpg')
img = o

g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure('Gray Result')
plt.subplot(221); plt.imshow(g, cmap=plt.cm.gray)
plt.subplot(222); plt.imshow(g, cmap=plt.cm.gray_r)
plt.subplot(223); plt.imshow(g, cmap='gray')
plt.subplot(224); plt.imshow(g, cmap='gray_r')

plt.show()