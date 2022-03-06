# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:30:10 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']#解决matplotlib不显示中文问题

img = cv2.imread('pics\\meixi.bmp',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
# 这里构建振幅图的公式没学过
magnitude_spectrum = 20*np.log(np.abs(fshift))
#逆变换
rows, cols = img.shape
crow,ccol = rows/2 , cols/2
fshift[int(crow-40):int(crow+40), int(ccol-40):int(ccol+40)] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
# 取绝对值
img_back = np.abs(img_back)


#opencv中函数
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum1 = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
#opencv低通
rows1, cols1 = img.shape
crow1,ccol1 = rows1/2 , cols1/2
# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows1,cols1,2),np.uint8)
mask[int(crow1-30):int(crow1+30), int(ccol1-30):int(ccol1+30)] = 1#低频区域设置为1
# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back1 = cv2.idft(f_ishift)
img_back1 = cv2.magnitude(img_back1[:,:,0],img_back1[:,:,1])
#显示
plt.subplot(231),plt.imshow(img, cmap = 'gray')
plt.title('原图'), plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('傅里叶变换-直流分量居中-构建振幅图'), plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(img_back,cmap = 'gray')
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(magnitude_spectrum1,cmap = 'gray')
plt.title('opencv'), plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(img_back1,cmap = 'gray')
plt.title('opencv-傅里叶逆变换'), plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()