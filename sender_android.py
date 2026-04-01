import socket

# GANTI "100.x.y.z" dengan IP Tailscale komputer Receiver (Raspberry)
TARGET_IP = "100.80.67.3" 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Mengirim pesan pertama
sock.sendto(b"Hello from sender!", (TARGET_IP, 5000))

# Menunggu balasan dari receiver
data, addr = sock.recvfrom(1024)
print(f"Reply: {data.decode()}")

sock.close()