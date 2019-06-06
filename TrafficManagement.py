import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while (1):
    ret, frame = cap.read()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    threshold_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    edges = cv2.Canny(gray_image,100,200)

    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.dilate(edges,kernel,iterations=1)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);
    img = cv2.drawContours(frame, contours, -1, (255,255,255), 3)

#    cnt = contours[0]
 #   x, y, w, h = cv2.boundingRect(cnt)
 #   box=cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Real Image", frame)
    cv2.imshow("gray image",gray_image)
    cv2.imshow("threshold image",threshold_image)
    cv2.imshow("canny",edges)
    cv2.imshow("eroded image",erosion)
    cv2.imshow("contours",img)
   # cv2.imshow("rectangle box", box)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
       break

cap.release()
cv2.destroyAllWindows()