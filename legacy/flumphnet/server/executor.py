import logging


class Executor:
    """formats and sends commands to a flumph"""

    def __init__(self, transmitter):
        self.transmitter = transmitter
        self.logger = logging.getLogger(__name__)

    def execute_command(self, api_name, function_name, params={}):
        """call a function on the flumph, returns a variable sized array of return values"""
        self.__send_command(api_name, function_name, params)
        # return response_values()
        return_values = []

        # number_of_return_values = int(self.reader.readline())
        # for i in range(number_of_return_values):
        #     value = self.read_line()
        #     formatted_value = self.__format_value(value)
        #     return_values.append(formatted_value)
        # return return_values

    def __send_command(self, api_name, function_name, params):
        command_string = self.__build_command_string(api_name, function_name, params)
        self.logger.debug("sending command string: " + command_string)
        self.transmitter.transmit(command_string)

    @staticmethod
    def __format_value(value):
        """turns strings into their respective types"""
        if value == "nil":
            return None
        elif value == "true":
            return True
        elif value == "false":
            return False
        return value
