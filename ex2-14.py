# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:25:57 2021

@author: d19fd
"""

import numpy as np
import cv2

a = cv2.imread('lena-full.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('original', a)
face = np.random.randint(0,256,size=(180,100,3), dtype=np.uint8)
a[220:400,250:350] = face
cv2.imshow('result', a)
cv2.waitKey()
cv2.destroyAllWindows()