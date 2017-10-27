import cv2
import numpy as np


img = cv2.imread("timg.jpg")
#print img
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, grayimg = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
cv2.imwrite("test.jpg",grayimg)
#cv2.imshow("test",grayimg)
print retval
#cv2.waitKey(10)
#cv2.destroyAllWindows()