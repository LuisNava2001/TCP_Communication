import socket

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5000))
    print("============================")
    print("Conectado al servidor TCP...")
    print("============================\n")

    while True:
        mensaje=input("Ingrese el mensaje para enviar al servidor (o 'DESCONEXION' para salir):\n")
        client_socket.sendall(mensaje.encode())
        if mensaje.strip()=="DESCONEXION":
            client_socket.close()
            print("Conexion cerrada...")
            print("Desconectando del servidor....")
            break
        respuesta=client_socket.recv(1024).decode()
        print(f"Respuesta del servidor: {respuesta}")

tcp_client()