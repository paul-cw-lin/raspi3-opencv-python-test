import cv2

o1 = cv2.imread('img6.jpg')
o2 = cv2.imread('img9.jpg')
o3 = cv2.imread('yuko2.jpg')

gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)

ret, binary1 = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
ret, binary2 = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
ret, binary3 = cv2.threshold(gray3, 127, 255, cv2.THRESH_BINARY)

contours1, hierarchy = cv2.findContours(binary1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours2, hierarchy = cv2.findContours(binary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours3, hierarchy = cv2.findContours(binary3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt1 = contours1[0]
cnt2 = contours2[0]
cnt3 = contours3[0]

ret0 = cv2.matchShapes(cnt1, cnt1, 1, 0.0)
ret1 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
ret2 = cv2.matchShapes(cnt1, cnt3, 1, 0.0)

print('same picture matchShape = ', ret0)
print('similar picture matchShape = ', ret1)
print('different matchShape = ', ret2)

cv2.imshow('o1', o1)
cv2.imshow('o2', o2)
cv2.imshow('o3', o3)
cv2.waitKey()
cv2.destroyAllWindows()