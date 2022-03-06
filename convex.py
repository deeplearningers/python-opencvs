# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:05:52 2014
@author: duan
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']#解决matplotlib不显示中文问题

im = cv2.imread('pics\\source.bmp')
im2 = im.copy()
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,120,255,0)
image, contours, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img0 = cv2.drawContours(im, contours[0], -1, (255,0,0), 5)
img1 = cv2.drawContours(im, contours[1], -1, (0,255,0), 3)
img2 = cv2.drawContours(im, contours[2], -1, (0,0,255), 3)
img3 = cv2.drawContours(im, contours[3], -1, (255,255,0), 3)
#cnt = contours[0]

hull = cv2.convexHull(contours[1],clockwise=True,returnPoints=True)
k = cv2.isContourConvex(contours[1])#返回true说明是凸的，没有凹缺陷
#直边界矩形
x,y,w,h = cv2.boundingRect(contours[1])
img4 = cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,0),2)

#面积最小的旋转边界矩形
rect = cv2.minAreaRect(contours[3])
x1, y1 = rect[0]# 中心坐标
cv2.circle(im, (int(x1), int(y1)), 3, (0, 255, 0), 5)
width, height = rect[1]# 长宽
angle = rect[2]# 角度:[-90,0)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(im, [box], 0, (0, 0, 255), 2)

#最小外接圆
(x2,y2),radius = cv2.minEnclosingCircle(contours[2])
center = (int(x2),int(y2))
radius = int(radius)
img5 = cv2.circle(im,center,radius,(0,255,0),2)

#椭圆拟合-旋转边界矩形的内切椭圆
ellipse = cv2.fitEllipse(contours[1])
img6 = cv2.ellipse(im,ellipse,(0,255,0),2)
#掩模
mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,[contours[2]],0,255,-1)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray,mask = mask)#？？？？？
mean_val = cv2.mean(imgray,mask = mask)#???
print(min_val, max_val, min_loc, max_loc,mean_val)

#极值
cnt = contours[2]
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
cv2.circle(im,leftmost,5,(255,0,0),2)
cv2.circle(im,rightmost,5,(255,0,0),2)
cv2.circle(im,topmost,5,(255,0,0),2)
cv2.circle(im,bottommost,5,(255,0,0),2)
print(leftmost, rightmost, topmost, bottommost)

#寻找凸缺陷
cnt1 =contours[1]#返回轮廓坐标
hull2 = cv2.convexHull(cnt1,returnPoints = False)#返回凸包的序号
defects = cv2.convexityDefects(cnt1,hull2)#n维数组， [起点索引，终点索引，最远的点索引，到最远点的近似距离]
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]#第i个点，第1行
    start = tuple(cnt1[s][0])#起点坐标
    end = tuple(cnt1[e][0])
    far = tuple(cnt1[f][0])
    cv2.line(im2,start,end,[0,255,0],3)
    cv2.circle(im2,far,4,[0,0,255],-1)
#判断点在内外上
dist = cv2.pointPolygonTest(cnt1,(50,50),True)
print(dist)
cv2.circle(im,(50,50),2,(255,0,0),10)
#显示
plt.subplot(1,3,1),plt.imshow(im,'gray')
plt.title('原图'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(mask, 'gray')
plt.title('掩模'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(im2, 'gray')
plt.title('凸包检测'), plt.xticks([]), plt.yticks([])
plt.show()
