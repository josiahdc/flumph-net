from src.flumphnet.organization import Cloister


class MineCloister(Cloister):
    def __init__(self, name, create=False, x=None, y=None, z=None):
        super().__init__(name, create=create, x=x, y=y, z=z)
        self.lane_size = 100

        # get the lane array, which contains a T for every excavated lane
        if create:
            self.mine_lanes = ["F" for i in range(self.lane_size)]
            self.mine_status = "building"
        else:
            self.mine_lanes = self.red_conn.get(self.name + ":mine-lanes").split(",")
            self.mine_status = self.red_conn.get(self.name + ":mine-status")

    def get_next_lane(self):
        """get the next valid mine lane, or None if all of them have been excavated"""
        for i in range(self.lane_size):
            if self.mine_lanes[i] == "F":
                self.mine_lanes[i] = "IP"
                return i
        return None

    def get_mine_status(self):
        return self.mine_status

    def complete_lane(self, lane):
        self.mine_lanes[lane] = "T"
        for lane in self.mine_lanes:
            if lane == "F" or lane == "IP":
                return
        # all lanes are complete
        self.set_status("complete")

    def set_status(self, status):
        self.mine_status = status

    def _sub_shutdown(self):
        # record in progress ones as full
        str_mine_lanes = ["T" if i == "T" else "F" for i in self.mine_lanes]
        self.red_conn.set(self.name + ":mine-lanes", ",".join(str_mine_lanes))
        self.red_conn.set(self.name + ":mine-status", self.mine_status)
        return "mine"