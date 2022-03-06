# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:37:21 2014
@author: duan
"""

import cv2
import numpy as np

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']#解决matplotlib不显示中文问题

img = cv2.imread('pics\\LenaRGB.bmp',1)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#opecv
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
#numpy
hue=hsv[:,:,0]
sat=hsv[:,:,1]
hist2, xbins, ybins = np.histogram2d(hue.ravel(),sat.ravel(),[180,256],[[0,180],[0,256]])
#显示
cv2.imshow('1',hist)
cv2.imshow('2',hist2)
cv2.waitKey()
