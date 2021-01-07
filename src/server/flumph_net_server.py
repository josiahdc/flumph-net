import socketserver


class FlumphNetServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def __init__(self, host, request_handler, gestalt):
        super().__init__(host, request_handler)
        self.gestalt = gestalt
