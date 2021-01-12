from src.database.hoard.hoard import Hoard
from src.flumph.flumph_factory import FlumphFactory
from src.organization.cloister.cloister_factory import CloisterFactory


class Gestalt:
    def __init__(self, database_connector):
        self._hoard = Hoard(database_connector)
        self._cloisters = CloisterFactory.recover_all_cloisters(self._hoard)

    def shutdown(self):
        for cloister in self._cloisters:
            self._hoard.save_cloister(cloister)
            self._hoard.save_directive(cloister.directive)
            # for home in cloister.homes:
            #     self._hoard.save_home(home)

    def add_cloister(self, cloister_name, origin):
        cloister = CloisterFactory.create_stripmine(self._hoard, cloister_name, origin)
        self._cloisters.append(cloister)

    def handle_connection(self, executor):
        flumph = FlumphFactory.recover(self._hoard, executor, self.cloister)
        if flumph is None:
            flumph = FlumphFactory.create_stripminer(executor, self.cloister, self.cloister.origin.duplicate())
        flumph.work()
        self._hoard.save_flumph(flumph)
