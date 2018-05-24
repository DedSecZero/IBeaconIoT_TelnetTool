import time
import webbrowser
import sys
import os
import subprocess
from beacontools import BeaconScanner, IBeaconFilter
import threading, commands

rangeMax = -40
def openBrowserCam():
   os.system("/usr/bin/python /home/pi/Desktop/IBeaconIoT_TelnetTool/beacontools/examples/openBrowser.py")
   #os.system("sudo su - pi -c '/usr/bin/python /home/pi/Desktop/IBeaconIoT_TelnetTool/beacontools/examples/openBrowser.py'")
   #os.system("/bin/su - pi -c '/usr/bin/python /home/pi/Desktop/IBeaconIoT_TelnetTool/beacontools/examples/openBrowser.py'")
def openBrowserBlack():
    os.system("sudo chromium-browser -no-sandbox file:///home/pi/Desktop/prueba2/beacontools/examples/index.html")

def closeBrowser():
    #os.system("sudo killall chromium-browser")
    os.system("/usr/bin/killall chromium-browse")

def callback(bt_addr, rssi, packet, additional_info):
    print("aqui, <%d>" %(rssi))
    if rssi > rangeMax:
        print("aqui, <%d>" %(rssi))
        output = commands.getoutput('ps -A')
        print('Ejecucion Hilo Navegador')
        threading.Thread(target=openBrowserCam).start()
        time.sleep(30) #del
        closeBrowser()
    else:
        output = commands.getoutput('ps -A')
        if 'chromium-browse' in output:
           closeBrowser()


# scan for all iBeacon advertisements from beacons with the specified uuid
print("Iniciando Hilo de Scanner")
scanner = BeaconScanner(callback,
    device_filter=IBeaconFilter(uuid="00000003-0000-0000-0000-000000000000"))

scanner.start()
print(threading.current_thread())
time.sleep(30)
print("Stop externo")
scanner.stop()
sys.exit(0)
