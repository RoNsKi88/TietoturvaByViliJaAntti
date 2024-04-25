import socket
import ssl

localhost = "127.0.0.1"
port = 65432
def run_server(certfile=None, keyfile=None, hostname=localhost, port=port):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=certfile,keyfile=keyfile)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((hostname, port))
    sock.listen(5)
    ssock = context.wrap_socket(sock, server_side=True)
    print(f'Secure server listening on {hostname}:{port}')
    conn, addr = ssock.accept()
    print("chipher",conn.cipher())
    print("connection data",conn)
    print(f'Connected by {addr}')
    data = conn.recv(2048)
    receivedMessage = data.decode()
    
    print(f'Message from client: {receivedMessage}')
    receivedMessage = (receivedMessage + " this is added in server.").encode()
    conn.sendall(receivedMessage)

run_server("cert.pem", "key.pem")

# RSA keyfile 2048 bits
# openssl genpkey -algorithm RSA -out key.pem -pkeyopt rsa_keygen_bits:2048

# Self signed 
# openssl req -new -x509 -days 365 -key key.pem -out cert.pem

