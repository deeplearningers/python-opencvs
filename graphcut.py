# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:24:24 2014
@author: duan
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('pics\\meixi.bmp')
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,350,200)
# 函数的返回值是更新的 mask, bgdModel, fgdModel,迭代5次
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
#cv2.GC_BGD,cv2.GC_FGD,cv2.GC_PR_BGD,cv2.GC_PR_FGD分别是0 1 2 3
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')#mask=0或2即背景则是0，否则是1
img = img*mask2[:,:,np.newaxis]
plt.imshow(img),plt.colorbar(),plt.show()