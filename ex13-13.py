import cv2
import matplotlib.pyplot as plt

o = cv2.imread('annie.jpg')
img = o

imgBGR = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure('Result')
plt.subplot(122)
plt.imshow(img)
plt.axis('off')
plt.subplot(121)
plt.imshow(imgBGR)
plt.axis('off')
plt.show()
