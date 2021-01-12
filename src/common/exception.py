class DatabaseConnectionError(Exception):
    pass


class FlumphError(Exception):
    def __init__(self, flumph_name):
        self.flumph_name = flumph_name


class StuckFlumphError(FlumphError):
    pass


class CannotMoveError(StuckFlumphError):
    pass
