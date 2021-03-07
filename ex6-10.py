# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:10:38 2021

@author: d19fd
"""

import cv2

img = cv2.imread('mai.jpg', 0)

t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

cv2.imshow('img', img)
cv2.imshow('rst', rst)

cv2.waitKey()
cv2.destroyAllWindows()
