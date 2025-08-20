import paho.mqtt.client as mqtt
from time import sleep

def thingspeak_mqtt(data1, data2, data3):
    client = mqtt.Client("BiYcOjAbJxA3CjoqJigYNAw")
    client.username_pw_set(username="BiYcOjAbJxA3CjoqJigYNAw", password="W+Mepn+V0SMhwR4oAIC5F8WM")
    client.connect("mqtt3.thingspeak.com", 1883, 60)
    channel_ID = "2255818"
    client.publish("channels/%s/publish" %(channel_ID),"field1=%s&field2=%s&field3=%s" %(data1,data2,data3))

while True:
    try:
        data1 = randint(10,50)#Nhi?t d?
        data2 = randint(60,99)#Ð? ?m
        data3 = randint(0,100)#random
        print ("data:{}".format(data1))
        print ("data2:{}".format(data2))
        print ("data3:{}".format(data3))
        thingspeak_mqtt(data1,data2,data3)
        sleep(20)
    except:
        print("Not Connect.")
        print("Reconnect",end="")
        for i in range(10):
            print('.', end='')
        print()
        sleep(1)
