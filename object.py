from ultralytics import YOLO
import cv2
import math
import torch 
import Jetson.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

# start webcam
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

#set I/O relay
l1 = 11

GPIO.setup(l1, GPIO.OUT)
GPIO.output(l1, GPIO.HIGH)


# model
model = YOLO("/home/jetson/Desktop/T/models/bestv6.pt")
if torch.cuda.is_available():
	torch.cuda.set_device(0)
	dev ='cuda:0'
	print("oke GPU")
 
model.to(device=dev)
# object classes
classNames = ["violet","green","blue","red"]


while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            # class name
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])
            if(classNames[cls] == 'blue'):
            	GPIO.output(l1, GPIO.LOW)

            '''# object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2'''

            '''cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)'''

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
