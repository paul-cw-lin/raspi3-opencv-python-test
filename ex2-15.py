# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:55:06 2021

@author: d19fd
"""

import cv2

lena = cv2.imread('lena-full.jpg', cv2.IMREAD_UNCHANGED)
hallie = cv2.imread('hallie.jpg', cv2.IMREAD_UNCHANGED)
#cv2.imshow('lena', lena)
#cv2.imshow('hallie', hallie)
face = lena[220:400,250:350]
hallie[80:260,180:280] = face
cv2.imshow('result', hallie)
cv2.waitKey()
cv2.destroyAllWindows()