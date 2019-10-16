import socket

newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newsocket.bind((socket.gethostname(), 1234))
newsocket.listen(5)

while True:
    clientsocket, address = newsocket.accept()
    print(f"{address} adresindeki bağlantı kuruldu!")
    clientsocket.send(bytes("Server'a hoşgeldiniz! (Bu yollanan bir veridir.)", "utf-8"))
