# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:12:42 2021

@author: d19fd
"""

import cv2

o = cv2.imread('kate3.jpg')
r5 = cv2.blur(o, (5,5))
r30 = cv2.blur(o, (30,30))

cv2.imshow('o', o)
cv2.imshow('r5', r5)
cv2.imshow('r30', r30)

cv2.waitKey()
cv2.destroyAllWindows()
