<<<<<<< HEAD
import cv2
import numpy as np,sys
from matplotlib import pyplot as plt

A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)
# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)
# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)
# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)
# Now add left and right halves of images in each level
#numpy.hstack(tup)
#Take a sequence of arrays and stack them horizontally
#to make a single array.
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:int(cols/2)], lb[:,int(cols/2):]))#水平(按列顺序)把数组给堆叠起来
    LS.append(ls)
# now reconstruct
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])
# image with direct connecting each half
real = np.hstack((A[:,:int(cols/2)],B[:,int(cols/2):]))
cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)
#cv2.imshow('1',ls_)
#cv2.imshow('2',real)
#RGB顺序
b,g,r=cv2.split(ls_)#OpenCV 中是按 BGR
img1=cv2.merge((r,g,b))#atplotlib 中是按 RGB 排列
b,g,r=cv2.split(real)#OpenCV 中是按 BGR
img2=cv2.merge((r,g,b))#atplotlib 中是按 RGB 排列
#显示
plt.subplot(1,2,1),plt.imshow(img1,'gray')
plt.title('Pyramid_blending2'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(img2, 'gray')
plt.title('Direct_blending'), plt.xticks([]), plt.yticks([])
=======
import cv2
import numpy as np,sys
from matplotlib import pyplot as plt

A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)
# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)
# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)
# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)
# Now add left and right halves of images in each level
#numpy.hstack(tup)
#Take a sequence of arrays and stack them horizontally
#to make a single array.
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:int(cols/2)], lb[:,int(cols/2):]))#水平(按列顺序)把数组给堆叠起来
    LS.append(ls)
# now reconstruct
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])
# image with direct connecting each half
real = np.hstack((A[:,:int(cols/2)],B[:,int(cols/2):]))
cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)
#cv2.imshow('1',ls_)
#cv2.imshow('2',real)
#RGB顺序
b,g,r=cv2.split(ls_)#OpenCV 中是按 BGR
img1=cv2.merge((r,g,b))#atplotlib 中是按 RGB 排列
b,g,r=cv2.split(real)#OpenCV 中是按 BGR
img2=cv2.merge((r,g,b))#atplotlib 中是按 RGB 排列
#显示
plt.subplot(1,2,1),plt.imshow(img1,'gray')
plt.title('Pyramid_blending2'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(img2, 'gray')
plt.title('Direct_blending'), plt.xticks([]), plt.yticks([])
>>>>>>> 25f74d288cff6279e8d50298f4b7bc15d138bd62
plt.show()