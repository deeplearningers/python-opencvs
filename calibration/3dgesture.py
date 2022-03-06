# -*- coding: utf-8 -*-

import cv2
import numpy as np
import glob
import os
#棋盘格规格
w,h= 9,6
# Load previously saved data
with np.load('calib.npz') as X:
    mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]
#绘制函数
def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    return img
#终止条件、对象点（棋盘上的 3D 角点）、坐标轴点
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((h*w,1,3), np.float32)
objp[:,:,:2] = np.mgrid[0:w,0:h].T.reshape(-1,1,2)
axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)#3D空间中的坐标轴点是为了绘制坐标轴
#
for i,fname in enumerate(glob.glob('img\\xx*.jpg'),start=1):
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (w,h),None)#查找角点
    if ret == True:
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)#优化到亚像素级别
        # Find the rotation and translation vectors.
        _,rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners2, mtx, dist)#求解图像到空间点的RT
        # project 3D points to image plane
        imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)#映射坐标轴点
        img = draw(img,corners2,imgpts)
        cv2.imshow('img%s'%i,img)
        if cv2.waitKey() & 0xFF == ord('s'):
            cv2.imwrite('img\\3d_%d'%i + '.png', img)
    if os.path.exists('img\\3d_%d'%i + '.png'):
        print('3d_%d'%i + '已经存在')
    else:
        print('3d_%d' %i + '不存在')
cv2.destroyAllWindows()
