class StuckFlumphError(Exception):
    def __init__(self, flumph_name):
        self.flumph_name = flumph_name


class CannotMoveError(StuckFlumphError):
    pass
