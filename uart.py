import time
import serial

ser = serial.Serial(
    # port='/dev/ttyTHS0',
    port = '/dev/ttyACM0',
    # port='COM4',
    baudrate=115200,
    timeout=1)
while True:
	    ser.write(b'#1P1386#2P2271#3P1957#4P500#5P614#6P1500#7P1500#8P1500#9P1500#10P1500#11P1500#12P1500#13P1500#14P1500#15P1500#16P1500#17P1500#18P1500#19P1500#20P1500#21P1500#22P1500#23P1500#24P1500#25P1500#26P1500#27P1500#28P1500#29P1500#30P1500#31P1500#32P1500T500D500\r\n')
	    time.sleep(2)
	    ser.write(b'#1P1329#2P1843#3P2443#4P1700#5P614T1000D500\r\n')
	    time.sleep(2)
	    ser.write(b'#1P1243#2P1500#3P2243#4P1843#5P500T1000D500\r\n')
	    time.sleep(2)
	    ser.write(b'#4P1843#5P2500T1000D500\r\n')
	    time.sleep(2)
	    ser.write(b'#1P2157#3P2186T1000D500\r\n')
	    time.sleep(2)
	    ser.write(b'#5P500T1000D500\r\n')
		
