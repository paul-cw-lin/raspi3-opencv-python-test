# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:21:16 2021

@author: d19fd
"""

import cv2
import numpy as np

img0 = np.ones((3,4), dtype=np.uint8)
img1 = np.ones((3,4), dtype=np.uint8)*100
img2 = np.ones((3,4), dtype=np.uint8)*10

gamma = 3

img3 = cv2.addWeighted(img1, 0.6, img2, 5, gamma)
print(img0)
print(img1)
print(img2)
print(img3)
