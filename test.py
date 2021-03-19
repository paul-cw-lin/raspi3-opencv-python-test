import cv2
import numpy as np

img = cv2.imread('img3.jpg', 0)

ret, out1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(out1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#print(type(contours))
#print(type(contours[0]))

print('contours No.= ', len(contours))
print('contours[0]=\n', contours[0:])

print('hierarchy=\n', hierarchy)

#print('contours[0]= ', len(contours[0]))
#print('contours[1]= ', len(contours[1]))
#print('contours[2]= ', len(contours[2]))

#print('contours[0].shape= ', contours[0].shape)
#print('contours[1].shape= ', contours[1].shape)
#print('contours[2].shape= ', contours[2].shape)

#print(contours[0])

#cv2.imshow('img', img)
#cv2.imshow('out1', out1)

#cv2.waitKey()
#cv2.destroyAllWindows()