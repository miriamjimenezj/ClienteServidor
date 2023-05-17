import socket, os

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

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
    exit()

while True: 
    ss.listen(5) 
    ns, dirc = ss.accept()
    print ("Se ha establecido una conexión con el cliente " , dirc)
    pid = os.fork() 

    if pid: # padre, proceso servidor. 
        ns.close()
        continue
    else: #hijo
        data = ns.recv(1024)
        print("El cliente" , dirc , "ha pedido el fichero" , data.decode('utf8').strip())
        try:
            f = open(data.decode('utf8').strip(), 'rb') # Abre el fichero que le pasa el cliente
            line = f.readline() 
            while line !='':   # Bucle que lee las lineas del fichero y las escribe 
                ns.send(line.encode('utf8'))
                line = f.readline() 
        except:
            ns.send("El fichero no existe o no se puede abrir".encode('utf8'))
        ns.close()
        print("El cliente", dirc, "ha cerrado conexión")
        exit()
