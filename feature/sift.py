# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('..\\pics\\chessboard.bmp')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#sift算法
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
#img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img=cv2.drawKeypoints(gray,kp,img)
cv2.imwrite('sift_keypoints.jpg',img)
cv2.imshow('sift',img)

#surf算法
surf = cv2.xfeatures2d.SURF_create(10000)
surf.setHessianThreshold(12000)
surf.setUpright(False)#设置是否计算方向
surf.setExtended(True)#关键点描述符的大小128
print(surf.getHessianThreshold(),surf.getUpright(),surf.descriptorSize())#获取hessian阈值
kp1, des1 = surf.detectAndCompute(img,None)
img1=img.copy()
img1=cv2.drawKeypoints(gray,kp1,img1,(255,0,0),3)
cv2.imwrite('surf_keypoints.jpg',img1)
cv2.imshow('surf',img1)
print(len(kp1),des1.shape)


cv2.waitKey()