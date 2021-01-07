from src.config import FLUMPH_NET_SERVER_PORT, FLUMPH_NET_SERVER_ADDRESS
from src.organization.gestalt_factory import GestaltFactory
from src.server.flumph_connection import FlumphNetRequestHandler
from src.server.flumph_net_server import FlumphNetServer


def main():
    FlumphNetServer.allow_reuse_address = True
    flumph_net_host = (FLUMPH_NET_SERVER_ADDRESS, FLUMPH_NET_SERVER_PORT)
    gestalt = GestaltFactory.create()
    with FlumphNetServer(flumph_net_host, FlumphNetRequestHandler, gestalt) as flumph_net_server:
        flumph_net_server.serve_forever()


if __name__ == "__main__":
    main()
