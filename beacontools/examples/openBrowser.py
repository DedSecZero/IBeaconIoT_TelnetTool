import os,time
print("Abriendo Navegador")
#os.system("/usr/bin/chromium-browser -no-sandbox  http://172.71.10.23:8080/?action=stream")
os.system("/usr/bin/chromium-browser -no-sandbox http://192.168.43.29:8080/?action=stream")
#os.system("su - pi -c '/usr/bin/chromium-browser -no-sandbox http://192.168.43.29:8080/?action=stream'")

print("Delay fin python navegador")
time.sleep(30)
