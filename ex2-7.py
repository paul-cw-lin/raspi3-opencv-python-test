# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:05:34 2021

@author: d19fd
"""

import numpy as np
img = np.random.randint(10,99,size=[5,5],dtype=np.uint8)
print('img=\n', img)
print('read pixel img.item(3,2) =', img.item(3,2))
img.itemset((3,2), 255)
print('fixed img=\n', img)
print('fixed pixel img.item(3,2)', img.item(3,2))