# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:47:08 2021

@author: d19fd
"""

import cv2
import numpy as np

a = cv2.imread('mai-color.jpg',0)
b = np.random.randint(0,128, size=[512,512], dtype=np.uint8)

result1 = a + b
result2 = cv2.add(a, b)

cv2.imshow('original', a)
cv2.imshow('result1', result1)
cv2.imshow('result2', result2)

cv2.waitKey()
cv2.destroyAllWindows()
