import socket
import threading
import logging
from datetime import datetime

def handle_client(conn, address_client, client_id):
    log_filename = f"client_{client_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logger = logging.getLogger(f"Client-{client_id}")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_filename)
    fh.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logger.addHandler(fh)

    logger.info(f"Connection established with {address_client}")

    print(f"[NEW CONNECTION] {address_client}")
    while True:
        try:
            datos = conn.recv(1024).decode().strip()
            if not datos:
                break
            print(f"CLIENT {address_client}: {datos}")
            logger.info(f'CLIENT: {datos}')
            if datos.upper() == "DISCONNECT":
                conn.sendall("CLOSING CONNECTION...".encode())
                break
            else:   
                if "como estas" in datos:
                    datos = "Muy bien, gracias por preguntar, y tu?"
                conn.sendall(datos.upper().encode())
        except ConnectionResetError:
            print(f"[ERROR] CLIENT {address_client} DISCONNECTED UNEXPECTEDLY.")
            break
        except OSError:
            print(f"[ERROR] CLIENT {address_client} CLOSED THE CONNECTION.")
            break
    logger.info("CONNECTION CLOSED")
    conn.close()
    print(f"[CLOSED CONNECTION] {address_client}")

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen(5)
    print("========================================================")
    print("[SERVER] LISTENING ON localhost::5000...")
    print("========================================================\n")

    client_id = 0
    while True:
        conn, address = server_socket.accept()
        client_id += 1
        thread = threading.Thread(target=handle_client, args=(conn, address, client_id))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.active_count()-1}")

if __name__ == "__main__":
    tcp_server()
