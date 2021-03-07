# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:42:05 2021

@author: d19fd
"""

import cv2
import numpy as np

img = cv2.imread('hermione.jpg')
rows, cols = img.shape[:2]

mapx = np.zeros(img.shape[:2], np.float32)
mapy = np.zeros(img.shape[:2], np.float32)

for i in range(rows) :
    for j in range(cols) :
        mapx.itemset((i,j), j)
        mapy.itemset((i,j), i)
        
rst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

cv2.imshow('img', img)
cv2.imshow('rst', rst)

cv2.waitKey()
cv2.destroyAllWindows()
