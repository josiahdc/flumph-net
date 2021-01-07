from loguru import logger

from src.config import CLOISTER_INITIAL_HOME_COUNT
from src.organization.cloister.cloister import Cloister
from src.organization.cloister.directive.directive_factory import DirectiveFactory
from src.orm.info import Info


class CloisterFactory:
    @staticmethod
    def recover(db_session, cloister_name):
        cloister_info = Cloister.retrieve_info(db_session, cloister_name)
        if cloister_info is not None:
            logger.info(f"loaded {cloister_name}")
            cloister = Cloister(cloister_name, cloister_info.origin)
            directive = DirectiveFactory.recover(db_session, cloister)
            cloister.set_directive(directive)
        else:
            logger.info(f"{cloister_name} does not exist")
            cloister = None
        return cloister

    @staticmethod
    def create_stripmine(db_session, cloister_name, origin):
        logger.info(f"creating {cloister_name}")
        cloister = Cloister(cloister_name, origin)
        Info.save(db_session, cloister)
        directive = DirectiveFactory.create_stripmine(db_session, cloister)
        cloister.set_directive(directive)
        cloister.designate_homes(db_session, 0, CLOISTER_INITIAL_HOME_COUNT)
        return cloister
