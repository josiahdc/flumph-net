from src.common.location import Location
from src.organization.cloister.home import Home


class HomeFactory:
    @staticmethod
    def recover_all_homes(hoard, cloister):
        homes = []
        home_data = hoard.load_all_home_data(cloister)
        for home_row in home_data:
            origin = Location.deserialize(home_row["home_origin"])
            flumph_id = home_row["flumph_id"]
            home_id = home_row["home_id"]
            home = Home(cloister, origin, flumph_id, home_id=home_id)
            homes.append(home)
        return homes

    @staticmethod
    def create(hoard, cloister, origin, flumph):
        home = Home(cloister, origin, flumph.flumph_id)
        home_id = hoard.insert_home(home)
        home.set_home_id(home_id)
        return home
