from ultralytics import YOLO
import cv2
import math
import torch
from time import sleep


labelPredict = ''

# start webcam
cap = cv2.VideoCapture("D:\\Dev_Vision\\video\\all.mp4")
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("models/bestv6.pt")
# object classes
classNames = ["violet", "green", "blue", "red"]

def armRobot(lb):
    print("active")
    sleep(10)

while True:
    success, img = cap.read()
    results = model(img, stream=True)
    print("----------------------------hello F------------------------------------")
    # coordinates
    for r in results:
        boxes = r.boxes
        print("----------------------------hello------------------------------------")
        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)

            # class name
            cls = int(box.cls[0])
            label = classNames[cls]
            print("Class name -->", classNames[cls])
            if labelPredict != label:
                labelPredict = label
            else:
                break
            armRobot(labelPredict)
        break
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
