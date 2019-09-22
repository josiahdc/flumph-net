from flumph import Flumph

class Miner(Flumph):
    def __init__(self, cloister, reader, writer):
        super().__init__(cloister, reader, writer)

    # standards
    def tunnel(self, distance, width=3):
        """mine a tunnel (robot is assumed to be in the upper left corner) ends in upper left corner"""
        self.down()
        for i in range(distance):
            self.slice_forward()
            self.right()
            self.slice_forward(width - 1)
            self.back(width - 1)
            self.left()
        self.up()

    # convenience methods
    def slice_forward(self, distance=1):
        for i in range(distance):
            self.mine_forward()
            self.mine_up()
            self.mine_down()
            self.suck_all()

    # basic mines
    def mine(self):
        return self.execute("robot", "swing")[0]

    def mine_up(self):
        while not self.passable_up():
            self.execute("robot", "swingUp")

    def mine_down(self):
        while not self.passable_down():
            self.execute("robot", "swingDown")

    def mine_forward(self):
        while not self.passable():
            self.mine()
        self.try_forward()