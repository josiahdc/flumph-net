from yoyo import step

__depends__ = {}

steps = [
    step(
        """
        CREATE TABLE cloister (
            cloister_id SERIAL PRIMARY KEY,
            cloister_name VARCHAR(64) UNIQUE NOT NULL,
            cloister_origin VARCHAR(64) NOT NULL
        );
        """,
        """
        DROP TABLE cloister;
        """
    ),
    step(
        """
        CREATE TABLE flumph (
            flumph_id SERIAL PRIMARY KEY,
            cloister_id INT REFERENCES cloister(cloister_id) NOT NULL,
            flumph_name VARCHAR(64) UNIQUE NOT NULL,
            flumph_location VARCHAR(64) NOT NULL
        );
        """,
        """
        DROP TABLE flumph;
        """
    ),
    step(
        """
        CREATE TABLE home (
            home_id SERIAL PRIMARY KEY,
            cloister_id INT REFERENCES cloister(cloister_id) NOT NULL,
            flumph_id INT REFERENCES flumph(flumph_id) NOT NULL,
            home_origin VARCHAR(64) NOT NULL
        );
        """,
        """
        DROP TABLE home;
        """
    ),
    step(
        """
        CREATE TABLE occupation (
            occupation_id SERIAL PRIMARY KEY,
            flumph_id INT REFERENCES flumph(flumph_id) NOT NULL
        );
        """,
        """
        DROP TABLE occupation;
        """
    ),
    step(
        """
        CREATE TABLE directive (
            directive_id SERIAL PRIMARY KEY,
            cloister_id INT REFERENCES cloister(cloister_id) NOT NULL
        );
        """,
        """
        DROP TABLE directive;
        """
    ),
    step(
        """
        CREATE TABLE ticket (
            ticket_id SERIAL PRIMARY KEY,
            directive_id INT REFERENCES directive(directive_id) NOT NULL,
            flumph_id INT REFERENCES flumph(flumph_id) NOT NULL,
            ticket_completed BOOLEAN NOT NULL
        );
        """,
        """
        DROP TABLE ticket;
        """
    ),
    step(
        """
        CREATE TABLE stripmine_directive (
            stripmine_directive_id SERIAL PRIMARY KEY,
            directive_id INT REFERENCES directive(directive_id) NOT NULL,
            directive_last_ticket_origin VARCHAR(64)
        );
        """,
        """
        DROP TABLE stripmine_directive;
        """
    ),
    step(
        """
        CREATE TABLE stripminer_occupation (
            stripminer_occupation_id SERIAL PRIMARY KEY,
            occupation_id INT REFERENCES occupation(occupation_id) NOT NULL
        );
        """,
        """
        DROP TABLE stripminer_occupation;
        """
    ),
    step(
        """
        CREATE TABLE stripmining_ticket (
            stripmining_ticket_id SERIAL PRIMARY KEY,
            ticket_id INT REFERENCES ticket(ticket_id) NOT NULL,
            ticket_origin VARCHAR(64) NOT NULL,
            ticket_x_range INTEGER NOT NULL,
            ticket_z_range INTEGER NOT NULL,
            ticket_y_range INTEGER NOT NULL
        );
        """,
        """
        DROP TABLE stripmining_ticket;
        """
    )
]
