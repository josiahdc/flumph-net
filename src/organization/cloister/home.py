class Home:
    def __init__(self, cloister, origin, flumph_name, home_id=None):
        self.cloister = cloister
        self.origin = origin
        self.flumph_name = flumph_name
        self.home_id = home_id

    def set_home_id(self, home_id):
        self.home_id = home_id
