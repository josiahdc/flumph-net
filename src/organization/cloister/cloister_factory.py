from loguru import logger

from src.common.location import Location
from src.organization.cloister.cloister import Cloister
from src.organization.cloister.directive.directive_factory import DirectiveFactory


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
            # home_data = hoard.load_all_home_data(cloister)
            # for home_row in home_data:
            #     home = Home(
            #         cloister,
            #         Location.deserialize(home_row["cloister_origin"]),
            #         home_row["flumph_name"],
            #         home_row["home_id"]
            #     )
            #     cloister.add_home(home)
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
