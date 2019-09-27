from rssi import RSSI

def main():
	siglevel=RSSI('NETROBO(11n)','wlan0')
	rssi=siglevel.calcRSSI()
	print(rssi)

if __name__ == '__main__':
	main()
