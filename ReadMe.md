# Proyecto de Comunicación TCP

Este proyecto implementa un servidor y un cliente que se comunican entre sí a través de una conexión TCP/IP en la misma máquina (localhost). El servidor y el cliente están escritos en Python, y los archivos `.bat` proporcionan una forma sencilla de ejecutar ambos programas en sistemas Windows.

## Requisitos

- Python 3.x instalado en tu máquina.
- Archivos `.bat` para ejecutar el servidor y el cliente fácilmente.

## Archivos incluidos

- `server.py`: El servidor TCP que espera conexiones de clientes.
- `client.py`: El cliente TCP que se conecta al servidor y envía mensajes.
- `Run_Server.bat`: Script de Windows para ejecutar el servidor.
- `Run_Client.bat`: Script de Windows para ejecutar el cliente.

## Instrucciones para usar

### 1. Preparativos iniciales
Asegúrate de tener Python instalado en tu sistema. Si no lo tienes, puedes descargarlo desde [aquí](https://www.python.org/downloads/).

### 2. Ejecutar el Servidor
1. Abre una terminal o ventana de comandos.
2. Navega a la carpeta donde tienes los archivos `Server.py` y `Run_Server.bat`.
3. Ejecuta el archivo `Run_Server.bat` haciendo doble clic sobre él. Esto iniciará el servidor TCP, que estará esperando conexiones en el puerto `5000` en `localhost`.
4. Una vez iniciado, el servidor mostrará un mensaje similar a este: `Servidor TCP en espera de conexiones en localhost:5000...`

### 3. Ejecutar el Cliente
1. Abre una terminal o ventana de comandos.
2. Navega a la carpeta donde tienes los archivos `Client.py` y `Run_Client.bat`.
3. El cliente pedirá que ingreses un mensaje para enviar al servidor: `Ingrese el mensaje a enviar al servidor (o 'DESCONEXION' para salir):`

## Ejemplo de ejecución



