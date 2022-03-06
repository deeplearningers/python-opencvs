# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt
imgL = cv2.imread('tsukuba_l.png',0)
imgR = cv2.imread('tsukuba_r.png',0)
#立体匹配算法：BM、SGBM和GC
#blockSize奇数；numberOfDisparities：视差搜索范围，其值必须为16的整数倍
stereo_BM = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity_BM = stereo_BM.compute(imgL,imgR)
#SGBM
blockSize = 48
stereo_SGBM = cv2.StereoSGBM_create(minDisparity=1,#最小可能的差异值。通常情况下，它是零，但有时整流算法可能会改变图像，所以这个参数需要作相应的调整。
             numDisparities=16,#最大差异减去最小差异。该值总是大于零。在当前的实现中，该参数必须可以被16整除。
             blockSize=15,#匹配的块大小。它必须是> = 1的奇数。通常情况下，它应该在3-11的范围内
             uniquenessRatio = 10,#最佳（最小）计算成本函数值应该“赢”第二个最佳值以考虑找到的匹配正确的百分比保证金。通常，5-15范围内的值就足够了。
             speckleWindowSize = 150,#平滑视差区域的最大尺寸，以考虑其噪声斑点和无效。将其设置为0可禁用斑点过滤。否则，将其设置在50-200的范围内。
             speckleRange = 2,#每个连接组件内的最大视差变化。如果你做斑点过滤，将参数设置为正值，它将被隐式乘以16.通常，1或2就足够好了。
             disp12MaxDiff = 200,#左右视差检查中允许的最大差异（以整数像素为单位）。将其设置为非正值以禁用检查
             P1 = 8*3*blockSize**2,#控制视差平滑度的第一个参数。P1是相邻像素之间的视差变化加或减1的惩罚。
             P2 = 32*3*blockSize**2)#第二个参数控制视差平滑度。值越大，差异越平滑。P2是相邻像素之间的视差变化超过1的惩罚。该算法需要P2> P1。
disparity_SGBM = stereo_SGBM.compute(imgL,imgR)
#GC
#stereo_BM = cv2.GC
#显示
plt.subplot(121), plt.imshow(disparity_BM,'gray'),plt.title('BM')
plt.subplot(122), plt.imshow(disparity_SGBM,'gray'),plt.title('SGBM')
#plt.subplot(133), plt.imshow(mask,'gray'),plt.title('GC')
plt.show()