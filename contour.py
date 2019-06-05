import numpy as np
import cv2

image = cv2.imread("E:\\Projects\\Python\\OpenCV\\traffic.png")
imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
box=cv2.drawContours(image, contours, -1, (0,255,0), 3)


cv2.imshow("contour",box)

cv2.waitKey(0)
cv2.destroyAllWindows()