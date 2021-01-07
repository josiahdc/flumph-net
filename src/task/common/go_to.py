import random

from loguru import logger

from src.common.orientation import Orientation
from src.task.task import Task


class GoTo(Task):
    def __init__(self, flumph, destination):
        super().__init__(flumph)
        self._destination = destination

    def perform(self):
        logger.info(f"moving {self.flumph.name} to {self._destination}")
        vertical_lane = random.randint(2, 10)
        self.flumph.up(vertical_lane)
        if self.flumph.location.x > self._destination.x:
            self.flumph.orient(Orientation.WEST)
            self.flumph.forward(self.flumph.location.x - self._destination.x)
        if self.flumph.location.x < self._destination.x:
            self.flumph.orient(Orientation.EAST)
            self.flumph.forward(self._destination.x - self.flumph.location.x)
        if self.flumph.location.z > self._destination.z:
            self.flumph.orient(Orientation.NORTH)
            self.flumph.forward(self.flumph.location.z - self._destination.z)
        if self.flumph.location.z < self._destination.z:
            self.flumph.orient(Orientation.SOUTH)
            self.flumph.forward(self._destination.z - self.flumph.location.z)
        self.flumph.down(vertical_lane)
        self.flumph.orient(self._destination.orientation)
        yield
