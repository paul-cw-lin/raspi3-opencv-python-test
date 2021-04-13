import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('yuko.jpg')
img = o

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

f = np.fft.fft2(gray)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121)
plt.imshow(gray, cmap='gray')
plt.title('original')
plt.axis('off')

plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Result')
plt.axis('off')

plt.show()