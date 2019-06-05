import cv2

image = cv2.imread("E:\Projects\Python\OpenCV\clouds.jpg")
resized = cv2.resize(image, (400,100))
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Over the Clouds", resized)
cv2.imshow("Over the Clouds - gray", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

