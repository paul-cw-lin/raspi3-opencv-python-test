# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:59:59 2021

@author: d19fd
"""

import cv2

nachan = cv2.imread('nachan1.jpg')

gray = cv2.cvtColor(nachan, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

print('nachan.shape', nachan.shape)
print('gray.shape', gray.shape)
print('rgb.shape', rgb.shape)

cv2.imshow('nachan', nachan)
cv2.imshow('gray', gray)
cv2.imshow('rgb', rgb)

cv2.waitKey()
cv2.destroyAllWindows()
