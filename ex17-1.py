import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('img13.jpg')
img = o

k = np.zeros((3,3), np.uint8)
e = cv2.erode(img, k, iterations = 5)
b = cv2.subtract(img, e)

plt.subplot(221)
plt.imshow(img)
plt.axis('off')
plt.subplot(222)
plt.imshow(e)
plt.axis('off')
plt.subplot(223)
plt.imshow(b)
plt.axis('off')

#cv2.imshow('b', b)

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()