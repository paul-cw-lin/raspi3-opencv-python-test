import cv2

o = cv2.imread('img10.jpg')
img = o

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

hull = cv2.convexHull(contours[0], returnPoints=True)
print('returnPoints = True, return value hull (coordinate) :\n', hull)
hull2 = cv2.convexHull(contours[0], returnPoints=False)
print('returnPoints = False, return value hull (index):\n', hull2)