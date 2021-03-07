# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:45:35 2021

@author: d19fd
"""

import cv2

img = cv2.imread('emma3.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
minHue = 5
maxHue = 170
hueMask = cv2.inRange(h, minHue, maxHue)

minSat = 25
maxSat = 166
satMask = cv2.inRange(s, minSat, maxSat)

mask = hueMask & satMask

roi = cv2.bitwise_and(img, img, mask= mask)

cv2.imshow('img', img)
cv2.imshow('ROI', roi)

cv2.waitKey()
cv2.destroyAllWindows()
