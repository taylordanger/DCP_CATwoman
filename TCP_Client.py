import socket
target_host = "www.google.com"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect that fool
client.connect((target_host,target_port))

client.send("GET / HTTP/1.1\rnHOST: google.com\r\n\r\n")

#get that datatatataatatattaa

response = clientrecv(4096)

print(response)