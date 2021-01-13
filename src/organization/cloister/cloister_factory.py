from loguru import logger

from src.common.location import Location
from src.organization.cloister.cloister import Cloister
from src.organization.cloister.directive.directive_factory import DirectiveFactory
from src.organization.cloister.home_factory import HomeFactory


class CloisterFactory:
    @staticmethod
    def recover_all_cloisters(hoard):
        cloisters = []
        data = hoard.load_all_cloister_data()
        for cloister_data in data:
            cloister_name = cloister_data["cloister_name"]
            cloister_origin = Location.deserialize(cloister_data["cloister_origin"])
            cloister_id = cloister_data["cloister_id"]
            logger.info(f"loading {cloister_name}")
            cloister = Cloister(cloister_name, cloister_origin, cloister_id=cloister_id)
            directive = DirectiveFactory.recover(hoard, cloister)
            cloister.set_directive(directive)
            homes = HomeFactory.recover_all_homes(hoard, cloister)
            cloister.set_homes(homes)
            cloisters.append(cloister)
        return cloisters

    @staticmethod
    def create_stripmine(hoard, cloister_name, origin):
        logger.info(f"creating {cloister_name}")
        cloister = Cloister(cloister_name, origin)
        cloister_id = hoard.insert_cloister(cloister)
        cloister.set_cloister_id(cloister_id)
        directive = DirectiveFactory.create_stripmining_directive(hoard, cloister)
        cloister.set_directive(directive)
        return cloister
