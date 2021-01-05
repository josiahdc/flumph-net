import socketserver

from src.config import FLUMPH_CONNECTION_PORT, FLUMPH_CONNECTION_ADDRESS
from src.server.flumph_connection import FlumphConnection


def main():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer((FLUMPH_CONNECTION_ADDRESS, FLUMPH_CONNECTION_PORT), FlumphConnection) as server:
        server.serve_forever()


if __name__ == '__main__':
    main()
