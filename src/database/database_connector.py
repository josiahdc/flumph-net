from contextlib import contextmanager
from time import perf_counter, sleep

from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool, PoolError

from src.common.exception import DatabaseConnectionError
from src.config import DATABASE_DB, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT, \
    DATABASE_MAX_CONNECTIONS, DATABASE_ACQUIRE_CONNECTION_TIMEOUT_SEC


class DatabaseConnector:
    def __init__(self):
        self.pool = None

    def __enter__(self):
        self.pool = ThreadedConnectionPool(
            1,
            DATABASE_MAX_CONNECTIONS,
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            dbname=DATABASE_DB,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD
        )
        return self

    def __exit__(self, type, value, traceback):
        self.pool.closeall()

    @contextmanager
    def get_cursor(self):
        start_time = perf_counter()
        success = False
        connection = None
        while not success and perf_counter() - start_time < DATABASE_ACQUIRE_CONNECTION_TIMEOUT_SEC:
            try:
                with self.pool.getconn() as connection:
                    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                        success = True
                        yield cursor
            except PoolError:
                sleep(0.5)
            finally:
                if connection is not None:
                    self.pool.putconn(connection)
        if not success:
            raise DatabaseConnectionError("timed out while waiting for database connection")
