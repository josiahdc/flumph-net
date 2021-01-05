from src.common.orientation import Orientation


class Location:
    def __init__(self, x, z, y, orientation):
        self.x = x
        self.z = z
        self.y = y
        self.orientation = orientation

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
