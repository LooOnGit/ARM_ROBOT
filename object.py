from ultralytics import YOLO
import cv2
import math
import torch 
import Jetson.GPIO as GPIO
from time import sleep
import serial
from urllib import request

GPIO.setmode(GPIO.BOARD)

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#set I/O relay
l1 = 11

#set uart 
ser = serial.Serial(
    # port='/dev/ttyTHS0',
    port = '/dev/ttyACM1',
    # port='COM4',
    baudrate=115200,
    timeout=1)

GPIO.setup(l1, GPIO.OUT)
GPIO.output(l1, GPIO.HIGH)

labelPredict = ''

#number color
dataBackup = {'violet': 0, 'red': 0, 'green': 0, 'blue': 0}

# model
model = YOLO("/home/jetson/Desktop/T/ARM_ROBOT/models/bestv6.pt")
if torch.cuda.is_available():
	torch.cuda.set_device(0)
	dev ='cuda:0'
	print("oke GPU")
 
model.to(device=dev)
# object classes
classNames = ["violet","green","blue","red"]

ser.write(b'#1P1386#2P2271#3P1957#4P500#5P614#6P1500#7P1500#8P1500#9P1500#10P1500#11P1500#12P1500#13P1500#14P1500#15P1500#16P1500#17P1500#18P1500#19P1500#20P1500#21P1500#22P1500#23P1500#24P1500#25P1500#26P1500#27P1500#28P1500#29P1500#30P1500#31P1500#32P1500T500D500\r\n')
sleep(2)
cond = [b'#1P2214#2P1643#3P2500#4P1614#5P2500T1000D500\r\n', b'#1P2157#3P2186T1000D500\r\n', b'#1P1757#2P1814#3P2500#4P1529T1000D500\r\n', b'#1P1814#5P2500T1000D500\r\n']

def armRobot(cc):
    GPIO.output(l1, GPIO.LOW)
    ser.write(b'#1P1386#2P2271#3P1957#4P500#5P614#6P1500#7P1500#8P1500#9P1500#10P1500#11P1500#12P1500#13P1500#14P1500#15P1500#16P1500#17P1500#18P1500#19P1500#20P1500#21P1500#22P1500#23P1500#24P1500#25P1500#26P1500#27P1500#28P1500#29P1500#30P1500#31P1500#32P1500T500D500\r\n')
    sleep(2)
    ser.write(b'#1P1271#2P1671#3P2471#4P2014#5P1500#6P1500#7P1500#8P1500#9P1500#10P1500#11P1500#12P1500#13P1500#14P1500#15P1500#16P1500#17P1500#18P1500#19P1500#20P1500#21P1500#22P1500#23P1500#24P1500#25P1500#26P1500#27P1500#28P1500#29P1500#30P1500#31P1500#32P1500T500D500\r\n')
    sleep(2)
    ser.write(b'#1P1300T500D500\r\n')
    sleep(2)
    ser.write(b'#1P1329#2P1329#3P2357#4P2271#5P500T500D500\r\n')
    sleep(2)
    ser.write(b'#5P2500T500D500\r\n')
    sleep(2)

    ser.write(cond[cc])
    sleep(2)
    ser.write(b'#5P500T1000D500\r\n')
    sleep(2)
    GPIO.output(l1, GPIO.HIGH)

#http
def Post_HTTP(data):

    url="https://api.thingspeak.com/update?api_key=JGIG4EQSXMJLQLRI&"+data
    r=request.urlopen(url)
    print("HTTP SEND")  
    return r


while True:
    GPIO.output(l1, GPIO.HIGH)
    success, img = cap.read()
    results = model(img, stream=True)
    flag = 0
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
            #print("Confidence --->",confidence)

            # class name
            cls = int(box.cls[0])
            label = classNames[cls]
            #print("Class name -->", classNames[cls])
            if labelPredict != label:
                labelPredict = label
                dataBackup[classNames[cls]] +=1
            else:
                break
            armRobot(cls)
            data="field1="+str(dataBackup['blue'])
            data+="&field2="+str(dataBackup['red'])
            data+="&field3="+str(dataBackup['violet'])
            data+="&field4="+str(dataBackup['green'])
            Post_HTTP(data)
            print(dataBackup)
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
