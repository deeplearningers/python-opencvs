import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']#解决matplotlib不显示中文问题

img = cv2.imread('pics\\1.bmp',0)
#img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)#形态学梯度
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)#顶帽
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


#'gray'解决显示成彩色问题
plt.subplot(181),plt.imshow(img,'gray'),plt.title('原图')
plt.xticks([]), plt.yticks([])
plt.subplot(172),plt.imshow(erosion,'gray'),plt.title('腐蚀')
plt.xticks([]), plt.yticks([])
plt.subplot(173),plt.imshow(dilation,'gray'),plt.title('膨胀')
plt.xticks([]), plt.yticks([])
plt.subplot(174),plt.imshow(opening,'gray'),plt.title('开运算')
plt.xticks([]), plt.yticks([])
plt.subplot(175),plt.imshow(closing,'gray'),plt.title('闭运算')
plt.xticks([]), plt.yticks([])
plt.subplot(176),plt.imshow(gradient,'gray'),plt.title('形态学梯度')
plt.xticks([]), plt.yticks([])
plt.subplot(177),plt.imshow(tophat,'gray'),plt.title('顶帽')
plt.xticks([]), plt.yticks([])
plt.subplot(177),plt.imshow(blackhat,'gray'),plt.title('黑帽')
plt.xticks([]), plt.yticks([])
plt.show()