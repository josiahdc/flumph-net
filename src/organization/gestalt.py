from src.database.hoard.hoard import Hoard
from src.flumph.flumph_factory import FlumphFactory
from src.organization.cloister.cloister_factory import CloisterFactory
from src.organization.cloister.cloister_registry import CloisterRegistry


class Gestalt:
    def __init__(self, database_connector):
        self._hoard = Hoard(database_connector)
        self._cloister_registry = CloisterRegistry(self._hoard)

    def shutdown(self):
        for cloister in self._cloister_registry:
            self._hoard.save_cloister(cloister)
            self._hoard.save_directive(cloister.directive)
            for home in cloister.homes:
                self._hoard.save_home(home)
            for ticket in cloister.directive.tickets:
                self._hoard.save_ticket(ticket)

    def add_cloister(self, cloister_name, origin):
        cloister = CloisterFactory.create_stripmine(self._hoard, cloister_name, origin)
        self._cloister_registry.add_cloister(cloister)

    def handle_connection(self, executor):
        if FlumphFactory.flumph_exists(self._hoard, executor):
            flumph = FlumphFactory.recover(self._hoard, executor, self._cloister_registry)
        else:
            cloister = self._cloister_registry.get_cloister(1)
            flumph = FlumphFactory.create_stripminer(self._hoard, executor, cloister, cloister.origin.duplicate())
        flumph.work()
        self._hoard.save_flumph(flumph)
        self._hoard.save_occupation(flumph.occupation)
