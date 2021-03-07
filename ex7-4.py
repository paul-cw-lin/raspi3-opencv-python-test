# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:23:18 2021

@author: d19fd
"""

import cv2

o = cv2.imread('kate3.jpg')
r = cv2.boxFilter(o, -1, (2,2), normalize=0)

cv2.imshow('o', o)
cv2.imshow('r', r)

cv2.waitKey()
cv2.destroyAllWindows()
