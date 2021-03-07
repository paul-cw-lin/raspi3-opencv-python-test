# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:44:15 2021

@author: d19fd
"""

import cv2
import numpy as np

img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
rows, cols = img.shape
mapx = np.zeros(img.shape, np.float32)
mapy = np.zeros(img.shape, np.float32)

for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j), j)
        mapy.itemset((i,j), rows-1-i)
        
rst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

print('img\n', img)
print('mapx\n', mapx)
print('mapy\n', mapy)
print('rst\n', rst)
