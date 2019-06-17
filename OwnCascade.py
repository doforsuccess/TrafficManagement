import numpy as np
import cv2

car=cv2.CascadeClassifier('xmlFiles/cascade.xml')

img=cv2.imread('images/carimg.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=car.detectMultiScale(gray,1.01,7)
for (x,y,w,h) in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()