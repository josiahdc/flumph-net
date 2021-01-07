from src.flumph.occupation.occupation import Occupation
from src.flumph.occupation.stripminer_info import StripminerInfo


class Stripminer(Occupation):
    def generate_info(self, db_session):
        return StripminerInfo(self.flumph.retrieve_self_info(db_session))

    def work(self):
        pass
