import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('nanami.jpg', cv2.IMREAD_GRAYSCALE)
img = o

mask = np.zeros(img.shape, dtype=np.uint8)
mask[170:340, 170:340]=255
histImg = cv2.calcHist([img], [0], None, [256], [0,255])
histMI = cv2.calcHist([img], [0], mask, [256], [0,255])
plt.plot(histImg, color='b')
plt.plot(histMI, color='r')
plt.show()