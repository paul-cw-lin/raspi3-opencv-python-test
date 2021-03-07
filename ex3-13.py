# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:30:18 2021

@author: d19fd
"""

import cv2
import numpy as np

ashu = cv2.imread('ashu-color.jpg', 0)
cv2.imshow('ashu', ashu)

r, c = ashu.shape

x = np.zeros((r,c,8), dtype=np.uint8)
for i in range(8):
    x[:,:,i] = 2**i
        
r = np.zeros((r,c,8), dtype=np.uint8)
for i in range(8):
    r[:,:,i] = cv2.bitwise_and(ashu, x[:,:,i])
    mask = r[:,:,i] > 0
    r[mask] = 255
    cv2.imshow(str(i), r[:,:,i])

cv2.waitKey()
cv2.destroyAllWindows()
