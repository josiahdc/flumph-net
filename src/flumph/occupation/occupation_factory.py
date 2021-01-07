from src.flumph.occupation.occupation import Occupation
from src.flumph.occupation.stripminer import Stripminer
from src.flumph.occupation.stripminer_info import StripminerInfo
from src.orm.info import Info


class OccupationFactory:
    @staticmethod
    def recover(db_session, flumph):
        occupation_info = Occupation.retrieve_info(db_session, flumph.name)
        if isinstance(occupation_info, StripminerInfo):
            occupation = Stripminer(flumph)
        else:
            raise TypeError(f"unknown OccupationInfo type: {type(occupation_info)}")
        return occupation

    @staticmethod
    def create_stripminer(db_session, flumph):
        occupation = Stripminer(flumph)
        Info.save(db_session, occupation)
        return occupation
