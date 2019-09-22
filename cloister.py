from abc import abstractmethod, ABC
import redis as redis


class Cloister(ABC):
    def __init__(self, name, create=False, x=None, y=None, z=None):
        self.red_conn = redis.Redis(host='localhost', port=6379, db=7, decode_responses=True)
        self.name = name
        if not create:
            x, y, z = self.red_conn.get(name + ":coords").split(",")
        self.coords = {
            "x": int(x),
            "y": int(y),
            "z": int(z)
        }
        self.flumphs = []

    def add_flumph(self, new_flumph):
        self.flumphs.append(new_flumph)

    def shutdown(self):
        cloister_type = self._sub_shutdown()
        self.red_conn.set(self.name + ":coords", str(self.coords["x"]) + "," + str(self.coords["y"]) + "," + str(self.coords["z"]))
        self.red_conn.set(self.name + ":type", cloister_type)

    def get_coords(self):
        return self.coords

    @abstractmethod
    def _sub_shutdown(self):
        """called whenever system is about to shut down, should save any cloister specific data and return type"""
        pass

