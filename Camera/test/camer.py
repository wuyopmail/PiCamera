import cv2
img = cv2.imread('road.jpg')
cv2.imshow('image',img)
k = cv2.waitKey(0)
cv2.destroyAllWindows() 