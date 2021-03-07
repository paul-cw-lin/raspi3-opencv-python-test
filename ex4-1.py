# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:42:39 2021

@author: d19fd
"""

import cv2
import numpy as np

img = np.random.randint(0,256, size=[2,4,3], dtype=np.uint8)
rst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print('img=', img)
print('rst=', rst)
