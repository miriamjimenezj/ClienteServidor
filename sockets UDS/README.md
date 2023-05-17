# Sobre el proyecto 
Esta práctica consiste en realizar un sencillo sistema cliente-servidor utilizando sockets UDS. 

# Aplicación: cliente-servidor de ficheros
El objetivo es realizar una sencilla aplicación cliente-servidor de ficheros. 
1. El cliente se conecta al servidor mediante un socket UDS y le enviará el path completo de un fichero.
2. El servidor responderá con el contenido del fichero o con un mensaje de error si no pudiera proporcionárselos. 
3. El cliente muestra la respuesta recibida por el servidor en su salida estándar.

# Cómo ejecutar la Aplicación
Para ejecutar el servidor usa el siguiente comando:

    make servidor

Para ejecutar el cliente usa el siguiente comando:

    make cliente

Para limpiar una vez ejecutada la Aplicación:

    make clean
