from abc import ABC, abstractmethod


class Occupation(ABC):
    def __init__(self, flumph, occupation_id):
        self.flumph = flumph
        self.occupation_id = occupation_id

    def set_occupation_id(self, occupation_id):
        self.occupation_id = occupation_id

    @abstractmethod
    def work(self):
        pass
