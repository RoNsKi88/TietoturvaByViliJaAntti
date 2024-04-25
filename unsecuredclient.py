import socket

def main():
    host = "127.0.0.1"  # The server's hostname or IP address
    port = 65432      # The port used by the server

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))
    print("Connected to server.")
    message = "unsecure connection here"
    s.sendall(message.encode())  # Send data to the server
    data = s.recv(1024)  # Receive data from the server
    print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    main()