import cv2
import matplotlib.pyplot as plt

o = cv2.imread('m2.jpg')
img = o

#cv2.imshow('original', img)
plt.hist(img.ravel(), 256)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()