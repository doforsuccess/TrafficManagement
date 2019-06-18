import cv2

cap = cv2.VideoCapture('videos/new.mp4')
car_cascade = cv2.CascadeClassifier('xmlFiles/cascade.xml')

while True:
    ret, frame = cap.read()

    y = 0
    x = 0
    w = 1024
    h = 600
    # crops the live image from 0 px to 200px along x and from 0px to 100px along y
    crop1 = frame[y:y + h, x:x + 512]

    # crops the live image from 200 px to 400px along x and from 100px to 300px along y
    crop2 = frame[y :600, x + 512:1024]

    gray1 = cv2.cvtColor(crop1, cv2.COLOR_BGR2GRAY)

    cars1 = car_cascade.detectMultiScale(gray1, 1.1, 1)

    # To draw a rectangle in each cars
    for (x, y, w, h) in cars1:
        cv2.rectangle(crop1, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('First Croped Image', crop1)



    gray2 = cv2.cvtColor(crop2, cv2.COLOR_BGR2GRAY)

    cars2 = car_cascade.detectMultiScale(gray2, 1.1, 1)

    # To draw a rectangle in each cars
    for (x, y, w, h) in cars2:
        cv2.rectangle(crop2, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Second Croped Image', crop2)

    print(len(cars1),len(cars2))


#Here will be the code to turn on and off led of different roads
    if len(cars1)>len(cars2):
        print('road1 green led on and road2 red led on')
    else:
        print('road2 green led on and road1 red led on')

    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
      break

cap.release()
cv2.destroyAllWindows()
