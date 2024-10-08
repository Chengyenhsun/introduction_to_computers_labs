import socket

HOST = '10.3.141.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)


while True:
    print('Server start at: %s:%s' % (HOST, PORT))
    print('Waiting for connection...')

    conn, addr = s.accept()
    print('connected by ' + str(addr))

    while True:
        indata = conn.recv(1024)
        if len(indata) == 0: # connection closed
            conn.close()
            print(str(addr) + ' closed connection.')
            break
        print(str(addr) + ' : ' + indata.decode())

        outdata = 'Echo : ' + indata.decode()
        conn.send(outdata.encode())

