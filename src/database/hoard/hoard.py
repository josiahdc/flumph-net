from src.database.hoard.cloister_hoard_mixin import CloisterHoardMixin
from src.database.hoard.directive_hoard_mixin import DirectiveHoardMixin
from src.database.hoard.flumph_hoard_mixin import FlumphHoardMixin
from src.database.hoard.home_hoard_mixin import HomeHoardMixin
from src.database.hoard.occupation_hoard_mixin import OccupationHoardMixin
from src.database.hoard.ticket_hoard_mixin import TicketHoardMixin


class Hoard(CloisterHoardMixin, DirectiveHoardMixin, FlumphHoardMixin, OccupationHoardMixin, HomeHoardMixin,
            TicketHoardMixin):
    def __init__(self, database_connector):
        self.database_connector = database_connector
