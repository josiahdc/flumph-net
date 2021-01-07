class FlumphError(Exception):
    def __init__(self, flumph_name):
        self.flumph_name = flumph_name


class StuckFlumphError(FlumphError):
    pass


class CannotMoveError(StuckFlumphError):
    pass


class NoHomeAvailableError(FlumphError):
    def __init__(self, flumph_name, cloister_name):
        super().__init__(flumph_name)
        self.cloister_name = cloister_name
