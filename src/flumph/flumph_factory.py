from src.common.location import Location
from src.common.orientation import Orientation
from src.flumph.flumph import Flumph
from src.server.executor import Executor
from src.server.relay import Relay


class FlumphFactory:
    @staticmethod
    def create(reader, writer, home):
        relay = Relay(reader, writer)
        executor = Executor(relay)
        location = Location(-1700, -700, 70, Orientation.NORTH)
        return Flumph(executor, location, home)
