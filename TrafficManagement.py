import cv2
import numpy as np

image = cv2.imread("E:\\Projects\\Python\\OpenCV\\traffic.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

edges = cv2.Canny(gray_image,100,200)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.dilate(edges,kernel,iterations=1)

im2, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
box = cv2.drawContours(image, contours, -1, (0,255,0), 3)

cv2.imshow("Real Image", image)
cv2.imshow("gray image",gray_image)
cv2.imshow("Gray image",threshold_image)
cv2.imshow("edges image",edges)
cv2.imshow("eroded image",erosion)
cv2.imshow("eroded image",box)

cv2.waitKey(0)
cv2.destroyAllWindows()