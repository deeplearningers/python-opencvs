# -*- coding: utf-8 -*-
import cv2
import numpy as np
cap = cv2.VideoCapture("video.avi")
ret, frame1 = cap.read()#上一帧
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
while(1):
    #下一帧
    ret, frame2 = cap.read()
    if ret is True:
        next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    else:
        break
    """
cv2.calcOpticalFlowFarneback(prev, next, pyr_scale, levels, winsize, iterations, poly_n,poly_sigma, flags[)
1. _prev0：输入前一帧图像 
2. _next0：输入后一帧图像 
3. _flow0：输出的光流 
4. pyr_scale：金字塔上下两层之间的尺度关系 ,0.5代表下一层比上一层小2倍
5. levels：金字塔层数 
6. winsize：均值窗口大小，越大越能 denoise 并且能够检测快速移动目标，但会引起模糊运动区域 
7. iterations：迭代次数 
8. poly_n：计算光流方程多项式展开的像素邻域范围大小，一般为 5、7 等 
9. poly_sigma：高斯标准差，一般为 1～1.5（函数处理中需要高斯分布权重） 5~1.1；7~1.5
10. flags：计算方法，包括0： OPTFLOW_USE_INITIAL_FLOW 和1： OPTFLOW_FARNEBACK_GAUSSIAN，1 慢但准确
    """
    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 1)
    #cv2.cartToPolar Calculates the magnitude and angle of 2D vectors.
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    cv2.imshow('frame2',rgb)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png',frame2)
        cv2.imwrite('opticalhsv.png',rgb)
    prvs = next
cap.release()
cv2.destroyAllWindows()