from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.orm.orm import DeclarativeBase
from src.orm.serializable_location import SerializableLocation


class Home(DeclarativeBase):
    cloister_id = Column(Integer, ForeignKey("cloister_info.id"), nullable=False)
    flumph_id = Column(Integer, ForeignKey("flumph_info.id"), nullable=True)
    origin = Column(SerializableLocation, nullable=False)

    cloister_info = relationship("CloisterInfo", back_populates="homes")
    flumph_info = relationship("FlumphInfo", back_populates="home")

    def __init__(self, cloister_info, origin):
        self.cloister_info = cloister_info
        self.origin = origin
