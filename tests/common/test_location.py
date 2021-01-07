from src.common.location import Location
from src.common.orientation import Orientation


class TestLocation:
    def test_to_string(self):
        location = Location(-12, 24, 0, Orientation.SOUTH)
        result = str(location)
        assert result == "-12, 24, 0, 2"

    def test_serialize(self):
        location = Location(1, -3, 12, Orientation.EAST)
        result = location.serialize()
        assert result == "1, -3, 12, 1"

    def test_deserialize(self):
        location = Location(1, -3, 12, Orientation.EAST)
        serialized_location = location.serialize()
        deserialized_location = Location.deserialize(serialized_location)
        assert deserialized_location == location

    def test_duplicate(self):
        location = Location(-12, 24, 0, Orientation.SOUTH)
        result = location.duplicate()
        assert result == location
        assert result is not location

    def test_forward_north(self):
        location = Location(0, 0, 0, Orientation.NORTH)
        location.forward()
        assert location == Location(0, -1, 0, Orientation.NORTH)

    def test_forward_east(self):
        location = Location(0, 0, 0, Orientation.EAST)
        location.forward()
        assert location == Location(1, 0, 0, Orientation.EAST)

    def test_forward_south(self):
        location = Location(0, 0, 0, Orientation.SOUTH)
        location.forward()
        assert location == Location(0, 1, 0, Orientation.SOUTH)

    def test_forward_west(self):
        location = Location(0, 0, 0, Orientation.WEST)
        location.forward()
        assert location == Location(-1, 0, 0, Orientation.WEST)

    def test_back_north(self):
        location = Location(0, 0, 0, Orientation.NORTH)
        location.back()
        assert location == Location(0, 1, 0, Orientation.NORTH)

    def test_back_east(self):
        location = Location(0, 0, 0, Orientation.EAST)
        location.back()
        assert location == Location(-1, 0, 0, Orientation.EAST)

    def test_back_south(self):
        location = Location(0, 0, 0, Orientation.SOUTH)
        location.back()
        assert location == Location(0, -1, 0, Orientation.SOUTH)

    def test_back_west(self):
        location = Location(0, 0, 0, Orientation.WEST)
        location.back()
        assert location == Location(1, 0, 0, Orientation.WEST)

    def test_up(self):
        location = Location(0, 0, 0, Orientation.NORTH)
        location.up()
        assert location == Location(0, 0, 1, Orientation.NORTH)

    def test_down(self):
        location = Location(0, 0, 0, Orientation.NORTH)
        location.down()
        assert location == Location(0, 0, -1, Orientation.NORTH)

    def test_turn_right(self):
        location = Location(0, 0, 0, Orientation.NORTH)
        location.turn_right()
        assert location == Location(0, 0, 0, Orientation.EAST)
        location.turn_right()
        assert location == Location(0, 0, 0, Orientation.SOUTH)
        location.turn_right()
        assert location == Location(0, 0, 0, Orientation.WEST)
        location.turn_right()
        assert location == Location(0, 0, 0, Orientation.NORTH)

    def test_turn_left(self):
        location = Location(0, 0, 0, Orientation.NORTH)
        location.turn_left()
        assert location == Location(0, 0, 0, Orientation.WEST)
        location.turn_left()
        assert location == Location(0, 0, 0, Orientation.SOUTH)
        location.turn_left()
        assert location == Location(0, 0, 0, Orientation.EAST)
        location.turn_left()
        assert location == Location(0, 0, 0, Orientation.NORTH)
