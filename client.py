# import socket
# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# print(key)
# key = b'BaTJP9VRW_Ira2Glv6eQcND83246bZyqCNKxpX5K8Z4='
# chipher_suite = Fernet(key)

# # soketti = socket.socket


# # Määritellään isäntä ja portti (samat kuin palvelimella)
# host = '80.246.148.30'
# port = 65432
# message = ""
# # Luodaan socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((host, port))  # Muodostetaan yhteys palvelimeen
# while message != "q":
#     message = input("lähetäviesti: ")
    
#     if message.lower() in ["q","quit","exit"]:
#         break
#     byteMessage = bytearray(message,encoding="utf-8")
#     encryptedMessage = chipher_suite.encrypt(message.encode())
    
#     s.sendall(encryptedMessage)  # Lähetetään viesti
#     data = s.recv(1024)  # Vastaanotetaan vastaus

#     print(f"Viesti palvelimelta: {data.decode()}")

# s.close()  # Suljetaan socket

import socket
import ssl
from cryptography.fernet import Fernet
key: bytes = Fernet.generate_key()

# localhost = 127.0.0.1

def run_client(server_hostname='localhost', port=65432, cafile='cert.pem'):
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=cafile)
    context.check_hostname = False  # Since we're using IP addresses or localhost

    with socket.create_connection((server_hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=server_hostname) as ssock:
            ssock.sendall(b"secure connection here")
            print(f'Message from server: {ssock.recv(1024).decode()}')

run_client()
