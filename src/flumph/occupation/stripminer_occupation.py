from loguru import logger

from src.common.exception import StuckFlumphError
from src.flumph.occupation.occupation import Occupation


class StripminerOccupation(Occupation):
    def __init__(self, flumph, occupation_id=None):
        super().__init__(flumph, occupation_id)

    def work(self):
        ticket = self.flumph.cloister.retrieve_ticket(self.flumph)
        if ticket is None:
            ticket = self.flumph.cloister.allocate_ticket(self.flumph)
        try:
            ticket.completed = True
        except StuckFlumphError as exception:
            logger.error(f"{exception.flumph_name} got stuck: {exception}")
