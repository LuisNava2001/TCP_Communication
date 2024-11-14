import socket

def tcp_server():
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#   He decidido utilizar IPV4 para este ejemplo con .AF_INET
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen(5) #   Coloqué en espera más de un cliente
    print("===================================================")
    print("Servidor esperando conexiones en localhost::5000...")
    print("===================================================\n")

    while True:
        conn, address_cliente =server_socket.accept()
        print(f"Conexion Establecida con el Cliente: {address_cliente}")

        while True:
            try:
                datos=conn.recv(1024).decode()
                if not datos:
                    break
                print(f"Mensaje recibido del cliente: {datos}")
                if datos=="DESCONEXION":
                    print("Se cerro la conexion con el Cliente...")
                    respuesta="Solicito cerrar la conexion con el Servidor..."
                    conn.sendall(respuesta.encode())
                    conn.close()
                    print("Cerrando...")
                else:
                    respuesta=datos.upper()
                    conn.sendall(respuesta.encode())
            except ConnectionResetError:
                print("Cliente desconectado abuptamente...")
                break
            except OSError:
                print("Error: El cliente desconecto abuptamente...")
                break

        print("Esperando nueva conexion...")

tcp_server()