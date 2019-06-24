import sys
import subprocess

def main():
	essid='eduroam'
	cmd="sudo iwlist wlan0 scan | grep -e Signal -e ESSID"
	process = (subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]).decode('utf-8')
	iwlist=process.split('\n')
	for idx,line in enumerate(iwlist):
#		line = line.strip()
		if essid in line:
			print(line)
			sigline_idx = idx+1
			sigline = iwlist[sigline_idx]
			print(sigline)
			tmp = sigline.rfind('=')
			tmp1 = sigline.rfind('/')
			rssi_per = sigline[tmp+1:tmp1]
			rssi_dBm = (0.6*int(rssi_per))-95

			print('RSSI[%] = {rssi_per} -> RSSI[dBm] = {rssi_dBm}'
			.format(rssi_per=rssi_per,rssi_dBm=rssi_dBm))

			break

if __name__ == "__main__":
	main()
