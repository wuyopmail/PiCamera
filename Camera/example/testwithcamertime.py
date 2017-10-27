import cv2
import numpy as np
import datetime
import time

start =time.clock()

cap = cv2.VideoCapture(0)
#img = cv2.imread("timg.jpg")
#print img
while(1):
	whilestart = time.clock()
	ret, img = cap.read()
	img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	retval, grayimg = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
	whileend = time.clock()
	show = whileend - whilestart
	cv2.putText(grayimg,str(show),(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(50,0,0))
	
	cv2.imshow("capture", grayimg)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.imwrite("test.jpg",grayimg)
#cv2.imshow("test",grayimg)
print retval
cap.release()
cv2.destroyAllWindows() 
#cv2.waitKey(10)
#cv2.destroyAllWindows()

#time.sleep(1)
end = time.clock()

print('Running time: %s Seconds'%(end-start))

