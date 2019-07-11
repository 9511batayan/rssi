
from rssi import RSSI

def print_rssi_loop(self, essid, wlan_man):
	siglevel = RSSI(essid,wlan_man)
	while True:
		key = input()
		rssi = siglevel.GetRSSI()
		print(rssi)
		if key == 'c':
			break

def main():
        while True:
                print('Search target ESSID')
                essid = input()
                print('Wlan manager is wlan0 or wlan1 ?')
                wlan_man = input()
                print('ESSID = ' + essid + 'wlan manager = ' + wlan_man + ' : Y/N')
                can = input()
                if can == 'Y' and can == 'y':
               	 	print_rssi_loop()
                        return
                else:
                        print('Input again')

if __name__ == '__main__':
        main()