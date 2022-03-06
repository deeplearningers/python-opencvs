<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:10:49 2014
@author: duan
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('pics\\qianbi.bmp')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('thresh',thresh)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)#先腐蚀后膨胀,去掉白色噪点
cv2.imshow('opening',opening)
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)#膨胀
cv2.imshow('sure_bg',sure_bg)
# 第二个参数 0,1,2 分别表示 CV_DIST_L1, CV_DIST_L2 , CV_DIST_C
dist_transform = cv2.distanceTransform(opening,1,3)#3是掩模大小
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
sure_fg = np.uint8(sure_fg)
cv2.imshow('sure_fg',sure_fg)#肯定是硬币区域

unknown = cv2.subtract(sure_bg,sure_fg)#相减
cv2.imshow('unknown',unknown)


# Marker labelling不确定区域标为0，其他的从1开始标记
ret, markers1 = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers1+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0
#分水岭算法
markers3 = cv2.watershed(img,markers)
img[markers3 == -1] = [255,0,0]#边界
img[markers3 == 0] = [0,255,0]#未知的
img[markers3 == 1] = [0,0,255]#背景
for i in range(50):
    img[markers3 == 2+i] = [0,10+30*i,0]

cv2.imshow('img',img)
=======
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:10:49 2014
@author: duan
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('pics\\qianbi.bmp')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('thresh',thresh)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)#先腐蚀后膨胀,去掉白色噪点
cv2.imshow('opening',opening)
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)#膨胀
cv2.imshow('sure_bg',sure_bg)
# 第二个参数 0,1,2 分别表示 CV_DIST_L1, CV_DIST_L2 , CV_DIST_C
dist_transform = cv2.distanceTransform(opening,1,3)#3是掩模大小
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
sure_fg = np.uint8(sure_fg)
cv2.imshow('sure_fg',sure_fg)#肯定是硬币区域

unknown = cv2.subtract(sure_bg,sure_fg)#相减
cv2.imshow('unknown',unknown)


# Marker labelling不确定区域标为0，其他的从1开始标记
ret, markers1 = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers1+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0
#分水岭算法
markers3 = cv2.watershed(img,markers)
img[markers3 == -1] = [255,0,0]#边界
img[markers3 == 0] = [0,255,0]#未知的
img[markers3 == 1] = [0,0,255]#背景
for i in range(50):
    img[markers3 == 2+i] = [0,10+30*i,0]

cv2.imshow('img',img)
>>>>>>> 25f74d288cff6279e8d50298f4b7bc15d138bd62
cv2.waitKey()