import os, sys, time
# Tubería que va de servidor a cliente (cliente escribe y servidor lee)
rd,wd = os.pipe() # son file descriptors, no file objects (crea tubería)
r, w = os.fdopen(rd,'rb',0), os.fdopen(wd,'wb',0) # file objects 

pid_serv = os.fork() # Creamos 2 procesos que van a hacer lo mismo 
if pid_serv: # padre
    w.close() # cliente no necesita escribir en tubería 
    pid_cli = os.fork() 
    if pid_cli: #padre
        r.close() 
    else: # hijo cliente
        data = r.readline() # Cliente lee contenido de tubería 
        sys.stdout.write(data.decode('utf8').strip())
        r.close()

else: # hijo servidor 
    r.close() # servidor no necesita leer en tubería 

    tiempo = time.ctime(time.time())
    w.write(tiempo.encode('utf8'))
    w.flush()

    w.close()
