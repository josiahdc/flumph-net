class CloisterHoardMixin:
    def insert_cloister(self, cloister):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO cloister (cloister_name, cloister_origin)
                VALUES (%(cloister_name)s, %(cloister_origin)s)
                RETURNING cloister_id;
                """,
                {
                    "cloister_name": cloister.name,
                    "cloister_origin": cloister.origin.serialize()
                }
            )
            return cursor.fetchone()["cloister_id"]

    def save_cloister(self, cloister):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                UPDATE cloister
                    SET cloister_origin = %(cloister_origin)s
                    WHERE cloister.cloister_id = %(cloister_id)s;
                """,
                {
                    "cloister_id": cloister.cloister_id,
                    "cloister_origin": cloister.origin.serialize()
                }
            )

    def load_all_cloister_data(self):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM cloister;
                """,
                {}
            )
            return cursor.fetchall()
