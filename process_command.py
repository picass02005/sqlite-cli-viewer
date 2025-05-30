from commands import *


def process_command(input_str: str, commands: Commands):
    match input_str.lower():
        case ".tables" | ".table":
            commands.tables(input_str)

        case _:
            print("TODO")
