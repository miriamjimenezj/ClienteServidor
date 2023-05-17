# CLIENTE:
# 1. Creación del socket local. Socket UDS 
# 2. Preparación de la dirección del servidor.
# 3. Envío del mensaje.
# 4. Espera del resultado.
# 5. Explotación del resultado.
import socket, sys

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
peticion = ''
sc.sendto(peticion.encode('utf8'), (dir_socket, int(puerto)))

# 4 y 5 
data, dir = sc.recvfrom(1024) # Cliente lee contenido del socket
sys.stdout.write(data.decode('utf8').strip()) 
print("\n")
sc.close()
