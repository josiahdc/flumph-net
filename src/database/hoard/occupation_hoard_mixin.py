from src.flumph.occupation.stripminer_occupation import StripminerOccupation


class OccupationHoardMixin:
    def insert_occupation(self, occupation):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO occupation (flumph_id)
                VALUES (%(flumph_id)s)
                RETURNING occupation_id;
                """,
                {
                    "flumph_id": occupation.flumph.flumph_id
                }
            )
            occupation_id = cursor.fetchone()["occupation_id"]
            if isinstance(occupation, StripminerOccupation):
                cursor.execute(
                    """
                    INSERT INTO stripminer_occupation (occupation_id)
                    VALUES (%(occupation_id)s);
                    """,
                    {
                        "occupation_id": occupation_id
                    }
                )
            else:
                raise TypeError(f"unknown Occupation type: {type(occupation)}")

    def save_occupation(self, occupation):
        with self.database_connector.get_cursor() as cursor:
            if isinstance(occupation, StripminerOccupation):
                pass
            else:
                raise TypeError(f"unknown Occupation type: {type(occupation)}")

    def load_occupation_data(self, flumph):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM occupation
                    LEFT JOIN stripminer_occupation on occupation.occupation_id = stripminer_occupation.occupation_id
                WHERE occupation.flumph_id = %(flumph_id)s;
                """,
                {
                    "flumph_id": flumph.flumph_id
                }
            )
            return cursor.fetchone()
