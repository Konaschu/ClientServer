import platform
import psutil
import socket
import cpuinfo

class Computer():
    
    def __init__(self, cpu, cpu_speed,ram,os,ip):
        self._cpu = cpu
        self._cpuclock = cpu_speed
        self._ram = ram
        self._os = os
        self._ip = ip
        
    def getInfo(self):
    
        #CPU Marke und Model
        #Bitte folgende 5 Zeilen auskommentieren falls Server und Client nicht starten
        #Und die 2 auskommentierten Zeilen wieder benutzbar machen
        #Der erste Ansatz ist eher wie im Beispiel und funktioniert über cpuinfo und der zweite über platform weshalb es universell laufen sollte
        cpu_info = cpuinfo.get_cpu_info()
        cpu_type = cpu_info.get("brand_raw")
        cpu_model = cpu_info.get("model_raw")
        self._cpu = cpu_type + " " + cpu_model
        print(f"CPU-Type: {self._cpu}")

#        self._cpu = platform.processor()
#        print(f"CPU: {self._cpu} ")
        
        #CPU Clock Speed
        self._cpuclock = psutil.cpu_freq() 
        cpu_freq_ghz = round(self._cpuclock.max / 1024, 2)
        print(f"CPU-Speed: {cpu_freq_ghz} GHz")
        
        #Eingebaute Ram Menge
        self._ram = round(psutil.virtual_memory().total / 1024**3, 0)
        print(f"RAM: {self._ram} GB")
        
        #Betriebsystem und Version 
        os_name = platform.system()
        os_version = platform.release()
        self._os = os_name + " " + os_version
        print(f"OS: {self._os}")
        
        #IP Adresse vom Gerät
        self._ip = socket.gethostbyname(socket.gethostname())
        print(f"IP-Adresse: {self._ip}")