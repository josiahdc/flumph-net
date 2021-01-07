import socketserver

from loguru import logger

from src.server.executor import Executor
from src.server.relay import Relay


class FlumphNetRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        logger.info("new connection")
        relay = Relay(self.rfile, self.wfile)
        executor = Executor(relay)
        self.server.gestalt.handle_connection(executor)
        logger.info("connection terminated")
