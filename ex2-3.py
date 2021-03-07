# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:47:44 2021

@author: d19fd
"""

import cv2
import numpy as np

blue = np.zeros((300,300,3), dtype=np.uint8)
blue[:,:,0] = 255
print('blue = \n', blue)
cv2.imshow('blue', blue)


cv2.waitKey()
cv2.destroyAllWindows()