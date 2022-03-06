# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 创建 25 个训练数据,0~100之间，25个，二维（x，y）
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
# 标签，红0蓝1
responses = np.random.randint(0,2,(25,1)).astype(np.float32)
# 画出红色类
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],100,'r','^')
# 画出蓝色类，100是大小
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],100,'b','s')
#测试数据集newcomer
newcomer = np.random.randint(0,100,(10,2)).astype(np.float32)#10个测试样本
plt.scatter(newcomer[:,0],newcomer[:,1],100,'g','o')
knn = cv2.ml.KNearest_create()
knn.train(trainData,cv2.ml.ROW_SAMPLE,responses)#训练集和标签
ret, results, neighbours ,dist = knn.findNearest(newcomer, 3)#k=3
print("result: ", results,"\n")
print("neighbours: ", neighbours,"\n")
print("distance: ", dist)

plt.show()