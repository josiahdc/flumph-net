from loguru import logger

from src.common.exception import NoHomeAvailableError
from src.common.location import Location
from src.common.orientation import Orientation
from src.flumph.flumph_factory import FlumphFactory
from src.organization.cloister.cloister_factory import CloisterFactory
from src.orm import Session


class Gestalt:
    def __init__(self):
        cloister_name = "cloister-0"
        db_session = Session()
        self.cloister = CloisterFactory.recover(db_session, cloister_name)
        if self.cloister is None:
            cloister_origin = Location(-1700, -700, 70, Orientation.NORTH)
            self.cloister = CloisterFactory.create_stripmine(db_session, cloister_name, cloister_origin)
        db_session.commit()
        db_session.close()

    def handle_connection(self, executor):
        db_session = Session()
        flumph = FlumphFactory.recover(db_session, executor, self.cloister)
        if flumph is None:
            try:
                flumph = FlumphFactory.create_stripminer(
                    db_session,
                    executor,
                    self.cloister,
                    self.cloister.origin.duplicate()
                )
                db_session.commit()
                db_session.close()
            except NoHomeAvailableError as exception:
                logger.error(
                    f"{exception.cloister_name} has no available homes for {exception.flumph_name}: {exception}")
                db_session.rollback()
                db_session.close()
                return
        # try:
        #     do_task(Reset(flumph))
        # except StuckFlumphError as exception:
        #     logger.error(f"{exception.flumph_name} got stuck: {exception}")
