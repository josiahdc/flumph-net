import logging
import socketserver
from time import sleep

from src.flumphnet import constants
from src.flumphnet.server.transmitter import Transmitter

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# gestalt = Gestalt()

class FlumphAdapter(socketserver.StreamRequestHandler):
    def handle(self):
        transmitter = Transmitter(self.rfile, self.wfile)
        logger.debug("new connection")
        requester_type = self.get_requester_type(transmitter)
        if requester_type == "flumph":
            self.create_and_start_flumph(transmitter)
        elif requester_type == "controller":
            self.create_controller()
        logger.debug("connection terminated")

    def get_requester_type(self, transmitter):
        result = transmitter.read_string()
        logger.debug("requester type: " + str(result))
        return result

    def create_and_start_flumph(self, transmitter):
        logger.debug("creating new flumph")
        while True:
            transmitter.transmit("robot.forward()")
            logger.debug("sent instruction")
            print(transmitter.read_string())
            transmitter.transmit("robot.back()")
            logger.debug("sent instruction")
            print(transmitter.read_string())

        # new_flumph = gestalt.new_flumph(self.rfile, self.wfile)
        # if new_flumph is not None:
        #     logger.debug("starting new flumph")
        #     new_flumph.main()
        #     logger.debug("shutting down flumph")
        #     new_flumph.shutdown()

    def create_controller(self):
        logger.debug("creating new flumph")
        command = self.rfile.readline().decode("utf-8").strip()
        if command == "shutdown":
            print("terminating")
            gestalt.shutdown()


def create_and_start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", constants.ADAPTER_PORT), FlumphAdapter) as server:
        server.serve_forever()


if __name__ == "__main__":
    create_and_start_server()
