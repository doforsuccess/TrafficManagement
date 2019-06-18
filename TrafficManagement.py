import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    ret, frame = cap.read()

    y = 0
    x = 0
    w = 1024
    h = 600
    # crops the live image from 0 px to 200px along x and from 0px to 100px along y
    crop1 = frame[y:y + h, x:x + 320]

    # crops the live image from 200 px to 400px along x and from 100px to 300px along y
    crop2 = frame[y:600, x + 320:1024]

    gray_image1 = cv2.cvtColor(crop1, cv2.COLOR_BGR2GRAY)

    threshold_image1 = cv2.adaptiveThreshold(gray_image1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    edges1 = cv2.Canny(gray_image1,100,200)

    kernel1 = np.ones((5,5),np.uint8)
    erosion1 = cv2.dilate(edges1,kernel1,iterations=1)

    contours1, hierarchy1 = cv2.findContours(edges1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);
    img1 = cv2.drawContours(crop1, contours1, -1, (255,255,255), 3)

#    cnt = contours[0]
 #   x, y, w, h = cv2.boundingRect(cnt)
 #   box=cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
   # cv2.imshow("rectangle box", box)

    gray_image2 = cv2.cvtColor(crop2, cv2.COLOR_BGR2GRAY)

    threshold_image2 = cv2.adaptiveThreshold(gray_image2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,
                                             1)

    edges2 = cv2.Canny(gray_image2, 100, 200)

    kernel2 = np.ones((5, 5), np.uint8)
    erosion2 = cv2.dilate(edges2, kernel2, iterations=1)

    contours2, hierarchy2 = cv2.findContours(edges2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);
    img2 = cv2.drawContours(crop2, contours2, -1, (255, 255, 255), 3)

    #    cnt = contours[0]
    #   x, y, w, h = cv2.boundingRect(cnt)
    #   box=cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("canny1",edges1)
    cv2.imshow("contours1",img1)

    cv2.imshow("canny2", edges2)
    cv2.imshow("contours2", img2)

    a=len(contours1)
    b=len(contours2)

    if a>b:
        print('image one is dense')
    else:
        print('image two is dense')


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
       break

cap.release()
cv2.destroyAllWindows()