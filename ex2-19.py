# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:57:03 2021

@author: d19fd
"""

import cv2

gray = cv2.imread('lena.bmp')
color = cv2.imread('lena-full.jpg')

print('gray.shape', gray.shape)
print('gray.size', gray.size)
print('gray.dtype', gray.dtype)

print('color.shape', color.shape)
print('color.size', color.size)
print('color.dtype', color.dtype)
