import serial
import webbrowser
from lib.cilok import urlEncode16
from lib import config

port="/dev/cu.wch ch341 USB=>RS232 3d10"
baudrate = 115200

ser = serial.Serial(port, baudrate)
temp = ''
while 1:
	data=ser.readline().rstrip('\n')
	#print data
	data=data.strip()
	print data
	if data[:1]=="0":
		print "\a"
		trimdata = data.replace(" ","")
		thedata = urlEncode16(trimdata)
		uri = config.keyuri+'%input%ktp%'+trimdata
		thedata = urlEncode16(uri)
		webbrowser.open_new(config.host+thedata)

