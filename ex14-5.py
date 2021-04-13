import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('yuko.jpg', 0)
img = o

dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
print('dft.shape=', dft.shape)
dftShift = np.fft.fftshift(dft)
print('dftShift.shape=', dftShift.shape)
ishift = np.fft.ifftshift(dftShift)
print('ishift.shape=', ishift.shape)
iImg = cv2.idft(ishift)
print('iImg.shape=', iImg.shape)
iImg = cv2.magnitude(iImg[:, :, 0], iImg[:, :, 1])

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('original'), plt.axis('off')
plt.subplot(122), plt.imshow(iImg, cmap='gray')
plt.title('iImg'), plt.axis('off')
plt.show()