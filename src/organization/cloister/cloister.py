from loguru import logger

from src.common.location import Location
from src.organization.cloister.home_factory import HomeFactory


class Cloister:
    def __init__(self, name, origin, cloister_id=None):
        self.name = name
        self.origin = origin
        self.cloister_id = cloister_id
        self.homes = []
        self.directive = None

    def set_cloister_id(self, cloister_id):
        self.cloister_id = cloister_id

    def set_directive(self, directive):
        self.directive = directive

    def set_homes(self, homes):
        self.homes = homes

    def allocate_home(self, hoard, flumph):
        logger.info(f"allocating a home for {flumph.name}")
        if len(self.homes) > 0:
            proposed_home_location = self.homes[-1].origin.duplicate()
            proposed_home_location.x += 1
        else:
            proposed_home_location = Location(
                self.origin.x + 5,
                self.origin.z - 2,
                self.origin.y,
                self.origin.orientation
            )
        home = HomeFactory.create(hoard, self, proposed_home_location, flumph)
        self.homes.append(home)
        return home

    def retrieve_home(self, flumph):
        for home in self.homes:
            if home.flumph_id == flumph.flumph_id:
                return home
        raise ValueError(f"{flumph} does not have a home allocated in {self.name}")

    def allocate_ticket(self, flumph):
        return self.directive.allocate_ticket(flumph)

    def retrieve_ticket(self, flumph):
        return self.directive.retrieve_ticket(flumph)
