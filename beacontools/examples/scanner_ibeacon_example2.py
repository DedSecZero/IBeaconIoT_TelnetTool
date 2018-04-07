import time
import webbrowser
import sys
import os
import subprocess
from beacontools import BeaconScanner, IBeaconFilter
import threading

rangeMax = -65
Fin = False
print(Fin)
def openBrowser():
   #webbrowser.open("http://www.google.com.co")
   os.system("sudo chromium-browser -no-sandbox http://www.google.com.co")

def closeBrowser():
   os.system("sudo killall chromium-browser")
#   os.system("sudo killall epiphany-browser")

def callback(bt_addr, rssi, packet, additional_info):
    if rssi > rangeMax:
       	print("aqui, <%d>" %(rssi))
	Fin = True
        print(Fin)
        print('Abriendo Navegador')
        threading.Thread(target=openBrowser).start() #os.system("chromium-browser http://www.google.com.co")
        print('Delay de espera')
        time.sleep(10) #del
        print('Cerrando Navegador')
        closeBrowser() #threading.Thread(target=closeBrowser).start()
        sys.exit(0)


# scan for all iBeacon advertisements from beacons with the specified uuid
scanner = BeaconScanner(callback,
    device_filter=IBeaconFilter(uuid="00000003-0000-0000-0000-000000000000"))

scanner.start()
