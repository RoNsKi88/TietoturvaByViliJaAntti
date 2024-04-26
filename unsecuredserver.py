import socket

def main():
    host = "127.0.0.1"
    port = 65432

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host,port))
    sock.listen(5)
    print(f"Unsecure server listening {host}:{port}")
    conn,addr = sock.accept()

    if conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)  # Receive data from the client
            if not data:
                break
            message = data.decode()
            print(f"Received from {addr}: {message}")
            data = ("Server: " + message).encode()
            conn.sendall(data)      # Send data back to the client (echo)

main()