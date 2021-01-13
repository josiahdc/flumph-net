import ujson

from src.flumph.occupation.stripminer_occupation import StripminerOccupation


class OccupationFactory:
    @staticmethod
    def recover(hoard, flumph):
        data = hoard.load_occupation_data(flumph)
        occupation_id = data["occupation_id"]
        if data.get("stripminer_occupation_id", None) is not None:
            occupation = StripminerOccupation(flumph, occupation_id=occupation_id)
        else:
            raise TypeError(f"could not discern occupation type from data: {ujson.dumps(data)}")
        return occupation

    @staticmethod
    def create_stripminer(hoard, flumph):
        occupation = StripminerOccupation(flumph)
        occupation_id = hoard.insert_occupation(occupation)
        occupation.set_occupation_id(occupation_id)
        return occupation
