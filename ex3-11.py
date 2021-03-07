# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:44:33 2021

@author: d19fd
"""

import cv2
import numpy as np

a = cv2.imread('ashu-color.jpg',1)
w,h,c = a.shape
mask = np.zeros((w,h), dtype=np.uint8)
mask[100:400, 200:400] = 255
mask[100:500, 100:200] = 255

c = cv2.bitwise_and(a, a, mask)

print('a.shape=', a.shape)
print('mask.shape=', mask.shape)

cv2.imshow('a', a)
cv2.imshow('mask', mask)
cv2.imshow('c', c)

cv2.waitKey()
cv2.destroyAllWindows()
