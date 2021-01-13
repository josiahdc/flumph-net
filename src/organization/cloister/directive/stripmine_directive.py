from src.config import STRIPMINE_DEFAULT_Z_RANGE, STRIPMINE_DEFAULT_X_RANGE, STRIPMINE_DEFAULT_Y_RANGE
from src.flumph.occupation.stripminer_occupation import StripminerOccupation
from src.organization.cloister.directive.directive import Directive
from src.organization.cloister.directive.ticket.ticket_factory import TicketFactory


class StripmineDirective(Directive):
    def __init__(self, hoard, cloister, last_ticket_origin, directive_id=None):
        super().__init__(hoard, cloister, directive_id)
        self.last_ticket_origin = last_ticket_origin

    def allocate_ticket(self, flumph):
        if isinstance(flumph.occupation, StripminerOccupation):
            if self.last_ticket_origin is not None:
                origin = self.last_ticket_origin.duplicate()
                origin.x += STRIPMINE_DEFAULT_X_RANGE
            else:
                origin = self.cloister.origin.duplicate()
                origin.z -= 4
            ticket = TicketFactory.create_stripmining_ticket(
                self.hoard,
                self,
                flumph.flumph_id,
                origin,
                STRIPMINE_DEFAULT_X_RANGE,
                STRIPMINE_DEFAULT_Z_RANGE,
                STRIPMINE_DEFAULT_Y_RANGE
            )
            self.last_ticket_origin = origin
            self.tickets.append(ticket)
            return ticket
        else:
            raise ValueError(
                f"{type(self)} cannot allocate ticket to {flumph.name} with occupation {type(flumph.occupation)}"
            )
