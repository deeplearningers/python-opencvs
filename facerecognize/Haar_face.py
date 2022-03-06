# -*- coding: utf-8 -*-

import numpy as np
import cv2
# 加载需要的XML分类器，绝对路径
face_cascade = cv2.CascadeClassifier('F:\\opencv3.1.0\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')#人脸
eye_cascade = cv2.CascadeClassifier('F:\\opencv3.1.0\\sources\\data\\haarcascades\\haarcascade_eye_tree_eyeglasses.xml')#带眼镜眼睛
#smile_cascade = cv2.CascadeClassifier('F:\\opencv3.1.0\\sources\\data\\haarcascades\\haarcascade_smile.xml')#笑脸
font = cv2.FONT_HERSHEY_SIMPLEX
# img = cv2.imread('E:\\studyOpencv\\python-opencv\\pics\\LenaRGB.bmp')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 连接摄像头的对象 0表示摄像头的编号
camera = cv2.VideoCapture(0)
while(1):
    # 读取当前帧
    ret, frame = camera.read()
    if ret ==True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #检测脸部、笑脸
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        #smile = smile_cascade.detectMultiScale(gray)
        #画出人脸框并检测眼睛
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)#此处是roi_color
                cv2.putText(frame, 'Eye', (ex + x, ey + y), font, 0.5, (11, 255, 255), 1, cv2.LINE_AA)
        # #画出笑脸
        # for (sm_x, sm_y, sm_w, sm_h) in smile:
        #     cv2.rectangle(frame, (sm_x, sm_y), (sm_x + sm_w, sm_y + sm_h), (0, 0, 255), 2)
        cv2.imshow('img',frame)
        if cv2.waitKey(10) & 0xff == ord("q"):
            break
    else:
        break

camera.release()
cv2.destroyAllWindows()
