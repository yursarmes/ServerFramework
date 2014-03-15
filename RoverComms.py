#Communications to the rover. This is the only code that actually talks to the rover. All communications goes through this.

import thread
import time
import threading
import socket # for COMMS_UDP

ROVER_RECV_UDP_IP = "127.0.0.1"
ROVER_RECV_UDP_PORT = 5005
ROVER_SEND_UDP_IP = "127.0.0.1"
ROVER_SEND_UDP_PORT = 5006

SERVER_RECV_UDP_IP = "127.0.0.1"
SERVER_RECV_UDP_PORT = 10000
SERVER_SEND_UDP_IP = "127.0.0.1"
SERVER_SEND_UDP_PORT = 10001

# COMMS MODE
COMMS_UDP    = 0
COMMS_SERIAL = 1

THREAD_DELAY = 0.01

class RoverComms:
	def __init__(self, mode):
		self.mode = mode
		_initUDPComms()
		_initSerialComms()
		thread1 = roverRecvThread(recvFunc, THREAD_DELAY)

	def _initUDPComms(self):
		self.roverSock = socket.socket(socket.AF_INET, # Internet
				 socket.SOCK_DGRAM) # UDP
		self.roverSock.bind((ROVER_RECV_UDP_IP, ROVER_RECV_UDP_PORT))

	def _initSerialComms(self):
		return;

	def UDPSend(self, msg):
		roverSock.sendto(MESSAGE, (ROVER_SEND_UDP_IP, ROVER_SEND_UDP_PORT))
		return;

	def _UDPRecv(self):
		data, addr = roverSock.recvfrom(1024) # buffer size is 1024 bytes
		return data

	class recvThread (threading.Thread):
		def __init__(self, recvFunc, delay):
			threading.Thread.__init__(self)
			self.recvFunc = recvFunc
			self.delay = delay

		def run(self):
			isRunning = True
			while isRunning:
				data = self.recvFunc()
				if data == 'end':
					isRunning = False
				print 'recv:',data
				time.sleep(self.delay)