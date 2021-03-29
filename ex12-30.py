import cv2

o = cv2.imread('img10-2.jpg')
img = o.copy()
img = img [5:318, 5:480]
#cv2.imshow('img', img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
t, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours[2], -1, (0,0,255), 2)
cntArea = cv2.contourArea(contours[2])
hull = cv2.convexHull(contours[2])
hullArea = cv2.contourArea(hull)

cv2.polylines(img, [hull], True, (0,255,0), 2)

solidity = float(cntArea)/hullArea

print(solidity)

cv2.imshow('result', img)

cv2.waitKey()
cv2.destroyAllWindows()