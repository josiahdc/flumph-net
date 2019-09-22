import socketserver
from gestalt import Gestalt

class FlumphAdapter(socketserver.StreamRequestHandler):

    def handle(self):
        print("new connection")

        # get connection type
        conn_type = self.rfile.readline().decode("utf-8").strip()
352692
        if conn_type == "flumph":
            # create flumph and start main loop
            new_flumph = gestalt.new_flumph(self.rfile, self.wfile)
            if new_flumph is not None:
                new_flumph.main()
                new_flumph.shutdown()

        elif conn_type == "controller":
            command = self.rfile.readline().decode("utf-8").strip()
            if command == "shutdown":
                print("terminating")
                gestalt.shutdown()
                server.shutdown()

        print("connection terminated")

if __name__ == "__main__":
    PORT = 8181
    gestalt = Gestalt()
    with socketserver.TCPServer(("", PORT), FlumphAdapter) as server:
        server.serve_forever()