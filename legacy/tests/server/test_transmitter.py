from unittest.mock import Mock

from legacy.flumphnet import Transmitter


def test_read_string():
    reader_mock = Mock()
    reader_mock.readline.return_value = str.encode("  magic")
    transmitter = Transmitter(reader_mock, Mock())
    assert transmitter.read_string() == "magic"


def test_read_int():
    reader_mock = Mock()
    reader_mock.readline.return_value = 14
    transmitter = Transmitter(reader_mock, Mock())
    assert transmitter.read_int() == 14


def test_transmit():
    test_string = "hello flumph\n"
    writer_mock = Mock()
    transmitter = Transmitter(Mock(), writer_mock)
    transmitter.transmit(test_string)
    assert writer_mock.write.called_once_with(str.encode(test_string))
