from loguru import logger

from src.flumph.flumph import Flumph
from src.flumph.occupation.occupation_factory import OccupationFactory
from src.orm.info import Info


class FlumphFactory:
    @staticmethod
    def recover(db_session, executor, cloister):
        flumph_name = executor.execute_function("robot.name()")[0]
        flumph_info = Flumph.retrieve_info(db_session, flumph_name)
        if flumph_info is not None:
            logger.info(f"loaded {flumph_name}")
            flumph = Flumph(executor, cloister, flumph_info.name, flumph_info.location)
            occupation = OccupationFactory.recover(db_session, flumph)
            flumph.set_occupation(occupation)
        else:
            logger.info(f"{flumph_name} does not exist")
            flumph = None
        return flumph

    @staticmethod
    def create_stripminer(db_session, executor, cloister, location):
        flumph_name = executor.execute_function("robot.name()")[0]
        logger.info(f"creating {flumph_name}")
        flumph = Flumph(executor, cloister, flumph_name, location)
        Info.save(db_session, flumph)
        occupation = OccupationFactory.create_stripminer(db_session, flumph)
        flumph.set_occupation(occupation)
        cloister.assign_home(db_session, flumph)
        return flumph
