from src.flumph.occupation.stripminer import Stripminer
from src.organization.cloister.directive.directive import Directive
from src.organization.cloister.directive.stripmine_directive_info import StripmineDirectiveInfo


class StripmineDirective(Directive):
    def generate_info(self, db_session):
        return StripmineDirectiveInfo(self.cloister.retrieve_self_info(db_session))

    def assign_ticket(self, flumph):
        if isinstance(flumph.occupation, Stripminer):
            pass
        else:
            raise ValueError(f"cannot assign ticket to {flumph.name} with occupation {type(flumph.occupation)}")
