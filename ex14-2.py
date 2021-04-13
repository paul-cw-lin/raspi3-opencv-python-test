import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('yuko.jpg', 0)
img = o

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)

iimg = np.abs(iimg)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('original'), plt.axis('off')
plt.subplot(122), plt.imshow(iimg, cmap='gray')
plt.title('iimg'), plt.axis('off')
plt.show()