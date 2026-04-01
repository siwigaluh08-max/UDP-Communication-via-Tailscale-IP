import socket

# Gunakan "0.0.0.0" agar bisa menerima dari IP mana saja (termasuk Tailscale)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5000)) 

print("Receiver siap, menunggu pesan...")

data, addr = sock.recvfrom(1024)
print(f"Received: {data.decode()}")

# Mengirim balasan balik ke pengirim
sock.sendto(b"Hello back from receiver!", addr)

sock.close()