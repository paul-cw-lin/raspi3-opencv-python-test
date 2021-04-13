import cv2
import matplotlib.pyplot as plt

o = cv2.imread('natalia.jpg', cv2.IMREAD_GRAYSCALE)
img = o

equ = cv2.equalizeHist(img)

cv2.imshow('original', img)
cv2.imshow('result', equ)

plt.figure('Original Bar Graph')
plt.hist(img.ravel(),256)
plt.figure('Equalize Bar Graph')
plt.hist(equ.ravel(),256)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

