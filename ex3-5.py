# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:45:57 2021

@author: d19fd
"""

import cv2

a = cv2.imread('m2-color.jpg')
b = cv2.imread('mai-color.jpg')

result = cv2.addWeighted(a, 0.5, b, 0.5, 0)

cv2.imshow('m2', a)
cv2.imshow('mai', b)
cv2.imshow('result', result)

cv2.waitKey()
cv2.destroyAllWindows()