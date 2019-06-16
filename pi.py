# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
car_cascade = cv2.CascadeClassifier('xmlFiles/cars.xml')

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    y = 0
    x = 0
    h = 100
    w = 200
    # crops the live image from 0 px to 200px along x and from 0px to 100px along y
    crop1 = image[y:y + h, x:x + w]

    # crops the live image from 200 px to 400px along x and from 100px to 300px along y
    crop2 = image[y + h:300, x + w:400]

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

    print(len(cars1), len(cars2))

    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break


"""""        
        
car_cascade = cv2.CascadeClassifier('xmlFiles/cars.xml')

while True:
    ret, frame = cap.read()

    y = 0
    x = 0
    h = 100
    w = 200
    # crops the live image from 0 px to 200px along x and from 0px to 100px along y
    crop1 = frame[y:y + h, x:x + w]

    # crops the live image from 200 px to 400px along x and from 100px to 300px along y
    crop2 = frame[y + h:300, x + w:400]

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
"""