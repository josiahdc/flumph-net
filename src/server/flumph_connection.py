import random
import socketserver

from loguru import logger

from src.common.exception import StuckFlumphError
from src.flumph.flumph_factory import FlumphFactory
from src.task.common.reset import Reset


class FlumphConnection(socketserver.StreamRequestHandler):
    def handle(self):
        logger.info("new connection")
        flumph = FlumphFactory.create(self.rfile, self.wfile)
        flumph.forward(random.randint(1, 12))
        flumph.turn_left()
        flumph.forward(random.randint(4, 12))
        task = Reset(flumph)
        try:
            task.perform()
        except StuckFlumphError as exception:
            logger.error(f"{exception.flumph_name} got stuck: {exception}")
        logger.info("connection terminated")
