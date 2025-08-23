import socket
import os

def setup_terminal(title="TCP_CLIENT", width=100, height=100):
    os.system("color 0A")
    os.system(f"title {title}")
    os.system(f"mode con: cols={width} lines={height}")

def tcp_client():
    setup_terminal(title="TCP CLIENT", width=100, height=100)
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
