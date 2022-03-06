# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:46:12 2014
@author: duan
"""
import cv2
import numpy as np

img = cv2.imread('dragon.bmp',0)
blur = cv2.GaussianBlur(img,(5,5),0)

# 计算归一化直方图
hist = cv2.calcHist([blur],[0],None,[256],[0,256])#使用的图像；使用的通道；没有使用mask；HistSize；直方图柱的范围
hist_norm = hist.ravel()/hist.max()#ravel函数功能是将多维数组降为一维数组
Q = hist_norm.cumsum()#求累积次数
bins = np.arange(256)
fn_min = np.inf
thresh = -1
for i in range(1,256):
    p1,p2 = np.hsplit(hist_norm,[i]) # probabilities
    q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes
    b1,b2 = np.hsplit(bins,[i]) # weights
    # finding means and variances
    m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
    v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
    # calculates the minimization function
    fn = v1*q1 + v2*q2
    if fn < fn_min:
        fn_min = fn
        thresh = i
# find otsu's threshold value with OpenCV function
ret, otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(thresh,ret)