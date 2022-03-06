# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
#加载数据，并把字母转换成ASIC码
data= np.loadtxt('letter-recognition.data', dtype= 'float32', delimiter = ',',converters= {0: lambda ch: ord(ch)-ord('A')})#匿名函数
# 数据切分为训练集和测试集
train, test = np.vsplit(data,2)#沿着其竖轴拆分成两部分，每部分10000个字母
# split trainData and testData to features and responses
responses, trainData = np.hsplit(train,[1])#沿着其横轴拆分原array
labels, testData = np.hsplit(test,[1])#沿着其横轴拆分原array，[1]表示从第1列开始切分
# Initiate the kNN, classify, measure accuracy.
knn = cv2.ml.KNearest_create()
knn.train(trainData,cv2.ml.ROW_SAMPLE, responses)
ret, result, neighbours, dist = knn.findNearest(testData, k=1)
correct = np.count_nonzero(result == labels)
accuracy = correct*100.0/10000
print(accuracy)