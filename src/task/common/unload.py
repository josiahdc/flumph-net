from src.common.orientation import Orientation
from src.task.task import Task


class Unload(Task):
    def perform(self):
        self._flumph.down()
        self._flumph.turn_right(2)
        for slot in range(self._flumph.inventory_size()):
            self._flumph.select(slot + 1)
            self._flumph.drop()
        self._flumph.orient(Orientation.NORTH)
        self._flumph.up()
        yield
