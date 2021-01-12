from src.flumph.occupation.stripminer_occupation import StripminerOccupation
from src.organization.cloister.directive.directive import Directive


class StripmineDirective(Directive):
    def get_ticket(self, flumph):
        if isinstance(flumph.occupation, StripminerOccupation):
            pass
        else:
            raise ValueError(f"cannot assign ticket to {flumph.name} with occupation {type(flumph.occupation)}")
