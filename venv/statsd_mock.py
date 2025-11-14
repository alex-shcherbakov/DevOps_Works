import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 9999

# створюємо UDP-сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"The simulated StatsD server listens on {UDP_IP}:{UDP_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Message received from {addr}: {data.decode('utf-8')}")
