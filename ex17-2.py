import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('img21.jpg')
img = o

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ishow = img.copy()

t, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3,3), np.uint8)

#cv2.imshow('thresh', thresh)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)

dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

ret, fore = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

#cv2.imshow('dist', ishow)

plt.subplot(221)
plt.imshow(ishow)
plt.axis('off')
plt.subplot(223)
plt.imshow(dist_transform)
plt.axis('off')
plt.subplot(224)
plt.imshow(fore)
plt.axis('off')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()