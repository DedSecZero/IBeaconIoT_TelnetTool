#Librerias
import threading
import sys,os
import telnetlib
import errno
from socket import error as socket_error
#Declaracion de variable que contiene la Ip a la cual se le realiza telnet
#HOST = "172.71.10.23"
HOST = "localhost"
#puerto = sys.argv[1]
#print(puerto)
#Definicion de funcion
def scanner():
   print("Ejecucion de Scanner en progreso")
   os.system("/usr/bin/python /home/pi/Desktop/IBeaconIoT_TelnetTool/beacontools/examples/scanner_beacon.py")
   print("Escaneo Finalizado")
def validarTelnet():
#   global puerto
   try: #Validacion en caso de error
      #tn = telnetlib.Telnet(HOST,8080)
      while True:
#         print("haciendo telnet")
         tn = telnetlib.Telnet(HOST,8080) #8080)
#         puerto = 8080
         print("Connect  ",HOST,":",8080) #imprimir connect en caso exitoso
         scanner()
         break
   except socket_error as serr: #control de error
      if serr.errno != errno.ECONNREFUSED:
         raise serr

#while True: #ciclo para que el programa se ejecute siempre
#threading.Thread(target=validarTelnet).start() #ejecutar hilo de validacion de telnet
while True:
   validarTelnet()
   pass
#pass # continar ciclo hasta interrupcion de teclado o servicio por parte del usuario
