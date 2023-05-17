# Sobre el proyecto 
Esta práctica consiste en realizar un sencillo sistema cliente-servidor utilizando FIFOs (tuberías con nombre) de Unix. 

# Aplicación: cliente-servidor de fecha y hora
El objetivo es realizar una sencilla aplicación cliente-servidor que muestre la fecha y hora. 
1. El cliente se conecta al servidor mediante una tubería FIFO
2. El servidor responderá con una cadena de carácteres que represente la fecha y la hora.
3. El cliente muestra la respuesta recibida por el servidor en su salida estándar.

# Cómo ejecutar la Aplicación
Para ejecutar el servidor usa el siguiente comando:

    make servidor

Para ejecutar el cliente usa el siguiente comando:

    make cliente

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
