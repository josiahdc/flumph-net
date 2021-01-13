from src.organization.cloister.cloister_factory import CloisterFactory


class CloisterRegistry:
    def __init__(self, hoard):
        cloisters = CloisterFactory.recover_all_cloisters(hoard)
        self.registry = {}
        for cloister in cloisters:
            self.registry[cloister.cloister_id] = cloister

    def get_cloister(self, cloister_id):
        return self.registry[cloister_id]

    def add_cloister(self, cloister):
        self.registry[cloister.cloister_id] = cloister

    def __iter__(self):
        return self.registry.values().__iter__()
