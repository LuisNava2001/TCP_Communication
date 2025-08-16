import socket
import threading

def handle_client(conn, address_client):
    print(f"[NEW CONNECTION] {address_client}")
    while True:
        try:
            datos = conn.recv(1024).decode().strip()
            if not datos:
                break
            print(f"CLIENT {address_client}: {datos}")
            if datos.upper() == "DISCONNECT":
                conn.sendall("CLOSING CONNECTION...".encode())
                break
            else:
                conn.sendall(datos.upper().encode())
        except ConnectionResetError:
            print(f"[ERROR] CLIENT {address_client} DISCONNECTED UNEXPECTEDLY.")
            break
        except OSError:
            print(f"[ERROR] CLIENT {address_client} CLOSED THE CONNECTION.")
            break
    conn.close()
    print(f"[CLOSED CONNECTION] {address_client}")

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen(5)
    print("========================================================")
    print("[SERVER] LISTENING ON localhost::5000...")
    print("========================================================\n")

    while True:
        conn, address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.active_count()-1}")

tcp_server()
