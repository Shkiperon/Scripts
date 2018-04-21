import serial
import sys
import time
from operator import xor

ID =  ''
Znach = ''
Checksumma = 0
Tag = 0

StartFl = "\x02"
EndFl = "\x03"

UART = serial.Serial("/dev/ttyAMA0",9600)
# UART.close()
# UART.open()
while True:
	Checksumma = 0
	Checksumma_Tag = 0
	IdOld = ID
	ID = ''
	UART.close()
	UART.open()
	try:
		Znach = UART.read()
		if Znach == StartFl:
			for Counter in range(13):
				Znach = UART.read()
				if Znach <> EndFl:
					ID = ID + str(Znach)
				else:
					UART.close()
					for I in range(0,9,2):
						Checksumma = Checksumma ^ (((int(ID[I], 16)) << 4) + int(ID[I+1], 16))
					Checksumma = hex(Checksumma)
					Tag = ((int(ID[1], 16)) << 8) + ((int(ID[2], 16)) << 4) + ((int(ID[3], 16)) << 0)
					Tag = hex(Tag)
					if ID==IdOld:
						print "*****************************************"
						print "------->> DUBLICATE ATTENTION!!! <<------"
						print "*****************************************"
					print "-----------------------------------------"
					print "Data: ", ID
					print "Tag: ", Tag
					print "ID: ", ID[4:10], " - ", int(ID[4:10], 16)
					print "Checksum: ", Checksumma
					print "-----------------------------------------"
					time.sleep(3)
					UART.open()
	except OSError:
		print "RRRRRRRR"
