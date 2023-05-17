# SERVIDOR:
# 1. Creación y enlace al puerto de servicio de un socket.
# 2. Bucle infinito en el cual el servidor:
#   a. Espera una petición.
#   b. La trata.
#   c. Calcula y formatea la respuesta.
#   d. Envía la respuesta.
import socket
import sys, time, os

# 1
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0) # creo socket
dir_socket = input("Introduzca el nombre del socket: ") 
if not dir_socket:
    dir_socket = 'socketp4'
if os.path.exists('/tmp/' + dir_socket):
    os.remove("/tmp/" + dir_socket)
# enlazar el socket con una direccion a la cual se va a conectar el cliente 
try:
    s.bind("/tmp/" + dir_socket) 
except:
    print("Error al enlazar el socket, vuelva a intentarlo")
    exit()


# 2
i = 0
while True: 
    s.listen(5) # 2a 
    ns, direccion = s.accept() # 2b
    print ("Se ha establecido una conexión con el cliente nº" , i)
    pid = os.fork() 

    if pid: # padre, proceso servidor. 
        i+=1
        ns.close()
        continue
    else: # hijo, proceso que gestiona el hijo
        # 2c y 2d 
        data = ns.recv(1024)
        print("El cliente" , i , "ha pedido el fichero" , data.decode('utf8').strip())
        try:
            f = open(data.decode('utf8').strip(), 'r') # Abre el fichero que le pasa el cliente
            line = f.readline() 
            while line !='':   # Bucle que lee las lineas del fichero y las escribe 
                ns.send(line.encode('utf8'))
                line = f.readline() 
        except:
            ns.send("El fichero no existe o no se puede abrir".encode('utf8'))
        
        ns.close()
        print("El cliente" , i , "ha cerrado conexión")
        exit()