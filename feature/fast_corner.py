# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:06:18 2014
@author: duan
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('pics\\Goldhill.bmp',0)
# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create(threshold=25)
# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, None,color=(255,0,0))
# Print all default params
print("Threshold: ", fast.getThreshold())
print("nonmaxSuppression: ", fast.getNonmaxSuppression())
print("neighborhood: ", fast.getType())
print("Total Keypoints with nonmaxSuppression: ", len(kp))
cv2.imwrite('pics\\fast_true.png',img2)
# Disable nonmaxSuppression
fast.setNonmaxSuppression(True)#不使用非极大值抑制
kp = fast.detect(img,cv2.FAST_FEATURE_DETECTOR_TYPE_5_8)#设置选取圆周像素点的个数是8
print("Total Keypoints without nonmaxSuppression: ", len(kp))
img3 = cv2.drawKeypoints(img, kp,None, color=(255,0,0))
cv2.imwrite('pics\\fast_false.png',img3)

cv2.imshow('1',img3)
cv2.waitKey()