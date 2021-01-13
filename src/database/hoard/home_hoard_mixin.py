class HomeHoardMixin:
    def insert_home(self, home):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO home (cloister_id, flumph_id, home_origin)
                VALUES (%(cloister_id)s, %(flumph_id)s, %(home_origin)s)
                RETURNING home_id;
                """,
                {
                    "cloister_id": home.cloister.cloister_id,
                    "flumph_id": home.flumph_id,
                    "home_origin": home.origin.serialize()
                }
            )
            return cursor.fetchone()["home_id"]

    def save_home(self, home):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                UPDATE home
                SET cloister_id = %(cloister_id)s,
                    flumph_id = %(flumph_id)s,
                    home_origin = %(home_origin)s
                WHERE home.home_id = %(home_id)s;
                """,
                {
                    "cloister_id": home.cloister.cloister_id,
                    "flumph_id": home.flumph_id,
                    "home_origin": home.origin.serialize(),
                    "home_id": home.home_id
                }
            )

    def load_all_home_data(self, cloister):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM home
                WHERE home.cloister_id = %(cloister_id)s
                """,
                {
                    "cloister_id": cloister.cloister_id
                }
            )
            return cursor.fetchall()
