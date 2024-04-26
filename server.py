import socket
import ssl

localhost = "127.0.0.1"
port = 65432
certFileName = "cert.pem"
keyFileName = "key.pem"
def run_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=certFileName,keyfile=keyFileName)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((localhost, port))
    sock.listen(5)
    ssock = context.wrap_socket(sock, server_side=True)
    print(f'Secure server listening on {localhost}:{port}')
    conn, addr = ssock.accept()
    print(f'Connected by {addr}')
    data = conn.recv(2048)
    receivedMessage = data.decode()
    
    print(f'Message from client: {receivedMessage}')
    receivedMessage = ("Server: " + receivedMessage).encode()
    conn.sendall(receivedMessage)

run_server()

# RSA keyfile 2048 bits
# openssl genpkey -algorithm RSA -out key.pem -pkeyopt rsa_keygen_bits:2048

# Self signed 
# openssl req -new -x509 -days 365 -key key.pem -out cert.pem

