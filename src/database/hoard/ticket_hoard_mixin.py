from src.database.hoard.directive_hoard_mixin import DirectiveHoardMixin


class HomeHoardMixin:
    def save_new_ticket(self, ticket):
        with self.database_connector.get_cursor() as cursor:
            directive_id = DirectiveHoardMixin.get_directive_id(cursor, ticket.directive.cloister.cloister_id)
