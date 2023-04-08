import socket

target_host = "127.0.0.1"
target_port = 80

#create that sock yobyect
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("AAAABBBBCCCCDDDD" ,(target_host,target_port))
data, addr = client.recvfrom(4096)

print(data)