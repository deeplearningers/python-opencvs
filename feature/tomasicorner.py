# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 20:40:25 2014
@author: duan
"""
#目标跟踪中适合使用
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('pics\\star2.bmp')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,25,0.01,45)#获取图像中 25个最好的角点，角点质量水平0.01，两个角点之间欧式距离10
# 返回的结果是 [[ 311., 250.]] 两层括号的数组。
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
plt.imshow(img),plt.show()