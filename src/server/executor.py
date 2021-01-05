import ujson as ujson
from loguru import logger
from slpp import slpp


class Executor:
    def __init__(self, relay):
        self._relay = relay

    def execute_function(self, command):
        logger.debug(f"executing command: {command}")
        self._relay.transmit(f"return {command}")
        raw_return_value = self._relay.receive()
        result = self.return_value_formatter(raw_return_value)
        logger.debug(f"formatted return values: {ujson.dumps(result)}")
        return result

    @staticmethod
    def return_value_formatter(raw_return_value):
        parsed_return_value = slpp.decode(raw_return_value)
        if isinstance(parsed_return_value, list):
            return parsed_return_value
        result = []
        first_index = True
        first_gap = True
        last_index = None
        for index, value in parsed_return_value.items():
            if not isinstance(index, int):
                if value != len(result):
                    logger.error(
                        f"inconsistency found between expected and actual return value count: {raw_return_value}"
                    )
                return result
            if first_index:
                if index == 0:
                    gap_size = 0
                else:
                    gap_size = index - 1
                    first_gap = False
                first_index = False
            else:
                if first_gap and index - last_index > 1:
                    gap_size = index - last_index - 2
                    first_gap = False
                else:
                    gap_size = index - last_index - 1
            for i in range(gap_size):
                result.append(None)
            result.append(value)
            last_index = index
        return result
