import importlib
import os

COMMANDS = {}

def load_commands():
    """Dynamically load command modules from the commands directory."""
    command_folder = 'calculator/commands'
    for filename in os.listdir(command_folder):
        if filename.endswith('_command.py'):
            module_name = filename[:-3]
            try:
                # Dynamically import the module
                module = importlib.import_module(f'calculator.commands.{module_name}')
                command_name = module_name.replace('_command', '').lower()
                # Add the command to the COMMANDS dictionary
                COMMANDS[command_name] = getattr(module, f"{command_name.capitalize()}Command")()
            except ImportError as e:
                print(f"Error importing module {module_name}: {e}")
def repl():
    """Run the Read-Evaluate-Print Loop for the calculator."""
    load_commands()
    print("Calculator REPL. Type 'menu' for available commands, 'quit' to exit.")
    while True:
        user_input = input("> ").strip().lower()
        if user_input == "quit":
            break
        elif user_input == "menu":
            print("Available commands:", ', '.join(COMMANDS.keys()))
        else:
            try:
                cmd, *args = user_input.split()
                if cmd in COMMANDS:
                    result = COMMANDS[cmd].execute(*args)
                    print("Result:", result)
                else:
                    print("Unknown command. Type 'menu' for available commands.")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    repl()
