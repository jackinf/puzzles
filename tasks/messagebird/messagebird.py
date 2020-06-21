import requests
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 6667)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
sock.sendall('test'.encode())

amount_received = 0
while amount_received < 10_000:
    data = sock.recv(5000)
    amount_received += len(data)
    print(sys.stderr, f'received {data}')


input_str = "https://www.google.com/search?ei=9vImXZvBEYzSa7DNqcAI&q=MessageBird&oq=MessageBird\nhttps://messagebird.com/en/#\nhttps://github.com/yandex/ClickHouse/blob/master/dbms/programs/server/users.xml\nhttp://www.google.com"
inputs = input_str.split("\n")

with open('result.txt', 'w') as f:
    for url in inputs:
        res = requests.get(url)
        f.write(f'{url},{res.status_code}\n')