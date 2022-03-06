# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:51:59 2014
@author: duan
"""
import cv2
import numpy as np

#参数
SZ=20
bin_n = 16 # Number of bins
affine_flags = cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR

#进行抗扭斜（deskew）处理
def deskew(img):
    m = cv2.moments(img)
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    skew = m['mu11']/m['mu02']
    M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
    img = cv2.warpAffine(img,M,(SZ, SZ),flags=affine_flags)
    return img

#用方向梯度直方图HOG作为特征向量表示图像
def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)#梯度的大小和方向（笛卡尔坐标转极坐标）
    bins = np.int32(bin_n*ang/(2*np.pi)) # 16个bin对应这些梯度方向，x轴是梯度方向，y轴是梯度大小
    bin_cells = bins[:10,:10], bins[10:,:10], bins[:10,10:], bins[10:,10:]#bin分成4个小方块
    mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]#梯度大小分成4个小方块
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists) # hist is a 64 bit vector
    return hist

#读取手写体
img = cv2.imread('E:\\studyOpencv\\python-opencv\\pics\\digits.png',0)
cells = [np.hsplit(row,100) for row in np.vsplit(img,50)]#切分方法
#分割数据集
train_cells = [ i[:50] for i in cells ]
test_cells = [ i[50:] for i in cells]
#训练
deskewed = [list(map(deskew,row)) for row in train_cells]#map映射函数和变量
hogdata = [list(map(hog,row)) for row in deskewed]
trainData = np.float32(hogdata).reshape(-1,64)
labels = np.repeat(np.arange(10),250)[:,np.newaxis]
#设置训练参数
svm = cv2.ml.SVM_create()
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setType(cv2.ml.SVM_C_SVC)#//使用预先定义的内核初始化
svm.setC(2.67)## 此参数决定分类器的训练误差和预测误差
svm.setGamma(5.383)#核函数的参数
svm.train(trainData,cv2.ml.ROW_SAMPLE,labels)
svm.save('svm_data.dat')
#测试
deskewed = [list(map(deskew,row)) for row in test_cells]
hogdata = [list(map(hog,row)) for row in deskewed]
testData = np.float32(hogdata).reshape(-1,bin_n*4)
#准确度
ret,result = svm.predict(testData)
mask = result==labels
correct = np.count_nonzero(mask)
print(correct * 100.0 / len(result), '%')