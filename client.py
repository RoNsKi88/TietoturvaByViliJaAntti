import socket
import ssl

host = "127.0.0.1"
port = 65432
certFileName = "cert.pem"
def run_client():
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=certFileName)
    context.check_hostname = False  # Since we're using IP addresses or localhost

    sock = socket.create_connection((host, port))
    ssock = context.wrap_socket(sock, server_hostname=host)
    print("ssock verison: ",ssock.version())
    ssock.sendall(b"Client: secure connection here")
    print(f'Message from server: {ssock.recv(2048).decode()}')

run_client()
