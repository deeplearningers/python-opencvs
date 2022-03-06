# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 09:32:51 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('LenaRGB.bmp')
# None 本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子,因此这里为 None
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
#OR
# 这里呢，我们直接设置输出图像的尺寸，所以不用设置缩放因子
height,width=img.shape[:2]
print(img.shape,height,width,img.shape[0:2])
res=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)

#旋转，第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
M=cv2.getRotationMatrix2D((width/2,height/2),45,0.6)
# 第三个参数是输出图像的尺寸中心
dst=cv2.warpAffine(img,M,(2*width,2*height))

#仿射变换
pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])
M=cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(width,height))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
#透视变化-4个点
pts3 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts4 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M1=cv2.getPerspectiveTransform(pts3,pts4)
dst1=cv2.warpPerspective(img,M1,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input1')
plt.subplot(122),plt.imshow(dst1),plt.title('Output1')
plt.show()
#全局阈值
imggray = cv2.imread('lena.bmp',0)
ret,thresh1=cv2.threshold(imggray,120,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(imggray,120,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(imggray,120,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(imggray,120,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(imggray,120,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [imggray, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()



while(1):
    cv2.imshow('res',res)
    cv2.imshow('img',img)
    #旋转
    cv2.imshow('img1',dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()