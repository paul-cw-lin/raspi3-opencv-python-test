import cv2
import matplotlib.pyplot as plt

o = cv2.imread('natalia.jpg', cv2.IMREAD_GRAYSCALE)
img = o

equ = cv2.equalizeHist(img)
plt.figure('subplot example')
plt.subplot(121), plt.hist(img.ravel(),256)
plt.subplot(122), plt.hist(equ.ravel(),256)
plt.show()