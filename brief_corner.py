# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:28:03 2014
@author: duan
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('pics\\Goldhill.bmp',0)
# 初始化STAR检测器
star = cv2.xfeatures2d.StarDetector_create()
# 初始化BRIEF特征提取器
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
# 使用STAR寻找特征点
kp = star.detect(img,None)
# 计算特征描述符
kp, des = brief.compute(img, kp)
#显示
img = cv2.drawKeypoints(img,kp,img,color=(255,0,0))
print(brief.descriptorSize())#特征描述子的默认32字节
print(des.shape)

cv2.imshow('Brief',img)
cv2.waitKey(0)

