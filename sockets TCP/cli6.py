import socket, os

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

dir_socket = input("Introduzca la dirección del servidor: ") 
puerto = input("Introduzca el puerto del servidor: ")
if not dir_socket:
    dir_socket = '127.0.0.1'
if not puerto:
    puerto = '8000'

try:
    sc.connect((dir_socket, int(puerto))) # El cliente se conecta al socket 
    
except:
    print("Error al conectar, vuelva a intentarlo")
    exit()

path = input ("Introduzca el path del archivo que quiere leer: ")
sc.send(path.encode('utf8'))

print("Path enviado. El contenido del fichero en", path, "es: ") 

while True:
    data = sc.recv(1024)
    if not data:
        break
    print(data.decode('utf8'))
sc.close()

