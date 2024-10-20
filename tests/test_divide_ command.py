# tests/test_divide_command.py
import pytest
from calculator.commands.divide_command import DivideCommand
def test_divide_command():
    command = DivideCommand()
    assert command.execute(20, 4) == 5
    assert command.execute(100, 5, 2) == 10

    # Test division by zero
    with pytest.raises(ZeroDivisionError):
        command.execute(10, 0)

    # Test for ValueError when fewer than two arguments are provided
    with pytest.raises(ValueError):
        command.execute(5)

    # Test with negative numbers
    assert command.execute(-20, 4) == -5
    assert command.execute(20, -4) == -5
    assert command.execute(-20, -4) == 5
