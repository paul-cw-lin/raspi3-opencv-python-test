import cv2

o = cv2.imread('img12.jpg')
img = o

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])
image = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0,255,0), 2)

distA = cv2.pointPolygonTest(hull, (320, 115), False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'A', (320, 115), font, 1, (255,0,0), 3)
print('distA = ', distA)

distB = cv2.pointPolygonTest(hull, (300, 200), False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'B', (300, 200), font, 1, (255,0,0), 3)
print('distB = ', distB)

distC = cv2.pointPolygonTest(hull, (440, 76), False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'C', (440, 76), font, 1, (255,0,0), 3)
print('distC = ', distC)

#print(hull)

cv2.imshow('result', image)
cv2.waitKey()
cv2.destroyAllWindows()
