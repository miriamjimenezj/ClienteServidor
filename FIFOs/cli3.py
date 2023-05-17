# El cliente crea una FIFO
import os, time, sys
cliserv_fifo = '/tmp/cliserv_fifo' # Guardamos el path del archivo en la variable cliserv_fifo
if not os.path.exists(cliserv_fifo):
    print("No existe", cliserv_fifo, ", ejecute el proceso servidor")
    exit()

# El cliente solo tiene que leer en contenido que le muestra el servidor: 
fifo_cli = open(cliserv_fifo, 'r') # fifo_serv = open(cliserv_fifo, os.O_RDONLY)
data = fifo_cli.readline() # Cliente lee contenido del FIFO
sys.stdout.write(data.strip()) 
fifo_cli.close()
