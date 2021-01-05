import time

from src.task.task import Task


class Recharge(Task):
    def perform(self):
        while self._flumph.energy() < self._flumph.max_energy() - 100:
            time.sleep(1)
        yield
