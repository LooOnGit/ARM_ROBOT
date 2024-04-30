from time import sleep
from urllib import request
import random
# from seeed_dht import DHT
# sensor=DHT('11',16)
def Post_HTTP(data):

    url="https://api.thingspeak.com/update?api_key=WAYJCP9LBKHGFL4U&"+data
    r=request.urlopen(url)
    print("HTTP SEND")  
    return r
while True:
    try:
        temp=random.randint(0,5)
        data="field1="+str(temp)
        data+="&field2="+str(temp)
        Post_HTTP(data)
        sleep(20)
    except:
        print("Lose connection")
        sleep(1)   