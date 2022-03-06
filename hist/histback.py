# -*- coding: utf-8 -*-
"""
如果一幅图像的区域中显示的是一种结构纹理或者一个独特的物体，那么这个区域的直方图可以看作一个概率函数，
它给的是某个像素属于该纹理或物体的概率。
所谓反向投影就是首先计算某一特征的直方图模型，然后使用模型去寻找测试图像中存在的该特征。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 要查找的目标图像
roi = cv2.imread('..\\pics\\caodi.bmp')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
# 待搜索的输入图像
target = cv2.imread('..\\pics\\meixi.bmp')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
#计算颜色直方图，h、s通道，histsize[180,256]即横轴分180个bin，纵轴分256个bin，考虑hs两个通道往直方图加点；
# ranges[,,,,]，M和I都是180*256大小，黑白代表了这个位置像素的个数，越白亮个数越多
M = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
I = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )#大图
# cv2.imshow('1',M)
# cv2.waitKey()
R = M/(I+1)#R越接近于1（越大）应该越是目标区域，概率图
#print R.max()
# cv2.normalize(prob,prob,0,255,cv2.NORM_MINMAX,0)
h,s,v = cv2.split(hsvt)#大图
B = R[h.ravel(),s.ravel()]#通过h、s的定位到R概率图中的概率值存为B
B = np.minimum(B,1)#概率值不超过1
B = B.reshape(hsvt.shape[:2])#大图的行列，hs比值图
#去噪声
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))#椭圆算子
cv2.filter2D(B,-1,disc,B)#卷积
B = np.uint8(B)#转换数据类型
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)#归一化

ret,thresh = cv2.threshold(B,50,255,0)#二值化显示
res = cv2.bitwise_and(target,target,mask = thresh)#与操作，在原图中分割出目标区域
#cv2.imshow('B',B)
#cv2.imshow('thresh',thresh)
res = np.hstack((target,cv2.merge((B,B,B)),cv2.merge((thresh,thresh,thresh)),res))#竖向排列,排列的通道数必须一致
cv2.imshow("result",res)
cv2.waitKey(0)


#opencv进行直方图重映射--提取感兴趣区域
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )#计算hs直方图
# 归一化之后的直方图便于显示，归一化之后就成了 0 到 255 之间的数了。
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
# 此处卷积可以把分散的点连在一起
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
dst=cv2.filter2D(dst,-1,disc)#filter2D作用取决于掩模结构
ret,thresh = cv2.threshold(dst,50,255,0)#二值化
# 别忘了是三通道图像，因此这里使用 merge 变成 3 通道
thresh = cv2.merge((thresh,thresh,thresh))
# 按位与操作
res = cv2.bitwise_and(target,thresh)
res = np.hstack((target,thresh,res))
#cv2.imwrite('res.jpg',res)
# 显示图像
cv2.imshow('opencv',res)
cv2.waitKey(0)

cv2.destroyAllWindows()