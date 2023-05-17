# CLIENTE:
# 1. Creación del socket local. Socket UDS 
# 2. Preparación de la dirección del servidor.
# 3. Envío del mensaje.
# 4. Espera del resultado.
# 5. Explotación del resultado.
import socket, os 

#1 
sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) # 1 (dominio, tipo, protocolo)

#2
dir_socket = input("Introduzca la dirección del servidor: ") 
puerto = input("Introduzca el puerto del servidor: ")
if not dir_socket:
    dir_socket = '127.0.0.1'
if not puerto:
    puerto = '8000'

# 3
path = input ("Introduzca el path del archivo que quiere leer: ")
sc.sendto(path.encode('utf8'), (dir_socket, int(puerto)))

# 4 y 5 ?????
print("Path enviado. El contenido del fichero en", path, "es: ") 
while True:
    data, dir = sc.recvfrom(1024) # Cliente lee contenido del socket
    if not data: 
        break
    print(data.decode('utf8')) 

sc.close()

