
import cv2
# capture frames from a camera
cap = cv2.VideoCapture(0)
HIGH=1000
#you may change HIGH value to find maximum resolution of camera
# visit 'https://en.wikipedia.org/wiki/List_of_common_resolutions' for list of common resolution
cap.set(3,HIGH)
cap.set(4,HIGH)
wc = cap.get(3)
hc= cap.get(4)
print("Maximun resolution of camera:")
print(str(wc)+'*'+str(hc))
while (1):
    ret, frame = cap.read()
    y=0
    x=0
    #partitioning 25% of pixel
    crop1 = frame[y:int(hc*0.25), x:int(wc*0.25)]
    #partitioning remaining 75%
    crop2 = frame[int(hc*0.25):int(hc),int(wc*0.25):int(wc)]
    #diaplaying the fragments of the live image
    cv2.imshow('Crop1', crop1)
    cv2.imshow('Crop2', crop2)
    #to break the flow of the while loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()