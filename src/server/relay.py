class Relay:
    """handles reading from and writing to flumph buffers"""

    def __init__(self, reader, writer):
        self._reader = reader
        self._writer = writer

    def receive(self):
        return str(self._reader.readline().decode("utf-8")).strip()

    def transmit(self, message):
        self._writer.write(str.encode(message + "\n"))
