# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('pics\\Goldhill.bmp',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('pics\\Goldhill1.bmp',cv2.IMREAD_GRAYSCALE)
#创建orb检测器，最大特征点数,需要修改，5000太大。
orb = cv2.ORB_create(800)
# 提取并计算特征点
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
# 创建匹配对象
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)#匹配条件加严
#暴力匹配
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
#显示
result = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],img2,flags=2)
cv2.imshow('result',result)
cv2.waitKey()
