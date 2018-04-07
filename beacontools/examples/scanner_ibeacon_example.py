import time
import webbrowser
import sys
from beacontools import BeaconScanner, IBeaconFilter

rangeMax = -65
b = 0

def callback(bt_addr, rssi, packet, additional_info):
    if rssi > rangeMax:
       	# print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))
	print("aqui, <%d>" %(rssi))
	webbrowser.open_new("https://www.google.com.co")
	sys.exit(0)
   #else:
#	print("lejos, <%d>" % (rssi))


# scan for all iBeacon advertisements from beacons with the specified uuid
scanner = BeaconScanner(callback,
    device_filter=IBeaconFilter(uuid="00000003-0000-0000-0000-000000000000"))

scanner.start()
# time.sleep(0.5)
# scanner.stop()
