# El servidor crea una FIFO
import os, time, sys
cliserv_fifo = '/tmp/cliserv_fifo' # Guardamos el path del archivo en la variable cliserv_fifo
if not os.path.exists(cliserv_fifo):
    os.mkfifo(cliserv_fifo) # Crea el FIFO


while True: # Para que pueda atender a varios clientes
    # Abrimos el servidor solo en modo escritura: 
    fifo_serv = open(cliserv_fifo, 'w') # fifo_serv = open(cliserv_fifo, os.O_WRONLY)
    tiempo = time.ctime(time.time()) # Calcula el tiempo
    fifo_serv.write(tiempo) # El servidor escribe el tiempo 
    fifo_serv.close()
    time.sleep(1)