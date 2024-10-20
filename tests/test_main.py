import pytest
from main import calculate_and_print
from calculator.plugin_manager import PluginManager

# Helper function to set up the PluginManager
def setup_manager():
    # Create and load the PluginManager
    manager = PluginManager("calculator.commands")
    manager.load_plugins()
    return manager

# Parametrize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize(
    "a_string, b_string, operation_string, expected_string",
    [
        ("5", "3", "add", "The result of 5 add 3 is equal to 8"),
        ("10", "2", "subtract", "The result of 10 subtract 2 is equal to 8"),
        ("4", "5", "multiply", "The result of 4 multiply 5 is equal to 20"),
        ("20", "4", "divide", "The result of 20 divide 4 is equal to 5"),
        ("1", "0", "divide", "An error occurred: Cannot divide by zero"), # Adjusted expected message
        ("3", "4", "unknown", "Unknown operation: unknown"), # Test for unknown operation
        ("a", "3", "add", "Invalid number input: a or 3 is not a valid number."), # Test for invalid input
        ("5", "b", "subtract", "Invalid number input: 5 or b is not a valid number.") # Test for another invalid input
    ]
)
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    # Set up the manager
    manager = setup_manager()

    # Call the function with the manager argument
    calculate_and_print(a_string, b_string, operation_string, manager)

    # Capture the output and compare it with the expected result
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
