import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('yuko.jpg', 0)
img = o

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)

fshift[crow-35:crow+35, ccol-35:ccol+35] = 0
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)

#plt.subplot(121)

#plt.figure('original')
#plt.imshow(img, cmap='gray')

#plt.title('original')
#plt.axis('off')

#plt.subplot(111)
#plt.figure('iimg')
plt.figure('original')
plt.imshow(iimg, cmap='gray')
plt.title('iimg')
plt.axis('off')
plt.show()