from src.common.exception import CannotMoveError
from src.flumph.flumph_info import FlumphInfo


class Flumph:
    def __init__(self, executor, cloister, name, location):
        self._executor = executor
        self._cloister = cloister
        self.name = name
        self.location = location
        self._occupation = None

    def generate_info(self, db_session):
        return FlumphInfo(self._cloister.retrieve_self_info(db_session), self.name, self.location)

    def retrieve_self_info(self, db_session):
        return self.retrieve_info(db_session, self.name)

    @staticmethod
    def retrieve_info(db_session, name):
        return db_session.query(FlumphInfo).filter(FlumphInfo.name == name).one_or_none()

    def set_occupation(self, occupation):
        self._occupation = occupation

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
