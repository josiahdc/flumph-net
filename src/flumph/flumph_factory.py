from loguru import logger

from src.common.location import Location
from src.flumph.flumph import Flumph
from src.flumph.occupation.occupation_factory import OccupationFactory


class FlumphFactory:
    @staticmethod
    def recover(hoard, executor, cloister):
        flumph_name = executor.execute_function("robot.name()")[0]
        data = hoard.load_flumph_data(flumph_name)
        if data is not None:
            logger.info(f"loaded {flumph_name}")
            flumph = Flumph(executor, cloister, data["flumph_name"], Location.deserialize(data["flumph_location"]))
            occupation = OccupationFactory.recover(hoard, flumph)
            flumph.set_occupation(occupation)
            home = cloister.retrieve_home(flumph)
            flumph.set_home(home)
        else:
            logger.info(f"{flumph_name} does not exist")
            flumph = None
        return flumph

    @staticmethod
    def create_stripminer(executor, cloister, location):
        flumph_name = executor.execute_function("robot.name()")[0]
        logger.info(f"creating {flumph_name}")
        flumph = Flumph(executor, cloister, flumph_name, location)
        occupation = OccupationFactory.create_stripminer(flumph)
        flumph.set_occupation(occupation)
        home = cloister.assign_home(flumph)
        flumph.set_home(home)
        return flumph
