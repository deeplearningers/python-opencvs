# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt
img1 = cv2.imread('pics\\Goldhill.bmp',0) #queryImage
img2 = cv2.imread('pics\\Goldhill1.bmp',0) # trainImage
#创建sift检测器
sift = cv2.xfeatures2d.SIFT_create(10)
# 提取并计算特征点
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# FLANN匹配器 parameters
FLANN_INDEX_KDTREE = 0#对于SIFT和URF算法
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50) # 遍历的次数
flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)

# Need to draw only good matches, 创建掩模
matchesMask = [[0,0] for i in range(len(matches))]
# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i]=[1,0]
draw_params = dict(matchColor = (0,255,0),singlePointColor = (255,0,0),matchesMask = matchesMask,flags = 0)
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
#plt.imshow(img3,),plt.show()
cv2.imshow('result',img3)
cv2.waitKey()