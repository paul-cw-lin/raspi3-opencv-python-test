import cv2

o = cv2.imread('yuko.jpg')

down = cv2.pyrDown(o)
up = cv2.pyrUp(down)
diff = up-o

print('o.shape', o.shape)
print('up.shape', up.shape)

cv2.imshow('o', o)
cv2.imshow('up', up)
cv2.imshow('diff', diff)

cv2.waitKey()
cv2.destroyAllWindows()
