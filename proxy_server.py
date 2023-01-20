import socket
import time
import threading

HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 1024

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

def handleConnection(conn, address):
    print("Connected by", address) # confirm the connection

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy:
        print("Connecting to Google")
        
        # get host IP
        hostIP = socket.gethostbyname("www.google.com")

        # connect proxy
        proxy.connect((hostIP, 80))

        # send data
        data = conn.recv(BUFFER_SIZE)
        print(f"Sending recieved data {data} to google")
        proxy.sendall(data)

        # shut down
        proxy.shutdown(socket.SHUT_WR)

        more_data = proxy.recv(BUFFER_SIZE)
        print(f"Sending recieved data {more_data} to client")
        # send data back
        conn.send(data)
    
    conn.close()

        
if __name__ == "__main__":
    main()