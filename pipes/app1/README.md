# Sobre el proyecto 
Esta práctica consiste en realizar un sencillo sistema cliente-servidor utilizando pipes (tuberías) de Unix. 

# Aplicación: cliente-servidor de ficheros
El objetivo es realizar una sencilla aplicación cliente-servidor de ficheros. 
1. El cliente se conecta al servidor mediante una tubería (pipe) y le enviará el path completo de un fichero.
2. El servidor responderá con el contenido del fichero o con un mensaje de error si no pudiera proporcionárselos. 
3. El cliente muestra la respuesta recibida por el servidor en su salida estándar.

# Cómo ejecutar la Aplicación
Para ejecutar la Aplicación usa el siguiente comando:

    make

Para limpiar una vez ejecutada la Aplicación:

    make clean

## Licencia

Copyright 2023 Miriam Jiménez

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
	
  http://www.apache.org/licenses/LICENSE-2.0
	
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License
