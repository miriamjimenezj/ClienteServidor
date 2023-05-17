# SERVIDOR:
# 1. Creación y enlace al puerto de servicio de un socket.
# 2. Bucle infinito en el cual el servidor:
#   a. Espera una petición.
#   b. La trata.
#   c. Calcula y formatea la respuesta.
#   d. Envía la respuesta.
import socket, os 
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
        print("El cliente" , dirc , "ha pedido el fichero" , data.decode('utf8').strip())
        try:
            f = open(data.decode('utf8').strip(), 'r') # Abre el fichero que le pasa el cliente
            line = True
            while line:   # Bucle que lee las lineas del fichero y las escribe 
                line = f.read(1024) 
                ss.sendto(line.encode('utf8'), dirc)  
        except:
            ss.sendto("El fichero no existe o no se puede abrir".encode('utf8'), dirc)
            ss.sendto(''.encode('utf8'), dirc)
        
        ss.close()
        print("El cliente" , dirc , "ha cerrado conexión")
        exit()
