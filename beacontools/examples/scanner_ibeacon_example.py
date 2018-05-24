import time
import webbrowser
import sys,threading
from beacontools import BeaconScanner, IBeaconFilter

rangeMax = -38

def callback(bt_addr, rssi, packet, additional_info):
    print(threading.current_thread().)
    if rssi > rangeMax:
	print("aqui, <%d>" %(rssi))
   #else:
	


# scan for all iBeacon advertisements from beacons with the specified uuid
scanner = BeaconScanner(callback,
    device_filter=IBeaconFilter(uuid="00000003-0000-0000-0000-000000000000"))

scanner.start()
# time.sleep(0.5)
# scanner.stop()
