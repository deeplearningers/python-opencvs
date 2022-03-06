# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:57:38 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']#解决matplotlib不显示中文问题

img = cv2.imread('1.bmp',0)
img1 = cv2.imread('LenaRGB.bmp',1)#彩色改成1
color = ('b','g','r')
# 别忘了中括号 [img],[0],None,[256],[0,256] ，只有 mask 没有中括号
#hist = cv2.calcHist([img],[0],None,[256],[0,256])

#单通道
plt.hist(img.ravel(),256,[0,256]);
#plt.show()

#多通道
# 对一个列表或数组既要遍历索引又要遍历元素时，使用内置 enumerrate 更直接
#enumerate 会将数组或列表组成一个索引序列，使我们再获取索引和索引内容的时候更加方便
for i,col in enumerate(color):
    histr = cv2.calcHist([img1],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
#plt.show()

#掩模直方图
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[48:150, 15:150] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)
# cv2.imshow('1',mask)
# cv2.waitKey(0)
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221), plt.imshow(img, 'gray'),plt.title('原图')
plt.subplot(222), plt.imshow(mask,'gray'),plt.title('掩模图')
plt.subplot(223), plt.imshow(masked_img, 'gray'),plt.title('原图+掩模图')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask),plt.title('直方图')
plt.xlim([0,256])
plt.show()

#直方图均衡化
#flatten()将数组变成一维
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()# 计算累积分布图
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
