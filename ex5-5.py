# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:36:07 2021

@author: d19fd
"""

import cv2
import numpy as np

img = cv2.imread('kate2.jpg')
height, width = img.shape[:2]

x = 100
y = 200

M = np.float32([[1, 0, x], [0, 1, y]])
move = cv2.warpAffine(img, M, (width, height))

cv2.imshow('img', img)
cv2.imshow('move', move)

cv2.waitKey()
cv2.destroyAllWindows()
