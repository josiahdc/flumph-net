import time

from loguru import logger

from src.task.task import Task


class Recharge(Task):
    def perform(self):
        logger.info(f"recharging {self.flumph.name}")
        while self.flumph.energy() < self.flumph.max_energy() - 100:
            time.sleep(1)
        yield
