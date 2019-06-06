import cv2
import numpy as np
from matplotlib import pyplot as plt

imge = cv2.imread(r"C:/Users/santosh/Downloads/circle.png",1)
edges = cv2.Canny(imge,100,200)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);
print(contours)
img = cv2.drawContours(imge, contours, -1, (255,0,0), 3)

#cv2.imshow("hellboy",edges)
cv2.imshow("hellboy",img)
cv2.imshow("hello",imge)

cv2.waitKey(0)
cv2.destroyAllWindows()
