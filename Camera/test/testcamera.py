# -*- coding: utf-8 -*-
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
#print cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH) #最大分辨率
#print cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
starttime = time.time()
#img = cv2.imread("timg.jpg")
precent = 50 #0-100黑点百分比
while(1):
    wst = time.time()
    ret, img = cap.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    retval, grayimg = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    wet = time.time()
    #grayimg[0:10,5:10] = 125 #更改区域图像
    #grayimg[10,50] = 125 #更改像素
    #grayimg[1,2] = 125 #grayimg[i行(0-7),j列(0-7)](分辨率8*8的情况下)
    #print grayimg[0:3,0:3]
    #arr = grayimg[0:10,5:10]
    white = 0
    count = 0
    #grayimg[0:10,0:10] = 125 #先查看区域是否正确
    print grayimg[0:10,0:10] #先查看区域是否正确
    for i in range(0, 10): #行
        for j in range(0, 10): #列
            count = count + 1
            if(grayimg[i,j] == 255): #再等于125测试区域是否正确
                white = white + 1
    wprecent = white / float(count)
    print white
    print wprecent
    print "run time:" + str((wet - wst))
    cv2.imshow("camera",img)
    cv2.imshow("test",grayimg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
#print img
print retval

endtime = time.time()

print "run time:" + str((endtime - starttime))
