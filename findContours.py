# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:05:52 2014
@author: duan
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']#解决matplotlib不显示中文问题

im = cv2.imread('source.bmp')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,120,255,0)
image, contours, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(im, contours, -1, (255,0,0), 3)

#矩
cnt = contours[2]
M = cv2.moments(cnt)
#重心
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
#面积
area = cv2.contourArea(cnt)
print(M)
print(cx,cy,area)
#轮廓近似
epsilon = 0.008*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,False)
cv2.drawContours(im, approx, -1, (255,0,255), 5)

cv2.imshow('1',img)
cv2.waitKey(0)