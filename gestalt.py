import redis
from minecloister import MineCloister
from stripminer import Strip_Miner


class Gestalt:
    def __init__(self):
        self.red_conn = redis.Redis(host='localhost', port=6379, db=7, decode_responses=True)
        self.cloisters = {}

        # get the cloisters and instantiate them
        cloister_names = self.red_conn.get("cloisters").split(",")
        for cloister_name in cloister_names:
            cloister_type = self.red_conn.get(cloister_name + ":type")
            if cloister_type == "mine":
                self.cloisters[cloister_name] = MineCloister(cloister_name)

    def new_flumph(self, reader, writer):
        # get configuration settings
        flumph_type = reader.readline().decode("utf-8").strip()
        desired_cloister = reader.readline().decode("utf-8").strip()

        # create a new flumph of the correct type and add it to its cloister
        new_flumph = None
        if flumph_type == "strip-miner":
            new_flumph = Strip_Miner(self.cloisters[desired_cloister], reader, writer)

        if new_flumph is not None:
            self.cloisters[desired_cloister].add_flumph(new_flumph)
            return new_flumph
        else:
            return None

    def shutdown(self):
        for cloister_name, cloister in self.cloisters.items():
            cloister.shutdown()
        self.red_conn.set("cloisters", ",".join(self.cloisters.keys()))