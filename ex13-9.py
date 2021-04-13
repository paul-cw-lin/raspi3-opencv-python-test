import cv2
import numpy as np

mask = np.zeros([512,512], dtype=np.uint8)
mask[170:340, 170:340]=255
cv2.imshow('mask', mask)

cv2.waitKey()
cv2.destroyAllWindows()