import socket

HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 1024
request = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(addr)
            s.sendall(request.encode())
            s.shutdown(socket.SHUT_WR)

            full_data = s.recv(BUFFER_SIZE)
            print(full_data)
    
    except Exception as e:
        print(e)

    finally:
        s.close


def main():
    connect(('127.0.0.1', 8001))

if __name__ == "__main__":
    main()