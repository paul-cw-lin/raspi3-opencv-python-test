import cv2
import numpy as np

o = cv2.imread('img8.jpg')
img = o

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
t, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(gray.shape, dtype=np.uint8)
cnt = contours[0]
cv2.drawContours(mask, [cnt], 0, 255, -1)

leftpole = tuple(cnt [ cnt[:,:,0].argmin() ] [0])
rightpole = tuple(cnt [ cnt[:,:,0].argmax() ] [0])
toppole = tuple(cnt [ cnt[:,:,1].argmin() ] [0])
bottompole = tuple(cnt [ cnt[:,:,1].argmax() ] [0])

print('leftpole = ', leftpole)
print('rihtpole = ', rightpole)
print('toppole = ', toppole)
print('bottompole = ', bottompole)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'A', leftpole, font, 1, (0,255,0), 2)
cv2.putText(img, 'B', rightpole, font, 1, (0,255,0), 2)
cv2.putText(img, 'C', toppole, font, 1, (0,255,0), 2)
cv2.putText(img, 'D', bottompole, font, 1, (0,255,0), 2)

cv2.circle(img, leftpole, 10, (0,0,255), 2)
cv2.circle(img, rightpole, 10, (0,0,255), 2)
cv2.circle(img, toppole, 10, (0,0,255), 2)
cv2.circle(img, bottompole, 10, (0,0,255), 2)

cv2.imshow('result', img)

cv2.waitKey()
cv2.destroyAllWindows()