# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:38:31 2014
@author: duan
"""
import cv2
import numpy as np
img = cv2.imread('pics\\hough.bmp')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 5)
#一般hough变换
lines = cv2.HoughLines(edges,1,np.pi/1800,200)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,255,255),2)
cv2.imwrite('pics\\houghresult.bmp',img)
#简化的hough变换
minLineLength =50
maxLineGap = 15
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for i in range(lines.shape[0]):
    for x1,y1,x2,y2 in lines[i]:
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imwrite('pics\\houghresult1.bmp',img)

#huogh圆检测-霍夫梯度法
#minDist为圆心之间的最小距离，小于该值是同一个圆
#param1=50边缘检测时使用Canny算子的高阈值
# param2=39累积数量大于该阈值对应圆心和半径
#minRadius和maxRadius为所检测到的圆半径的最小值和最大值
circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,dp=1,minDist=20,param1=50,param2=39,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
# draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
# draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('1',img)
cv2.waitKey()