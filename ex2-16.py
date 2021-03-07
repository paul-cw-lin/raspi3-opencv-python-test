# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:16:48 2021

@author: d19fd
"""

import cv2

amber = cv2.imread('amber.jpg')
cv2.imshow('amber', amber)

b = amber[:,:,0]
g = amber[:,:,1]
r = amber[:,:,2]
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

amber[:,:,0] = 0
cv2.imshow('amberb0', amber)
amber[:,:,1] = 0
cv2.imshow('amberg0', amber)

cv2.waitKey()
cv2.destroyAllWindows()