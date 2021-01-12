from src.database.hoard.cloister_hoard_mixin import CloisterHoardMixin


class FlumphHoardMixin:
    def save_flumph(self, flumph):
        with self.database_connector.get_cursor() as cursor:
            cloister_id = CloisterHoardMixin.get_cloister_id(cursor, flumph.cloister.name)
            cursor.execute(
                """
                INSERT INTO flumph (cloister_id, flumph_name, flumph_location)
                VALUES (%(cloister_id)s, %(flumph_name)s, %(flumph_location)s)
                ON CONFLICT (flumph_name) DO UPDATE
                    SET cloister_id = %(cloister_id)s,
                        flumph_name = %(flumph_name)s,
                        flumph_location = %(flumph_location)s;
                """,
                {
                    "cloister_id": cloister_id,
                    "flumph_name": flumph.name,
                    "flumph_location": flumph.location.serialize()
                }
            )
        self.save_occupation(flumph.occupation)

    def load_flumph_data(self, flumph_name):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM flumph
                WHERE flumph_name = %(flumph_name)s
                """,
                {
                    "flumph_name": flumph_name
                }
            )
            return cursor.fetchone()

    @staticmethod
    def get_flumph_id(cursor, flumph_name):
        cursor.execute(
            """
            SELECT flumph.flumph_id
            FROM flumph
            WHERE flumph.flumph_name = %(flumph_name)s
            """,
            {
                "flumph_name": flumph_name
            }
        )
        return cursor.fetchone()["flumph_id"]
