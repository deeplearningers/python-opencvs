# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('pics\\Goldhill.bmp',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('pics\\Goldhill1.bmp',cv2.IMREAD_GRAYSCALE)
#创建sift检测器
sift = cv2.xfeatures2d.SIFT_create(100)
# 提取并计算特征点
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
# 创建匹配器，并knn匹配
bf = cv2.BFMatcher()#匹配条件加严
matches = bf.knnMatch(des1,des2, k=2)
# 比值测试，获取与A距离最近的点B和次近C，当 B/C小于阈值0.75才是匹配，因为假设匹配是一一对应的，真正的匹配的理想距离为 0
#Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
#显示
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)#默认也是绘制两条最佳匹配路线
cv2.imshow('result',img3)
cv2.waitKey()
