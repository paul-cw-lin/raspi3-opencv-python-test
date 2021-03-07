# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:28:19 2021

@author: d19fd
"""

import cv2

amber = cv2.imread('amber.jpg')

b,g,r = cv2.split(amber)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)



cv2.waitKey()
cv2.destroyAllWindows()