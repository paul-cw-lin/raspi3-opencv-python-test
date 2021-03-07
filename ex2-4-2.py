import numpy as np
import cv2

'''
imgb = np.zeros((512,512), dtype=np.uint8)
cv2.imshow('black', imgb)

imgb[:,256:512] = 255
cv2.imshow('img b w', imgb)

cv2.imwrite('black-white.jpg', imgb)
'''

imgbw = cv2.imread('black-white.jpg')
cv2.imshow('b&w', imgbw)

cv2.waitKey()
cv2.destroyAllWindows()