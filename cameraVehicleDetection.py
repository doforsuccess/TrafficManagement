import cv2

cap = cv2.VideoCapture(0)
car_cascade = cv2.CascadeClassifier('car.xml')

while True:
    ret, frames = cap.read()
    img= cv2.imread(r"C://Users//santosh//Desktop//git//TrafficManagement//images//trafficnice.jpg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # To draw a rectangle in each cars
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('video2', img)

    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
      break

cv2.destroyAllWindows()
