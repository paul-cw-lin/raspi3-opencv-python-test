# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:46:33 2021

@author: d19fd
"""

import cv2

img = cv2.imread('blonde.jpg', 0)

t1, thd = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
t2, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('img', img)
cv2.imshow('thd', thd)
cv2.imshow('otsu', otsu)

cv2.waitKey()
cv2.destroyAllWindows()
