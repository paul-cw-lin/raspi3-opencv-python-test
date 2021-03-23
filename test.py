import cv2
import numpy as np

img = cv2.imread('yuko.jpg')
img2 = cv2.imread('yuko2.jpg')
img4 = cv2.imread('yuko4.jpg')

#r1 = cv2.Canny(img, 32, 128)

#cv2.imshow('o', img)
#cv2.imshow('r1', r1)
#img2 = cv2.resize(img, (480,270))
cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('img4', img4)
#cv2.imwrite('yuko4.jpg', img2)


#ret, out1 = cv2.threshold(img, 135, 255, cv2.THRESH_BINARY)

#cv2.imshow('binary', out1)
#cv2.imwrite('paul-binary.jpg', out1)

'''
contours, hierarchy = cv2.findContours(out1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#print(type(contours))
#print(type(contours[0]))

print('contours No.= ', len(contours))
print('contours[0]=\n', contours[0:])

print('hierarchy=\n', hierarchy)
'''
#print('contours[0]= ', len(contours[0]))
#print('contours[1]= ', len(contours[1]))
#print('contours[2]= ', len(contours[2]))

#print('contours[0].shape= ', contours[0].shape)
#print('contours[1].shape= ', contours[1].shape)
#print('contours[2].shape= ', contours[2].shape)

#print(contours[0])


#cv2.imshow('out1', out1)

cv2.waitKey()
cv2.destroyAllWindows()