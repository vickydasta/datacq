import serial
import glob

class port:
	def __init__(self):
		pass
	def portlist(self):
		ports = glob.glob('/dev/tty[A-Za-z]*')
		res = []
		for port in ports:
			try:
				s = serial.Serial(port)
				s.close()
				res.append(port)
			except Exception:
				pass
		return res[0]

def main():
	port = port().portlist()
	print port

if __name__ == '__main__':
	main()
