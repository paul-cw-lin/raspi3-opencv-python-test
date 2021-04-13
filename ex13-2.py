import cv2
import matplotlib.pyplot as plt

o = cv2.imread('m2.jpg')
img = o

plt.hist(img.ravel(),16)
plt.show()