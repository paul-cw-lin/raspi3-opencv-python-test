import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('img16.jpg')
img = o

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)

orgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
oshow = orgb.copy()

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 1, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(orgb, (x1, y1), (x2, y2), (255,0,0), 5)
    
plt.subplot(121)
plt.imshow(oshow)
plt.axis('off')
plt.subplot(122)
plt.imshow(orgb)
plt.axis('off')
plt.show()