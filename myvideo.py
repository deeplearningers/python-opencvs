import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
#编码
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret==True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        #设置参数
        print(cap.get(3),cap.get(4))
        ret = cap.set(3,320)
        ret = cap.set(4,240)
        print(cap.get(3), cap.get(4))

        frame2 = cv2.flip(frame,2)#翻转方式0,1，2..
        out.write(frame2)
        cv2.imshow('flip',frame2)

        if cv2.waitKey(1) & 0xFF== ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()