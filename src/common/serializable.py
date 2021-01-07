from abc import ABC, abstractmethod


class Serializable(ABC):
    @abstractmethod
    def serialize(self):
        pass

    @staticmethod
    @abstractmethod
    def deserialize(value):
        pass
