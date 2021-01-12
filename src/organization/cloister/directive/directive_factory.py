import ujson

from src.organization.cloister.directive.stripmine_directive import StripmineDirective


class DirectiveFactory:
    @staticmethod
    def recover(hoard, cloister):
        data = hoard.load_directive_data(cloister)
        if data.get("stripmine_directive_id", None) is not None:
            directive = StripmineDirective(cloister, directive_id=data["directive_id"])
        else:
            raise TypeError(f"could not discern directive type from data: {ujson.dumps(data)}")
        return directive

    @staticmethod
    def create_stripmining_directive(hoard, cloister):
        directive = StripmineDirective(cloister)
        directive_id = hoard.insert_directive(directive)
        directive.set_directive_id(directive_id)
        return directive
