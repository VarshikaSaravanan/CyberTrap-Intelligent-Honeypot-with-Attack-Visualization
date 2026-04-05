import socket
from config import PORTS, WELCOME_MESSAGES
from logger import log_attack

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", port))
    server.listen(5)

    print(f"[✓] Honeypot running on port {port}")

    while True:
        client, addr = server.accept()
        print(f"[+] Connection from {addr}")

        try:
            client.send(WELCOME_MESSAGES[port])

            data = client.recv(1024).decode(errors="ignore").strip()

            if data.startswith("GET"):
             return  # ignore browser traffic

            print(f"[ATTACK] {addr} -> {data}")

            log_attack(addr[0], port, data)

            client.send(b"Access Denied\n")

        except:
            pass

        client.close()

if __name__ == "__main__":
    for port in PORTS:
        start_server(port)