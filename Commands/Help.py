import os
from typing import List

import pretty_print
from CommandObjects import CommandObject, CommandConstant


class Help(CommandObject):
    aliases = ["help", "?"]
    arguments = []
    help_message = "Show help message"

    @staticmethod
    def callback(cmd_const: CommandConstant, input_str: str) -> None:
        from CommandsManager import CommandsManager  # Local import to avoid circular import

        commands: List[CommandObject] = CommandsManager.COMMAND_CLASSES
        commands.sort(key=lambda x: x.aliases[0])

        Help.pretty_print_commands(commands)

    @staticmethod
    def pretty_print_commands(commands: List[CommandObject]):
        print(commands)
