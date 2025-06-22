import os

from CommandObjects import CommandObject, CommandConstant


class Clear(CommandObject):
    aliases = ["clear", "c"]
    arguments = []
    help_message = "Clear the terminal"

    @staticmethod
    def callback(cmd_const: CommandConstant, input_str: str) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
