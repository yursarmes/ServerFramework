#Rover Model Version 0.1
'''
Rover Model:
IMU:
	Euler Angle Rotations: [double x, double y, double z]
	Compass Heading: [double heading]
GPS: 
	Position: [double lati, double long]
ICCE Box:
	Temperature: [double temp]
	Voltage: [double voltage]
	current: [double current]
Drive Motors:
	ForwardLeft/Right, RearLeft/Right:[double voltage]
'''
from collections import namedtuple

Orientation = namedtuple('Orientation', 'x y z')# Euler Angles
Compass = namedtuple('Compass', 'heading')
GPS = namedtuple('GPS', 'lati long')
ICCE = namedtuple('ICCE', 'Temp volt curr')
Drive = namedtuple('Drive', 'FL FR RL RR')

class RoverModel:
	def __init__(self):
		self._IMU_Orientation = Orientation(0.0, 0.0, 0.0)
		self._IMU_CompassHeading = Compass(0.0)
		self._GPS_Position = GPS(0.0, 0.0)
		self._ICCE_Box = ICCE(0.0, 0.0, 0.0)
		self._DriveMotors = Drive(0.0, 0.0, 0.0, 0.0)

	def getOrientation(self):
		return self._IMU_Orientation

	def getCompassHeading(self):
		return self._IMU_CompassHeading

	def getGPS(self):
		return self._GPS_Position

	def getICCE_Box(self):
		return self._ICCE_Box

	def getDriveMotors(self):
		return self._DriveMotors