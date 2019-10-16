import socket

newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newsocket.connect((socket.gethostname(), 1234))

msg = newsocket.recv(1024)
print(msg.decode("utf-8"))