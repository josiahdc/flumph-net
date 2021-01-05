from src.task.task import Task


class Stripmine(Task):
    def __init__(self, flumph, size):
        super().__init__(flumph)
        self._size = size
        self._depth = 0

    def perform(self):
        while self._attempt_to_mine_down():
            self._flumph.down()
            self._depth += 1
            for lane_index in range(self._size):
                self._mine_forward(self._size - 1)
                if lane_index != self._size - 1:
                    self._set_up_next_lane(lane_index)
            self._return_to_shaft(self._size)
        self._flumph.up(self._depth)
        yield

    def _set_up_next_lane(self, lane_index):
        if lane_index % 2 == 0:
            self._flumph.turn_right()
            self._mine_forward()
            self._flumph.turn_right()
        else:
            self._flumph.turn_left()
            self._mine_forward()
            self._flumph.turn_left()

    def _mine_forward(self, distance=1):
        for i in range(distance):
            self._flumph.swing()
            self._flumph.forward()

    def _return_to_shaft(self, lane_index):
        if lane_index % 2 != 0:
            self._flumph.turn_right(2)
            self._flumph.forward(self._size - 1)
        self._flumph.turn_right()
        self._flumph.forward(self._size - 1)
        self._flumph.turn_right()

    def _attempt_to_mine_down(self):
        swing_result = self._flumph.swing_down()
        if swing_result[0] is True or swing_result[1] != "block":
            return True
        else:
            return False
