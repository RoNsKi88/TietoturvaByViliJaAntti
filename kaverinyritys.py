import socket
import ssl
from cryptography.fernet import Fernet
key: bytes = Fernet.generate_key()



def run_client(server_hostname='192.168.68.109', port=65432, cafile='cert.pem'):
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=cafile)
    context.check_hostname = False  # Since we're using IP addresses or localhost

    with socket.create_connection((server_hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=server_hostname) as ssock:
            ssock.sendall(b'Hello, server!')
            print(f'Message from server: {ssock.recv(1024).decode()}')

run_client()
