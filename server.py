from computer import Computer
import socket, sys                                                          
from datetime import datetime                                                 

class Server(Computer):                                                     

    _service = ''
    __sockIP = None
    __sockPort = None

    def __init__(self, cpu, cpuclock, ram, os, ip, service):
        super().__init__(cpu, cpuclock, ram, os, ip)                        
        self._service = service                                             

    def createSocket(self, sockIP, sockPort):

        try:
            #Den Socket-Server erstellen
            server_socket = socket.socket()                                 
            self.__sockIP = str(sockIP); self.__sockPort = int(sockPort)  
            #IP und Port auf den Server einbinden
            server_socket.bind((self.__sockIP, self.__sockPort))            
            self.__sock = server_socket                                     
        except Exception as e:
            print(f'Error')
        

    def runningServer(self):
             
        try:
            server_socket = self.__sock    
            #Maximal auf 2 verbindungen hören den wert in der klammer austauschen für mehr 
            server_socket.listen(2)                                         
            print('Server started...')
            conn, addr = server_socket.accept()                             
            print(f"Got connection from: {str(addr[0])}:{str(addr[1])}")
            clientmsg = 'Got connection message from:  '
            conn.send(clientmsg.encode())                                   

            while True:
                #auf Nachrichten in 1024 bit warten
                client_input = conn.recv(1024).decode()  
                #wenn die nachricht "shutdown" lautet den Server herunterfahren
                if client_input == 'shutdown':                              
                    print("Receive remote-command: Server is shutting down")
                    conn.close()                                            
                    sys.exit()          
                #ansonsten die Nachrichten ausgeben mit Uhrzeit/IP/Port
                else:
                    if client_input:                                        
                        print(f"{datetime.now().strftime('%H:%M:%S')} [{addr[0]}]: {str(client_input)}")  
        except Exception as e:                                              
            print(f'Error')                                      


if __name__ == '__main__':
    #Beispieldaten um den Server zu initialisieren 
    server = Server('CPU',4.04, 404, 'OS', '192.168.1.1', 'TCP Socket Server')
    #Holt die neuen richtigen daten und ersetzt die Platzhalter
    server.getInfo()                                                        
    print(f'Service: {server._service}')
    print("________________________________")
    server.createSocket('127.0.0.1',1337)                                   
    server.runningServer()                                                  