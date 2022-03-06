import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.bmp')
kernel = np.ones((5,5),np.float32)/25#滤波器核
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
blur2= cv2.boxFilter(img,-1,(5,5))
blur3 = cv2.GaussianBlur(img,(5,5),0)#标准差0
median = cv2.medianBlur(img,5)
blur4 = cv2.bilateralFilter(img,9,75,75)

plt.subplot(171),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(172),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(173),plt.imshow(blur),plt.title('Averaging2')
plt.xticks([]), plt.yticks([])
plt.subplot(174),plt.imshow(blur2),plt.title('Averaging3')
plt.xticks([]), plt.yticks([])
plt.subplot(175),plt.imshow(blur3),plt.title('Averaging4')
plt.xticks([]), plt.yticks([])
plt.subplot(176),plt.imshow(median),plt.title('Averaging5')
plt.xticks([]), plt.yticks([])
plt.subplot(177),plt.imshow(blur4),plt.title('Averaging6')
plt.xticks([]), plt.yticks([])
plt.show()
