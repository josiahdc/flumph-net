from abc import ABC

from src.organization.cloister.cloister_info import CloisterInfo
from src.organization.cloister.directive.directive_info import DirectiveInfo


class Directive(ABC):
    def __init__(self, cloister):
        self.cloister = cloister

    def retrieve_self_info(self, db_session):
        return self.retrieve_info(db_session, self.cloister.name)

    @staticmethod
    def retrieve_info(db_session, cloister_name):
        return db_session.query(DirectiveInfo).join(CloisterInfo). \
            filter(CloisterInfo.name == cloister_name).one_or_none()
