from loguru import logger

from src.common.location import Location
from src.organization.cloister.home import Home


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

    def add_home(self, home):
        self.homes.append(home)

    def add_ticket(self, ticket):
        self.directive.add_ticket(ticket)

    def assign_home(self, flumph):
        logger.info(f"assigning a home to {flumph.name}")
        if len(self.homes) > 0:
            proposed_home_location = self.homes[-1].origin.duplicate()
            proposed_home_location.x += 1
        else:
            proposed_home_location = Location(
                self.origin.x + 5,
                self.origin.z + 2,
                self.origin.y,
                self.origin.orientation
            )
        home = Home(self, proposed_home_location, flumph.name)
        self.homes.append(home)
        return home

    def retrieve_home(self, flumph):
        for home in self.homes:
            if home.flumph_name == flumph.name:
                return home
        raise ValueError(f"{flumph} does not have a home assigned with {self.name}")

    def get_ticket(self, flumph):
        self.directive.get_ticket(flumph)
