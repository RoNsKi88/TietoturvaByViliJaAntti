# import socket
# from cryptography.fernet import Fernet
# # Määritellään isäntä ja portti
# host = '192.168.68.109'
# port = 65432

# key = b'BaTJP9VRW_Ira2Glv6eQcND83246bZyqCNKxpX5K8Z4='
# chipher_suite = Fernet(key)
# # Luodaan socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((host, port))  # Yhdistetään socket isäntään ja porttiin
# s.listen()            # Kuunnellaan yhteyksiä
# print(f"Palvelin kuuntelee osoitteessa {host}:{port}")

# conn, addr = s.accept()  # Hyväksytään yhteys
# print(f"Yhdistetty osoitteesta {addr}")
# while True:
#     data = conn.recv(1024)  # Vastaanotetaan dataa clientilta
#     if not data:
#         break
#     print(f"Viesti clientilta: {data}")
#     decodedMessage = chipher_suite.decrypt(data).decode()
#     print(f"{decodedMessage}")
#     conn.sendall(data)  # Lähetetään vastaanotettu data takaisin clientille

# conn.close()  # Suljetaan yhteys
# s.close()     # Suljetaan socket

import socket
import ssl
import threading

# localhost = 127.0.0.1

def run_server(certfile=None, keyfile=None, hostname='localhost', port=65432):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=certfile,keyfile=keyfile)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((hostname, port))
        sock.listen(5)
        with context.wrap_socket(sock, server_side=True) as ssock:
            print(f'Server listening on {hostname}:{port}')
            conn, addr = ssock.accept()
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f'Message from client: {data.decode()}')
                conn.sendall(data)
while True:
    run_server("cert.pem", "key.pem")
