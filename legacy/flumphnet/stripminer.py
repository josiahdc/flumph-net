from legacy.flumphnet import Miner


class Strip_Miner(Miner):
    def __init__(self, cloister, reader, writer):
        super().__init__(cloister, reader, writer)
        self.distance = 50
        self.lane = None

    def main(self):
        if self.cloister.get_mine_status() == "building":
            # should be placed in the center of the hall leading to the mine
            self.slice_forward()
            self.right()
            self.slice_forward(2)
            self.left(2)
            self.forward(2)
            self.slice_forward(2)
            self.right()
            self.up()
            self.tunnel(6, width=5)
            self.back()
            self.left()
            self.tunnel(146, width=2)
            self.back(150)
            self.right()
            self.forward()
            self.right()
            self.tunnel(146, width=2)
            self.back(150)
            self.right()
            self.down(2)
            self.forward(3)
            self.left()
            self.forward(2)
            self.cloister.set_status("operational")
        while self.status_check() and self.cloister.get_mine_status() == "operational":
            self.goto_next_lane()
            self.tunnel(self.distance)
            self.deposit_stripped_ore()

    def goto_next_lane(self):
        """get and dig the next mine lane, assumes the main lane is already excavated"""
        self.lane = self.cloister.get_next_lane()
        if self.lane is None:
            self.shutdown()
            return
        # move out of base
        self.up(2)
        self.forward(2)
        self.left()
        self.forward(3)
        if self.lane > 50:
            self.right()
            self.forward((self.lane - 50) * 3)
            self.left()
            self.forward()
            return
        self.forward()
        if self.lane == 50:
            # lane is right in front of the flumph
            return
        else:
            # lane is to the left
            self.left()
            self.forward((50 - self.lane) * 3)
            self.right()
            return

    def deposit_stripped_ore(self):
        """return to cloister hub and drop off mined goods"""
        self.cloister.complete_lane(self.lane)

        # get out of the tunnel
        self.down(2)
        self.right()
        self.forward(2)
        self.left()
        for i in range(self.distance):
            self.back()

        # return to cloister hub
        if self.lane < 48:
            self.back()
            self.right()
            self.forward((48 - self.lane) * 3)
            self.right()
        elif self.lane == 48:
            self.back()
            self.left(2)
        else:
            self.left()
            self.forward((self.lane - 48) * 3)
            self.left()
            self.forward()

        # drop off items
        self.forward(3)
        self.left()
        self.forward(2)
        self.deposit_all_down()

    def status_check(self):
        """returns true if the robot is good to do another branch"""
        energy_remaining = self.get_remaining_energy()
        durability = self.get_durability()
        if energy_remaining < 10000 or durability < 9 * self.distance + 10:
            return False
        return True

    def create_mine(self):
        """dig a mine"""