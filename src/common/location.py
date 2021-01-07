from src.common.orientation import Orientation
from src.common.serializable import Serializable


class Location(Serializable):
    def __init__(self, x, z, y, orientation, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.z = z
        self.y = y
        self.orientation = orientation

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.orientation == other.orientation

    def __str__(self):
        return f"{self.x}, {self.z}, {self.y}, {self.orientation}"

    def serialize(self):
        return str(self)

    @staticmethod
    def deserialize(serialized_location):
        pieces = serialized_location.split(", ")
        return Location(int(pieces[0]), int(pieces[1]), int(pieces[2]), int(pieces[3]))

    def duplicate(self):
        return Location(self.x, self.z, self.y, self.orientation)

    def forward(self):
        if self.orientation == Orientation.NORTH:
            self.z -= 1
        elif self.orientation == Orientation.EAST:
            self.x += 1
        elif self.orientation == Orientation.SOUTH:
            self.z += 1
        elif self.orientation == Orientation.WEST:
            self.x -= 1

    def back(self):
        if self.orientation == Orientation.NORTH:
            self.z += 1
        elif self.orientation == Orientation.EAST:
            self.x -= 1
        elif self.orientation == Orientation.SOUTH:
            self.z -= 1
        elif self.orientation == Orientation.WEST:
            self.x += 1

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def turn_right(self):
        self.orientation += 1
        if self.orientation > 3:
            self.orientation = 0

    def turn_left(self):
        self.orientation -= 1
        if self.orientation < 0:
            self.orientation = 3
