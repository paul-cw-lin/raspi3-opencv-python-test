# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:39:25 2021

@author: d19fd
"""

import numpy as np
import cv2

img1 = np.random.randint(0,256,size=[3,3],dtype=np.uint8)
img2 = np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print('img1=\n', img1)
print('\n')
print('img2=\n', img2)
print('\n')
img3 = cv2.add(img1, img2)
print('img3=\n', img3)