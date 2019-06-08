import numpy as np
import cv2


# capture frames from a camera
cap = cv2.VideoCapture(0)

# loop runs if capturing has been initialized
while (1):
    ret, frame = cap.read()
    
    y=0
    x=0
    h=100
    w=200
    #crops the live image from 0 px to 200px along x and from 0px to 100px along y
    crop1 = frame[y:y+h, x:x+w]
    
    #crops the live image from 200 px to 400px along x and from 100px to 300px along y
    crop2 = frame[y+h:300,x+w:400]
    #for diaplaying the fragments of the live image
    cv2.imshow('Image1', crop1)
    cv2.imshow('Image2', crop2)
    #to break the flow of the while loop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

#for closing the window   
cv2.waitKey(0)
cv2.destroyAllWindows()
