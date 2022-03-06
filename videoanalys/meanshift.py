# -*- coding: utf-8 -*-
import numpy as np
import cv2
cap = cv2.VideoCapture('video.avi')
# ret判断是否读到图片；frame读取到的当前帧的矩阵
ret,frame = cap.read()
#print(type(ret), ret)#true、false
#print(type(frame), frame)
# 设定初始追踪窗口位置
height = int(frame.shape[0]/4)
width = int(frame.shape[1]/4)
row = int(frame.shape[1]/100)
col = int(frame.shape[0]/20)
track_window = (col,row,width,height)
cv2.rectangle(frame,(col,row),(col+width,row+height),255,2)
# 设置初始roi
roi = frame[row:row+height, col:col+width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#用函数 cv2.inRange() 将低亮度的值忽略掉，设置亮度阈值,二值化
#h-[0,180];s-[0,255];v-[0,255]，lower_red～upper_red之间的值变成255，将低于和高于阈值的值设为0
mask = cv2.inRange(hsv_roi, np.array((77.,19,10.)), np.array((180.,255.,255.)))
# cv2.imshow("frame",mask)
# cv2.waitKey(0)
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])#掩模感兴趣区域直方图
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)#线性归一化
# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )#设置迭代的终止标准，最多十次迭代
while(1):
    ret ,frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #反向投影是一种记录给定图像中的像素点如何适应直方图模型像素分布的方式
        #反向投影就是首先计算某一特征的直方图模型，然后使用模型去寻找图像中存在的特征
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)#dst像素值代表概率大小，相当于在Hsv中寻找roi_hist
        # 用meanshift找新的位置，输入图像直方图的反向投影图，返回一个窗口位置
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        # Draw it on image
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        cv2.imshow('img2',img2)
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        elif k == ord('s'):
            cv2.imwrite(chr(k)+".jpg",img2)
    else:
        break
cv2.destroyAllWindows()
cap.release()