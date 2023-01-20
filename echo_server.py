import socket
import time
import threading

HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 4096

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        print("Starting proxy server")
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2) # allows 2 connections
        
        print("Listening...")

        # listen for connections
        while True:
            conn, address = s.accept()
            t = threading.Thread(target=handleConnection, args=(conn, address))
            t.run()

# made the listener threaded instead of a singular while loop in main
def handleConnection(conn, address):
    with conn:
        print("Connected by", address) # confirm the connection
        
        while True:
            full_data = conn.recv(BUFFER_SIZE)
            if not full_data:
                break
            conn.sendall(full_data)
    
if __name__ == "__main__":
    main()