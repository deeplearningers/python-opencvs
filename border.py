import cv2
import numpy as np
from matplotlib import pyplot as plt

print(cv2.useOptimized())#默认优化开启

e1 = cv2.getTickCount()
BLUE=[255,0,0]
img1=cv2.imread('lenaRGB.bmp',cv2.IMREAD_COLOR)
# b,g,r=cv2.split(img1)#OpenCV 中是按 BGR
# img1=cv2.merge((r,g,b))#解决rgb顺序，matplotlib 中是按 RGB 排列
replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print(time)
#混合
img2 = cv2.imread('lena.bmp',1)
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
#cv2.imshow('dst',dst)
#cv2.destroyAllWindows()
#add?????????=========================================
img3 = cv2.imread('opencv.bmp',1)
img4=cv2.imread('meixi.bmp',1)
rows,cols,channels = img3.shape
roi = img3[0:rows, 0:cols ]
img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,200, 255, cv2.THRESH_BINARY)#掩模
mask_inv = cv2.bitwise_not(mask)#掩模反向

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)#roi与mask求与操作
img2_fg = cv2.bitwise_and(img4,img4,mask = mask_inv)#与
dst = cv2.add(img1_bg,img2_fg)
img3[0:rows, 0:cols ] = dst
cv2.imshow('dst',img1_bg)


cv2.waitKey(0)
