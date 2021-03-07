# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:36:05 2021

@author: d19fd
"""

import cv2
import numpy as np

a = cv2.imread('nanami-color.jpg', 0)
b = np.zeros(a.shape, dtype=np.uint8)

b[27:327, 150:400] = 255
b[327:450, 200:300] = 255

c = cv2.bitwise_and(a,b)

cv2.imshow('a', a)
cv2.imshow('b', b)
cv2.imshow('c', c)

cv2.waitKey()
cv2.destroyAllWindows()
