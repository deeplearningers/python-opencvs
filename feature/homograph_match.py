# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10
img1 = cv2.imread('pics\\Goldhill.bmp',0)
img2 = cv2.imread('pics\\Goldhill1.bmp',0)
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
        good.append(m)#此处改成了m而不是[m]

#
if len(good)>MIN_MATCH_COUNT:
# 获取关键点的坐标
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
    #计算单应性矩阵M，第四个参数取值范围在1到10，拒绝一个点对的阈值5-原图像的点经过变换后点与目标图像上对应点的误差，超过误差就认为是 outlier
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()
    # 获得原图像的高和宽
    h,w = img1.shape
    # 使用得到的变换矩阵对原图像的四个角进行变换，获得在目标图像上对应的坐标
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)
    # 原图像为灰度图
    cv2.polylines(img2,[np.int32(dst)],True,255,10, cv2.LINE_AA)
else:
    print("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))
    matchesMask = None
#显示
draw_params = dict(matchColor = (0,255,0), singlePointColor = None,matchesMask = matchesMask,flags = 2)
img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
#plt.imshow(img3, 'gray'),plt.show()
cv2.imshow('result',img3)
cv2.waitKey()
