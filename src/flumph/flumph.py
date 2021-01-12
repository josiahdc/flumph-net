from src.common.exception import CannotMoveError


class Flumph:
    def __init__(self, executor, cloister, name, location, flumph_id=None):
        self._executor = executor
        self.cloister = cloister
        self.name = name
        self.location = location
        self.flumph_id = flumph_id
        self.occupation = None
        self.home = None

    def set_flumph_id(self, flumph_id):
        self.flumph_id = flumph_id

    def set_occupation(self, occupation):
        self.occupation = occupation

    def set_home(self, home):
        self.home = home

    def work(self):
        self.occupation.work()

    def energy(self):
        return int(self._executor.execute_function("computer.energy()")[0])

    def max_energy(self):
        return int(self._executor.execute_function("computer.maxEnergy()")[0])

    def inventory_size(self):
        return int(self._executor.execute_function("robot.inventorySize()")[0])

    def select(self, slot):
        self._executor.execute_function(f"robot.select({slot})")

    def drop(self):
        return self._executor.execute_function("robot.drop()")[0]

    def detect(self):
        return self._executor.execute_function("robot.detect()")

    def swing(self):
        return self._executor.execute_function(f"robot.swing()")

    def swing_up(self):
        return self._executor.execute_function(f"robot.swingUp()")

    def swing_down(self):
        return self._executor.execute_function(f"robot.swingDown()")

    def forward(self, distance=1):
        for i in range(distance):
            result = self._executor.execute_function("robot.forward()")
            if result[0] is True:
                self.location.forward()
            else:
                raise CannotMoveError(self.name())

    def back(self, distance=1):
        for i in range(distance):
            result = self._executor.execute_function("robot.back()")
            if result[0] is True:
                self.location.back()
            else:
                raise CannotMoveError(self.name())

    def up(self, distance=1):
        for i in range(distance):
            result = self._executor.execute_function("robot.up()")
            if result[0] is True:
                self.location.up()
            else:
                raise CannotMoveError(self.name())

    def down(self, distance=1):
        for i in range(distance):
            result = self._executor.execute_function("robot.down()")
            if result[0] is True:
                self.location.down()
            else:
                raise CannotMoveError(self.name())

    def turn_right(self, count=1):
        for i in range(count):
            result = self._executor.execute_function("robot.turnRight()")
            if result[0] is True:
                self.location.turn_right()
            else:
                raise CannotMoveError(self.name())

    def turn_left(self, count=1):
        for i in range(count):
            result = self._executor.execute_function("robot.turnLeft()")
            if result[0] is True:
                self.location.turn_left()
            else:
                raise CannotMoveError(self.name())

    def orient(self, desired_orientation):
        while self.location.orientation != desired_orientation:
            self.turn_right()
