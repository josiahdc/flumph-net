from loguru import logger

from src.common.orientation import Orientation
from src.task.task import Task


class Unload(Task):
    def perform(self):
        logger.info(f"unloading {self.flumph.name}")
        self.flumph.down()
        self.flumph.turn_right(2)
        for slot in range(self.flumph.inventory_size()):
            self.flumph.select(slot + 1)
            self.flumph.drop()
        self.flumph.orient(Orientation.NORTH)
        self.flumph.up()
        yield
