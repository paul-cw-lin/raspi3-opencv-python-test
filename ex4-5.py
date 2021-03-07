# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:06:57 2021

@author: d19fd
"""

import cv2

nachan = cv2.imread('nachan2.jpg')

rgb = cv2.cvtColor(nachan, cv2.COLOR_BGR2RGBA)

print('nachan.shape', nachan.shape)

cv2.imshow('nachan', nachan)
cv2.imshow('rgb', rgb)

cv2.waitKey()
cv2.destroyAllWindows()