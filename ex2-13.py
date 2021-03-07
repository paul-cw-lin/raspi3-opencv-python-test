# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:20:13 2021

@author: d19fd
"""

import numpy as np
import cv2

a = cv2.imread('lena-full.jpg', cv2.IMREAD_UNCHANGED)
face = a[220:400,250:350]
cv2.imshow('orginal', a)
cv2.imshow('face', face)
cv2.waitKey()
cv2.destroyAllWindows()