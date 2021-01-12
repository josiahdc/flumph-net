from src.organization.cloister.directive.stripmine_directive import StripmineDirective


class DirectiveHoardMixin:
    def insert_directive(self, directive):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO directive (cloister_id)
                VALUES (%(cloister_id)s)
                RETURNING directive_id;
                """,
                {
                    "cloister_id": directive.cloister.cloister_id
                }
            )
            directive_id = cursor.fetchone()["directive_id"]
            if isinstance(directive, StripmineDirective):
                cursor.execute(
                    """
                    INSERT INTO stripmine_directive (directive_id)
                    VALUES (%(directive_id)s);
                    """,
                    {
                        "directive_id": directive_id
                    }
                )
            else:
                raise TypeError(f"unknown Directive type: {type(directive)}")
            return directive_id

    def save_directive(self, directive):
        with self.database_connector.get_cursor() as cursor:
            if isinstance(directive, StripmineDirective):
                pass
            else:
                raise TypeError(f"unknown Directive type: {type(directive)}")

    def load_directive_data(self, cloister):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM directive
                    LEFT JOIN stripmine_directive on directive.directive_id = stripmine_directive.directive_id
                WHERE directive.cloister_id = %(cloister_id)s;
                """,
                {
                    "cloister_id": cloister.cloister_id
                }
            )
            return cursor.fetchone()