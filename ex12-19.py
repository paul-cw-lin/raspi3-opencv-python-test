import cv2

o = cv2.imread('img8.jpg')
img = o

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# epsilon = 0.1 x Perimeter
adp = img.copy()
epsilon = 0.1*cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0,255,0), 2)
cv2.imshow('result0.1', adp)

# epsilon = 0.09 x Perimeter
adp = img.copy()
epsilon = 0.09*cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0,255,0), 2)
cv2.imshow('result0.09', adp)

# epsilon = 0.05 x Perimeter
adp = img.copy()
epsilon = 0.05*cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0,255,0), 2)
cv2.imshow('result0.05', adp)

# epsilon = 0.01 x Perimeter
adp = img.copy()
epsilon = 0.01*cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0,255,0), 2)
cv2.imshow('result0.01', adp)

# epsilon = 0.02 x Perimeter
adp = img.copy()
epsilon = 0.02*cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0,255,0), 2)
cv2.imshow('result0.02', adp)

cv2.waitKey()
cv2.destroyAllWindows()