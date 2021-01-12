from loguru import logger

from src.common.exception import StuckFlumphError
from src.flumph.occupation.occupation import Occupation


class StripminerOccupation(Occupation):
    def work(self):
        ticket = self.flumph.cloister.get_ticket(self.flumph)
        try:
            pass
        except StuckFlumphError as exception:
            logger.error(f"{exception.flumph_name} got stuck: {exception}")
