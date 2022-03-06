# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:57:38 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']#解决matplotlib不显示中文问题
img = cv2.imread('Lena.bmp',0)
#============直方图均衡化前
#flatten()将数组变成一维
hist,bins = np.histogram(img.flatten(),256,[0,256])#np直方图绘制函数
cdf = hist.cumsum()# 计算累积分布图
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.subplot(131), plt.plot(hist, color = 'b'),plt.plot(cdf_normalized, color = 'r'),plt.title('均衡前直方图')
plt.legend(('均衡化前直方图','均衡化前累积分布图'), loc = 'upper left')

#============直方图均衡化后
# 构建 Numpy 掩模数组， cdf 为原数组，当数组元素为 0 时，掩盖（计算时被忽略）。
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())#均衡化公式，归一化到0~256
# 对被掩盖的元素赋值，这里赋值为 0
cdf2 = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf2[img]
hist2,bins2 = np.histogram(img2.flatten(),256,[0,256])#np直方图绘制函数
cdf3 = hist2.cumsum()# 计算累积分布图
cdf_normalized2 = cdf3 * hist2.max()/ cdf3.max()
#显示
cv2.imwrite('res1.png',img2)
plt.subplot(132), plt.plot(hist2, color = 'b'),plt.plot(cdf_normalized2, color = 'r'),plt.title('均衡后直方图')
plt.xlim([0,256])
plt.legend(('均衡化后直方图','均衡化后累积分布图'), loc = 'upper left')
#==============opencv实现均衡化
equ = cv2.equalizeHist(img)
hist3,bins3 = np.histogram(equ.flatten(),256,[0,256])#np直方图绘制函数
cdf4 = hist3.cumsum()# 计算累积分布图
cdf_normalized3 = cdf4 * hist3.max()/ cdf4.max()
plt.subplot(133), plt.plot(hist3, color = 'b'),plt.plot(cdf_normalized3, color = 'r'),plt.title('opencv均衡后直方图')
plt.legend(('均衡化后直方图','均衡化后累积分布图'), loc = 'upper left')
plt.show()
#stacking images side-by-side
res = np.hstack((img,equ))
cv2.imwrite('res.png',res)


#自适应直方图均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.imwrite('res3.png',cl1)

