import socket

HOST = '10.3.141.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('Connected to: %s:%s' % (HOST, PORT))

while True:
    outdata = input('Send : ')
    s.send(outdata.encode())
    
    indata = s.recv(1024)
    if outdata == "EXIT" : 
        s.close()
        print('Closed connection.')
        break
    print(indata.decode())