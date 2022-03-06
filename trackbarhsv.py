<<<<<<< HEAD
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def nothing(x):
    pass

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('H', 'image', 0, 360, nothing)
cv2.createTrackbar('S', 'image', 0, 100, nothing)
cv2.createTrackbar('V', 'image', 0, 100, nothing)
switch='0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)
#cv2.setMouseCallback('image', draw_circle)
while (1):
    cv2.imshow('image', img)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    (H, S, V) = cv2.split(img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
    h = cv2.getTrackbarPos('H', 'image')
    s = cv2.getTrackbarPos('S', 'image')
    v = cv2.getTrackbarPos('V', 'image')
    sw = cv2.getTrackbarPos(switch, 'image')
    if sw == 0:
        pass
    else:
        h_=h/2
        s_=int(s*2.55)
        v_ = int(v * 2.55)
        for i in range(0,H.shape[0]):
            for j in range(0,H.shape[1]):
                H[i,j]=h_
                S[i, j] = s_
                V[i, j] = v_
        #r, g, b = hsv2bgr(h, s, v)
        img=cv2.merge([H,S,V])
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
cv2.destroyAllWindows()

=======
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def nothing(x):
    pass

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('H', 'image', 0, 360, nothing)
cv2.createTrackbar('S', 'image', 0, 100, nothing)
cv2.createTrackbar('V', 'image', 0, 100, nothing)
switch='0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)
#cv2.setMouseCallback('image', draw_circle)
while (1):
    cv2.imshow('image', img)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    (H, S, V) = cv2.split(img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
    h = cv2.getTrackbarPos('H', 'image')
    s = cv2.getTrackbarPos('S', 'image')
    v = cv2.getTrackbarPos('V', 'image')
    sw = cv2.getTrackbarPos(switch, 'image')
    if sw == 0:
        pass
    else:
        h_=h/2
        s_=int(s*2.55)
        v_ = int(v * 2.55)
        for i in range(0,H.shape[0]):
            for j in range(0,H.shape[1]):
                H[i,j]=h_
                S[i, j] = s_
                V[i, j] = v_
        #r, g, b = hsv2bgr(h, s, v)
        img=cv2.merge([H,S,V])
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
cv2.destroyAllWindows()

>>>>>>> 25f74d288cff6279e8d50298f4b7bc15d138bd62
