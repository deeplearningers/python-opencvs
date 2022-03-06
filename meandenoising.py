<<<<<<< HEAD
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

# img = cv2.imread('pics\\die.bmp')
# b,g,r=cv2.split(img)
# img1=cv2.merge((r,g,b))
# #过滤器强度10，窗口7-21
# dst = cv2.fastNlMeansDenoisingColored(img1,None,10,10,7,21)
# plt.subplot(121),plt.imshow(img1)
# plt.subplot(122),plt.imshow(dst)
# plt.show()

cap = cv2.VideoCapture('pics\\video2.avi')
# create a list of first 5 frames
img = [cap.read()[1] for i in range(5)]#cap.read（）是一个元组，[0]是bool,[1]才是图像
# convert all to grayscale
gray = [cv2.cvtColor(i, cv2.COLOR_BGR2GRAY) for i in img]
# convert all to float64
gray = [np.float64(i) for i in gray]
# create a noise of variance 25
noise = np.random.randn(*gray[1].shape)*10#取第一帧图像加上噪声，第一个*指放入元组
# Add this noise to images
noisy = [i+noise for i in gray]
# Convert back to uint8
noisy = [np.uint8(np.clip(i,0,255)) for i in noisy]#将i限定在0~255之间
# Denoise 3rd frame considering all the 5 frames
dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 10, 7, 21)#传入5帧，对第3帧去燥,过滤器强度10关键。
plt.subplot(131),plt.imshow(gray[2],'gray'),plt.title('original')
plt.subplot(132),plt.imshow(noisy[2],'gray'),plt.title('noisy')
plt.subplot(133),plt.imshow(dst,'gray'),plt.title('denoising')
=======
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

# img = cv2.imread('pics\\die.bmp')
# b,g,r=cv2.split(img)
# img1=cv2.merge((r,g,b))
# #过滤器强度10，窗口7-21
# dst = cv2.fastNlMeansDenoisingColored(img1,None,10,10,7,21)
# plt.subplot(121),plt.imshow(img1)
# plt.subplot(122),plt.imshow(dst)
# plt.show()

cap = cv2.VideoCapture('pics\\video2.avi')
# create a list of first 5 frames
img = [cap.read()[1] for i in range(5)]#cap.read（）是一个元组，[0]是bool,[1]才是图像
# convert all to grayscale
gray = [cv2.cvtColor(i, cv2.COLOR_BGR2GRAY) for i in img]
# convert all to float64
gray = [np.float64(i) for i in gray]
# create a noise of variance 25
noise = np.random.randn(*gray[1].shape)*10#取第一帧图像加上噪声，第一个*指放入元组
# Add this noise to images
noisy = [i+noise for i in gray]
# Convert back to uint8
noisy = [np.uint8(np.clip(i,0,255)) for i in noisy]#将i限定在0~255之间
# Denoise 3rd frame considering all the 5 frames
dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 10, 7, 21)#传入5帧，对第3帧去燥,过滤器强度10关键。
plt.subplot(131),plt.imshow(gray[2],'gray'),plt.title('original')
plt.subplot(132),plt.imshow(noisy[2],'gray'),plt.title('noisy')
plt.subplot(133),plt.imshow(dst,'gray'),plt.title('denoising')
>>>>>>> 25f74d288cff6279e8d50298f4b7bc15d138bd62
plt.show()