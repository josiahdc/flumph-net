import random

from src.common.orientation import Orientation
from src.task.task import Task


class GoTo(Task):
    def __init__(self, flumph, destination):
        super().__init__(flumph)
        self._destination = destination

    def perform(self):
        vertical_lane = random.randint(2, 10)
        self._flumph.up(vertical_lane)
        if self._flumph.location.x > self._destination.x:
            self._flumph.orient(Orientation.WEST)
            self._flumph.forward(self._flumph.location.x - self._destination.x)
        if self._flumph.location.x < self._destination.x:
            self._flumph.orient(Orientation.EAST)
            self._flumph.forward(self._destination.x - self._flumph.location.x)
        if self._flumph.location.z > self._destination.z:
            self._flumph.orient(Orientation.NORTH)
            self._flumph.forward(self._flumph.location.z - self._destination.z)
        if self._flumph.location.z < self._destination.z:
            self._flumph.orient(Orientation.SOUTH)
            self._flumph.forward(self._destination.z - self._flumph.location.z)
        self._flumph.down(vertical_lane)
        self._flumph.orient(self._destination.orientation)
        yield
