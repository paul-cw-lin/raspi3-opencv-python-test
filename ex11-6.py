import cv2
import numpy as np

o = cv2.imread('yuko.jpg')
G0 = o

G1 = cv2.pyrDown(G0)
L0 = o-cv2.pyrUp(G1)
RO = L0 + cv2.pyrUp(G1)

print('o.shape', o.shape)
print('RO.shape', RO.shape)
result = abs(RO-o)
print('result= ', np.sum(result))

cv2.imshow('o', o)
cv2.imshow('RO', RO)

cv2.waitKey()
cv2.destroyAllWindows()
