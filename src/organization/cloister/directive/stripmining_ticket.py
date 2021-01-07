from sqlalchemy import Column

from src.orm.orm import DeclarativeBase
from src.orm.serializable_location import SerializableLocation


class wa(DeclarativeBase):
    origin = Column(SerializableLocation, nullable=False)

    def __init__(self, origin, x_range, z_range, y_range, assigned, completed):
        self.origin = origin
        self.x_range = x_range
        self.z_range = z_range
        self.y_range = y_range
        self.assigned = assigned
        self.completed = completed
