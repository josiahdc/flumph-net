from legacy.flumphnet import Command


def test_command_no_params():
    command = Command("robot", "dance")
    assert command.command_string == "0\nrobot\ndance\n"

def test_command_one_param():
    command = Command("robot", "dance")
    assert command.command_string == "0\nrobot\ndance\n"