# -*- coding: utf-8 -*-
import numpy as np
import cv2
cap = cv2.VideoCapture('video.avi')
#ShiTomasi角点参数--maxCorners：角点数目最大值，如果实际检测的角点超过此值，只返回前maxCorners个强角点；
#qualityLevel：角点的品质因子；minDistance：初选出的角点，在其周围minDistance范围内存在更强角点，则将此角点删除；blockSize：计算协方差矩阵时的窗口大小
feature_params = dict( maxCorners =100,qualityLevel = 0.4,minDistance =10,blockSize = 7)
#光流法参数,maxLevel使用的图像金字塔层
lk_params = dict( winSize = (15,15),maxLevel = 2,criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
color = np.random.randint(0,255,(100,3))
#上一帧
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
#跟踪特征点，单通道图像,p0保存检测到的点；
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)
while(1):
    #下一帧
    ret,frame = cap.read()
    if ret is True:#解决报错
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    # LK算法返回带状态st的点p1，误差err
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)#上一帧及点、下一帧、
    # Select good points
    good_new = p1[st==1]#找到下一帧的点
    good_old = p0[st==1]#找到的下一帧在上一帧对应的点
    if len(good_new):
        # draw the tracks
        for i,(new,old) in enumerate(zip(good_new,good_old)):#枚举0-n
            a,b = new.ravel()
            c,d = old.ravel()
            mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
            frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
            #cv2.imshow('1', mask)
            #cv2.waitKey()
        img = cv2.add(frame,mask)#把掩模上的特征点加到帧上
        cv2.imshow('frame',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        # Now update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1,1,2)
    else :
        print('未检测到追踪点！')
cv2.destroyAllWindows()
cap.release()