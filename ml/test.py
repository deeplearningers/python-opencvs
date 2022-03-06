import numpy as np
import cv2
from PIL import Image,ImageDraw, ImageFont,ImageColor
from matplotlib import pyplot as plt

im = Image.open('E:\\studyOpencv\\python-opencv\\pics\\2.jpg')
#im = cv2.imread('E:\\studyOpencv\\python-opencv\\pics\\2.jpg',1)
# b,g,r=cv2.split(im)#OpenCV 中是按 BGR
# img=cv2.merge((r,g,b))#解决rgb顺序，matplotlib 中是按 RGB 排列
x1 =281
y1 = 650
w,h = 14,34

for i in range(x1,x1+w):
    for j in range(y1,y1+h):
        im.putpixel((i,j),(161,152,143))

# draw = ImageDraw.Draw(im)
# myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf',size=30)
# mycolor = ImageColor.colormap.get('black')
# draw.text((282, 657), '8', font=myfont, fill=mycolor)

box = (50,50,14,34)
region = im.crop(box)
# region = region.transpose(Image.ROTATE_180)
# im.paste(region, box)

#cv2.imshow('1',im)
plt.subplot(121),plt.imshow(im,'gray'),plt.title('original')
#plt.subplot(122),plt.imshow(region,'gray'),plt.title('region')
plt.show()
#im.save('E:\\studyOpencv\\python-opencv\\pics\\2copy.jpg')
#cv2.waitKey()