class Home:
    def __init__(self, cloister, origin, flumph_id, home_id=None):
        self.cloister = cloister
        self.origin = origin
        self.flumph_id = flumph_id
        self.home_id = home_id

    def set_home_id(self, home_id):
        self.home_id = home_id
