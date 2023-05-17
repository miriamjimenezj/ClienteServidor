import socket 
import os, sys, time
# CLIENTE:
# 1. Creación del socket local. Socket UDS 
# 2. Preparación de la dirección del servidor.
# 3. Envío del mensaje.
# 4. Espera del resultado.
# 5. Explotación del resultado.

# try except???

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0) # 1 (dominio, tipo, protocolo)

# 2
dir_socket = input("Introduzca el nombre del socket: ") 
if not dir_socket:
    dir_socket = 'socketp4'
try:
    s.connect("/tmp/" + dir_socket) # El cliente se conecta al socket 
except:
    print("Error al conectar, vuelva a intentarlo")
    exit()

# 3
path = input ("Introduzca el path del archivo que quiere leer: ")
s.send(path.encode('utf8'))

# 4 y 5
print("Path enviado. El contenido del fichero en", path, "es: ") 
while True:
    data = s.recv(1024) # Cliente lee contenido del socket
    if not data: # Sale del bucle si ha llegado a un end of file (EOF)
        break
    print(data.decode('utf8').strip()) 
s.close()


