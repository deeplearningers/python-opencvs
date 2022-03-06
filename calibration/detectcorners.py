# -*- coding: utf-8 -*-
import numpy as np
import cv2
import glob
# 终止条件
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
#棋盘格规格
w,h= 9,6
# 世界坐标系中的棋盘格点,例如(0,0,0), (1,0,0), (2,0,0) ....,(8,5,0)，去掉Z坐标，记为二维矩阵
objp = np.zeros((w*h,3), np.float32)
objp[:,:2] = np.mgrid[0:w,0:h].T.reshape(-1,2)#空间坐标点

objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
#images = glob.glob('chessboard\\*.jpg')#用glob读入全部图片
imgs = glob.glob('img\\*.jpg')
for fname in imgs:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # 检测角点
    ret, corners = cv2.findChessboardCorners(gray,(w,h),None)#棋盘格角点行列数
    #  如果找到足够点对，将其存储起来
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        img = cv2.drawChessboardCorners(img,(w,h), corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(500)
cv2.destroyAllWindows()
# 标定
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
np.savez('calib.npz',mtx=mtx,dist=dist,rvecs=rvecs,tvecs=tvecs)#保存成字典的形式
#去畸变
for i,img in enumerate(imgs,start=1):
    frame = cv2.imread(img)
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height,width = frame.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(width,height),1,(width,height))#求得新的相机校正矩阵.0是自由比例参数,这里是1
    dst = cv2.undistort(frame, mtx, dist, None, newcameramtx)#校正
    # crop the image
    x, y, w1, h1 = roi
    dst = dst[y:y + h1, x:x + w1]
    name = 'img\\calib_IMG_%d.jpg'%i
    cv2.imwrite(name, dst)

# 反投影误差
total_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    total_error += error
print("total error: ", total_error/len(objpoints))