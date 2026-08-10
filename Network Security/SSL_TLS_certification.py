import ssl
import socket

hostname = 'www.google.com'
port = 443
context = ssl.create_default_context()
with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as sock:
        cert = sock.getpeercert()
        print("ssl certificate information:")
        print("_" * 40)
        for key, value in cert.items():
            print(f"{key}: {value}")