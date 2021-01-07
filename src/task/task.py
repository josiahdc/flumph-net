from abc import ABC, abstractmethod


class Task(ABC):
    """a collection of commands which make up a granular unit of work"""

    def __init__(self, flumph):
        self.flumph = flumph

    @abstractmethod
    def perform(self):
        """the steps required to complete the task, should be a python generator"""
        pass
