# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt
#随机产生一维数据
x = np.random.randint(25,100,25)
y = np.random.randint(175,255,25)
z = np.hstack((x,y))
z = z.reshape((50,1))
z = np.float32(z)
plt.hist(z,256,[0,256]),plt.show()
#终止条件：算法执行 10 次迭代或者精确度 epsilon = 1.0。
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
#设置如何选择起始重心
flags = cv2.KMEANS_RANDOM_CENTERS
#聚类，返回值有紧密度（compactness）, 标志和中心；分成2类，执行10次。
compactness,labels,centers = cv2.kmeans(z,2,None,criteria,10,flags)
#分组
A = z[labels==0]
B = z[labels==1]
# A 红色表示，B蓝色表示，重心黄色表示
plt.hist(A,256,[0,256],color = 'r')#256个bins；
plt.hist(B,256,[0,256],color = 'b')
plt.hist(centers,32,[0,256],color = 'y')
plt.show()
