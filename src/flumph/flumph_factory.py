from loguru import logger

from src.common.location import Location
from src.flumph.flumph import Flumph
from src.flumph.occupation.occupation_factory import OccupationFactory


class FlumphFactory:
    @staticmethod
    def flumph_exists(hoard, executor):
        flumph_name = executor.execute_function("robot.name()")[0]
        data = hoard.load_flumph_data(flumph_name)
        return data is not None

    @staticmethod
    def recover(hoard, executor, cloister_registry):
        flumph_name = executor.execute_function("robot.name()")[0]
        data = hoard.load_flumph_data(flumph_name)
        flumph_id = data["flumph_id"]
        flumph_name = data["flumph_name"]
        flumph_location = Location.deserialize(data["flumph_location"])
        cloister = cloister_registry.get_cloister(data["cloister_id"])
        logger.info(f"loading {flumph_name}")
        flumph = Flumph(executor, cloister, flumph_name, flumph_location, flumph_id=flumph_id)
        occupation = OccupationFactory.recover(hoard, flumph)
        flumph.set_occupation(occupation)
        home = cloister.retrieve_home(flumph)
        flumph.set_home(home)
        return flumph

    @staticmethod
    def create_stripminer(hoard, executor, cloister, location):
        flumph_name = executor.execute_function("robot.name()")[0]
        logger.info(f"creating {flumph_name}")
        flumph = Flumph(executor, cloister, flumph_name, location)
        flumph_id = hoard.insert_flumph(flumph)
        flumph.set_flumph_id(flumph_id)
        occupation = OccupationFactory.create_stripminer(hoard, flumph)
        flumph.set_occupation(occupation)
        home = cloister.allocate_home(hoard, flumph)
        flumph.set_home(home)
        return flumph
