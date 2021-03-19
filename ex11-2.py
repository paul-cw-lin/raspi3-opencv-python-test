import cv2

o = cv2.imread('yuko.jpg', cv2.IMREAD_GRAYSCALE)

r1 = cv2.pyrUp(o)

print('o.shape', o.shape)
print('r1.shape', r1.shape)

cv2.imshow('o', o)
cv2.imshow('r1', r1)

cv2.waitKey()
cv2.destroyAllWindows()
