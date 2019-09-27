
from rssi import RSSI

def print_rssi_loop(essid, wlan_man):
	siglevel = RSSI(essid, wlan_man)
	while True:
		key = raw_input()
		if key == 'c': break
		rssi = siglevel.calcRSSI()
		print(rssi)
		
def main():
	while True:
		essid = raw_input('Search target ESSID : ')
        	wlan_man = raw_input('Is wlan manager wlan0 or wlan1 ? : ')
        	can = raw_input('ESSID = ' + essid + ' wlan manager = ' + wlan_man + ' Y/N : ')
		if can == 'Y' or can == 'y':
        		print_rssi_loop(essid, wlan_man)
              		return
        	else:
                	print('Input again')

if __name__ == '__main__':
	main()

