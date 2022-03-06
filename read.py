import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lenaRGB.bmp',cv2.IMREAD_COLOR)#BGR形式彩色图
#img = cv2.imread('lena.bmp',0)
#像素值操作
px=img[100,100]
print(px)
blue=img[100,100,0]
print(blue)#BGR
#img[100,100]=[255,255,255]
print(img.item(100,100,0))
img.itemset((100,100,0),100)
print(img.item(100,100,0))
print(img.shape)#512,512,3
print(img.size)#786432
print(img.dtype)#uint8
# roi
roi=img[250:280,250:280]
cv2.imshow('1',roi)
#拆分及合并图像通道,b,g,r
b,g,r=cv2.split(img)
img2 = cv2.merge((b,g,r))
img3=img.copy()
img3[:,:,2]=0
cv2.imshow('2',img3)

#画几何
cv2.line(img,(0,0),(511,511),(255,255,0),5)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.circle(img,(447,63),63,(0,255,255),-1)
cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)
#多边形
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=pts.reshape((-1,1,2))


font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

cv2.namedWindow('window',cv2.WINDOW_NORMAL)
cv2.imshow('window',img)
#查看像素值和坐标时使用
plt.imshow(img,cmap='gray',interpolation='bicubic')#RGB形式彩色图
plt.xticks([]),plt.yticks([])
plt.show

#颜色空间
flags=[i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

cv2.waitKey(0)

if 0xFF==27:
    cv2.destroyAllWindows()
elif 0xFF == ord('s'):
    cv2.imwrite('lenacopy.bmp',img)
    cv2.destroyAllWindows()









