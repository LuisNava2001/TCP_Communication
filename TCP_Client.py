import socket

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5000))
    print("==========================================")
    print("[CLIENT] YOU ARE CONNECTED TO THE SERVER TCP...")
    print("==========================================\n")

    while True:
        mensaje=input("INPUT A MESSAGE TO THE SERVER ('DISCONNECT' TO CLOSE COMMUNICATION):\n[CLIENT]: ")
        if not mensaje.strip():
            print("Empty message, please try again!")
            continue
        client_socket.sendall(mensaje.encode())
        if mensaje.strip()=="DISCONNECT":
            client_socket.close()
            print(f"[CLOSED CONNECTION] {client_socket}")
            print("COMMUNICATION WITH THE SERVER WAS DISCONNECTED....")
            break
        respuesta=client_socket.recv(1024).decode().strip()
        print(f"[SERVER]: {respuesta}")

tcp_client()
