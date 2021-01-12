import ujson

from src.flumph.occupation.stripminer_occupation import StripminerOccupation


class OccupationFactory:
    @staticmethod
    def recover(hoard, flumph):
        data = hoard.load_occupation_data(flumph.name)
        if data.get("stripminer_occupation_id", None) is not None:
            occupation = StripminerOccupation(flumph)
        else:
            raise TypeError(f"could not discern occupation type from data: {ujson.dumps(data)}")
        return occupation

    @staticmethod
    def create_stripminer(flumph):
        occupation = StripminerOccupation(flumph)
        return occupation
