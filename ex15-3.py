import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('yuko.jpg', 0)
img = o
o1 = cv2.imread('yuko-eye.jpg', 0)
template = o1

w, h = template.shape[::-1]
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
#print('res=', res)
threshole = 0.75
loc = np.where(res >= threshole)
#print('loc=', loc)

for pt in zip(*loc[::-1]):
    print('pt=', pt)
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), 255, 2)
    
plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()
