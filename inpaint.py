<<<<<<< HEAD
import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('pics\\OpenCV_Logo_B.png')     # input
mask = cv2.imread('pics\\OpenCV_Logo_C.png',0)  # mask

dst_TELEA = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)#归一化加权修复
dst_NS = cv2.inpaint(img,mask,3,cv2.INPAINT_NS)

plt.subplot(221), plt.imshow(img),plt.title('degraded image')
plt.subplot(222), plt.imshow(mask, 'gray'),plt.title('mask image')
plt.subplot(223), plt.imshow(dst_TELEA),plt.title('TELEA')
plt.subplot(224), plt.imshow(dst_NS),plt.title('NS')

plt.tight_layout()
=======
import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('pics\\OpenCV_Logo_B.png')     # input
mask = cv2.imread('pics\\OpenCV_Logo_C.png',0)  # mask

dst_TELEA = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)#归一化加权修复
dst_NS = cv2.inpaint(img,mask,3,cv2.INPAINT_NS)

plt.subplot(221), plt.imshow(img),plt.title('degraded image')
plt.subplot(222), plt.imshow(mask, 'gray'),plt.title('mask image')
plt.subplot(223), plt.imshow(dst_TELEA),plt.title('TELEA')
plt.subplot(224), plt.imshow(dst_NS),plt.title('NS')

plt.tight_layout()
>>>>>>> 25f74d288cff6279e8d50298f4b7bc15d138bd62
plt.show()