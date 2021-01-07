from src.organization.cloister.directive.directive import Directive
from src.organization.cloister.directive.stripmine_directive import StripmineDirective
from src.organization.cloister.directive.stripmine_directive_info import StripmineDirectiveInfo
from src.orm.info import Info


class DirectiveFactory:
    @staticmethod
    def recover(db_session, cloister):
        directive_info = Directive.retrieve_info(db_session, cloister.name)
        if isinstance(directive_info, StripmineDirectiveInfo):
            directive = StripmineDirective(cloister)
        else:
            raise TypeError(f"unknown DirectiveInfo type: {type(directive_info)}")
        return directive

    @staticmethod
    def create_stripmining_directive(db_session, cloister):
        directive = StripmineDirective(cloister)
        Info.save(db_session, directive)
        return directive
