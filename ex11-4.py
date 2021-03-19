import cv2

o = cv2.imread('yuko.jpg')

up = cv2.pyrUp(o)
down = cv2.pyrDown(up)
diff = down-o

print('o.shape', o.shape)
print('down.shape', down.shape)

cv2.imshow('o', o)
cv2.imshow('down', down)
cv2.imshow('diff', diff)

cv2.waitKey()
cv2.destroyAllWindows()
