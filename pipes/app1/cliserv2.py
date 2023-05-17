# Cambiar nombres de los procesos 
# No abre archivos binarios, revisar más adelante
import os, sys, time
# Tubería que va de cliente a servidor (cliente escribe y servidor lee)
rd1,wd1 = os.pipe() # son file descriptors, no file objects (crea tubería)
r1, w1 = os.fdopen(rd1,'rb',0), os.fdopen(wd1,'wb',0) # file objects (abre tubería como un fichero)

# Tubería que va de servidor a cliente (cliente lee y servidor escribe)
rd2,wd2 = os.pipe() # son file descriptors, no file objects
r2, w2 = os.fdopen(rd2,'rb',0), os.fdopen(wd2,'wb',0) # file objects

pid_serv = os.fork() # Creamos 2 procesos que van a hacer lo mismo 
if pid_serv: # padre
    w2.close() # cliente no necesita escribir en tubería 2
    r1.close() # cliente no necesita leer de la tubería 1
    pid_cli = os.fork() 
    if pid_cli: #padre
        w1.close()
        r2.close()
    else: # hijo cliente
        path = './app1.txt'
        # path = '/etc/services'
        # path = '/bin/sh'
        w1.write(path.encode('utf8'))
        w1.write("\n".encode('utf8'))
        print("Path enviado. El contenido del fichero en", path, "es:") 
        while True:
            data = r2.readline() # Cliente lee contenido de tubería 2, es decir, lee las líneas del fichero que le va pasando el servidor 
            if not data: # Sale del bucle si ha llegado a un end of file (EOF)
                break
            print(data.decode('utf8').strip()) 
        w1.close()
        r2.close()

else: # hijo servidor (lee de tubería 1 y escibe en tubería 2)
    w1.close() # servidor no necesita escribir en tubería 1
    r2.close() # servidor no necesita leer de la tubería 2
    data = r1.readline() # Lee una línea de la tubería 1, es decir, lee el path que le envía el cliente
    try:
        f = open(data.decode('utf8').strip(), 'r') # Abre el fichero que le pasa el cliente
        line = f.readline() 
        while line !='':   # Bucle que lee las lineas del fichero y las escribe 
            w2.write(line.encode('utf8'))
            w2.flush()
            line = f.readline() 
    except:
        w2.write("El fichero no existe o no se puede abrir".encode('utf8'))
    
    w2.close()
    r1.close()
