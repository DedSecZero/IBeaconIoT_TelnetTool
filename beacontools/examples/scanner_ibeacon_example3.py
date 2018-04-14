import time
import webbrowser
import sys
import os
import subprocess
from beacontools import BeaconScanner, IBeaconFilter
import threading, commands

rangeMax = -40

def openBrowserCam():
   #os.system("sudo chromium-browser -no-sandbox http://172.71.10.23:8080/?action=stream")
    #os.system("sudo chromium-browser -no-sandbox http://www.google.com.co")
    os.system("sudo python openBrowser.py")
    
def openBrowserBlack():
    os.system("sudo chromium-browser -no-sandbox file:///home/pi/Desktop/prueba2/beacontools/examples/index.html")

def closeBrowser():
    os.system("sudo killall chromium-browser")

def callback(bt_addr, rssi, packet, additional_info):
    if rssi > rangeMax:
        print("aqui, <%d>" %(rssi))
        output = commands.getoutput('ps -A')
        #if 'chromium-browse' in output:
        #    closeBrowser()
        print('Ejecucion Hilo Navegador')
        #threading.Thread(target=openBrowserCam).start()
        #os.system("sudo chromium-browser -no-sandbox http://www.google.com.co")
        print("NAVEGADOR ABIERTO -----------------------------")
        #print('Delay de espera')
        time.sleep(15) #del
        #print('Cerrando Navegador')
	closeBrowser()
	#print("Close interno")
	#threading.Thread(target=closeBrowser).start()
        #closeBrowser()
# scan for all iBeacon advertisements from beacons with the specified uuid
print("Iniciando Hilo de Scanner")
scanner = BeaconScanner(callback,
    device_filter=IBeaconFilter(uuid="00000003-0000-0000-0000-000000000000"))
#threading.current_thread()

scanner.start()
time.sleep(15)
#print("Stop externo")
scanner.stop()


