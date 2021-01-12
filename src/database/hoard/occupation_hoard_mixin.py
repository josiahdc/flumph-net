from src.database.hoard.flumph_hoard_mixin import FlumphHoardMixin
from src.flumph.occupation.stripminer_occupation import StripminerOccupation


class OccupationHoardMixin:
    def save_occupation(self, occupation):
        with self.database_connector.get_cursor() as cursor:
            flumph_id = FlumphHoardMixin.get_flumph_id(cursor, occupation.flumph.name)
            cursor.execute(
                """
                INSERT INTO occupation (flumph_id)
                VALUES (%(flumph_id)s)
                ON CONFLICT DO NOTHING
                RETURNING occupation_id;
                """,
                {
                    "flumph_id": flumph_id
                }
            )
            occupation_id = cursor.fetchone()["occupation_id"]
            if isinstance(occupation, StripminerOccupation):
                cursor.execute(
                    """
                    INSERT INTO stripminer_occupation (occupation_id)
                    VALUES (%(occupation_id)s)
                    ON CONFLICT DO NOTHING;
                    """,
                    {
                        "occupation_id": occupation_id
                    }
                )
            else:
                raise TypeError(f"unknown Occupation type: {type(occupation)}")

    def load_occupation_data(self, flumph_name):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM occupation
                    JOIN flumph on occupation.flumph_id = flumph.flumph_id
                    LEFT JOIN stripminer_occupation on occupation.occupation_id = stripminer_occupation.occupation_id
                WHERE flumph.flumph_name = %(flumph_name)s
                """,
                {
                    "flumph_name": flumph_name
                }
            )
            return cursor.fetchone()
