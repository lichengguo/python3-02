
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            try:
                data = self.request.recv(1024)
            # 针对window
            except Exception as e:
                break
            # 针对linux
            if len(data) == 0:
                break
            print("客户：", data.decode())
            if data.decode() == "quit":
                self.request.close()
                break
            res = input("响应 >>>")
            self.request.send(res.encode())

server=socketserver.ThreadingTCPServer(("127.0.0.1",8899),MyServer)
server.serve_forever()
