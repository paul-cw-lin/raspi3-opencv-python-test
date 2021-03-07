# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:10:39 2021

@author: d19fd
"""

import cv2
import numpy as np

opencv = cv2.imread('opencv.png')
hsv = cv2.cvtColor(opencv, cv2.COLOR_BGR2HSV)
cv2.imshow('opencv', opencv)

minBlue = np.array([110,50,50])
maxBlue = np.array([130,255,255])

mask = cv2.inRange(hsv, minBlue, maxBlue)

blue = cv2.bitwise_and(opencv, opencv, mask= mask)
cv2.imshow('blue', blue)

cv2.waitKey()
cv2.destroyAllWindows()
