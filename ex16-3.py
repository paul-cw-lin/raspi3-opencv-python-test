import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('img17.jpg', 0)
img = o
o1 = cv2.imread('img17.jpg', -1)
imgo = o1

o2 = cv2.cvtColor(imgo, cv2.COLOR_BGR2RGB)
oshow = o2.copy()

img = cv2.medianBlur(img, 5)

#edges = cv2.Canny(img, 50, 150, apertureSize = 3)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=90, param2=45, minRadius=30, maxRadius=70)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(o2, (i[0], i[1]), i[2], (255,0,0), 5)
    cv2.circle(o2, (i[0], i[1]), 2, (255,0,0), 5)
    
plt.subplot(121)
plt.imshow(oshow)
plt.axis('off')
plt.subplot(122)
plt.imshow(o2)
plt.axis('off')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()