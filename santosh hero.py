import cv2
import numpy as np
from matplotlib import pyplot as plt



# capture frames from a camera
cap = cv2.VideoCapture(0)
#cv2.waitKey(500)
# loop runs if capturing has been initialized
while (1):
    ret, frame = cap.read()
    edges = cv2.Canny(frame,100,200)
    kernel = np.ones((5,5),np.uint8)
    closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);
    img = cv2.drawContours(frame, contours, -1, (0,0,255), 3)
    
    cv2.imshow("hellboy",edges)
    cv2.imshow("hello",closing)

    #cv2.imshow("hellboy",img)
    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
# Close the window
cap.release()
# De-allocate any associated memory usage
cv2.destroyAllWindows()