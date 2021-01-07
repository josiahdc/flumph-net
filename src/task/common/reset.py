from loguru import logger

from src.task.common.go_to import GoTo
from src.task.common.recharge import Recharge
from src.task.common.unload import Unload
from src.task.do_task import do_task
from src.task.task import Task


class Reset(Task):
    def perform(self):
        logger.info(f"resetting {self.flumph.name}")
        do_task(GoTo(self.flumph, self.flumph.home))
        do_task(Unload(self.flumph))
        do_task(Recharge(self.flumph))
        yield
