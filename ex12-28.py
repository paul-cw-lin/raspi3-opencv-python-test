import cv2

o = cv2.imread('img8.jpg')
img = o.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
t, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

x,y,w,h = cv2.boundingRect(contours[0])

cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0), 3)
aspectRatio = float(w)/h
print(aspectRatio)

cv2.imshow('result', img)
cv2.waitKey()
cv2.destroyAllWindows()