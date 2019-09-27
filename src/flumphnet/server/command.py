class Command:
    def __init__(self, api_name, function_name, params=None):
        self.api_name = str(api_name)
        self.function_name = str(function_name)
        if params is None:
            params = {}
        self.params = params
        self.command_string = self.__build_command_string()

    def __build_command_string(self):
        """builds up a command string out of its constituent parts"""
        command = str(len(self.params)) + "\n"
        command += str(self.api_name) + "\n"
        command += str(self.function_name) + "\n"
        for param, paramType in self.params.items():
            command += str(param) + "\n"
            command += str(paramType) + "\n"
        return command
