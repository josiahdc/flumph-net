from loguru import logger

from src.common.exception import NoHomeAvailableError
from src.common.location import Location
from src.organization.cloister.cloister_info import CloisterInfo
from src.organization.cloister.home import Home


class Cloister:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin
        self._directive = None

    def generate_info(self, db_session):
        return CloisterInfo(self.name, self.origin)

    def retrieve_self_info(self, db_session):
        return self.retrieve_info(db_session, self.name)

    @staticmethod
    def retrieve_info(db_session, name):
        return db_session.query(CloisterInfo).filter(CloisterInfo.name == name).one_or_none()

    def set_directive(self, directive):
        self._directive = directive

    def designate_homes(self, db_session, start_index, end_index):
        logger.info(f"designating homes {start_index} - {end_index} for {self.name}")
        home_origin_location = Location(self.origin.x + 5, self.origin.z + 2, self.origin.y, self.origin.orientation)
        for index in range(start_index, end_index):
            new_home_location = home_origin_location.duplicate()
            new_home_location.x += index
            home = Home(self.retrieve_self_info(db_session), new_home_location)
            db_session.add(home)

    def assign_home(self, db_session, flumph):
        logger.info(f"assigning a home to {flumph.name}")
        home = db_session.query(Home).filter(CloisterInfo.name == self.name).filter(Home.flumph_info == None).first()
        if home is None:
            raise NoHomeAvailableError(flumph.name, self.name)
        else:
            home.flumph_info = flumph.retrieve_self_info(db_session)

    def assign_ticket(self, flumph):
        self._directive.assign_ticket(flumph)
