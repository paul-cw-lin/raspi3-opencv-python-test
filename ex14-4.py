import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('yuko.jpg', 0)
img = o

dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
result = 20*np.log(cv2.magnitude(dftShift[:, :, 0], dftShift[:, :, 1]))

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('original'), plt.axis('off')
plt.subplot(122), plt.imshow(result, cmap='gray')
plt.title('result'), plt.axis('off')
plt.show()