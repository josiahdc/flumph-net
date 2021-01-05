from abc import ABC, abstractmethod


class Occupation(ABC):
    """a job for a flumph"""

    def __init__(self, flumph):
        self._flumph = flumph

    @abstractmethod
    def perform(self):
        """the steps required to complete the task, should be a python generator"""
        pass
