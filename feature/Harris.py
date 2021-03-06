# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:55:47 2014
@author: duan
"""
import cv2
import numpy as np
filename = 'pics\\chessboard.bmp'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)
# find centroids
#connectedComponentsWithStats(InputArray image, OutputArray labels, OutputArray stats,
#OutputArray centroids, int connectivity=8, int ltype=CV_32S)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)#寻找质心
# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)#定义迭代次数，达到或者精度条件满足后迭代就会停止
#Python: cv2.cornerSubPix(image, corners, winSize, zeroZone, criteria)
#zeroZone – Half of the size of the dead region in the middle of the search zone
#over which the summation in the formula below is not done. It is used sometimes
# to avoid possible singularities of the autocorrelation matrix. The value of (-1,-1)
# indicates that there is no such a size.
# 返回值由角点坐标组成的一个数组（而非图像）
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
# Now draw them
res = np.hstack((centroids,corners))#原角点质心-亚像素角点(绿色)
#np.int0 可以用来省略小数点后面的数字（非四舍五入）。
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]#红，x-列；y-行
img[res[:,3],res[:,2]] = [0,255,0]#绿
cv2.imwrite('pics\\subpixel5.png',img)
cv2.imshow('1',img)
cv2.waitKey()