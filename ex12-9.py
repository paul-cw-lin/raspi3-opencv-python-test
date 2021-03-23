import cv2

o1 = cv2.imread('img6.jpg')
gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)
HuM1 = cv2.HuMoments(cv2.moments(gray1)).flatten()

o2 = cv2.imread('img7.jpg')
gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)
HuM2 = cv2.HuMoments(cv2.moments(gray2)).flatten()

o3 = cv2.imread('yuko2.jpg')
gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)
HuM3 = cv2.HuMoments(cv2.moments(gray3)).flatten()

print('o1.shape= ', o1.shape)
print('o2.shape= ', o2.shape)
print('o3.shape= ', o3.shape)

print('\ncv2.moments(gray1)=\n', cv2.moments(gray1))
print('\ncv2.moments(gray2)=\n', cv2.moments(gray2))
print('\ncv2.moments(gray3)=\n', cv2.moments(gray3))

print('\nHuM1 =\n', HuM1)
print('\nHuM2 =\n', HuM2)
print('\nHuM3 =\n', HuM3)

print('\nHuM1-HuM2 =\n', HuM1-HuM2)
print('\nHuM1-HuM3 =\n', HuM1-HuM3)

cv2.imshow('o1', o1)
cv2.imshow('o2', o2)
cv2.imshow('o3', o3)

cv2.waitKey()
cv2.destroyAllWindows()