import cv2

o1 = cv2.imread('img12.jpg')
img1 = o1
cv2.imshow('original1', img1)

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
t, binary1 = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
contours1, hierarchy = cv2.findContours(binary1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours1[0]

o2 = cv2.imread('img14.jpg')
img2 = o2
cv2.imshow('original2', img2)

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
t, binary2 = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
contours2, hierarchy = cv2.findContours(binary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours2[0]

o3 = cv2.imread('img10-2.jpg')
img3 = o3
cv2.imshow('original3', img3)

gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
t, binary3 = cv2.threshold(gray3, 127, 255, cv2.THRESH_BINARY)
contours3, hierarchy = cv2.findContours(binary3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt3 = contours3[0]

sd = cv2.createShapeContextDistanceExtractor()

d1 = sd.computeDistance(cvt1, cnt1)
print('The distance with itself d1 = ', d1)

d2 = sd.computeDistance(cnt1, cnt2)
print('The distance between rotation item = ', d2)

d3 = sd.computeDistance(cnt1, cnt3)
print('The distance between different part = ', d3)

cv2.waitKey()
cv2.destroyAllWindows()