from src.task.common.go_to import GoTo
from src.task.common.recharge import Recharge
from src.task.common.unload import Unload
from src.task.do_task import do_task
from src.task.task import Task


class Reset(Task):
    def perform(self):
        do_task(GoTo(self._flumph, self._flumph.home))
        do_task(Unload(self._flumph))
        do_task(Recharge(self._flumph))
        yield
