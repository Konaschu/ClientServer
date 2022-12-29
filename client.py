from computer import Computer
import socket

class Client(Computer):                                                         
#Klasse zum Erstellen des Clients
    __remoteIP = None
    __remotePort: None

    def create_socket(self, remoteIP, remotePort):
    # Erstellt eine Socket-Verbindung
        try:
            client_socket = socket.socket()                                     
            self.__remoteIP = remoteIP; self.__remotePort = remotePort          
            client_socket.connect((self.__remoteIP,self.__remotePort))          
            print(f'{client_socket.recv(1024).decode()}')                       
            
            self.__sock = client_socket                                         
        except Exception as e:                                                  
            print(f'Error')
        
    def sendData(self, string=None):
    #Sendet Daten in form von nachrichten an den Server
        client_socket = self.__sock                                        

        if string == None:                                                 
            while True:
                string = input('Nachricht: ')                              
                if client_socket != None:      
                    #Der Shutdown befehl zum herunterfahren des Servers über den Client
                    if string == 'shutdown':                                  
                        print('Send remote-command: Server is shutting down')
                        client_socket.send(string.encode())                     
                        client_socket.close()                                   
                        break                                                   
                    else:
                        client_socket.send(string.encode())                     

if __name__ == '__main__':
    #Beispieldaten um den Client zu initialisieren 
    client = Client('CPU',4.04, 404, 'OS', '192.168.1.1')          
    #Holt die neuen richtigen daten und ersetzt die Platzhalter
    client.getInfo()
    print(f'Remote-IP: None')
    print(f'Remote-Port: None')
    client.create_socket('127.0.0.1',1337)                                          
    client.sendData()                                                               