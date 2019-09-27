'''
# @file rssi.py
# @brief This file is a program for obtaining 
# the received signal strength indicator.
# @author koji kawabata
# @date 2019/06/25
'''

import subprocess

class RSSI:
	'''
	# @param (essid) ESSID you want to find
	# @param (wlan_manager) wifi interface
	# self.cmd variable combined like "sudo iwlist (wlan0 or wlan1) scan | grep -e Signal -e ESSID"
	'''
	def __init__(self,essid,wlan_interface):
		self.essid = essid
		self.wlan_interface=wlan_interface
		self.rssi = 0
		self.cmd ='sudo iwlist '
		self.cmd = self.cmd + self.wlan_interface + ' scan | grep -e Signal -e ESSID'
	
	'''
	# @brief Find the line with essid from the output result of self.cmd, obtain the signal intensity 
	# in the next line by dividing it, and finally convert it to dBm.
	# @return RSSI converted from % to dBm
	'''
	def calcRSSI(self):
		process = (subprocess.Popen(self.cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]).decode('utf-8')
		iwlist_table = process.split('\n')
		for essid_line_idx,essid_line in enumerate(iwlist_table):
			if self.essid in essid_line:
				sigline_idx = essid_line_idx + 1
				sigline = iwlist[sigline_idx]
				begin_idx = sigline.rfind('=')
				end_idx = sigline.rfind('/')
				rssi_per = signal_line[begin_idx + 1 : end_idx]
				rssi_dBm = 0.6 * int(rssi_per) - 95
				return rssi_dBm

	def searchESSID(self):
		return self.essid

	def searchWlanInterface(self):
		return self.wlan_interface

	def cmd(self):
		return self.cmd