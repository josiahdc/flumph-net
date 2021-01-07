from abc import ABC, abstractmethod

from src.flumph.flumph_info import FlumphInfo
from src.flumph.occupation.occupation_info import OccupationInfo


class Occupation(ABC):
    def __init__(self, flumph):
        self.flumph = flumph

    def retrieve_self_info(self, db_session):
        return self.retrieve_info(db_session, self.flumph.name)

    @staticmethod
    def retrieve_info(db_session, flumph_name):
        return db_session.query(OccupationInfo).join(FlumphInfo). \
            filter(FlumphInfo.name == flumph_name).one_or_none()

    @abstractmethod
    def generate_info(self, db_session):
        pass

    @abstractmethod
    def work(self):
        pass
