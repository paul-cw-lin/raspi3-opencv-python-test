# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:46:07 2021

@author: d19fd
"""

import cv2

amber = cv2.imread('amber.jpg')

b,g,r = cv2.split(amber)

bgr = cv2.merge([b,g,r])
rgb = cv2.merge([r,g,b])

cv2.imshow('amber', amber)
cv2.imshow('bgr', bgr)
cv2.imshow('rgb', rgb)

cv2.waitKey()
cv2.destroyAllWindows()