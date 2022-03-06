# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:57:38 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']#解决matplotlib不显示中文问题

img1 = cv2.imread('star1.bmp',0)
img2 = cv2.imread('star2.bmp',0)
ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours[0]
image1, contours1, hierarchy1 = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours1[0]
ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print(ret)

plt.figure('返回值越小，匹配度越好') #图像标题
plt.subplot(1,2,1),plt.imshow(thresh,'gray')
plt.title('图1'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(thresh2, 'gray')
plt.title('图2'), plt.xticks([]), plt.yticks([])
#plt.text(-50,200,r'$\mu=100$',fontsize=15)# 注释
plt.text(-80,200,'匹配值：'+str(ret),fontsize=15)
plt.show()
