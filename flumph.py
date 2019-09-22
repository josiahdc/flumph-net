import copy
from abc import ABC, abstractmethod


class Flumph(ABC):
    def __init__(self, cloister, reader, writer):
        self.cloister = cloister
        self.reader = reader
        self.writer = writer
        self.terminate = False
        self.orientation = 0
        self.coords = copy.deepcopy(self.cloister.get_coords())
        self.cloister_coords = self.cloister.get_coords()
        self.inventory_size = self.get_inventory_size()

    @abstractmethod
    def main(self):
        """the insertion point, should repeat until connection closes"""
        pass

    def execute(self, api, function, params={}):
        """call a function on the robot, returns a variable sized array of return values"""
        call = str(len(params)) + "\n" + api + "\n" + function + "\n"
        for param, paramType in params.items():
            call += str(param) + "\n" + paramType + "\n"
        self.writer.write(str.encode(call))
        return_vals = []
        num_of_return_vals = int(self.reader.readline())
        for iteration in range(num_of_return_vals):
            val = self.reader.readline()
            val = val.decode("utf-8")
            val = val.strip()
            if val == "nil":
                val = None
            elif val == "true":
                val = True
            elif val == "false":
                val = False
            return_vals.append(val)
        return return_vals

    # command wrappers, use them when possible
    def skip(self):
        self.execute("control", "skip")

    def shutdown(self):
        self.execute("control", "shutdown")

    # detection
    def passable(self):
        return not self.execute("robot", "detect")[0]

    def passable_up(self):
        return not self.execute("robot", "detectUp")[0]

    def passable_down(self):
        return not self.execute("robot", "detectDown")[0]

    def detect(self):
        return self.execute("robot", "detect")[1]

    def detect_up(self):
        return self.execute("robot", "detectUp")[1]

    def detect_down(self):
        return self.execute("robot", "detectDown")[1]

    # movement
    def forward(self, distance=1):
        for i in range(distance):
            while self.try_forward() is not None:
                pass

    def back(self, distance=1):
        for i in range(distance):
            while self.try_back() is not None:
                pass

    def up(self, distance=1):
        for i in range(distance):
            while self.try_up() is not None:
                pass

    def down(self, distance=1):
        for i in range(distance):
            while self.try_down() is not None:
                pass

    def try_forward(self):
        """moves forward, adjusts position, and returns none if successful, or a string reason why it failed"""
        status = self.execute("robot", "forward")

        if status[0] == True:
            if self.orientation == 0:
                self.coords["z"] -= 1
            elif self.orientation == 1:
                self.coords["x"] += 1
            elif self.orientation == 2:
                self.coords["z"] += 1
            elif self.orientation == 3:
                self.coords["x"] -= 1
            return None
        else:
            return status[1]

    def try_back(self):
        """moves backward, adjusts position, and returns none if successful, or a string reason why it failed"""
        status = self.execute("robot", "back")

        if status[0] == True:
            if self.orientation == 0:
                self.coords["z"] += 1
            elif self.orientation == 1:
                self.coords["x"] -= 1
            elif self.orientation == 2:
                self.coords["z"] -= 1
            elif self.orientation == 3:
                self.coords["x"] += 1
            return None
        else:
            return status[1]

    def try_up(self):
        """moves up, adjusts position, and returns none if successful, or a string reason why it failed"""
        status = self.execute("robot", "up")

        if status[0] == True:
            self.coords["y"] += 1
            return None
        else:
            return status[1]

    def try_down(self):
        """moves down, adjusts position, and returns none if successful, or a string reason why it failed"""
        status = self.execute("robot", "down")

        if status[0] == True:
            self.coords["y"] -= 1
            return None
        else:
            return status[1]

    def left(self, times=1):
        for i in range(times):
            self.execute("robot", "turnLeft")
            self.orientation -= 1
            if self.orientation < 0:
                self.orientation = 3

    def right(self, times=1):
        for i in range(times):
            self.execute("robot", "turnRight")
            self.orientation += 1
            if self.orientation > 3:
                self.orientation = 0

    # status
    def get_remaining_energy(self):
        return float(self.execute("computer", "energy")[0])

    def get_inventory_size(self):
        return int(round(float(self.execute("robot", "inventorySize")[0])))

    def get_durability(self):
        return int(round(float(self.execute("robot", "durability")[1])))

    # inventory
    def suck_all(self):
        attempts = 0
        while not self.execute("beam", "suck") and attempts < 20:
            attempts += 1

    def deposit_all_down(self):
        for i in range(1, self.inventory_size + 1):
            self.select_slot(i)
            self.execute("robot", "dropDown")

    def select_slot(self, slot):
        self.execute("robot", "select", params={slot: "number"})
