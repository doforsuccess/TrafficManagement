import cv2
import numpy as np

cap = cv2.VideoCapture('E:\Projects\MiniProject\TrafficManagement\\videos\\new.mp4')

while (1):
    ret, frame = cap.read()
    y = 0
    x = 0
    w = 1024
    h = 600
    # crops the live image from 0 px to 200px along x and from 0px to 100px along y
    crop1 = frame[y:y + h, x:x + 512]

    # crops the live image from 200 px to 400px along x and from 100px to 300px along y
    crop2 = frame[y :600, x + 512:1024]
    # for diaplaying the fragments of the live image
    cv2.imshow('Image1', crop1)
    cv2.imshow('Image2', crop2)

    # to break the flow of the while loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()