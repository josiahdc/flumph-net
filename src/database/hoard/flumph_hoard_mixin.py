class FlumphHoardMixin:
    def insert_flumph(self, flumph):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO flumph (cloister_id, flumph_name, flumph_location)
                VALUES (%(cloister_id)s, %(flumph_name)s, %(flumph_location)s)
                RETURNING flumph_id;
                """,
                {
                    "cloister_id": flumph.cloister.cloister_id,
                    "flumph_name": flumph.name,
                    "flumph_location": flumph.location.serialize()
                }
            )
            return cursor.fetchone()["flumph_id"]

    def save_flumph(self, flumph):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                UPDATE flumph
                SET cloister_id = %(cloister_id)s,
                    flumph_name = %(flumph_name)s,
                    flumph_location = %(flumph_location)s
                WHERE flumph.flumph_id = %(flumph_id)s;
                """,
                {
                    "flumph_id": flumph.flumph_id,
                    "cloister_id": flumph.cloister.cloister_id,
                    "flumph_name": flumph.name,
                    "flumph_location": flumph.location.serialize()
                }
            )

    def load_flumph_data(self, flumph_name):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM flumph
                WHERE flumph_name = %(flumph_name)s;
                """,
                {
                    "flumph_name": flumph_name
                }
            )
            return cursor.fetchone()
