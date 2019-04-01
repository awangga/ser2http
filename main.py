import serial
from lib import config


ser = serial.Serial(config.port, config.baudrate)

while 1:
	#data=ser.readline().rstrip('\n')
	data=ser.readline()
	#print data
	#data=data.strip()
	print(data)
	#if data[:1]=="[":
	#	print "\a"
	#	trimdata = data.replace(" ","")
	#	thedata = urlEncode16(trimdata)
	#	uri = config.keyuri+'%input%ktp%'+trimdata
	#	thedata = urlEncode16(uri)
	#	webbrowser.open_new(config.host+thedata)

