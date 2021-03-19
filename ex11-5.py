import cv2

o = cv2.imread('yuko.jpg')

g0 = o
g1 = cv2.pyrDown(g0)
g2 = cv2.pyrDown(g1)
g3 = cv2.pyrDown(g2)

L0 = g0-cv2.pyrUp(g1)
L1 = g1-cv2.pyrUp(g2)
L2 = g2-cv2.pyrUp(g3)

print('L0.shape', L0.shape)
print('L2.shape', L1.shape)
print('L2.shape', L2.shape)

cv2.imshow('L0', L0)
cv2.imshow('L1', L1)
cv2.imshow('L2', L2)

cv2.waitKey()
cv2.destroyAllWindows()