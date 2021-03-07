# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np

img = np.zeros((8,8), dtype=np.uint8)
print('img=\n', img)
cv2.imshow('one', img)
print('read pixel img[0,3]=', img[0,3])
img[0,3] = 255
img[1,3] = 255
img[2,3] = 255
img[3,3] = 255
img[4,3] = 255
img[5,3] = 255
img[6,3] = 255
img[7,3] = 255
print('fixed img=\n', img)
print('read fixed pixel img[0,3]=', img[0,3])
cv2.imshow('two', img)
cv2.waitKey()
cv2.destroyAllWindows()
