import subprocess

#cmd="sudo iwlist wlan0 scan | grep -e Signal -e ESSID"
class RSSI:
	def __init__(self,essid,wlan_manager):
		self.essid=essid
		self.wlan_manager=wlan_manager
		self.rssi=0
		self.cmd='sudo iwlist '
		self.cmd = self.cmd + self.wlan_manager + ' scan | grep -e Signal -e ESSID'

	def GetRSSI(self):
		process = (subprocess.Popen(self.cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]).decode('utf-8')
		iwlist = process.split('\n')
		for idx,line in enumerate(iwlist):
#			line = line.strip()
			if self.essid in line:
				sigline_idx = idx + 1
				signal_line = iwlist[sigline_idx]
				tmp=signal_line.rfind('=')
				tmp1=signal_line.rfind('/')
				rssi_per=signal_line[tmp+1:tmp1]
				rssi_dBm=0.6*int(rssi_per)-95
				return rssi_dBm

