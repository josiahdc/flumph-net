from src.organization.cloister.directive.directive import Directive
from src.organization.cloister.directive.stripmine_directive_info import StripmineDirectiveInfo


class StripmineDirective(Directive):
    def generate_info(self, db_session):
        return StripmineDirectiveInfo(self.cloister.retrieve_self_info(db_session))
