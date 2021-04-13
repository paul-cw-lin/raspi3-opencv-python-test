import cv2
import numpy as np
import matplotlib.pyplot as plt

a = np.array([[3,6,8,77,66], [1,2,88,3,98]])
print(a)
print(a[::-1])
b = np.where(a>5)
print(b)
for i in zip(*b):
    print(i)

cv2.waitKey()
cv2.destroyAllWindows()