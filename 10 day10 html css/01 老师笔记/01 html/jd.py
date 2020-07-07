

import socket

sock=socket.socket()
sock.bind(("127.0.0.1",9000))
sock.listen(5)


while 1:
    print("wating...")
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("data",data)
    with open("jd.html","rb") as f:
        html=f.read()
    conn.send(b"HTTP/1.1 201 OK\r\n\r\n"+html)
    conn.close()


