# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('E:\\studyOpencv\\python-opencv\\pics\\digits.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 将图片分割出5000张小图, 每张20x20大小
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
# 放入Numpy数组. 大小(50,100,20,20)
x = np.array(cells)
#准备训练集和测试集
train = x[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400)，-1代表不知道可以分成多少行，但是我的需要是分成400列
test = x[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)
#准备标签
k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]#0到9每个重复250次，排成一列
test_labels = train_labels.copy()
# 初始化KNN， 训练训练数据，并设置k=5来测试测试数据
knn = cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE,train_labels)
ret,result,neighbours,dist = knn.findNearest(test,k=5)
# 计算分类的准确率
# For that, compare the result with test_labels and check which are wrong
matches = result==test_labels
correct = np.count_nonzero(matches)#非0的个数
accuracy = correct*100.0/result.size
print('准确率：',accuracy,'%')
#保存结果
np.savez('knn_data_num.npz', train=train, train_labels=train_labels, test=test, test_labels=test_labels)
#测试
with np.load('knn_data_num.npz') as data:
    print(data.files)
    train = data['train']
    train_labels = data['train_labels']
    test = data['test']
    test_labels = data['test_labels']
# 对数字进行预测
retval, results = knn.predict(test[903:905])
# Docstring: predict(samples[, results[, flags]]) -> retval, results
print(retval, results)  # (4.0, array([[ 4.],[ 4.]], dtype=float32))
# 对比
cv2.imshow('test', test[903].reshape((20, 20)))
cv2.waitKey(0)
cv2.destroyAllWindows()