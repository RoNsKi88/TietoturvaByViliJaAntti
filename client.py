import socket
import ssl

localhost = "127.0.0.1"
port = 65432

def run_client(server_hostname=localhost, port=port, cafile='cert.pem'):
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=cafile)
    context.check_hostname = False  # Since we're using IP addresses or localhost

    sock = socket.create_connection((server_hostname, port))
    ssock = context.wrap_socket(sock, server_hostname=server_hostname)
    print("ssock verison: ",ssock.version())
    ssock.sendall(b"secure connection here")
    print(f'Message from server: {ssock.recv(2048).decode()}')

run_client()
