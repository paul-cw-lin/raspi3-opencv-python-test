# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:49:30 2021

@author: d19fd
"""

import cv2
import numpy as np

a = cv2.imread('annie-color.jpg', 1)
b = np.zeros(a.shape, dtype=np.uint8)

b[5:200, 180:380]=255
b[200:300, 200:250]=255

c = cv2.bitwise_and(a,b)

print('a.shape', a.shape)
print('b.shape', b.shape)

cv2.imshow('a', a)
cv2.imshow('b', b)
cv2.imshow('c', c)

cv2.waitKey()
cv2.destroyAllWindows()
 