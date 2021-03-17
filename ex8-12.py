import cv2

kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

print('k1=\n', kernel1)
print('k2=\n', kernel2)
print('k3=\n', kernel3)