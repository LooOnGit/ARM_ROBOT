import time
import random
import paho.mqtt.client as mqtt
import json

mqtt_broker = "broker.example.com"  # Thay d?i th�nh d?a ch? IP ho?c t�n mi?n c?a broker MQTT
mqtt_port = 1883  
mqtt_topic = "NumberBlue"  #


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code "+str(rc))

def on_publish(client, userdata, mid):
    print("Message published")

# Kh?i t?o m?t d?i tu?ng client MQTT
client = mqtt.Client()

# Thi?t l?p c�c h�m callback
client.on_connect = on_connect
client.on_publish = on_publish

# K?t n?i v?i broker MQTT
client.connect(mqtt_broker, mqtt_port, 60)

# B?t d?u v�ng l?p d? g?i d? li?u l�n broker MQTT
try:
    while True:
        sensor_data = random.randint(0, 100)
        a=json.dumps(sensor_data)
        client.publish(mqtt_topic, sensor_data)

        print("Published data: " + sensor_data)
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    client.disconnect()