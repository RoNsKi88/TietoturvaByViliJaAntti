import socket

host = "127.0.0.1"  
port = 65432     

def run_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))
    print("Connected to server.")
    message = "Client: unsecure connection here"
    s.sendall(message.encode())     # Send data to the server
    data = s.recv(1024)             # Receive data from the server
    print(f"Received from server: {data.decode()}")


run_client()