# SERVIDOR:
# 1. Creación y enlace al puerto de servicio de un socket.
# 2. Bucle infinito en el cual el servidor:
#   a. Espera una petición.
#   b. La trata.
#   c. Calcula y formatea la respuesta.
#   d. Envía la respuesta.
import socket, os, time
# 1
ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) # creo socket

dir_socket = input("Introduzca la dirección del servidor: ") 
puerto = input("Introduzca el puerto del servidor: ")
if not dir_socket:
    dir_socket = '127.0.0.1'
if not puerto:
    puerto = '8000'
try:
    ss.bind((dir_socket, int(puerto)))
except:
    print("Error al asignar una dirección al servidor")

# 2
while True:  
    data, dirc = ss.recvfrom(1024)
    pid = os.fork()
    if pid: # padre, proceso servidor. 
        continue
    else: # hijo, proceso que gestiona el hijo
        # 2c y 2d 
        print("El cliente" , dirc , "ha pedido la hora")
        tiempo = time.ctime(time.time())
        ss.sendto(tiempo.encode('utf8'),dirc)
        
        ss.close()
        print("El cliente" , dirc , "ha cerrado conexión")
        exit()