from abc import ABC, abstractmethod


class Occupation(ABC):
    def __init__(self, flumph):
        self.flumph = flumph

    @abstractmethod
    def work(self):
        pass
