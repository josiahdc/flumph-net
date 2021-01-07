from sqlalchemy import ForeignKey, Integer, Column

from src.organization.cloister.directive.directive_info import DirectiveInfo


class StripmineDirectiveInfo(DirectiveInfo):
    id = Column(Integer, ForeignKey("directive_info.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "stripmine"
    }
