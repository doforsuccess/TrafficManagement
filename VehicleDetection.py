import cv2

cap = cv2.VideoCapture('video.avi')
car_cascade = cv2.CascadeClassifier('xmlFiles/cars.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # To draw a rectangle in each cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    y = 0
    x = 0
    h = 100
    w = 200
    # crops the live image from 0 px to 200px along x and from 0px to 100px along y
    crop1 = frame[y:y + h, x:x + w]

    # crops the live image from 200 px to 400px along x and from 100px to 300px along y
    crop2 = frame[y + h:300, x + w:400]

    cv2.imshow('first half', crop1)
    cv2.imshow('second half', crop2)


    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
      break

cv2.destroyAllWindows()
