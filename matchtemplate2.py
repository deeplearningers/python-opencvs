<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:33:15 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('pics\\mali.bmp')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('pics\\yingbi.bmp',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)#返回一个灰度图像，每一个像素值表示了此区域与模板的匹配程度
threshold = 0.8
#umpy.where(condition[, x, y])
#Return elements, either from x or y, depending on condition.
#If only condition is given, return condition.nonzero().
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
=======
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:33:15 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('pics\\mali.bmp')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('pics\\yingbi.bmp',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)#返回一个灰度图像，每一个像素值表示了此区域与模板的匹配程度
threshold = 0.8
#umpy.where(condition[, x, y])
#Return elements, either from x or y, depending on condition.
#If only condition is given, return condition.nonzero().
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
>>>>>>> 25f74d288cff6279e8d50298f4b7bc15d138bd62
cv2.imwrite('pics\\out.bmp',img_rgb)