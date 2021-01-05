class Transmitter:
    """handles reading from and writing to flumph buffers"""

    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def read_string(self):
        return str(self.reader.readline().decode("utf-8")).strip()

    def read_int(self):
        return int(self.reader.readline())

    def transmit(self, message):
        self.writer.write(str.encode(message + "\n"))
