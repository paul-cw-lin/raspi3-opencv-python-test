# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:21:03 2021

@author: d19fd
"""

import cv2

img = cv2.imread('kate.jpg')
x = cv2.flip(img, 0)
y = cv2.flip(img, 1)
xy = cv2.flip(img, -1)

cv2.imshow('img', img)
cv2.imshow('x', x)
cv2.imshow('y', y)
cv2.imshow('xy', xy)

cv2.waitKey()
cv2.destroyAllWindows()