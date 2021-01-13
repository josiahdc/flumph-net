from src.organization.cloister.directive.ticket.stripmining_ticket import StripminingTicket


class TicketHoardMixin:
    def insert_ticket(self, ticket):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO ticket (directive_id, flumph_id, ticket_completed)
                VALUES (%(directive_id)s, %(flumph_id)s, %(ticket_completed)s)
                RETURNING ticket_id;
                """,
                {
                    "directive_id": ticket.directive.directive_id,
                    "flumph_id": ticket.flumph_id,
                    "ticket_completed": ticket.completed
                }
            )
            ticket_id = cursor.fetchone()["ticket_id"]
            if isinstance(ticket, StripminingTicket):
                cursor.execute(
                    """
                    INSERT INTO stripmining_ticket (
                        ticket_id,
                        ticket_origin,
                        ticket_x_range,
                        ticket_y_range,
                        ticket_z_range
                    )
                    VALUES (
                        %(ticket_id)s,
                        %(ticket_origin)s,
                        %(ticket_x_range)s,
                        %(ticket_y_range)s,
                        %(ticket_z_range)s
                    );
                    """,
                    {
                        "ticket_id": ticket_id,
                        "ticket_origin": ticket.origin.serialize(),
                        "ticket_x_range": ticket.x_range,
                        "ticket_y_range": ticket.z_range,
                        "ticket_z_range": ticket.y_range
                    }
                )
            else:
                raise TypeError(f"unknown Ticket type: {type(ticket)}")
            return ticket_id

    def save_ticket(self, ticket):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                UPDATE ticket
                SET directive_id = %(directive_id)s,
                    flumph_id = %(flumph_id)s,
                    ticket_completed = %(ticket_completed)s
                WHERE ticket.ticket_id = %(ticket_id)s;
                """,
                {
                    "ticket_id": ticket.ticket_id,
                    "directive_id": ticket.directive.directive_id,
                    "flumph_id": ticket.flumph_id,
                    "ticket_completed": ticket.completed
                }
            )
            if isinstance(ticket, StripminingTicket):
                cursor.execute(
                    """
                    UPDATE stripmining_ticket
                    SET ticket_origin = %(ticket_origin)s,
                        ticket_x_range = %(ticket_x_range)s,
                        ticket_z_range = %(ticket_z_range)s,
                        ticket_y_range = %(ticket_y_range)s
                    WHERE stripmining_ticket.ticket_id = %(ticket_id)s;
                    """,
                    {
                        "ticket_id": ticket.ticket_id,
                        "ticket_origin": ticket.origin.serialize(),
                        "ticket_x_range": ticket.x_range,
                        "ticket_z_range": ticket.z_range,
                        "ticket_y_range": ticket.y_range
                    }
                )
            else:
                raise TypeError(f"unknown Ticket type: {type(ticket)}")

    def load_all_ticket_data(self, directive):
        with self.database_connector.get_cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM ticket
                    LEFT JOIN stripmining_ticket on ticket.ticket_id = stripmining_ticket.ticket_id
                WHERE ticket.directive_id = %(directive_id)s
                """,
                {
                    "directive_id": directive.directive_id
                }
            )
            return cursor.fetchall()
